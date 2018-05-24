
import os
import shutil


templates = [
    (k[16:], v)
    for k, v
    in os.environ.items()
    if k.startswith('NGINX_TEMPLATES_')]


for template_id, template_name in templates:
    if not os.path.exists('/etc/nginx/templates/%s.conf' % template_name):
        # raise warning ?
        continue
    if ('NGINX_SITES_%s' % template_id) in os.environ:
        sites = os.environ['NGINX_SITES_%s' % template_id].split(',')
        template = open('/etc/nginx/templates/%s.conf' % template_name).read()

        for site in sites:
            open('/etc/nginx/conf.d/%s.conf' % site, 'w').write(
                template.replace('$SERVER_NAME', site))
    else:
        shutil.copy(
            '/etc/nginx/templates/%s.conf' % template_name,
            '/etc/nginx/conf.d/%s.conf' % template_name)
