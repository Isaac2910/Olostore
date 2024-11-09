
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
import urllib.parse

#fonction d'affiche de base

def homepage(request):
    future_products = Product.objects.filter(product_type='future')
    available_products = Product.objects.filter(product_type='available')
    
    context = {
        'future_products': future_products,
        'available_products': available_products
    }
    return render(request,'store/base.html', context)


#pour la liste des produit et la recherche des produit
def product_list(request):
    query = request.GET.get('q', '')  # Use .get to avoid KeyError
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'store/base.html', {'products': products, 'query': query})


from django.shortcuts import render, get_object_or_404

def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product.html', {'product': product})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request,'store/product.html', product )


#Fonction pour supprimer un produit du panier
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    
    if pk in cart:
        del cart[pk]  # Supprimer le produit du panier
        
        # Si le panier est vide, supprimer la clé 'cart' de la session
        if not cart:
            del request.session['cart']
    
    return redirect('view-cart')



###Fontion pour ajouter au panier
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # Initialiser le panier s'il n'existe pas encore dans la session
    cart = request.session.get('cart', {})
    
    # Ajouter le produit au panier
    if pk in cart:
        cart[pk] += 1  # Incrémente la quantité si le produit est déjà dans le panier
    else:
        cart[pk] = 1  # Ajoute le produit avec une quantité de 1
    
    request.session['cart'] = cart  # Enregistrer le panier mis à jour dans la session
    return redirect('product-list')
#Fonction pour ajouter la quantitee du produit
def view_cart(request):
    cart = request.session.get('cart', {})
    products = []
    total_price = 0
    
    for pk, quantity in cart.items():
        product = get_object_or_404(Product, pk=pk)
        total_price += product.price * quantity
        products.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })

    return render(request, 'store/viewspanier.html', {'products': products, 'total_price': total_price})

def checkout(request):
    cart = request.session.get('cart', {})
    phone_number = '074160680'  

    # Construire le message de commande avec les détails de chaque produit dans le panier
    message = "Bonjour, je souhaite commander les produits suivants :\n\n"
    for pk, quantity in cart.items():
        product = get_object_or_404(Product, pk=pk)
        message += f"- {product.name} (x{quantity}) : {product.price * quantity} $\n"
    
    # Calculer le total
    total_price = sum(get_object_or_404(Product, pk=pk).price * qty for pk, qty in cart.items())
    message += f"\nTotal : {total_price} $"

    # Rediriger vers WhatsApp avec le message pré-rempli
    whatsapp_url = f"https://wa.me/{phone_number}?text={urllib.parse.quote(message)}"
    request.session['cart'] = {}  # Vider le panier après la commande
    return redirect(whatsapp_url)



def addpanier(request):
    return render(request, 'store/viewspanier.html')







