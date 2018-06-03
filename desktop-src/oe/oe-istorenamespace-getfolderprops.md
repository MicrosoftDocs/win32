---
title: IStoreNamespace GetFolderProps method
description: Gets properties of the specified message folder.
ms.assetid: ac32300f-bf50-4aeb-98ea-f09ef8b6fd55
keywords:
- GetFolderProps method Windows Mail (formerly Outlook Express)
- GetFolderProps method Windows Mail (formerly Outlook Express) , IStoreNamespace interface
- IStoreNamespace interface Windows Mail (formerly Outlook Express) , GetFolderProps method
topic_type:
- apiref
api_name:
- IStoreNamespace.GetFolderProps
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IStoreNamespace::GetFolderProps method

Gets properties of the specified message folder.

## Syntax


```C++
HRESULT GetFolderProps(
  [in]      STOREFOLDERID dwFolderId,
  [in]      DWORD         dwReserved,
  [in, out] LPFOLDERPROPS pProps
);
```



## Parameters

<dl> <dt>

*dwFolderId* \[in\]
</dt> <dd>

Type: **STOREFOLDERID**

Value that identifies the folder from which properties are to be retrieved.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> <dt>

*pProps* \[in, out\]
</dt> <dd>

Type: **LPFOLDERPROPS**

Pointer to a [**FOLDERPROPS**](oe-folderprops.md) structure that receives the properties.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *dwFolderId* is invalid, *dwReserved* is not 0, or *pProps* is **NULL**.<br/>                                                           |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**IStoreNamespace::Initialize**](oe-istorenamespace-initialize.md).<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





