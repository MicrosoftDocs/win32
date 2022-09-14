---
description: The VINES\_IP\_ADDRESS structure is an IP address on a Vines network.
ms.assetid: 681753a5-08a2-48e6-9e46-c028c12ad9c1
title: VINES_IP_ADDRESS structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- VINES_IP_ADDRESS
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# VINES\_IP\_ADDRESS structure

The **VINES\_IP\_ADDRESS** structure is an IP address on a Vines network.

## Syntax


```C++
typedef struct _VINES_IP_ADDRESS {
  DWORD NetID;
  WORD  SubnetID;
} VINES_IP_ADDRESS, *LPVINES_IP_ADDRESS;
```



## Members

<dl> <dt>

**NetID**
</dt> <dd>

The identifier of a specific machine on a specific subnet.

</dd> <dt>

**SubnetID**
</dt> <dd>

The identifier of a specific subnet on the whole network.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




