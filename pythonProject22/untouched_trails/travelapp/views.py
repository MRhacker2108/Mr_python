from django.shortcuts import render

# 12 Professional Destinations Ka Data
destinations_data = [
{
        'id': 1,
        'name': 'Mumbai Juhu Chowpatty',
        'price': '₹45,000',
        'cat': 'Influencer Famous',
        # 👇 Mumbai ki nayi image link
        'img': 'https://images.unsplash.com/photo-1567157577867-05ccb1388e66?auto=format&fit=crop&w=800&q=80',
        'rating': '4.8',
        'reviews': '120 Reviews'
    },
{
        'id': 2,
        'name': 'Manali Snow Expedition',
        'price': '₹55,000',
        'cat': 'Untouched Offbeat',
        # 👇 Manali ki nayi image link
        'img': 'https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=800&q=80',
        'rating': '4.9',
        'reviews': '85 Reviews'
    },
    {'id': 3, 'name': 'Gurez Valley, Kashmir', 'price': '₹35,000', 'cat': 'Untouched Offbeat', 'img': 'https://images.unsplash.com/photo-1595815771614-ade9d652a65d?w=800', 'rating': '5.0', 'reviews': '45 Reviews'},
    {'id': 4, 'name': 'Maldives Glass Villa', 'price': '₹2,10,000', 'cat': 'Influencer Famous', 'img': 'https://images.unsplash.com/photo-1514282401047-d79a71a590e8?w=800', 'rating': '4.7', 'reviews': '310 Reviews'},
{
        'id': 5,
        'name': 'Gurez Valley, Kashmir',
        'price': '₹65,000',
        'cat': 'Untouched Offbeat',
        'img': 'https://images.unsplash.com/photo-1595815771614-ade9d652a65d?auto=format&fit=crop&w=800&q=80',
        'rating': '5.0',
        'reviews': '45 Reviews'
    },
    {'id': 6, 'name': 'Bali Jungle Swing', 'price': '₹85,000', 'cat': 'Influencer Famous', 'img': 'https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=800', 'rating': '4.9', 'reviews': '450 Reviews'},
{
        'id': 7,
        'name': 'Andaman Blue Lagoon',
        'price': '₹75,000',
        'cat': 'Influencer Famous',
        'img': 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800',
        'rating': '4.9', 'reviews': '340 Reviews'
    },
    {'id': 8, 'name': 'Santorini Blue Domes', 'price': '₹2,50,000', 'cat': 'Influencer Famous', 'img': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=800', 'rating': '4.8', 'reviews': '280 Reviews'},
{
        'id': 9,
        'name': 'Ladakh Magnetic Hill',
        'price': '₹52,000',
        'cat': 'Influencer Famous',
        'img': 'https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?w=800',
        'rating': '4.9', 'reviews': '2.4k Reviews'
    },
    {'id': 10, 'name': 'Varanasi Ghat Rituals', 'price': '₹25,000', 'cat': 'Influencer Famous', 'img': 'https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800', 'rating': '4.7', 'reviews': '150 Reviews'},
{
        'id': 12,
        'name': 'Jaipur Hawa Mahal',
        'price': '₹18,000',
        'cat': 'Influencer Famous',
        'img': 'https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800',
        'rating': '4.8', 'reviews': '5.1k Reviews'
    },
{
    'id': 13,
    'name': 'Shoja, Himachal Pradesh',
    'price': '₹18,500',
    'cat': 'Hidden Forest',
    'img': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800',
    'rating': '4.9', 'reviews': '180 Reviews'
},
    {
        'id': 14,
        'name': 'Alleppey Houseboat',
        'price': '₹32,000',
        'cat': 'Influencer Famous',
        'img': 'https://images.unsplash.com/photo-1593181629936-11c609b8db9b?w=800',
        'rating': '4.9', 'reviews': '1.8k Reviews'
    },
{
    'id': 15,
    'name': 'Chopta, Uttarakhand',
    'price': '₹15,500',
    'cat': 'Mini Switzerland',
    'img': 'https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800',
    'rating': '4.8', 'reviews': '312 Reviews'
},
    {
        'id': 16,
        'name': 'Varkala Cliff, Kerala',
        'price': '₹22,000',
        'cat': 'Coastal Offbeat',
        'img': 'https://images.unsplash.com/photo-1590523741831-ab7e8b8f9c7f?w=800',
        'rating': '4.7', 'reviews': '425 Reviews'
    },
]

def home(request):
    return render(request, 'travelapp/index.html')

def destinations_view(request):
    return render(request, 'travelapp/destinations.html', {'places': destinations_data})

def book_destination(request, place_id):
    # Har destination ko uski ID se open karega
    place = next((item for item in destinations_data if item['id'] == place_id), None)
    return render(request, 'travelapp/book.html', {'place': place})

def login_view(request):
    return render(request, 'travelapp/login.html')

def register_view(request):
    return render(request, 'travelapp/register.html')

def dashboard_view(request):
    return render(request, 'travelapp/dashboard.html')

def about_view(request):
    return render(request, 'travelapp/about.html')