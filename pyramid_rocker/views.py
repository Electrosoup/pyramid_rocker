import os
import shutil
from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED


@view_config(
    route_name='rocker.update',
    permission=NO_PERMISSION_REQUIRED
    )
def update(request):

    url = request.headers['X-Url']

    introspector = request.registry.introspector

    #get the static views
    static_views = introspector.get_category('static views')

    #iterate through them extracting paths

    for i in static_views:

        resource = i['introspectable']

        if resource['name'] in url:

            file_path = url.partition(resource['name'])[2]

            package_name = resource['spec'].split(':')[0]

            static_path = resource['spec'].split(':')[1]

            package_path = __import__(
                package_name).__file__.split('__init__')[0]

            full_path = package_path + static_path + file_path

            shutil.move(full_path, '%s.__tmp' % full_path)

            try:

                f = open(full_path, 'w')

                f.write(request.body)

                f.close()

                os.remove('%s.__tmp' % full_path)

            except:

                shutil.move('%s.__tmp' % full_path, full_path)

    return request.response
