---
title: IPOP3Transport InitNew method
description: Initializes the Internet transport.
ms.assetid: 9ea9fe51-adcb-4f17-9652-e1422d69152a
keywords:
- InitNew method Windows Mail (formerly Outlook Express)
- InitNew method Windows Mail (formerly Outlook Express) , IPOP3Transport interface
- IPOP3Transport interface Windows Mail (formerly Outlook Express) , InitNew method
topic_type:
- apiref
api_name:
- IPOP3Transport.InitNew
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

# IPOP3Transport::InitNew method

\[**IPOP3Transport::InitNew** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Initializes the Internet transport.

## Syntax


```C++
HRESULT InitNew(
  [in] LPSTR         pszLogFilePath,
  [in] IPOP3Callback *pCallback
);
```



## Parameters

<dl> <dt>

*pszLogFilePath* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the full path and name of the file in which to log the protocol commands. **NULL** is a valid value (no logging).

</dd> <dt>

*pCallback* \[in\]
</dt> <dd>

Type: **[**IPOP3Callback**](oe-ipop3callback.md)\***

Specifies a pointer to the transport callback interface.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                               | Description                                                      |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>              | Indicates that *pCallback* is **NULL**. <br/>              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>             | Indicates that an attempt to allocate memory failed. <br/> |
| <dl> <dt>**IXP\_E\_ALREADY\_CONNECTED**</dt> </dl> | Indicates that the transport is currently connected. <br/> |



 

## Remarks

This method must be called to start the transport before any other methods can be called.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





