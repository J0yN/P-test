from flask import Flask, render_template

app = Flask(__name__)

# Portfolio data with Unsplash images and descriptions
PORTFOLIO_CATEGORIES = {
    'nature': {
        'title': 'Nature',
        'cover': 'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05',
        'images': [
            {
                'url': 'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05',
                'description': 'Misty mountain peaks emerge through clouds, creating a dreamlike landscape that reminds us of nature\'s grandeur.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1447752875215-b2761acb3c5d',
                'description': 'Ancient forest canopy reaching skyward, filtering sunlight through layers of emerald leaves.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1433086966358-54859d0ed716',
                'description': 'Majestic waterfall cascading down moss-covered rocks, creating a natural symphony.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07',
                'description': 'Serene lake reflecting snow-capped mountains like a mirror to nature\'s beauty.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1469474968028-56623f02e42e',
                'description': 'Golden sunset painting the landscape in warm hues, marking the day\'s peaceful end.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1472214103451-9374bd1c798e',
                'description': 'Rolling hills dressed in morning mist, revealing nature\'s gentle awakening.'
            }
        ]
    },
    'architecture': {
        'title': 'Architecture',
        'cover': 'https://images.unsplash.com/photo-1470723710355-95304d8aece4',
        'images': [
            {
                'url': 'https://images.unsplash.com/photo-1470723710355-95304d8aece4',
                'description': 'Modern skyscraper reaching into clouds, showcasing human ambition in steel and glass.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1477959858617-67f85cf4f1df',
                'description': 'Historic cathedral spires piercing the sky, telling stories of centuries past.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b',
                'description': 'Geometric patterns in contemporary design creating a mesmerizing urban rhythm.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1496564203457-11bb12075d90',
                'description': 'Bridge spanning vast waters, connecting communities through engineering marvel.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1486325212027-8081e485255e',
                'description': 'Minimalist interior space where light and shadow dance in perfect harmony.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1487958449943-2429e8be8625',
                'description': 'Urban landscape at twilight, when city lights begin their nightly performance.'
            }
        ]
    },
    'people': {
        'title': 'People',
        'cover': 'https://images.unsplash.com/photo-1517841905240-472988babdf9',
        'images': [
            {
                'url': 'https://images.unsplash.com/photo-1517841905240-472988babdf9',
                'description': 'Portrait of joy captured in a moment of pure, unscripted laughter.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f',
                'description': 'Team collaboration bringing ideas to life through shared creativity.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1524601500432-1e1a4c71d692',
                'description': 'Street artist expressing their vision, adding color to urban spaces.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e',
                'description': 'Fashion portrait showcasing individual style and confidence.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1488161628813-04466f872be2',
                'description': 'Musicians lost in the moment, creating melodies that move souls.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1484688493527-670f98f9b195',
                'description': 'Cultural celebration bringing communities together in vibrant tradition.'
            }
        ]
    },
    'animals': {
        'title': 'Animals',
        'cover': 'https://images.unsplash.com/photo-1474511320723-9a56873867b5',
        'images': [
            {
                'url': 'https://images.unsplash.com/photo-1474511320723-9a56873867b5',
                'description': 'Wild fox in natural habitat, displaying nature\'s clever beauty.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1484406566174-9da000fda645',
                'description': 'Majestic eagle soaring freely against azure skies.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1450778869180-41d0601e046e',
                'description': 'Gentle pandas sharing a peaceful moment in bamboo forest.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1425082661705-1834bfd09dca',
                'description': 'Curious lion cub exploring world with playful wonder.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1442689859438-97407280183f',
                'description': 'Elegant butterfly resting on flower, showcasing nature\'s delicate art.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1437622368342-7a3d73a34c8f',
                'description': 'Marine turtle gliding through crystal waters with graceful ease.'
            }
        ]
    },
    'travel': {
        'title': 'Travel',
        'cover': 'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800',
        'images': [
            {
                'url': 'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800',
                'description': 'Road trip through endless horizon, where adventure awaits at every turn.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1',
                'description': 'Ancient temple shrouded in morning mist, keeper of timeless secrets.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1473625247510-8ceb1760943f',
                'description': 'Colorful streets of foreign cities telling stories through architecture.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828',
                'description': 'Local market bustling with authentic culture and traditions.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1469474968028-56623f02e42e',
                'description': 'Mountain trail leading to breathtaking views and new perspectives.'
            },
            {
                'url': 'https://images.unsplash.com/photo-1508672019048-805c876b67e2',
                'description': 'Coastal paradise where turquoise waters meet pristine beaches.'
            }
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html', categories=PORTFOLIO_CATEGORIES)