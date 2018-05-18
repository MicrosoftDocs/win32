---
title: ISMTPTransport SendDataStream method
description: Sends a Simple Mail Transport Protocol (SMTP) message stream to the server.
ms.assetid: '61dd2fdc-a3cf-4b67-8114-b4c246799939'
keywords: ["SendDataStream method Windows Mail (formerly Outlook Express)", "SendDataStream method Windows Mail (formerly Outlook Express) , ISMTPTransport interface", "ISMTPTransport interface Windows Mail (formerly Outlook Express) , SendDataStream method"]
topic_type:
- apiref
api_name:
- ISMTPTransport.SendDataStream
api_location:
- Inetcomm.dll
api_type:
- COM
---

# ISMTPTransport::SendDataStream method

\[**ISMTPTransport::SendDataStream** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends a Simple Mail Transport Protocol (SMTP) message stream to the server.

## Syntax


```C++
HRESULT SendDataStream(
  [in] IStream *pStream,
  [in] ULONG   cbSize
);
```



## Parameters

<dl> <dt>

*pStream* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that contains the ANSI MIME/[RFC 822](http://www.ietf.org/rfc/rfc822.txt) message stream.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the size of the message in bytes.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                              |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success. <br/>                                                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *pStream* is **NULL**. <br/>                                                        |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed. <br/>                                         |
| <dl> <dt>**IXP\_E\_NOT\_CONNECTED**</dt> </dl>       | Indicates that either the server connection has not yet been established or it has been lost.<br/> |
| <dl> <dt>**IXP\_E\_SOCKET\_WRITE\_ERROR**</dt> </dl> | Indicates that an unknown error occurred. <br/>                                                    |



 

## Remarks

This method calls the [**ISMTPTransport::CommandDOT**](oe-ismtptransport-commanddot.md) method when it is finished.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





