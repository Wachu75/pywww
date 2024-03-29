from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count

from galleries.models import Gallery
from galleries.models import Status
from galleries.models import Photo
from galleries.forms import GalleryForm
from galleries.forms import PhotoForm


def galleries_list(request):
    """Return a galleries with status published and more than 0 photos."""
    #galleries = Gallery.objects.filter(status=Status.PUBLISHED)
    galleries = Gallery.objects.filter(status=Status.PUBLISHED).annotate(p_count=Count('photos')).filter(p_count__gt=0)
    # galleries = [ g for g in galleries if g.photos.count() > 0 ]
    per_page = request.GET.get('per_page', 4)
    page_number = request.GET.get('page')
    paginator = Paginator(galleries, per_page)
    page_obj = paginator.get_page(page_number)
    return render(request, 'galleries.html', {'page_obj': page_obj})


def gallery_details(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)
    return render(request, 'gallery_details.html', {'gallery': gallery})


def add_gallery_view(request):
    """Add new galleries to database."""
    if request.method == 'GET':
        gallery_form = GalleryForm()
    elif request.method == 'POST':
        gallery_form = GalleryForm(request.POST)
        if gallery_form.is_valid():
            gallery = gallery_form.save()
            return HttpResponseRedirect(reverse('galleries:add_photo', args=[gallery.id]))
    return render(request, "galleries.html", {"gallery_form": gallery_form})


def add_photo_view(request, gallery_id):
    """Add new photo to database."""
    gallery = Gallery.objects.get(pk=gallery_id)
    photo_form = PhotoForm()
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.gallery = gallery
            instance.save()
        return HttpResponseRedirect(reverse("galleries:add_photo", args=[gallery_id]))
    return render(
        request,
        'galleries.html',
        {'photo_form': photo_form, 'gallery': gallery}
    )


def update_photo_view(request, gallery_id, photo_id):
    """Update photo"""
    gallery = Gallery.objects.get(pk=gallery_id)
    photo = Photo.objects.get(pk=photo_id)
    if request.method == 'POST':
        photo_form = PhotoForm(request.POST, request.FILES, instance=photo)
        if photo_form.is_valid():
            photo_form.save()
            return HttpResponseRedirect(reverse("galleries:add_photo", args=[gallery_id]))
    else:
        photo_form = PhotoForm(instance=photo)
    return render(request, 'galleries.html', {'photo_form': photo_form, 'gallery': gallery})
