from modeltranslation.translator import TranslationOptions,register
from .models import Comment

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('post_comment', )