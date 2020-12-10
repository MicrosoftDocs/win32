---
title: WINBIO_POLICY_SOURCE enumeration (Winbio\_types.h)
description: Lists the possible sources of policy information for the detection of spoofing for biometric factors.
ms.assetid: 3DC3BB0B-1FD7-473C-8E0B-B7E0A4A44E9E
keywords:
- WINBIO_POLICY_SOURCE enumeration Windows Biometric Framework API
- PWINBIO_POLICY_SOURCE enumeration pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_POLICY_SOURCE
api_location:
- winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_POLICY\_SOURCE enumeration

Lists the possible sources of policy information for the detection of spoofing for biometric factors.

## Syntax


```C++
typedef enum _WINBIO_POLICY_SOURCE { 
  WINBIO_POLICY_UNKNOWN  = 0x00000000,
  WINBIO_POLICY_DEFAULT  = 0x00000001,
  WINBIO_POLICY_LOCAL    = 0x00000002,
  WINBIO_POLICY_ADMIN    = 0x00000003
} WINBIO_POLICY_SOURCE, *PWINBIO_POLICY_SOURCE;
```



## Constants

<dl> <dt>

<span id="WINBIO_POLICY_UNKNOWN"></span><span id="winbio_policy_unknown"></span>**WINBIO\_POLICY\_UNKNOWN**
</dt> <dd>

The source of the policy is unknown.

</dd> <dt>

<span id="WINBIO_POLICY_DEFAULT"></span><span id="winbio_policy_default"></span>**WINBIO\_POLICY\_DEFAULT**
</dt> <dd>

The policy is the default policy that the Windows Biometric Framework provides.

</dd> <dt>

<span id="WINBIO_POLICY_LOCAL"></span><span id="winbio_policy_local"></span>**WINBIO\_POLICY\_LOCAL**
</dt> <dd>

The policy that the individual user set for their account by using the **Settings** app. This policy overrides the default policy.

</dd> <dt>

<span id="WINBIO_POLICY_ADMIN"></span><span id="winbio_policy_admin"></span>**WINBIO\_POLICY\_ADMIN**
</dt> <dd>

A group policy that the IT administrator set for the enterprise. Individual users cannot override this policy.

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
</dt> </dl>

 

 





