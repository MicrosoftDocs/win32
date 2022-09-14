---
title: File System Operation Notifications
description: Describes how a provider can receive notifications of file system operations.
ms.assetid: <GUID-GOES-HERE>
ms.date: 10/04/2018
ms.topic: article
---

# File System Operation Notifications

In addition to required callbacks for handling enumeration, returning file metadata, and file contents, a provider may optionally register a **[PRJ_NOTIFICATION_CB]()** callback in its call to **[PrjStartVirtualizing]()**.  This callback receives notifications of file system operations performed on files and directories beneath the instance's virtualization root.  Some of the notifications are "post-operation" notifications, which tell the provider that an operation has just completed.  The other notifications are "pre-operation" notifications, meaning that the provider is notified before the operation happens.  In a pre-operation notification the provider can veto the operation by returning an error code from the callback.  This causes the operation to fail with the returned error code.

## How to Specify Notifications to Receive

If the provider supplies an implementation of **PRJ_NOTIFICATION_CB** when it starts a virtualization instance, it should also specify which notifications it wishes to receive.  The notifications for which the provider can register are defined in the [PRJ_NOTIFICATION](/windows/win32/api/projectedfslib/ne-projectedfslib-prj_notification) enum.

When the provider specifies the notifications it wishes to receive, it does so using an array of one or more [PRJ_NOTIFICATION_MAPPING](/windows/desktop/api/projectedfslib/ns-projectedfslib-prj_notification_mapping) structures.  These define "notification mappings".  A notification mapping is a pairing between a directory, referred to as a "notification root", and a set of notifications, expressed as a bit mask, which ProjFS should send for that directory and its descendants.  A notification mapping can also be established for a single file.  A file or directory specified in a notification mapping does not have to exist already at the time the provider calls **PrjStartVirtualizing**, the provider can specify any path and the mapping will apply to it if it is ever created.

If the provider specifies multiple notification mappings, and some are descendants of others, the mappings must be specified in descending depth.  Notification mappings at deeper levels override higher-level ones for their descendants.

If the provider does not specify a set of notification mappings, ProjFS will default to sending it PRJ_NOTIFY_FILE_OPENED, PRJ_NOTIFY_NEW_FILE_CREATED, and PRJ_NOTIFY_FILE_OVERWRITTEN for all files and directories beneath the virtualization root.

The following code snippet illustrates how to register a set of notifications when starting a virtualization instance.

```C++
PRJ_CALLBACKS callbackTable;

// Supply required callbacks.
callbackTable.StartDirectoryEnumerationCallback = MyStartEnumCallback;
callbackTable.EndDirectoryEnumerationCallback = MyEndEnumCallback;
callbackTable.GetDirectoryEnumerationCallback = MyGetEnumCallback;
callbackTable.GetPlaceholderInfoCallback = MyGetPlaceholderInfoCallback;
callbackTable.GetFileDataCallback = MyGetFileDataCallback;

// The rest of the callbacks are optional.  We want notifications, so specify
// our notification callback.
callbackTable.QueryFileNameCallback = nullptr;
callbackTable.NotificationCallback = MyNotificationCallback;
callbackTable.CancelCommandCallback = nullptr;

// Assume the provider has created a new virtualization root at C:\VirtRoot and
// initialized it with this layout:
//
//     C:\VirtRoot
//     +--- baz
//     \--- foo
//          +--- subdir1
//          \--- subdir2
//
// The provider wants these notifications:
// * Notification of new file/directory creates for all locations within the
//   virtualization root that are not subject to one of the following more
//   specific notification mappings.
// * Notification of new file/directory creates, file opens, post-renames, and
//   pre- and post-deletes for C:\VirtRoot\foo
// * No notifications for C:\VirtRoot\foo\subdir1
PRJ_STARTVIRTUALIZING_OPTIONS startOpts = {};
PRJ_VIRTUALIZATION_MAPPING notificationMappings[3];

// Configure default notifications - notify of new files for most of the tree.
notificationMappings[0].NotificationRoot = L"";
notificationMappings[0].NotificationBitMask = PRJ_NOTIFY_NEW_FILE_CREATED;

// Override default notifications - notify of new files, opened files, and file
// deletes for C:\VirtRoot\foo and its descendants.
notificationMappings[1].NotificationRoot = L"foo";
notificationMappings[1].NotificationBitMask = PRJ_NOTIFY_NEW_FILE_CREATED |
                                              PRJ_NOTIFY_FILE_OPENED |
                                              PRJ_NOTIFY_PRE_DELETE |
                                              PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_DELETED |
                                              PRJ_NOTIFY_FILE_RENAMED;

// Override all notifications for C:\VirtRoot\foo\subdir1 and its descendants.
notificationMappings[2].NotificationRoot = L"foo\\subdir1";
notificationMappings[2].NotificationBitMask = PRJ_NOTIFY_SUPPRESS_NOTIFICATIONS;

startOpts.NotificationMappings = notificationMappings;
startOpts.NotificationMappingsCount = ARRAYSIZE(notificationMapping);

// Start the instance and provide our notification mappings.
HRESULT hr;
PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT instanceHandle;
hr = PrjStartVirtualizing(rootName,
                          &callbackTable,
                          nullptr,
                          &startOpts,
                          &instanceHandle);
if (FAILED(hr))
{
    wprintf(L"Failed to start the virtualization instance (0x%08x)\n", hr);
    return;
}
```

## Receiving Notifications

ProjFS sends notifications of file system operations by calling the provider's **PRJ_NOTIFICATION_CB** callback.  It does this for each operation the provider has registered for.  If, as in the above example, the provider registered for PRJ_NOTIFY_NEW_FILE_CREATED | PRJ_NOTIFY_FILE_OPENED | PRJ_NOTIFY_PRE_DELETE | PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_DELETED | PRJ_NOTIFY_FILE_RENAMED, and an application created a new file in the notification root, ProjFS would call the **PRJ_NOTIFICATION_CB** callback with the new file's path name and the _notification_ parameter set to PRJ_NOTIFICATION_NEW_FILE_CREATED.

ProjFS sends the notifications in the following list before the associated file system operation takes place.  If the provider returns a failure code from the **PRJ_NOTIFICATION_CB** callback, the file system operation will fail and return the failure code the provider specified.

* PRJ_NOTIFICATION_PRE_DELETE - The file is about to be deleted.
* PRJ_NOTIFICATION_PRE_RENAME - The file is about to be renamed.
* PRJ_NOTIFICATION_PRE_SET_HARDLINK - A hard link is about to be created for the file.
* PRJ_NOTIFICATION_FILE_PRE_CONVERT_TO_FULL - A file is about to be expanded from a placeholder to a full file, which indicates its contents are likely to be modified.

ProjFS sends the notifications in the following list after the associated file system operation has completed.

* PRJ_NOTIFICATION_FILE_OPENED - An existing file has been opened.
  * Even though this notification is sent after the file has been opened, the provider can return a failure code.  In response, ProjFS will cancel the open and return the failure to the caller.
* PRJ_NOTIFICATION_NEW_FILE_CREATED - A new file has been created.
* PRJ_NOTIFICATION_FILE_OVERWRITTEN - An existing file has been overwritten, for example by calling [CreateFileW](/windows/desktop/api/fileapi/nf-fileapi-createfilew) with the **CREATE_ALWAYS** _dwCreationDisposition_ flag.
* PRJ_NOTIFICATION_FILE_RENAMED - A file has been renamed.
* PRJ_NOTIFICATION_HARDLINK_CREATED - A [hard link](/windows/desktop/FileIO/hard-links-and-junctions#hard-links) has been created for a file.
* PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_NO_MODIFICATION - A file handle has been closed, and the file's content was not modified, nor was the file deleted.
* PRJ_NOTIFICATION_FILE_HANLDE_CLOSED_FILE_MODIFIED - A file handle has been closed, and the file's content has been modified.
* PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_DELETED - A file handle has been closed, and the file was deleted as part of closing the handle.

For more details on each notification refer to the documentation for **[PRJ_NOTIFICATION](/windows/desktop/api/projectedfslib/ne-projectedfslib-prj_notification)**.

The **PRJ_NOTIFICATION_CB** callback's _notificationParameters_ parameter specifies extra parameters for certain notifications.  If a provider receives a PRJ_NOTIFICATION_FILE_OPENED, PRJ_NOTIFICATION_NEW_FILE_CREATED, or PRJ_NOTIFICATION_FILE_OVERWRITTEN, or PRJ_NOTIFICATION_FILE_RENAMED notification, the provider can specify a new set of notifications to receive for the file. For further details, refer to the documentation for **[PRJ_NOTIFICATION_CB](/windows/desktop/api/projectedfslib/nc-projectedfslib-prj_notification_cb)**.

The following sample shows simple examples of how a provider might process the notifications it registered for in the code snippet above.

```C++
#include <windows.h>

HRESULT
MyNotificationCallback(
    _In_ const PRJ_CALLBACK_DATA* callbackData,
    _In_ BOOLEAN isDirectory,
    _In_ PRJ_NOTIFICATION notification,
    _In_opt_z_ PCWSTR destinationFileName,
    _Inout_ PRJ_NOTIFICATION_PARAMETERS* operationParameters
    )
{
    HRESULT hr = S_OK;

    switch (notification)
    {
    case PRJ_NOTIFY_NEW_FILE_CREATED:

        wprintf(L"A new %ls was created at [%ls].\n",
                isDirectory ? L"directory" : L"file",
                callbackData->FilePathName);

        // Let's stop getting notifications inside newly-created directories.
        if (isDirectory)
        {
            operationParameters->PostCreate.NotificationMask = PRJ_NOTIFY_SUPPRESS_NOTIFICATIONS;
        }
        break;

    case PRJ_NOTIFY_FILE_OPENED:

        wprintf(L"Handle opened to %ls [%ls].\n",
                isDirectory ? L"directory": L"file",
                callbackData->FilePathName);
        break;

    case PRJ_NOTIFY_PRE_DELETE:

        wprintf(L"Attempt to delete %ls [%ls]: ",
                isDirectory ? L"directory": L"file",
                callbackData->FilePathName);

        // MyAllowDelete is a routine the provider might implement to decide
        // whether to allow a given file/directory to be deleted.
        if (!MyAllowDelete(callbackData->FilePathName, isDirectory))
        {
            wprintf(L"DENIED\n");
            hr = HRESULT_FROM_WIN32(ERROR_ACCESS_DENIED);
        }
        else
        {
            wprintf(L"ALLOWED\n");
        }
        break;

    case PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_DELETED:

        wprintf(L"The %ls [%ls] was deleted.\n",
                isDirectory ? L"directory": L"file",
                callbackData->FilePathName);
        break;

    case PRJ_NOTIFY_FILE_RENAMED:

        if (wcslen(callbackData->FilePathName) == 0)
        {
            // If callbackData->FilePathName is an empty string, then the item
            // that was renamed was originally in a location not under the
            // virtualization root.
            wprintf(L"A %ls was renamed into the virtualization root,\n",
                    isDirectory ? L"directory": L"file");
            wprintf(L"Its new location is [%ls].\n",
                    destinationFileName);
        }
        else if (wcslen(destinationFileName) == 0)
        {
            // If destinationFileName is an empty string, then the item that was
            // renamed is now in a location not under the virtualization root.
            wprintf(L"A %ls was renamed out of the virtualization root.\n",
                    isDirectory ? L"directory": L"file");
            wprintf(L"Its original location was [%ls].\n",
                    callbackData->FilePathName);
        }
        else
        {
            // If both names are specified, both the new and old names are under
            // the virtualization root (it is never the case that nether name is
            // specified).
            wprintf(L"A %ls [%ls] was renamed.\n",
                    isDirectory ? L"directory": L"file",
                    callbackData->FilePathName);
            wprintf(L"Its new name is [%ls].\n", destinationFileName);
        }
        break;

    default:
        wprintf(L"Unrecognized notification: 0x%08x");
    }

    // Note that this may be a failure code from MyAllowDelete().
    return hr;
}
```