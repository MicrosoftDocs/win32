---
description: Contains a port number used for IP or IPX protocols.
ms.assetid: 730f6ee6-7b7d-4e10-91ee-a4ba87aae5aa
title: GENERIC_PORT union (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GENERIC_PORT
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# GENERIC\_PORT union

The **GENERIC\_PORT** structure contains a port number used for IP or IPX protocols.

## Syntax


```C++
typedef union {
  BYTE IPPort;
  WORD ByteSwappedIPXPort;
} GENERIC_PORT;
```



## Members

<dl> <dt>

**IPPort**
</dt> <dd>

IP port number filled in.

</dd> <dt>

**ByteSwappedIPXPort**
</dt> <dd>

IPX port number filled in.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




