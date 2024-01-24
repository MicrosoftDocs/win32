---
title: Enumerating Files and Directories
description: Describes how a ProjFS provider participates in directory enumeration.
ms.assetid: <GUID-GOES-HERE>
ms.date: 09/25/2018
ms.topic: article
---

# Enumerating Files and Directories

When a provider first creates a virtualization root it is empty on the local system.  That is, none of the items in the backing data store have yet been cached to disk.  As each item is opened it is cached, but until an item is opened it only exists in the backing data store.

Since unopened items have no local presence, normal directory enumeration would not reveal their existence to the user.  Therefore the provider must participate in directory enumeration by returning information to ProjFS about items in its backing data store.  ProjFS merges the information from the provider with what is on the local file system to present to the user a unified list of the contents of a directory.

## Directory Enumeration Callbacks

To participate in directory enumeration the provider must implement the **[PRJ_START_DIRECTORY_ENUMERATION_CB](/windows/win32/api/projectedfslib/nc-projectedfslib-prj_start_directory_enumeration_cb)**, **[PRJ_GET_DIRECTORY_ENUMERATION_CB](/windows/win32/api/projectedfslib/nc-projectedfslib-prj_get_directory_enumeration_cb)**, and **[PRJ_END_DIRECTORY_ENUMERATION_CB](/windows/win32/api/projectedfslib/nc-projectedfslib-prj_end_directory_enumeration_cb)** callbacks.  When a directory under the provider's virtualization root gets enumerated, ProjFS performs the following actions:

1. ProjFS calls the provider's **PRJ_START_DIRECTORY_ENUMERATION_CB** callback to start an enumeration session.

    As part of processing this callback the provider should prepare to perform the enumeration.  For example, it should allocate any memory it may need to track the progress of the enumeration in its backing data store.

    ProjFS identifies the directory being enumerated in the **FilePathName** member of the callback's _callbackData_ parameter.  This is specified as a path relative to the virtualization root.  For example, if the virtualization root is located at `C:\virtRoot`, and the directory being enumerated is `C:\virtRoot\dir1\dir2`, the **FilePathName** member will contain `dir1\dir2`.  The provider will prepare to enumerate that path in its backing data store.  Depending on the capabilities of a provider's backing store it may make sense to perform the backing store enumeration in the **PRJ_START_DIRECTORY_ENUMERATION_CB** callback.

    Because multiple enumerations may occur in parallel in the same directory, each enumeration callback has an _enumerationId_ argument to enable the provider to associate the callback invocations into a single enumeration session.

    If the provider returns S_OK from the **PRJ_START_DIRECTORY_ENUMERATION_CB** callback, it must maintain any enumeration session information it has until ProjFS invokes the **PRJ_END_DIRECTORY_ENUMERATION_CB** callback with the same value for _enumerationId_.  If the provider returns an error from **PRJ_START_DIRECTORY_ENUMERATION_CB**, ProjFS will not invoke the **PRJ_END_DIRECTORY_ENUMERATION_CB** callback for that _enumerationId_.

1. ProjFS calls the provider's **PRJ_GET_DIRECTORY_ENUMERATION_CB** callback one or more times to get the directory contents from the provider.

    In response to this callback the provider returns a sorted list of items from its backing data store.

    The callback may provide a search expression in its _searchExpression_ parameter that the provider uses to scope the results of the enumeration.  If _searchExpression_ is NULL, the provider returns all the entries in the directory being enumerated.  If it is non-NULL, the provider can use **[PrjDoesNameContainWildCards](/windows/win32/api/projectedfslib/nf-projectedfslib-prjdoesnamecontainwildcards)** to determine whether there are wildcards in the expression.  If there are, the provider uses **[PrjFileNameMatch](/windows/win32/api/projectedfslib/nf-projectedfslib-prjfilenamematch)** to determine whether an entry in the directory matches the search expression.

    The provider should capture the value of _searchExpression_ on the first invocation of this callback.  It uses the captured value on any subsequent invocation of the callback in the same enumeration session, unless PRJ_CB_DATA_FLAG_ENUM_RESTART_SCAN is set in the **Flags** field of the callback's _callbackData_ parameter.  In that case it should recapture the value of _searchExpression_.

    If there are no matching entries in its backing store, the provider simply returns S_OK from the callback.  Otherwise the provider formats each matching entry from its backing store into a **[PRJ_FILE_BASIC_INFO](/windows/win32/api/projectedfslib/ns-projectedfslib-prj_file_basic_info)** structure, and then uses **[PrjFillDirEntryBuffer](/windows/win32/api/projectedfslib/nf-projectedfslib-prjfilldirentrybuffer)** to fill the buffer provided by the callback's _dirEntryBufferHandle_ parameter.  The provider keeps adding entries until it has added them all or until **PrjFillDirEntryBuffer** returns HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER).  Then the provider returns S_OK from the callback.  Note that the provider must add the entries to the _dirEntryBufferHandle_ buffer in the correct sort order.  The provider should use **[PrjFileNameCompare](/windows/win32/api/projectedfslib/nf-projectedfslib-prjfilenamecompare)** to determine the correct sort order.

    > The provider must supply a value for the **IsDirectory** member of **PRJ_FILE_BASIC_INFO**.  If **IsDirectory** is FALSE, the provider must also supply a value for the **FileSize** member.
    >
    > If the provider does not supply values for the **CreationTime**, **LastAccessTime**, **LastWriteTime**, and **ChangeTime** members, ProjFS will use the current system time.
    >
    > ProjFS will use whatever FILE_ATTRIBUTE flags the provider sets in the **FileAttributes** member except for FILE_ATTRIBUTE_DIRECTORY; it will set the correct value for FILE_ATTRIBUTE_DIRECTORY in the **FileAttributes** member according to the supplied value of the **IsDirectory** member.

    If **PrjFillDirEntryBuffer** returns HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER) before the provider runs out of entries to add to it, the provider must keep track of the entry it was trying to add when it received the error.  The next time ProjFS calls the **PRJ_GET_DIRECTORY_ENUMERATION_CB** callback for the same enumeration session, the provider must resume adding entries to the _dirEntryBufferHandle_ buffer with the entry it was trying to add.

    > If the backing store supports symbolic links, the provider must use **[PrjFillDirEntryBuffer2](/windows/win32/api/projectedfslib/nf-projectedfslib-prjfilldirentrybuffer2)** to fill the buffer provided by the callback's _dirEntryBufferHandle_ parameter.  **PrjFillDirEntryBuffer2** supports an extra buffer input that allows the provider to specify that the enumeration entry is a symbolic link and what its target is.  It otherwise behaves as described above for **PrjFillDirEntryBuffer**.  The following sample uses **PrjFillDirEntryBuffer2** to illustrate support for symbolic links.
    >
    > Note that **PrjFillDirEntryBuffer2** is supported as of Windows 10, version 2004.  A provider should probe for the existence of **PrjFillDirEntryBuffer2**, for instance by using **[GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress)**.

    ```C++
    typedef struct MY_ENUM_ENTRY MY_ENUM_ENTRY;

    typedef struct MY_ENUM_ENTRY {
        MY_ENUM_ENTRY* Next;
        PWSTR Name;
        BOOLEAN IsDirectory;
        INT64 FileSize;
        BOOLEAN IsSymlink;
        PWSTR SymlinkTarget;
    } MY_ENUM_ENTRY;

    typedef struct MY_ENUM_SESSION {
        GUID EnumerationId;
        PWSTR SearchExpression;
        USHORT SearchExpressionMaxLen;
        BOOLEAN SearchExpressionCaptured;
        MY_ENUM_ENTRY* EnumHead;
        MY_ENUM_ENTRY* LastEnumEntry;
        BOOLEAN EnumCompleted;
    } MY_ENUM_SESSION;

    HRESULT
    MyGetEnumCallback(
        _In_ const PRJ_CALLBACK_DATA* callbackData,
        _In_ const GUID* enumerationId,
        _In_opt_z_ PCWSTR searchExpression,
        _In_ PRJ_DIR_ENTRY_BUFFER_HANDLE dirEntryBufferHandle
        )
    {
        // MyGetEnumSession is a routine the provider might implement to find
        // information about the enumeration session that it first stored
        // when processing its PRJ_START_DIRECTORY_ENUMERATION_CB callback.
        //
        // In this example the PRJ_START_DIRECTORY_ENUMERATION_CB callback has
        // already retrieved a list of the items in the backing store located at
        // callbackData->FilePathName, sorted them using PrjFileNameCompare()
        // to determine collation order, and stored the list in session->EnumHead.
        MY_ENUM_SESSION* session = NULL;
        session = MyGetEnumSession(enumerationId);

        if (session == NULL)
        {
            return HRESULT_FROM_WIN32(ERROR_INVALID_PARAMETER);
        }

        if (!session->SearchExpressionCaptured ||
            (callbackData->Flags & PRJ_CB_DATA_FLAG_ENUM_RESTART_SCAN))
        {
            if (searchExpression != NULL)
            {
                if (wcsncpy_s(session->SearchExpression,
                              session->SearchExpressionMaxLen,
                              searchExpression,
                              wcslen(searchExpression)))
                {
                    // Failed to copy the search expression; perhaps the provider
                    // could try reallocating session->SearchExpression.
                }
            }
            else
            {
                if (wcsncpy_s(session->SearchExpression,
                              session->SearchExpressionMaxLen,
                              "*",
                              1))
                {
                    // Failed to copy the search expression; perhaps the provider
                    // could try reallocating session->SearchExpression.
                }
            }
            session->SearchExpressionCaptured = TRUE;
        }

        MY_ENUM_ENTRY* enumHead = NULL;

        // We have to start the enumeration from the beginning if we aren't
        // continuing an existing session or if the caller is requesting a restart.
        if (((session->LastEnumEntry == NULL) &&
             !session->EnumCompleted) ||
            (callbackData->Flags & PRJ_CB_DATA_FLAG_ENUM_RESTART_SCAN))
        {
            // Ensure that if the caller is requesting a restart we reset our
            // bookmark of how far we got in the enumeration.
            session->LastEnumEntry = NULL;

            // In case we're restarting ensure we don't think we're done.
            session->EnumCompleted = FALSE;

            // We need to start considering items from the beginning of the list
            // retrieved from the backing store.
            enumHead = session->EnumHead;
        }
        else
        {
            // We are resuming an existing enumeration session.  Note that
            // session->LastEnumEntry may be NULL.  That is okay; it means
            // we got all the entries the last time this callback was invoked.
            // Returning S_OK without adding any new entries to the
            // dirEntryBufferHandle buffer signals ProjFS that the enumeration
            // has returned everything it can.
            enumHead = session->LastEnumEntry;
        }

        if (enumHead == NULL)
        {
            // There are no items to return.  Remember that we've returned everything
            // we can.
            session->EnumCompleted = TRUE;
        }
        else
        {
            MY_ENUM_ENTRY* thisEntry = enumHead;
            int entriesAdded = 0;
            while (thisEntry != NULL)
            {
                // We'll insert the entry into the return buffer if it matches
                // the search expression captured for this enumeration session.
                if (PrjFileNameMatch(thisEntry->Name, session->SearchExpression))
                {
                    PRJ_FILE_BASIC_INFO fileBasicInfo = {};
                    fileBasicInfo.IsDirectory = thisEntry->IsDirectory;
                    fileBasicInfo.FileSize = thisEntry->FileSize;

                    // If our backing store says this is really a symbolic link,
                    // set up to tell ProjFS that it is a symlink and what its
                    // target is.
                    PRJ_EXTENDED_INFO extraInfo = {};
                    if (thisEntry->IsSymlink)
                    {
                        extraInfo.InfoType = PRJ_EXT_INFO_SYMLINK;
                        extraInfo.Symlink.TargetName = thisEntry->SymlinkTarget;
                    }

                    // Format the entry for return to ProjFS.
                    HRESULT fillResult = PrjFillDirEntryBuffer2(dirEntryBufferHandle,
                                                                thisEntry->Name,
                                                                &fileBasicInfo,
                                                                thisEntry->IsSymlink ? &extraInfo : NULL);

                    if (fillResult == HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER))
                    {
                        if (entriesAdded > 0)
                        {
                            // We couldn't add this entry to the buffer; remember where we left
                            // off for the next time we're called for this enumeration session.
                            session->LastEnumEntry = thisEntry;
                            return S_OK;
                        }
                        else
                        {
                            // The buffer should always have enough space for at least one entry, but
                            // we could not add even one entry. Return the error.
                            return fillResult;
                        }
                    }
                    else
                    {
                        // Any other error is unexpected. NOTE: Be sure to check for E_INVALIDARG to
                        // ensure you are calling PrjFillDirEntryBuffer2 correctly.
                        return fillResult;
                    }

                    ++entriesAdded;
                }

                thisEntry = thisEntry->Next;
            }

            // We reached the end of the list of entries; remember that we've returned
            // everything we can.
            session->EnumCompleted = TRUE;
        }

        return S_OK;
    }
    ```

1. ProjFS calls the provider's **PRJ_END_DIRECTORY_ENUMERATION_CB** callback to end the enumeration session.

    The provider should perform any cleanup it needs to do to end the enumeration session, such as deallocate memory allocated as part of processing **PRJ_START_DIRECTORY_ENUMERATION_CB**.
