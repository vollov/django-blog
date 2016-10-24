from blog.models import Blog, Tag

class BlogService:
    
    def __init__(self):
        pass
    
    def get_blogs_for_view(self, blogs):
        
        for blog in blogs:
            blog.tag_set = blog.tags.all()
        return blogs