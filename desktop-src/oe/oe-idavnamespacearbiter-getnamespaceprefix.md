---
title: IDAVNamespaceArbiter GetNamespacePrefix method
description: Retrieves the prefix of the namespace specified by the ID.
ms.assetid: 05a2769f-9cbc-4688-83a1-120e2e37f845
keywords:
- GetNamespacePrefix method Windows Mail (formerly Outlook Express)
- GetNamespacePrefix method Windows Mail (formerly Outlook Express) , IDAVNamespaceArbiter interface
- IDAVNamespaceArbiter interface Windows Mail (formerly Outlook Express) , GetNamespacePrefix method
topic_type:
- apiref
api_name:
- IDAVNamespaceArbiter.GetNamespacePrefix
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

# IDAVNamespaceArbiter::GetNamespacePrefix method

\[**IDAVNamespaceArbiter::GetNamespacePrefix** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the prefix of the namespace specified by the ID.

## Syntax


```C++
HRESULT GetNamespacePrefix(
  [in]  DWORD dwNamespaceID,
  [out] LPSTR *ppszNamespacePrefix
);
```



## Parameters

<dl> <dt>

*dwNamespaceID* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the ID of the namespace.

</dd> <dt>

*ppszNamespacePrefix* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the prefix.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppszNamespacePrefix* is **NULL**. <br/>    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





