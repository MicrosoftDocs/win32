---
title: IHTTPMailTransport CommandPROPPATCH method
description: Sends the PROPPATCH command to the HTTPMail server.
ms.assetid: bee4fb61-47b6-4940-9039-f81544dec016
keywords:
- CommandPROPPATCH method Windows Mail (formerly Outlook Express)
- CommandPROPPATCH method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface
- IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , CommandPROPPATCH method
topic_type:
- apiref
api_name:
- IHTTPMailTransport.CommandPROPPATCH
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

# IHTTPMailTransport::CommandPROPPATCH method

\[**IHTTPMailTransport::CommandPROPPATCH** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the PROPPATCH command to the HTTPMail server.

## Syntax


```C++
HRESULT CommandPROPPATCH(
  [in] LPCSTR            pszPath,
  [in] IPropPatchRequest *pRequest,
  [in] DWORD             dwContext
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the resource to set the properties for.

</dd> <dt>

*pRequest* \[in\]
</dt> <dd>

Type: **[**IPropPatchRequest**](oe-iproppatchrequest.md)\***

Specifies a pointer to the [**IPropPatchRequest**](oe-iproppatchrequest.md) object for managing properties.

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
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszPath* or *pRequest* is **NULL**. <br/>  |
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



 

 





