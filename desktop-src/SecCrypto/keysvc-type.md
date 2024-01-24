---
description: The KEYSVC\_TYPE enumeration defines whether a key applies to a computer or a service.
ms.assetid: 573a412a-1e9d-47ac-bd09-2319d4b9712b
title: KEYSVC_TYPE enumeration (Rkeysvcc.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- KEYSVC_TYPE
api_type: 
- HeaderDef
api_location: 
- Rkeysvcc.h
---

# KEYSVC\_TYPE enumeration

The **KEYSVC\_TYPE** enumeration defines whether a key applies to a computer or a service.

## Syntax


```C++
typedef enum _KEYSVC_TYPE { 
  KeySvcMachine,
  KeySvcService
} KEYSVC_TYPE;
```



## Constants

<dl> <dt>

<span id="KeySvcMachine"></span><span id="keysvcmachine"></span><span id="KEYSVCMACHINE"></span>**KeySvcMachine**
</dt> <dd>

The key is for a computer.

</dd> <dt>

<span id="KeySvcService"></span><span id="keysvcservice"></span><span id="KEYSVCSERVICE"></span>**KeySvcService**
</dt> <dd>

The key is for a service.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Rkeysvcc.h</dt> </dl> |



## See also

<dl> <dt>

[**RKeyOpenKeyService**](rkeyopenkeyservice.md)
</dt> </dl>

 

 




