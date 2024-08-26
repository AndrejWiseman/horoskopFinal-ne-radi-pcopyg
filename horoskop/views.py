from django.shortcuts import render
from django.http import Http404
import os
from django.conf import settings
import json
import requests
from bs4 import BeautifulSoup
import concurrent.futures


def prikazi_znak(request, znak):
    json_path = os.path.join(settings.STATICFILES_DIRS[0], 'data', 'horoskop.json')
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    return render(request, 'znak.html', {'znak': data[znak]})


def fetch_horoscope(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    entry_content_div = soup.find('div', class_='entry-content')
    paragraphs = entry_content_div.find_all('p', recursive=False)

    formatted_paragraphs = []
    for p in paragraphs:
        formatted_text = ''
        for content in p.contents:
            if content.name == 'strong':
                formatted_text += f'<strong style="font-weight: bold;">{content.text}</strong><br>'
            else:
                formatted_text += str(content)
        formatted_paragraphs.append(f'<p>{formatted_text}</p>')

    return ' '.join(formatted_paragraphs)


def get_horoscope_data(znak, urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_horoscope, urls))

    dnevni, sutra, nedeljni, mesecni, godisnji = results
    context = {
        'znak': znak,
        'dnevni': dnevni,
        'sutra': sutra,
        'nedeljni': nedeljni,
        'mesecni': mesecni,
        'godisnji': godisnji,
    }
    return context


def home(request):
    context = {}
    return render(request, 'index.html', context)


def horoskop(request, znak):
    urls = {
        'ovan': [
            'https://www.astroputnik.com/dnevni-horoskop-ovan/',
            'https://www.astroputnik.com/horoskop-za-sutra-ovan/',
            'https://www.astroputnik.com/nedeljni-horoskop-ovan/',
            'https://www.astroputnik.com/mesecni-horoskop-ovan/',
            'https://www.astroputnik.com/godisnji-horoskop-ovan/'
        ],
        'bik': [
            'https://www.astroputnik.com/dnevni-horoskop-bik/',
            'https://www.astroputnik.com/horoskop-za-sutra-bik/',
            'https://www.astroputnik.com/nedeljni-horoskop-bik/',
            'https://www.astroputnik.com/mesecni-horoskop-bik/',
            'https://www.astroputnik.com/godisnji-horoskop-bik/'
        ],
        'blizanci': [
            'https://www.astroputnik.com/dnevni-horoskop-blizanci/',
            'https://www.astroputnik.com/horoskop-za-sutra-blizanci/',
            'https://www.astroputnik.com/nedeljni-horoskop-blizanci/',
            'https://www.astroputnik.com/mesecni-horoskop-blizanci/',
            'https://www.astroputnik.com/godisnji-horoskop-blizanci/'
        ],
        'rak': [
            'https://www.astroputnik.com/dnevni-horoskop-rak/',
            'https://www.astroputnik.com/horoskop-za-sutra-rak/',
            'https://www.astroputnik.com/nedeljni-horoskop-rak/',
            'https://www.astroputnik.com/mesecni-horoskop-rak/',
            'https://www.astroputnik.com/godisnji-horoskop-rak/'
        ],
        'lav': [
            'https://www.astroputnik.com/dnevni-horoskop-lav/',
            'https://www.astroputnik.com/horoskop-za-sutra-lav/',
            'https://www.astroputnik.com/nedeljni-horoskop-lav/',
            'https://www.astroputnik.com/mesecni-horoskop-lav/',
            'https://www.astroputnik.com/godisnji-horoskop-lav/'
        ],
        'devica': [
            'https://www.astroputnik.com/dnevni-horoskop-devica/',
            'https://www.astroputnik.com/horoskop-za-sutra-devica/',
            'https://www.astroputnik.com/nedeljni-horoskop-devica/',
            'https://www.astroputnik.com/mesecni-horoskop-devica/',
            'https://www.astroputnik.com/godisnji-horoskop-devica/'
        ],
        'vaga': [
            'https://www.astroputnik.com/dnevni-horoskop-vaga/',
            'https://www.astroputnik.com/horoskop-za-sutra-vaga/',
            'https://www.astroputnik.com/nedeljni-horoskop-vaga/',
            'https://www.astroputnik.com/mesecni-horoskop-vaga/',
            'https://www.astroputnik.com/godisnji-horoskop-vaga/'
        ],
        'skorpija': [
            'https://www.astroputnik.com/dnevni-horoskop-skorpija/',
            'https://www.astroputnik.com/horoskop-za-sutra-skorpija/',
            'https://www.astroputnik.com/nedeljni-horoskop-skorpija/',
            'https://www.astroputnik.com/mesecni-horoskop-skorpija/',
            'https://www.astroputnik.com/godisnji-horoskop-skorpija/'
        ],
        'strelac': [
            'https://www.astroputnik.com/dnevni-horoskop-strelac/',
            'https://www.astroputnik.com/horoskop-za-sutra-strelac/',
            'https://www.astroputnik.com/nedeljni-horoskop-strelac/',
            'https://www.astroputnik.com/mesecni-horoskop-strelac/',
            'https://www.astroputnik.com/godisnji-horoskop-strelac/'
        ],
        'jarac': [
            'https://www.astroputnik.com/dnevni-horoskop-jarac/',
            'https://www.astroputnik.com/horoskop-za-sutra-jarac/',
            'https://www.astroputnik.com/nedeljni-horoskop-jarac/',
            'https://www.astroputnik.com/mesecni-horoskop-jarac/',
            'https://www.astroputnik.com/godisnji-horoskop-jarac/'
        ],
        'vodolija': [
            'https://www.astroputnik.com/dnevni-horoskop-vodolija/',
            'https://www.astroputnik.com/horoskop-za-sutra-vodolija/',
            'https://www.astroputnik.com/nedeljni-horoskop-vodolija/',
            'https://www.astroputnik.com/mesecni-horoskop-vodolija/',
            'https://www.astroputnik.com/godisnji-horoskop-vodolija/'
        ],
        'ribe': [
            'https://www.astroputnik.com/dnevni-horoskop-ribe/',
            'https://www.astroputnik.com/horoskop-za-sutra-ribe/',
            'https://www.astroputnik.com/nedeljni-horoskop-ribe/',
            'https://www.astroputnik.com/mesecni-horoskop-ribe/',
            'https://www.astroputnik.com/godisnji-horoskop-ribe/'
        ],
    }

    if znak not in urls:
        raise Http404("Horoskop za traženi znak nije pronađen.")

    context = get_horoscope_data(znak, urls[znak])
    return render(request, 'horoskop-detaljno.html', context)


