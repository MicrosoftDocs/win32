---
title: IStoreNamespace CreateFolder method
description: Creates a new message folder.
ms.assetid: 5a71c97e-80ee-4bb3-a5b8-2f21a1225584
keywords:
- CreateFolder method Windows Mail (formerly Outlook Express)
- CreateFolder method Windows Mail (formerly Outlook Express) , IStoreNamespace interface
- IStoreNamespace interface Windows Mail (formerly Outlook Express) , CreateFolder method
topic_type:
- apiref
api_name:
- IStoreNamespace.CreateFolder
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IStoreNamespace::CreateFolder method

Creates a new message folder.

## Syntax


```C++
HRESULT CreateFolder(
  [in]  STOREFOLDERID   dwParentId,
  [in]  LPCSTR          pszName,
  [in]  DWORD           dwReserved,
  [out] LPSTOREFOLDERID pdwFolderId
);
```



## Parameters

<dl> <dt>

*dwParentId* \[in\]
</dt> <dd>

Type: **STOREFOLDERID**

Specifies the parent message folder that the created folder will be a child of.

</dd> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the new display name of the created folder.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> <dt>

*pdwFolderId* \[out\]
</dt> <dd>

Type: **LPSTOREFOLDERID**

Pointer that receives the ID of the created folder.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *dwReserved* is not 0, the value of *dwParentId*, is invalid, or the value of *pszName* or *pdwFolderId* is **NULL**.<br/>              |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**IStoreNamespace::Initialize**](oe-istorenamespace-initialize.md).<br/> |



 

## Remarks

Each created folder must be a child of an existing parent folder that is not the root folder. If you specify a value of **FOLDERID\_ROOT** in the *dwParentId*, the method will fail.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





