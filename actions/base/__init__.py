def folder_to_dict(folder):
    return {
        'id': folder.folder_id,
        'name': folder.name,
        'class': folder.folder_class,
        'total_count': folder.total_count,
        'child_folder_count': folder.child_folder_count,
        'unread_count': folder.unread_count
    }


def item_to_dict(item, include_body=False):
    result = {
        'id': item.item_id,
        'changekeyid': item.changekey,
        'subject': item.subject,
        'sensitivity': item.sensitivity,
        'text_body': item.text_body,
        'body': item.body,
        'attachments': len(item.attachments),
        'datetime_received': item.datetime_received.ewsformat() if item.datetime_received else None,
        'categories': item.categories,
        'importance': item.importance,
        'is_draft': item.is_draft,
        'datetime_sent': item.datetime_sent.ewsformat() if item.datetime_sent else None,
        'datetime_created': item.datetime_created.ewsformat() if item.datetime_created else None,
        'reminder_is_set': item.reminder_is_set,
        'reminder_due_by': item.reminder_due_by.ewsformat() if item.reminder_due_by else None,
        'reminder_minutes_before_start': item.reminder_minutes_before_start,
        'last_modified_name': item.last_modified_name,
        'last_modified_time': item.last_modified_time.ewsformat() if item.last_modified_time else None
    }
    if not include_body:
        del result['body']
        del result['text_body']
    return result
