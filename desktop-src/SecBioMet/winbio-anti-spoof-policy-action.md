---
title: WINBIO_ANTI_SPOOF_POLICY_ACTION enumeration (Winbio\_types.h)
description: Specifies the types of actions you take for the antispoofing policy of a user.
ms.assetid: 846C0725-1796-49E4-883C-44AC7D618317
keywords:
- WINBIO_ANTI_SPOOF_POLICY_ACTION enumeration Windows Biometric Framework API
- PWINBIO_ANTI_SPOOF_POLICY enumeration pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_ANTI_SPOOF_POLICY_ACTION
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_ANTI\_SPOOF\_POLICY\_ACTION enumeration

Specifies the types of actions you take for the antispoofing policy of a user.

## Syntax


```C++
typedef enum _WINBIO_ANTI_SPOOF_POLICY_ACTION { 
  WINBIO_ANTI_SPOOF_DISABLE  = 0x00000000,
  WINBIO_ANTI_SPOOF_ENABLE   = 0x00000001,
  WINBIO_ANTI_SPOOF_REMOVE   = 0x00000002
} WINBIO_ANTI_SPOOF_POLICY_ACTION, *PWINBIO_ANTI_SPOOF_POLICY;
```



## Constants

<dl> <dt>

<span id="WINBIO_ANTI_SPOOF_DISABLE"></span><span id="winbio_anti_spoof_disable"></span>**WINBIO\_ANTI\_SPOOF\_DISABLE**
</dt> <dd>

Turns off the detection of spoofing for a biometric factor.

</dd> <dt>

<span id="WINBIO_ANTI_SPOOF_ENABLE"></span><span id="winbio_anti_spoof_enable"></span>**WINBIO\_ANTI\_SPOOF\_ENABLE**
</dt> <dd>

Turns on the detection of spoofing for a biometric factor.

</dd> <dt>

<span id="WINBIO_ANTI_SPOOF_REMOVE"></span><span id="winbio_anti_spoof_remove"></span>**WINBIO\_ANTI\_SPOOF\_REMOVE**
</dt> <dd>

Removes the entire antispoofing policy for the biometric factor from the account.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                                                                              |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                                                                     |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h for client applications or Winbio\_adapters.h for adapters)</dt> </dl> |



## See also

<dl> <dt>

[**WINBIO\_ANTI\_SPOOF\_POLICY\_ACTION**](winbio-anti-spoof-policy-action.md)
</dt> <dt>

[**WINBIO\_POLICY\_SOURCE**](winbio-policy-source.md)
</dt> </dl>

 

 





