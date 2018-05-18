---
title: BcdOSLoader\_NxPolicy enumeration
description: Specifies the no-execute page protection policies.
ms.assetid: 'd4c40fe6-7de2-4bbf-80ef-ee4100d71aa3'
keywords: ["BcdOSLoader_NxPolicy enumeration Boot Config"]
topic_type:
- apiref
api_name:
- BcdOSLoader_NxPolicy
api_type:
- NA
---

# BcdOSLoader\_NxPolicy enumeration

Specifies the no-execute page protection policies.

## Syntax


```C++
typedef enum BcdOSLoader_NxPolicy { 
  NxPolicyOptIn      = 0,
  NxPolicyOptOut     = 1,
  NxPolicyAlwaysOff  = 2,
  NxPolicyAlwaysOn   = 3
} BcdOSLoader_NxPolicy;
```



## Constants

<dl> <dt>

<span id="NxPolicyOptIn"></span><span id="nxpolicyoptin"></span><span id="NXPOLICYOPTIN"></span>**NxPolicyOptIn**
</dt> <dd>

The no-execute page protection is off by default.

</dd> <dt>

<span id="NxPolicyOptOut"></span><span id="nxpolicyoptout"></span><span id="NXPOLICYOPTOUT"></span>**NxPolicyOptOut**
</dt> <dd>

The no-execute page protection is on by default.

</dd> <dt>

<span id="NxPolicyAlwaysOff"></span><span id="nxpolicyalwaysoff"></span><span id="NXPOLICYALWAYSOFF"></span>**NxPolicyAlwaysOff**
</dt> <dd>

The no-execute page protection is always off.

</dd> <dt>

<span id="NxPolicyAlwaysOn"></span><span id="nxpolicyalwayson"></span><span id="NXPOLICYALWAYSON"></span>**NxPolicyAlwaysOn**
</dt> <dd>

The no-execute page protection is always on.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[BCD WMI Provider Enumerations](bcd-enumerations.md)
</dt> <dt>

[**BcdOSLoaderElementTypes**](bcdosloaderelementtypes.md)
</dt> </dl>

 

 





