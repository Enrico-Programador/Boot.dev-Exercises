My:
def restore_documents(originals, backups):
    originals_list = list(originals)
    backups_list = list(backups)
    
    originals_list2 = []
    backups_list2 = []
    
    for original in originals_list:
        if original.isdigit() == False:
            originals_list2.append(original.upper())
            
    for backup in backups_list:
        if backup.isdigit() == False:
            backups_list2.append(backup.upper())
            
    originals_list2 = tuple(originals_list2)
    backups_list2 = tuple(backups_list2)
    tuplessauro = originals_list2 + backups_list2

    
    return set(filter(lambda string: string in tuplessauro, tuplessauro))

Correct one: 

def restore_documents(originals, backups):
    return set(
        filter(
            lambda doc: not doc.isdigit(),
            map(lambda doc: doc.upper(), originals + backups),
        )
    )

