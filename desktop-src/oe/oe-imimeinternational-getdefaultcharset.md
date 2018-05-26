---
title: IMimeInternational GetDefaultCharset method
description: Gets a handle to the current default character set for MimeOLE.
ms.assetid: 186767f8-021f-4173-85db-c1b4fe53bd24
keywords:
- GetDefaultCharset method Windows Mail (formerly Outlook Express)
- GetDefaultCharset method Windows Mail (formerly Outlook Express) , IMimeInternational interface
- IMimeInternational interface Windows Mail (formerly Outlook Express) , GetDefaultCharset method
topic_type:
- apiref
api_name:
- IMimeInternational.GetDefaultCharset
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

# IMimeInternational::GetDefaultCharset method

Gets a handle to the current default character set for MimeOLE.

## Syntax


```C++
HRESULT GetDefaultCharset(
  [out] LPHCHARSET phCharset
);
```



## Parameters

<dl> <dt>

*phCharset* \[out\]
</dt> <dd>

Type: **LPHCHARSET**

Receives the handle of the default character set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                  |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that there is no default character set.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *phCharset* is **NULL**. <br/>          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





