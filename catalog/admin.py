from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


class BookInline(admin.TabularInline):
    model = Book
    extra = 0 #removes empty form rows in admin panel.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'display_due_date', 'borrower', 'display_status', 'id')
    list_filter = ('status', 'due_back')

    '''You can add "sections" to group related model information within the detail form, using the fieldsets attribute.'''
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
            }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
            }),
        )



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    inlines = [BookInline]

    '''
    The fields attribute lists just those fields that are to be displayed on the form, in order. 
    Fields are displayed vertically by default, but will display horizontally if you further
    group them in a tuple (as shown in the "date" fields above).
    '''
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]




# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author, AuthorAdmin) # Alternate syntax to decorators above.