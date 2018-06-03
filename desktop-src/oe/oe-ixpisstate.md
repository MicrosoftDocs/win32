---
title: IXPISSTATE enumeration
description: Indicates the state of the transport.
ms.assetid: cdd05971-0ed2-49e2-8532-1d0de40b73ae
keywords:
- IXPISSTATE enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# IXPISSTATE enumeration

\[**IXPISSTATE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Indicates the state of the transport.

## Syntax


```C++
typedef enum tagIXPISSTATE { 
  IXP_IS_CONNECTED      = 0,
  IXP_IS_BUSY           = 1,
  IXP_IS_READY          = 2,
  IXP_IS_AUTHENTICATED  = 3
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="IXP_IS_CONNECTED"></span><span id="ixp_is_connected"></span>**IXP\_IS\_CONNECTED**
</dt> <dd>

Indicates that the transport is currently connected.

</dd> <dt>

<span id="IXP_IS_BUSY"></span><span id="ixp_is_busy"></span>**IXP\_IS\_BUSY**
</dt> <dd>

Indicates that the transport is currently processing a command.

</dd> <dt>

<span id="IXP_IS_READY"></span><span id="ixp_is_ready"></span>**IXP\_IS\_READY**
</dt> <dd>

Indicates that the transport is ready for input.

</dd> <dt>

<span id="IXP_IS_AUTHENTICATED"></span><span id="ixp_is_authenticated"></span>**IXP\_IS\_AUTHENTICATED**
</dt> <dd>

Indicates that the transport has performed authentication.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





