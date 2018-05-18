---
title: IStoreNamespace DeleteFolder method
description: Recursively deletes a specified message folder and all items that are inside it, including child folders.
ms.assetid: '0061a609-4695-4e68-baaa-bbda56220bb6'
keywords: ["DeleteFolder method Windows Mail (formerly Outlook Express)", "DeleteFolder method Windows Mail (formerly Outlook Express) , IStoreNamespace interface", "IStoreNamespace interface Windows Mail (formerly Outlook Express) , DeleteFolder method"]
topic_type:
- apiref
api_name:
- IStoreNamespace.DeleteFolder
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreNamespace::DeleteFolder method

Recursively deletes a specified message folder and all items that are inside it, including child folders.

## Syntax


```C++
HRESULT DeleteFolder(
  [in] STOREFOLDERID dwFolderId,
  [in] DWORD         dwReserved
);
```



## Parameters

<dl> <dt>

*dwFolderId* \[in\]
</dt> <dd>

Type: **STOREFOLDERID**

Specifies the folder to be deleted.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *dwFolderId* is invalid.<br/>                                                                                                           |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**IStoreNamespace::Initialize**](oe-istorenamespace-initialize.md).<br/> |



 

## Remarks

Only user-created folders may be deleted. Special folders may not be deleted.

Deleted folders will be moved to the deleted items folder. If the folder specified by *dwFolderId* is already a child of the deleted items folder, the folder specified by *dwFolderId* and all items within it will be permanently deleted.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





