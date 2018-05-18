---
title: IStoreNamespace MoveFolder method
description: Moves a user-created message folder to become the child of a specified parent message folder.
ms.assetid: '460488a4-518d-429f-aabf-3f76ba96ed10'
keywords: ["MoveFolder method Windows Mail (formerly Outlook Express)", "MoveFolder method Windows Mail (formerly Outlook Express) , IStoreNamespace interface", "IStoreNamespace interface Windows Mail (formerly Outlook Express) , MoveFolder method"]
topic_type:
- apiref
api_name:
- IStoreNamespace.MoveFolder
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreNamespace::MoveFolder method

Moves a user-created message folder to become the child of a specified parent message folder.

## Syntax


```C++
HRESULT MoveFolder(
  [in] STOREFOLDERID dwFolderId,
  [in] STOREFOLDERID dwParentId,
  [in] DWORD         dwReserved
);
```



## Parameters

<dl> <dt>

*dwFolderId* \[in\]
</dt> <dd>

Type: **STOREFOLDERID**

Specifies the folder to be moved.

</dd> <dt>

*dwParentId* \[in\]
</dt> <dd>

Type: **STOREFOLDERID**

Specifies the parent folder under which the folder specified by *dwFolderId* will reside.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                               |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | An invalid argument was passed to the method.<br/>                                  |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace is not initialized.<br/>                                              |
| <dl> <dt>**STORE\_E\_CANTMOVESPECIAL**</dt> </dl>     | The folder specified by *dwFolderId* is a special folder, and cannot be moved.<br/> |
| <dl> <dt>**STORE\_E\_CANTMOVESERVERS**</dt> </dl>     | The folder specified by *dwFolderId* is a server, and cannot be moved.<br/>         |



 

## Remarks

Only user-created folders can be moved. Special folders cannot be moved, though user-created folders may be moved to become child folders of special folders.

To move a folder so that it is the child of the root folder, set the value of *dwParentId* to **FOLDERID\_ROOT**.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





