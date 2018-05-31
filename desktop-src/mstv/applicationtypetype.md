---
title: ApplicationTypeType enumeration
description: The ApplicationTypeType enumeration specifies the smart card application type, as defined in ANSI/SCTE 28.
ms.assetid: 8df28daf-7e45-416c-8376-6716bd1783d4
keywords:
- ApplicationTypeType enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- ApplicationTypeType
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
api_location:
- bdatypes.h
api_type:
- HeaderDef
---

# ApplicationTypeType enumeration

The **ApplicationTypeType** enumeration specifies the smart card application type, as defined in ANSI/SCTE 28.

## Syntax


```C++
typedef enum ApplicationTypeType { 
  SCTE28_ConditionalAccess             = 0,
  SCTE28_POD_Host_Binding_Information,
  SCTE28_IPService,
  SCTE28_NetworkInterface_SCTE55_2,
  SCTE28_NetworkInterface_SCTE55_1,
  SCTE28_CopyProtection,
  SCTE28_Diagnostic,
  SCTE28_Undesignated,
  SCTE28_Reserved
} ApplicationTypeType;
```



## Constants

<dl> <dt>

<span id="SCTE28_ConditionalAccess"></span><span id="scte28_conditionalaccess"></span><span id="SCTE28_CONDITIONALACCESS"></span>**SCTE28\_ConditionalAccess**
</dt> <dd>

Conditional access.

</dd> <dt>

<span id="SCTE28_POD_Host_Binding_Information"></span><span id="scte28_pod_host_binding_information"></span><span id="SCTE28_POD_HOST_BINDING_INFORMATION"></span>**SCTE28\_POD\_Host\_Binding\_Information**
</dt> <dd>

POD-Host binding information.

</dd> <dt>

<span id="SCTE28_IPService"></span><span id="scte28_ipservice"></span><span id="SCTE28_IPSERVICE"></span>**SCTE28\_IPService**
</dt> <dd>

IP service.

</dd> <dt>

<span id="SCTE28_NetworkInterface_SCTE55_2"></span><span id="scte28_networkinterface_scte55_2"></span><span id="SCTE28_NETWORKINTERFACE_SCTE55_2"></span>**SCTE28\_NetworkInterface\_SCTE55\_2**
</dt> <dd>

Network interface (SCTE 55-2).

</dd> <dt>

<span id="SCTE28_NetworkInterface_SCTE55_1"></span><span id="scte28_networkinterface_scte55_1"></span><span id="SCTE28_NETWORKINTERFACE_SCTE55_1"></span>**SCTE28\_NetworkInterface\_SCTE55\_1**
</dt> <dd>

Network interface (SCTE 55-1).

</dd> <dt>

<span id="SCTE28_CopyProtection"></span><span id="scte28_copyprotection"></span><span id="SCTE28_COPYPROTECTION"></span>**SCTE28\_CopyProtection**
</dt> <dd>

Copy protection

</dd> <dt>

<span id="SCTE28_Diagnostic"></span><span id="scte28_diagnostic"></span><span id="SCTE28_DIAGNOSTIC"></span>**SCTE28\_Diagnostic**
</dt> <dd>

Diagnostic.

</dd> <dt>

<span id="SCTE28_Undesignated"></span><span id="scte28_undesignated"></span><span id="SCTE28_UNDESIGNATED"></span>**SCTE28\_Undesignated**
</dt> <dd>

Undesignated.

</dd> <dt>

<span id="SCTE28_Reserved"></span><span id="scte28_reserved"></span><span id="SCTE28_RESERVED"></span>**SCTE28\_Reserved**
</dt> <dd>

Reserved. Do not use.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[BDA Reference](bda-reference.md)
</dt> </dl>

 

 





