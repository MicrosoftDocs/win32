---
title: BcdOSLoader\_PAEPolicy enumeration
description: Specifies the Physical Address Extension (PAE) policies.
ms.assetid: 8eb2b17b-1192-44eb-8277-6c22548a74cb
keywords:
- BcdOSLoader_PAEPolicy enumeration Boot Config
topic_type:
- apiref
api_name:
- BcdOSLoader_PAEPolicy
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# BcdOSLoader\_PAEPolicy enumeration

Specifies the Physical Address Extension (PAE) policies.

## Syntax


```C++
typedef enum BcdOSLoader_PAEPolicy { 
  PaePolicyDefault       = 0,
  PaePolicyForceEnable   = 1,
  PaePolicyForceDisable  = 2
} BcdOSLoader_PAEPolicy;
```



## Constants

<dl> <dt>

<span id="PaePolicyDefault"></span><span id="paepolicydefault"></span><span id="PAEPOLICYDEFAULT"></span>**PaePolicyDefault**
</dt> <dd>

Enable PAE if hot-pluggable memory is defined above 4GB.

</dd> <dt>

<span id="PaePolicyForceEnable"></span><span id="paepolicyforceenable"></span><span id="PAEPOLICYFORCEENABLE"></span>**PaePolicyForceEnable**
</dt> <dd>

PAE is enabled.

</dd> <dt>

<span id="PaePolicyForceDisable"></span><span id="paepolicyforcedisable"></span><span id="PAEPOLICYFORCEDISABLE"></span>**PaePolicyForceDisable**
</dt> <dd>

PAE is disabled.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[BCD WMI Provider Enumerations](bcd-enumerations.md)
</dt> <dt>

[**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)
</dt> </dl>

 

 





