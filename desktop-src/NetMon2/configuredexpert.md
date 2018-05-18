---
Description: 'The CONFIGUREDEXPERT structure associates an expert with its configuration data.'
ms.assetid: '96a6650b-6d6f-495e-83bb-385d44ff015d'
title: CONFIGUREDEXPERT structure
---

# CONFIGUREDEXPERT structure

The **CONFIGUREDEXPERT** structure associates an expert with its configuration data.

## Syntax


```C++
typedef struct {
  HEXPERT       hExpert;
  DWORD         StartupFlags;
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



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




