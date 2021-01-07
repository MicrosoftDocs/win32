---
description: The IPX\_ADDRESS structure provides an address at the IPX protocol level.
ms.assetid: 06939ac3-3718-4441-b2c8-c73adfe3babe
title: IPX_ADDRESS structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPX_ADDRESS
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# IPX\_ADDRESS structure

The **IPX\_ADDRESS** structure provides an address at the IPX protocol level.

## Syntax


```C++
typedef struct _IPX_ADDRESS {
  BYTE Subnet[4];
  BYTE Address[6];
} IPX_ADDRESS, *LPIPX_ADDRESS;
```



## Members

<dl> <dt>

**Subnet**
</dt> <dd>

Network subnet identifier.

</dd> <dt>

**Address**
</dt> <dd>

Subnet NIC identifier.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




