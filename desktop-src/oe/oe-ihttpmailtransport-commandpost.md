---
title: IHTTPMailTransport CommandPOST method
description: Sends the POST command to the HTTPMail server.
ms.assetid: baa959bc-ee63-42a1-ae12-7bda6b1657c3
keywords:
- CommandPOST method Windows Mail (formerly Outlook Express)
- CommandPOST method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface
- IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , CommandPOST method
topic_type:
- apiref
api_name:
- IHTTPMailTransport.CommandPOST
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

# IHTTPMailTransport::CommandPOST method

\[**IHTTPMailTransport::CommandPOST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the POST command to the HTTPMail server.

## Syntax


```C++
HRESULT CommandPOST(
  [in] LPCSTR  pszPath,
  [in] IStream *pStream,
  [in] LPCSTR  pszContentType,
  [in] DWORD   dwContext
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the resource under which the entity stream should stored.

</dd> <dt>

*pStream* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies a pointer to an [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that contains the data stream to be posted to the server.

</dd> <dt>

*pszContentType* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that indicates the type of content being posted.

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
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszPath* or *pStream* is **NULL**. <br/>   |
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



 

 





