from library import hello_world, hello_world_personalized


def call_hello_world():
    return hello_world()


def call_hello_world_personalized():
    return hello_world_personalized(name='Maciek', greeting='Hiya')
