---
title: IHTTPMailTransport CommandBDELETE method
description: Sends the BDELETE command to the HTTPMail server.
ms.assetid: f5a9727b-aa7b-486a-9890-013ed7820e4b
keywords:
- CommandBDELETE method Windows Mail (formerly Outlook Express)
- CommandBDELETE method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface
- IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , CommandBDELETE method
topic_type:
- apiref
api_name:
- IHTTPMailTransport.CommandBDELETE
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

# IHTTPMailTransport::CommandBDELETE method

\[**IHTTPMailTransport::CommandBDELETE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the BDELETE command to the HTTPMail server.

## Syntax


```C++
HRESULT CommandBDELETE(
  [in] LPCSTR           pszSourceCollection,
  [in] LPHTTPTARGETLIST pTargets,
  [in] DWORD            dwContext
);
```



## Parameters

<dl> <dt>

*pszSourceCollection* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the collection resource that contains the resources to delete.

</dd> <dt>

*pTargets* \[in\]
</dt> <dd>

Type: **LPHTTPTARGETLIST**

Specifies a pointer to the [**HTTPTARGETLIST**](oe-httptargetlist.md) structure that contains the list of target resources to be deleted.

</dd> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                 |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszSourceCollection* or *pTargets* is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>            |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





