---
title: Handling View Changes
description: Describes how to update the client view of a provider's backing store.
ms.assetid: <GUID-GOES-HERE>
ms.date: 10/09/2018
ms.topic: article
---

# Handling View Changes

As files and directories under the virtualization root are opened, the provider creates placeholders on disk, and as files are read the placeholders are hydrated with contents.  These placeholders represent the state of the backing store at the time they were created.  These cached items, combined with the items projected by the provider in enumerations, constitute the client's "view" of the backing store.  From time to time the provider may wish to update the client's view, whether because of changes in the backing store, or because of explicit action taken by the user to change their view.

> If the provider updates the view proactively, as the backing store changes, it is recommended that view changes be relatively infrequent.  This is because a view change to an item that has been opened, and therefore had a placeholder created on disk, requires that the on-disk item be either updated or deleted to reflect the view change.  Frequent updates may result in extra disk activity that can negatively impact system performance.

## Item Versioning

To support maintaining multiple views, ProjFS provides the **[PRJ_PLACEHOLDER_VERSION_INFO](/windows/desktop/api/projectedfslib/ns-projectedfslib-prj_placeholder_version_info)** struct.  A provider uses this struct standalone in calls to **[PrjMarkDirectoryAsPlaceholder](/windows/desktop/api/projectedfslib/nf-projectedfslib-prjmarkdirectoryasplaceholder)**, and it is embedded in the **[PRJ_PLACEHOLDER_INFO](/windows/desktop/api/projectedfslib/ns-projectedfslib-prj_placeholder_info)** and **[PRJ_CALLBACK_DATA](/windows/desktop/api/projectedfslib/ns-projectedfslib-prj_callback_data)** structs.  The **PRJ_PLACEHOLDER_VERSION_INFO**.ContentID field is where the provider stores up to 128 bytes of version information for a file or directory.  The provider may then internally associate this value to some value that identifies a particular view.

For example, a provider that virtualizes a source control repository might choose to use a hash of a file's contents to serve as the ContentID, and it might use timestamps to identify views of the repository at various points in time.  The timestamps might be the times that commits to the repository were performed.

Using the example of a timestamp-indexed repository, a typical flow for using an item's ContentID might be:

1. The client establishes a view by specifying the timestamp at which to present the repository contents.  This would be done through some interface implemented by the provider, not via a ProjFS API.  For example, the provider may have a command-line tool that could be used to tell the provider which view the user desires.
1. When the client creates a handle to a virtualized file or directory, the provider creates a placeholder for it, using file system metadata from the backing store.  The particular set of metadata it uses is identified by the ContentID value associated with the timestamp of the desired view.  When the provider calls **[PrjWritePlaceholderInfo](/windows/desktop/api/projectedfslib/nf-projectedfslib-prjwriteplaceholderinfo)** to write the placeholder information, it supplies the ContentID in the VersionInfo member of the _placeholderInfo_ argument.  The provider should then record that a placeholder for that file or directory was created in this view.
1. When the client reads from a placeholder, the provider's **[PRJ_GET_FILE_DATA_CB](/windows/desktop/api/projectedfslib/nc-projectedfslib-prj_get_file_data_cb)** callback is invoked.  The _callbackData_ parameter's VersionInfo member contains the ContentID the provider specified in **PrjWritePlaceholderInfo** when it created the file placeholder.  The provider uses that ContentID to retrieve the correct contents of the file from its backing store.
1. The client requests a view change by specifying a new timestamp.  For each placeholder the provider created in the previous view, if a different version of that file exists in the new view the provider may replace the placeholder on disk with an updated one whose ContentID is associated with the new timestamp by calling **[PrjUpdateFileIfNeeded](/windows/desktop/api/projectedfslib/nf-projectedfslib-prjupdatefileifneeded)**.  Alternatively, the provider may delete the placeholder by calling **[PrjDeleteFile](/windows/desktop/api/projectedfslib/nf-projectedfslib-prjdeletefile)** so that the new view of the file will be projected in enumerations.  If the file does not exist in the new view, the provider must delete it by calling **PrjDeleteFile**.

Note that the provider must ensure that when the client enumerates a directory, the provider will supply the contents that correspond to the client's view.  For example, the provider could use the VersionInfo member of the _callbackData_ parameter of the **[PRJ_START_DIRECTORY_ENUMERATION_CB](/windows/desktop/api/projectedfslib/nc-projectedfslib-prj_start_directory_enumeration_cb)** and **[PRJ_GET_DIRECTORY_ENUMERATION_CB](/windows/desktop/api/projectedfslib/nc-projectedfslib-prj_get_directory_enumeration_cb)** callbacks to retrieve directory contents on the fly.  Alternatively it could build a directory structure for that view in its backing store as part of establishing the view, and then simply enumerate that structure.

> Whenever a provider callback is invoked for a placeholder or partial file, the version information the provider specified when creating the item is provided in the VersionInfo member of the callback's _callbackData_ parameter.

## Updating the View

Below is a sample function illustrating how a provider might update the local view when the user specifies a new timestamp.  The function retrieves a list of the placeholders the provider created for the view the user has just changed from, and updates the local cache state based on each placeholder's state in the new view.  For clarity, this routine omits certain complexities of dealing with the file system.  For example, in the old view a given directory may have existed with some files or directories in it, but in the new view that directory (and its contents) may no longer exist.  To avoid encountering errors in such a situation the provider should update the state of the file and directories beneath the virtualization root in a depth-first fashion.

```C++
typedef struct MY_ON_DISK_PLACEHOLDER MY_ON_DISK_PLACEHOLDER;

typedef struct MY_ON_DISK_PLACEHOLDER {
    MY_ON_DISK_PLACEHOLDER* Next;
    PWSTR RelativePath;
} MY_ON_DISK_PLACEHOLDER;

HRESULT
MyViewUpdater(
    _In_ PRJ_CALLBACK_DATA callbackData,
    _In_ time_t newViewTime
    )
{
    HRESULT hr = S_OK;

    // MyGetOnDiskPlaceholders is a routine the provider might implement to produce
    // a pointer to a list of the placeholders the provider has created in the view.
    MY_ON_DISK_PLACEHOLDER* placeholder = MyGetOnDiskPlaceholders();
    while (placeholder != NULL)
    {
        // MyGetProjectedFileInfo is a routine the provider might implement to
        // determine whether a given file exists in its backing store at a
        // particular timestamp.  If it does, the routine returns a pointer to
        // a PRJ_PLACEHOLDER_INFO struct populated with information about the
        // file.
        PRJ_PLACEHOLDER_INFO* newViewPlaceholderInfo = NULL;
        UINT32 newViewPlaceholderInfoSize = 0;

        newViewPlaceholderInfo = MyGetProjectedFileInfo(placeholder->RelativePath,
                                                 newViewTime,
                                                 &newViewPlaceholderInfoSize);
        if (newViewPlaceholderInfo == NULL)
        {
            // The file no longer exists in the new view.  We want to remove its
            // placeholder from the local cache.
            PRJ_UPDATE_FAILURE_CAUSES deleteFailureReason;
            hr = PrjDeleteFile(callbackData->NamespaceVirtualizationContext,
                               placeholder->RelativePath,
                               PRJ_UPDATE_ALLOW_DIRTY_METADATA
                               | PRJ_UPDATE_ALLOW_DIRTY_DATA
                               | PRJ_UPDATE_ALLOW_TOMBSTONE,
                               &deleteFailureReason);

            if (hr == HRESULT_FROM_WIN32(ERROR_FILE_SYSTEM_VIRTUALIZATION_INVALID_OPERATION))
            {
                wprintf(L"Could not delete [%ls].\n", placeholder->RelativePath);
                wprintf(L"Failure reason: 0x%x", deleteFailureReason);
                return hr;
            }
            else
            {
                wprintf(L"Error deleting [%ls]: 0x%08x",
                        placeholder->RelativePath,
                        hr);
                return hr;
            }

            // MyRemovePlaceholderData is a routine the provider might implement
            // to remove an item from its list of placeholders it has created in
            // the view.
            MyRemovePlaceholderData(placeholder);
        }
        else
        {
            // The file exists in the new view.  Its local cache state may need
            // to be updated, for example if its content is different in this view.
            // As an optimization, the provider may compare the file's ContentID
            // in the new view (stored in newViewPlaceholderInfo->ContentId) with
            // the ContentID it had in the old view.  If they are the same, calling
            // PrjUpdateFileIfNeeded would not be needed.
            PRJ_UPDATE_FAILURE_CAUSES updateFailureReason;
            hr = PrjUpdateFileIfNeeded(callbackData->NamespaceVirtualizationContext,
                                       placeholder->RelativePath,
                                       newViewPlaceholderInfo,
                                       newViewPlaceholderInfoSize,
                                       PRJ_UPDATE_ALLOW_DIRTY_METADATA
                                       | PRJ_UPDATE_ALLOW_DIRTY_DATA
                                       | PRJ_UPDATE_ALLOW_TOMBSTONE,
                                       &updateFailureReason);

            if (hr == HRESULT_FROM_WIN32(ERROR_FILE_SYSTEM_VIRTUALIZATION_INVALID_OPERATION))
            {
                wprintf(L"Could not update [%ls].\n", placeholder->RelativePath);
                wprintf(L"Failure reason: 0x%x", updateFailureReason);
                return hr;
            }
            else
            {
                wprintf(L"Error updating [%ls]: 0x%08x",
                        placeholder->RelativePath,
                        hr);
                return hr;
            }

            // MyUpdatePlaceholderData is a routine the provider might implement
            // to update information about a placeholder it has created in the view.
            MyUpdatePlaceholderData(placeholder, newViewPlaceholderInfo);
        }

        placeholder = placeholder->Next;
    }

    return hr;
}
```