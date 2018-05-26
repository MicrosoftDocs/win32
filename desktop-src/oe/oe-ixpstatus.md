---
title: IXPSTATUS enumeration
description: Indicates the transport status types.
ms.assetid: 2dbe7213-193c-41f4-99fe-3c428be66188
keywords:
- IXPSTATUS enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IXPSTATUS enumeration

\[**IXPSTATUS** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates the transport status types.

## Syntax


```C++
typedef enum tagIXPSTATUS { 
  IXP_FINDINGHOST    = 0,
  IXP_CONNECTING     = 1,
  IXP_SECURING       = 2,
  IXP_CONNECTED      = 3,
  IXP_AUTHORIZING    = 4,
  IXP_AUTHRETRY      = 5,
  IXP_AUTHORIZED     = 6,
  IXP_DISCONNECTING  = 7,
  IXP_DISCONNECTED   = 8,
  IXP_LAST           = 9
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="IXP_FINDINGHOST"></span><span id="ixp_findinghost"></span>**IXP\_FINDINGHOST**
</dt> <dd>

Indicates that the transport is attempting to resolve the IP name and the host.

</dd> <dt>

<span id="IXP_CONNECTING"></span><span id="ixp_connecting"></span>**IXP\_CONNECTING**
</dt> <dd>

Indicates that the TCP/IP connection is in progress.

</dd> <dt>

<span id="IXP_SECURING"></span><span id="ixp_securing"></span>**IXP\_SECURING**
</dt> <dd>

Indicates that a TCP/IP socket connection has been established. The transport is securing a SSL connection.

</dd> <dt>

<span id="IXP_CONNECTED"></span><span id="ixp_connected"></span>**IXP\_CONNECTED**
</dt> <dd>

Indicates that a TCP/IP socket connection has been established. The transport is waiting for protocol response.

</dd> <dt>

<span id="IXP_AUTHORIZING"></span><span id="ixp_authorizing"></span>**IXP\_AUTHORIZING**
</dt> <dd>

Indicates that the transport is performing authorization with the server.

</dd> <dt>

<span id="IXP_AUTHRETRY"></span><span id="ixp_authretry"></span>**IXP\_AUTHRETRY**
</dt> <dd>

Indicates that the transport is retrying authorization with the server.

</dd> <dt>

<span id="IXP_AUTHORIZED"></span><span id="ixp_authorized"></span>**IXP\_AUTHORIZED**
</dt> <dd>

Indicates that authorization is successful. This is a transient state, which becomes **IXP\_CONNECTED** immediately after.

</dd> <dt>

<span id="IXP_DISCONNECTING"></span><span id="ixp_disconnecting"></span>**IXP\_DISCONNECTING**
</dt> <dd>

Indicates that the connection is being closed.

</dd> <dt>

<span id="IXP_DISCONNECTED"></span><span id="ixp_disconnected"></span>**IXP\_DISCONNECTED**
</dt> <dd>

Indicates that the transport has been disconnected from the server.

</dd> <dt>

<span id="IXP_LAST"></span><span id="ixp_last"></span>**IXP\_LAST**
</dt> <dd>

Indicates the last status value (for bounds checking).

</dd> </dl>

## Remarks

These values are returned in the [**OnStatus**](oe-itransportcallback-onstatus.md) callback method and in the [**GetStatus**](oe-iinternettransport-getstatus.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





