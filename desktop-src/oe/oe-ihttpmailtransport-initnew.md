---
title: IHTTPMailTransport InitNew method
description: Initializes the HTTPMail transport.
ms.assetid: 'a33d322f-e74c-4fff-a032-de66676f979e'
keywords: ["InitNew method Windows Mail (formerly Outlook Express)", "InitNew method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface", "IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , InitNew method"]
topic_type:
- apiref
api_name:
- IHTTPMailTransport.InitNew
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IHTTPMailTransport::InitNew method

\[**IHTTPMailTransport::InitNew** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Initializes the HTTPMail transport.

## Syntax


```C++
HRESULT InitNew(
  [in] LPCSTR            pszUserAgent,
  [in] LPCSTR            pszLogFilePath,
  [in] IHTTPMailCallback *pCallback
);
```



## Parameters

<dl> <dt>

*pszUserAgent* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the user agent string sent in HTTP queries.

</dd> <dt>

*pszLogFilePath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the full path and name of the file in which to log the protocol commands. **NULL** is a valid value (no logging).

</dd> <dt>

*pCallback* \[in\]
</dt> <dd>

Type: **[**IHTTPMailCallback**](oe-ihttpmailcallback.md)\***

Specifies a pointer to the transport callback interface.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                | Description                                                                       |
|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Indicates success. <br/>                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | Indicates that *pszUserAgent* or *pCallback* is **NULL**. <br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>              | Indicates that an attempt to allocate memory failed. <br/>                  |
| <dl> <dt>**IXP\_E\_ALREADY\_CONNECTED**</dt> </dl>  | Indicates that the transport is currently connected. <br/>                  |
| <dl> <dt>**IXP\_E\_SOCKET\_INIT\_ERROR**</dt> </dl> | Indicates that the TCP/IP socket connection could not be initialized. <br/> |



 

## Remarks

This method must be called to start the transport before any other methods can be called.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





