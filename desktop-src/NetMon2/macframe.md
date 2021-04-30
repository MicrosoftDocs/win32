---
description: The MACFRAME structure is a union of the most common initial protocols.
ms.assetid: ec7e3a54-a47f-4390-a137-9574c63c9a11
title: MACFRAME union (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MACFRAME
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# MACFRAME union

The **MACFRAME** structure is a union of the most common initial protocols.

## Syntax


```C++
typedef union {
  LPBYTE      MacHeader;
  LPETHERNET  Ethernet;
  LPTOKENRING Tokenring;
  LPFDDI      Fddi;
} MACFRAME, *LPMACFRAME;
```



## Members

<dl> <dt>

**MacHeader**
</dt> <dd>

Generic pointer to a frame.

</dd> <dt>

**Ethernet**
</dt> <dd>

Ethernet pointer to a frame.

</dd> <dt>

**Tokenring**
</dt> <dd>

Token ring pointer to a frame.

</dd> <dt>

**Fddi**
</dt> <dd>

FDDI pointer to a frame.

</dd> </dl>

## Remarks

This structure is most frequently used as an overlay. To make the properties of the first protocol accessible, cast the frame as the same type as the protocol.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




