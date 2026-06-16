```python
import sphinx_rtd_theme

# Buluta kurumsal temayı kullanmasını söylüyoruz
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Şirket logosu ve başlık ayarları
html_title = "Özdoğan Teknoloji - Geliştirici Portalı"
html_logo = "_static/sirket_logosu.png" # _static klasöründeki logo resminin adı

html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
}
```python
   def setup(app):
       app.add_css_file('custom.css')
