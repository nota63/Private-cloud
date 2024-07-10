from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import DocumentForm
from django.http import HttpResponse
from .models import Documents
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


def documents(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Document uploaded!")
            return redirect('documents')
    else:
        form = DocumentForm()
    return render(request, 'documents/documents.html', {'form': form})


def view_documents(request):
    documents = Documents.objects.all()
    if request.method == 'GET':
        doc_search = request.GET.get('doc_search')
        if doc_search != None:
            documents = Documents.objects.filter(name__icontains=doc_search)
    return render(request, 'documents/view_documents.html', {'documents': documents})


def delete_documents(request, documents_id):
    doc = get_object_or_404(Documents, id=documents_id)
    doc.delete()
    return redirect('view_documents')


