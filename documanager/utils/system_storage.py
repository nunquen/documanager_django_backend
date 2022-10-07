from documanager.settings import MEDIA_FOLDER

def upload_path_handler(document, filename):
    return "{MEDIA_FOLDER}{id}/{file}".format(MEDIA_FOLDER=MEDIA_FOLDER, id=document.user.id, file=filename)

def upload_path_handler2(revision, filename):
    return "{MEDIA_FOLDER}{id}/{doc_id}/v{number_i}/{file}".format(
        MEDIA_FOLDER=MEDIA_FOLDER,
        id=revision.document.user.id,
        doc_id=revision.document.id,
        number_i=revision.number_i,
        file=filename
    )
