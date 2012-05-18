#


def includeme(config):
    config.add_route('rocker.update', '/__rocker_update')
    config.scan('pyramid_rocker.views')
