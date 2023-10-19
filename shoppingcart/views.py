from django.shortcuts import render
from django.http import HttpResponse
from supabase_py import create_client


# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Cart")

def allProducts(request):
  supabase = create_client('njavlkatbrmooagusygw.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5qYXZsa2F0YnJtb29hZ3VzeWd3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc2NDg5OTAsImV4cCI6MjAxMzIyNDk5MH0.TTRiXLy-1szR6tjRRjV9vfTESPN6VnOBU0-gJ9Xl1eY')
  return render(request, 'test2', context)