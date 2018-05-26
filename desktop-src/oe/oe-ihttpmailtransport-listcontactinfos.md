---
title: IHTTPMailTransport ListContactInfos method
description: Returns contact information in the specified collection.
ms.assetid: e275736f-ccf7-473c-8074-c8708f30d12e
keywords:
- ListContactInfos method Windows Mail (formerly Outlook Express)
- ListContactInfos method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface
- IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , ListContactInfos method
topic_type:
- apiref
api_name:
- IHTTPMailTransport.ListContactInfos
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

# IHTTPMailTransport::ListContactInfos method

\[**IHTTPMailTransport::ListContactInfos** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns contact information in the specified collection.

## Syntax


```C++
HRESULT ListContactInfos(
  [in] LPCSTR pszCollectionPath,
  [in] DWORD  dwContext
);
```



## Parameters

<dl> <dt>

*pszCollectionPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the resource. It is assumed that this parameter points to a collection resource.

</dd> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszCollectionPath* is **NULL**. <br/>      |
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



 

 





