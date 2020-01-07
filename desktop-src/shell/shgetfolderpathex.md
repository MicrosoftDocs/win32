---
UID: 
title: SHGetFolderPathEx function
description: Retrieves the path of a known folder identified by the KNOWNFOLDERID.
old-location: 
ms.assetid: na
ms.date: 04/10/2019
ms.keywords: SHGetFolderPath
ms.topic: reference
req.header: Shlobj.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Shell32.lib
req.dll: API-MS-Win-Storage-Exports-Internal-L1-1-0.dll
req.irql: 
topic_type:
- APIRef
api_type: 
api_location:
- API-MS-Win-Storage-Exports-Internal-L1-1-0.dll
api_name:
- SHGetFolderPathEx
targetos: Windows
req.typenames: 
req.redist: 
---

# SHGetFolderPathEx function

## Description

\[Some information relates to pre-released product which may be substantially modified before it's commercially released.
Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Retrieves the full path of a known folder identified by the folder's [KNOWNFOLDERID](/windows/desktop/shell/knownfolderid).
This extends [SHGetKnownFolderPath](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderpath) by allowing you to set the initial size of the string buffer.

```cpp
HRESULT WINAPI SHGetFolderPathEx(
  _In_     REFKNOWNFOLDERID rfid,
  _In_     DWORD            dwFlags,
  _In_opt_ HANDLE           hToken,
  _Out_    LPWSTR           pszPath,
  _In_     UINT             cchPath
);
```

## Parameters

### rfid [in]

A reference to the **KNOWNFOLDERID** that identifies the folder.

### dwFlags [in]

Flags that specify special retrieval options.
This value can be 0; otherwise, one or more of the [KNOWN_FOLDER_FLAG](/windows/desktop/api/shlobj_core/ne-shlobj_core-known_folder_flag) values.

### hToken [in, optional]

An [access token](/windows/desktop/SecAuthZ/access-tokens) that represents a particular user.
If this parameter is **NULL**, which is the most common usage, the function requests the known folder for the current user.

Request a specific user's folder by passing the *hToken* of that user.
This is typically done in the context of a service that has sufficient privileges to retrieve the token of a given user.
That token must be opened with [TOKEN_QUERY](/windows/desktop/SecAuthZ/access-rights-for-access-token-objects) and [TOKEN_IMPERSONATE](/windows/desktop/SecAuthZ/access-rights-for-access-token-objects) rights.
In some cases, you also need to include [TOKEN_DUPLICATE](/windows/desktop/SecAuthZ/access-rights-for-access-token-objects).
In addition to passing the user's *hToken*, the registry hive of that specific user must be mounted.
See [Access Control](/windows/desktop/SecAuthZ/access-control) for further discussion of access control issues.

Assigning the *hToken* parameter a value of -1 indicates the Default User.
This allows clients of [SHGetKnownFolderPath](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderpath) to find folder locations (such as the **Desktop** folder) for the Default User.
The Default User user profile is duplicated when any new user account is created, and includes special folders such as **Documents** and **Desktop**.
Any items added to the Default User folder also appear in any new user account.
Note that access to the Default User folders requires administrator privileges.

### pszPath [out]

A null-terminated, Unicode string.
This buffer must be of size cchPath.
When **SHGetFolderPathEx** returns successfully, this parameter contains the path for the known folder.

### cchPath [in]

The size of the *ppszPath* buffer, in characters.

## Returns

Returns **S_OK** if successful, or an error value otherwise.

## Remarks

Since [SHGetFolderPath](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha) is a wrapper for [SHGetKnownFolderPath](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderpath), this function (**SHGetFolderPathEx**) also serves as an extension to **SHGetFolderPath**.

## See also

[KNOWNFOLDERID](/windows/desktop/shell/knownfolderid)

[KNOWN_FOLDER_FLAG](/windows/desktop/api/shlobj_core/ne-shlobj_core-known_folder_flag)

[SHGetFolderPath](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha)

[SHGetKnownFolderIDList](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderidlist)

[SHGetKnownFolderPath](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderpath)
