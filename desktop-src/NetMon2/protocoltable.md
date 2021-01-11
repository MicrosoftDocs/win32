---
description: The PROTOCOLTABLE structure contains a list of protocols.
ms.assetid: dad2b228-5916-44fe-b78e-ebc6507dc555
title: PROTOCOLTABLE structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PROTOCOLTABLE
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# PROTOCOLTABLE structure

The **PROTOCOLTABLE** structure contains a list of protocols.

## Syntax


```C++
typedef struct _PROTOCOLTABLE {
  DWORD     nProtocols;
  HPROTOCOL hProtocol[1];
} PROTOCOLTABLE;
```



## Members

<dl> <dt>

**nProtocols**
</dt> <dd>

Number of protocols that are enabled.

</dd> <dt>

**hProtocol**
</dt> <dd>

Array of handles to enabled protocols.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




