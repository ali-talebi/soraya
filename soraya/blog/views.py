from django.shortcuts import render
from .models import Post
from django.views import View


class TotalBlogsView(View) :

    template_name = 'blog/blog-masonry.html'

    def setup(self, request , *args , **kwargs ) :
        self.total_data = Post.objects.all()
        return super().setup(request , *args , **kwargs )

    def get(self , request ) :
        return render(request , self.template_name , {'total_blogs' : self.total_data} )





class DetailBlogView(View) :


    template_name = 'blog/blog-detail.html'



    def setup(self , request , *args , **kwargs ) :
        self.data = Post.objects.get(id = kwargs['id'])
        return super().setup(request , *args , **kwargs )


    def get(self , request , id ) :
        return render(request , self.template_name , {'data':self.data} )