---
description: Determines whether the Shell will be allowed to move, copy, delete, or rename a folder in a cloud provider's sync root.
title: IStorageProviderCopyHook::CopyCallback
ms.topic: reference
ms.date: 11/11/2020
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStorageProviderCopyHook::CopyCallback
api_type: 
- COM
api_location: 
- shobjidl.h
---

# IStorageProviderCopyHook::CopyCallback method

Determines whether the Shell will be allowed to move, copy, delete, or rename a folder in a cloud provider's sync root.

## Syntax

```C++
HRESULT CopyCallback( 
    HWND hwnd,
    UINT operation,
    UINT flags,
    LPCWSTR srcFile,
    DWORD srcAttribs,
    LPCWSTR destFile,
    DWORD destAttribs,
    UINT* result
);
```

## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

A handle to the window that the copy hook handler should use as the parent for any user interface elements the handler may need to display. If **FOF_SILENT** is specified in *operation*, the method should ignore this parameter.

</dd> </dl>

<dl> <dt>

*operation* \[in\]
</dt> <dd>

The operation to perform. This parameter can be one of the values listed under the **wFunc** member of the [SHFILEOPSTRUCT](/windows/win32/api/shellapi/ns-shellapi-shfileopstructa) structure.

</dd> </dl>

<dl> <dt>

*flags* \[in\]
</dt> <dd>

The flags that control the operation. This parameter can be one or more of the values listed under the *fFlags* member of the [SHFILEOPSTRUCT](/windows/desktop/api/shellapi/ns-shellapi-shfileopstructa) structure.

For printer copy hooks, this value is one of the following values defined in shellapi.h.

| Value       | Description |
|-------------|------------|
|  **PO_DELETE**      | A printer is being deleted. The *srcFile* parameter points to the full path to the specified printer.           |
|  **PO_RENAME**       | A printer is being renamed. The *srcFile* parameter points to the printer's new name. The *destFile* parameter points to the old name.           |
| **PO_PORTCHANGE**    | Not supported. Do not use.          |
| **PO_REN_PORT**    | Not supported. Do not use.           |

</dd> </dl>

<dl> <dt>

*srcFile* \[in\]
</dt> <dd>

A pointer to a string that contains the name of the source folder.

</dd> </dl>

*srcAttribs* \[in\]
</dt> <dd>

The attributes of the source folder. This parameter can be a combination of any of the file attribute flags (FILE_ATTRIBUTE_*) defined in the header files. See [File Attribute Constants](../fileio/file-attribute-constants.md).

</dd> </dl>

*destFile* \[in\]
</dt> <dd>

A pointer to a string that contains the name of the destination folder.

</dd> </dl>

*destAttribs* \[in\]
</dt> <dd>

The attributes of the destination folder. This parameter can be a combination of any of the file attribute flags (FILE_ATTRIBUTE_*) defined in the header files. See [File Attribute Constants](../fileio/file-attribute-constants.md).

</dd> </dl>

*result* \[out\]
</dt> <dd>

The integer value that indicates whether the Shell should perform the operation. One of the following:

| Value       | Description |
|-------------|------------|
| **IDYES**       | Allows the operation.           |
| **IDNO**        | Prevents the operation on this folder but continues with any other operations that have been approved (for example, a batch copy operation).           |
| **IDCANCEL**    | Prevents the current operation and cancels any pending operations.           |


</dd> </dl>


## Return value

Returns **S_OK** if successful, or an error code otherwise.

## Remarks

The Shell calls the cloud provider's copy hook handler for every folder under the registered sync root. To register a copy hook handler for cloud folders, set the **CopyHook** value under the **HKEY_LOCAL_MACHINE/Software/Microsoft/Windows/CurrentVersion/Explorer/SyncRootManager/{SyncRootId}** key to the CLSID of the copy hook object.

When the **CopyCallback** method is called, the Shell initializes the [IStorageProviderCopyHook](nn-shobjidl-istorageprovidercopyhook.md) interface directly without using an [IShellExtInit](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellextinit) interface first.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 Insider Preview Build 19624                                |
| Header                   | shobjidl.h   |

## See also

[Build a Cloud Sync Engine that Supports Placeholder Files](../cfapi/build-a-cloud-file-sync-engine.md)