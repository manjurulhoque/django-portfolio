import os


def _delete_file(path):
    """ Deletes file from filesystem. """
    if os.path.isfile(path):
        os.remove(path)


def file_cleanup(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    print(sender)
    if instance.image:
        _delete_file(instance.image.path)
