---
title: IInternetTransport Connect method
description: Connects the transport to the specified server.
ms.assetid: '4859f2b1-fa96-4141-994e-816386b6ef3c'
keywords: ["Connect method Windows Mail (formerly Outlook Express)", "Connect method Windows Mail (formerly Outlook Express) , IInternetTransport interface", "IInternetTransport interface Windows Mail (formerly Outlook Express) , Connect method"]
topic_type:
- apiref
api_name:
- IInternetTransport.Connect
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IInternetTransport::Connect method

\[**IInternetTransport::Connect** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Connects the transport to the specified server.

## Syntax


```C++
HRESULT Connect(
  [in] LPINETSERVER pInetServer,
  [in] boolean      fAuthenticate,
  [in] boolean      fCommandLogging
);
```



## Parameters

<dl> <dt>

*pInetServer* \[in\]
</dt> <dd>

Type: **LPINETSERVER**

Specifies a pointer to an [**INETSERVER**](oe-inetserver.md) structure that contains the Internet server connection information.

</dd> <dt>

*fAuthenticate* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether the transport should authenticate the server.



| Value                                                                                                                                                                                                                                                                                    | Meaning                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <span id="iitAUTHENTICATE"></span><span id="iitauthenticate"></span><span id="IITAUTHENTICATE"></span><dl> <dt>**iitAUTHENTICATE**</dt> <dt>**TRUE**</dt> </dl>                       | Indicates that the transport should authenticate the server (**TRUE**). <br/> |
| <span id="iitDONT_AUTHENTICATE"></span><span id="iitdont_authenticate"></span><span id="IITDONT_AUTHENTICATE"></span><dl> <dt>**iitDONT\_AUTHENTICATE**</dt> <dt>**FALSE**</dt> </dl> | Indicates that the client should authenticate the server (**FALSE**). <br/>   |



 

</dd> <dt>

*fCommandLogging* \[in\]
</dt> <dd>

Type: **boolean**

If you pass **FALSE**, the [**OnCommand**](oe-itransportcallback-oncommand.md) method will never be called.



| Value                                                                                                                                                                                                                                                                                    | Meaning                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| <span id="iitENABLE_ONCOMMAND"></span><span id="iitenable_oncommand"></span><span id="IITENABLE_ONCOMMAND"></span><dl> <dt>**iitENABLE\_ONCOMMAND**</dt> <dt>**TRUE**</dt> </dl>      | Constant for **TRUE**.<br/>  |
| <span id="iitDISABLE_ONCOMMAND"></span><span id="iitdisable_oncommand"></span><span id="IITDISABLE_ONCOMMAND"></span><dl> <dt>**iitDISABLE\_ONCOMMAND**</dt> <dt>**FALSE**</dt> </dl> | Constant for **FALSE**.<br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                   | Description                                                                            |
|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success. <br/>                                                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that *pInetServer* is **NULL** or one of its members is invalid. <br/> |
| <dl> <dt>**IXP\_E\_ALREADY\_CONNECTED**</dt> </dl>     | Indicates that the transport is currently connected and busy. <br/>              |
| <dl> <dt>**IXP\_E\_LOAD\_SICILY\_FAILED**</dt> </dl>   | Indicates that SPA failed. <br/>                                                 |
| <dl> <dt>**IXP\_E\_NOT\_INIT**</dt> </dl>              | Indicates that the transport has not been initialized. <br/>                     |
| <dl> <dt>**IXP\_E\_SOCKET\_INIT\_ERROR**</dt> </dl>    | Indicates that the TCP/IP socket connection could not be initialized. <br/>      |
| <dl> <dt>**IXP\_E\_SOCKET\_CONNECT\_ERROR**</dt> </dl> | Indicates that the connection to the TCP/IP socket failed. <br/>                 |



 

## Remarks

This method call is asynchronous.

Each transport defines a terminal connect state. For example, Simple Mail Transport Protocol (SMTP) defines the connect state by SMTP\_CONNECTED.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





