---
title: IStoreNamespace OpenFolder method
description: Opens a user-created message folder. User-created folders can be opened, renamed, moved, and deleted.
ms.assetid: 8c8af075-30b5-45cc-94e6-c967e448ab8b
keywords:
- OpenFolder method Windows Mail (formerly Outlook Express)
- OpenFolder method Windows Mail (formerly Outlook Express) , IStoreNamespace interface
- IStoreNamespace interface Windows Mail (formerly Outlook Express) , OpenFolder method
topic_type:
- apiref
api_name:
- IStoreNamespace.OpenFolder
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

# IStoreNamespace::OpenFolder method

Opens a user-created message folder. User-created folders can be opened, renamed, moved, and deleted.

## Syntax


```C++
HRESULT OpenFolder(
  [in]  STOREFOLDERID dwFolderId,
  [in]  DWORD         dwReserved,
  [out] IStoreFolder  **ppFolder
);
```



## Parameters

<dl> <dt>

*dwFolderId* \[in\]
</dt> <dd>

Type: **STOREFOLDERID**

Specifies the folder to open.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> <dt>

*ppFolder* \[out\]
</dt> <dd>

Type: **[**IStoreFolder**](oe-istorefolder.md)\*\***

Reference to a pointer that will receive the created [**IStoreFolder**](oe-istorefolder.md) object that represents the opened folder.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *dwFolderId* is invalid, the value of *dwReserved* is not 0, or *ppFolder* is **NULL**.<br/>                                            |
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



 

 





