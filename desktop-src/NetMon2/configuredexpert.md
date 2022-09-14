---
description: The CONFIGUREDEXPERT structure associates an expert with its configuration data.
ms.assetid: 96a6650b-6d6f-495e-83bb-385d44ff015d
title: CONFIGUREDEXPERT structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CONFIGUREDEXPERT
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# CONFIGUREDEXPERT structure

The **CONFIGUREDEXPERT** structure associates an expert with its configuration data.

## Syntax


```C++
typedef struct {
  HEXPERT       hExpert;
  DWORD         StartupFlags;
  PEXPERTCONFIG pConfig;
} CONFIGUREDEXPERT, *PCONFIGUREDEXPERT;
```



## Members

<dl> <dt>

**hExpert**
</dt> <dd>

Handle to an expert.

</dd> <dt>

**StartupFlags**
</dt> <dd>

Startup flag values of the expert.

</dd> <dt>

**pConfig**
</dt> <dd>

Pointer to an [**EXPERTCONFIG**](expertconfig.md) structure.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




