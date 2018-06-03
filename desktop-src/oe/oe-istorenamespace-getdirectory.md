---
title: IStoreNamespace GetDirectory method
description: Gets the file path of the message store.
ms.assetid: e049a1c3-a734-42e1-84b7-8ec5e10de6a7
keywords:
- GetDirectory method Windows Mail (formerly Outlook Express)
- GetDirectory method Windows Mail (formerly Outlook Express) , IStoreNamespace interface
- IStoreNamespace interface Windows Mail (formerly Outlook Express) , GetDirectory method
topic_type:
- apiref
api_name:
- IStoreNamespace.GetDirectory
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

# IStoreNamespace::GetDirectory method

Gets the file path of the message store.

## Syntax


```C++
HRESULT GetDirectory(
  [in, out] LPSTR pszPath,
  [in]      DWORD cchMaxPath
);
```



## Parameters

<dl> <dt>

*pszPath* \[in, out\]
</dt> <dd>

Type: **LPSTR**

Pointer that receives the path.

</dd> <dt>

*cchMaxPath* \[in\]
</dt> <dd>

Type: **DWORD**

Value that describes the length of *pszPath*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *pszPath* is **NULL**.<br/>                                                                                                             |
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



 

 





