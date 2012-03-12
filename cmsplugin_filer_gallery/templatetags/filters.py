from django.template.defaultfilters import register

@register.filter(name="aspect_ratio")
def aspect_ratio(image):
  return float(image.height)/image.width

