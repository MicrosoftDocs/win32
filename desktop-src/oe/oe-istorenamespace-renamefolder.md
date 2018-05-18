---
title: IStoreNamespace RenameFolder method
description: Renames a user-created message folder.
ms.assetid: 'b4491cd1-06c4-44bf-9e2d-35303ca9acb3'
keywords: ["RenameFolder method Windows Mail (formerly Outlook Express)", "RenameFolder method Windows Mail (formerly Outlook Express) , IStoreNamespace interface", "IStoreNamespace interface Windows Mail (formerly Outlook Express) , RenameFolder method"]
topic_type:
- apiref
api_name:
- IStoreNamespace.RenameFolder
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreNamespace::RenameFolder method

Renames a user-created message folder.

## Syntax


```C++
HRESULT RenameFolder(
  [in] STOREFOLDERID dwFolderId,
  [in] DWORD         dwReserved,
  [in] LPCSTR        pszNewName
);
```



## Parameters

<dl> <dt>

*dwFolderId* \[in\]
</dt> <dd>

Type: **STOREFOLDERID**

Specifies the folder to be renamed.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> <dt>

*pszNewName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the new display name for the folder.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *dwFolderId* is invalid, *dwReserved* is not 0, or *pszNewName* is **NULL**.<br/>                                                       |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**IStoreNamespace::Initialize**](oe-istorenamespace-initialize.md).<br/> |



 

## Remarks

Only user-created folders can be renamed. Special folders cannot be renamed.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





