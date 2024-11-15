
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
import urllib.parse

#fonction d'affiche de base

def product_list(request):
    query = request.GET.get('q')  # Récupère le terme de recherche
    available_products = Product.objects.filter(product_type='available')
    future_products = Product.objects.filter(product_type='future')

    if query:
        # Filtre les produits disponibles et futurs en fonction du terme de recherche
        available_products = available_products.filter(
            Q(name_icontains=query) | Q(description_icontains=query)
        )
        future_products = future_products.filter(
            Q(name_icontains=query) | Q(description_icontains=query)
        )
    
    context = {
        'available_products': available_products,
        'future_products': future_products,
        'query': query,
    }
    
    return render(request, 'store/base.html', context)


#pour le panier

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += 1  # Incrémente la quantité si déjà présent
    else:
        cart[str(product_id)] = 1  # Ajoute avec une quantité de 1

    request.session['cart'] = cart  # Enregistre le panier dans la session
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })
        total += product.price * quantity

    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'store/cart.html', context)





#pour le whatsapp

from django.shortcuts import get_object_or_404, redirect
import urllib.parse

def checkout(request, product_id=None, quantity=1):
    """
    Permet de passer une commande en utilisant le panier ou en commandant un produit directement.

    Args:
        request: La requête HTTP.
        product_id (int, optional): L'ID du produit à commander directement. Si None, utilise le panier.
        quantity (int, optional): La quantité du produit à commander. Par défaut, 1.
    """
    cart = request.session.get('cart', {})
    phone_number = '074160680'
    message = "Bonjour, je souhaite commander les produits suivants :\n\n"

    if product_id:
        # Commander un produit spécifique sans passer par le panier
        product = get_object_or_404(Product, pk=product_id)
        message += f"- {product.name} (x{quantity}) : {product.price * quantity} $\n"
        total_price = product.price * quantity
    else:
        # Commander les produits du panier
        for pk, qty in cart.items():
            product = get_object_or_404(Product, pk=pk)
            message += f"- {product.name} (x{qty}) : {product.price * qty} $\n"
        
        total_price = sum(get_object_or_404(Product, pk=pk).price * qty for pk, qty in cart.items())
        request.session['cart'] = {}  # Vider le panier après la commande

    message += f"\nTotal : {total_price} $"

    # Rediriger vers WhatsApp avec le message pré-rempli
    whatsapp_url = f"https://wa.me/{phone_number}?text={urllib.parse.quote(message)}"
    return redirect(whatsapp_url)




def checkout1(request, product_id, quantity=1):
    """
    Permet de commander un produit spécifique en cliquant directement dessus.

    Args:
        request: La requête HTTP.
        product_id (int): L'ID du produit à commander.
        quantity (int, optional): La quantité du produit à commander. Par défaut, 1.
    """
    phone_number = '074160680'
    product = get_object_or_404(Product, pk=product_id)
    
    # Construire le message de commande
    message = "Bonjour, je souhaite commander le produit suivant :\n\n"
    message += f"- {product.name} (x{quantity}) : {product.price * quantity} $\n"
    total_price = product.price * quantity
    message += f"\nTotal : {total_price} $"

    # Rediriger vers WhatsApp avec le message pré-rempli
    whatsapp_url = f"https://wa.me/{phone_number}?text={urllib.parse.quote(message)}"
    return redirect(whatsapp_url)








#voir les details d'un produit


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    context = {
        'product': product
    }
    
    return render(request, 'store/product_detail.html', context)


#recherche
def search_products(request):
    query = request.GET.get('q')

    products = Product.objects.filter(name__icontains=query) if query else None
    return render(request, 'store/search_results.html', {'products': products, 'query': query})



from django.shortcuts import render
from .models import Product

def product_listes(request):
    # Récupérer tous les produits
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

