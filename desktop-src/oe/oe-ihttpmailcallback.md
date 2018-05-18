---
title: IHTTPMailCallback interface
description: Callback interface for the HTTPMail transport.
ms.assetid: 'a83b495e-6303-404e-bf65-2b978b66723e'
keywords: ["IHTTPMailCallback interface Windows Mail (formerly Outlook Express)", "IHTTPMailCallback interface Windows Mail (formerly Outlook Express) , described"]
topic_type:
- apiref
api_name:
- IHTTPMailCallback
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IHTTPMailCallback interface

\[**IHTTPMailCallback** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Callback interface for the HTTPMail transport.

## Members

The **IHTTPMailCallback** interface inherits from [**ITransportCallback**](oe-itransportcallback.md) but does not have additional members.

## Remarks

This transport works in an asynchronous mode. It is assumed that the client application has a message pump on the thread in which a transport object is created.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





