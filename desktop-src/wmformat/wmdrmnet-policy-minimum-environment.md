---
title: WMDRMNET_POLICY_MINIMUM_ENVIRONMENT structure (Wmdrmsdk.h)
description: The WMDRMNET\_POLICY\_MINIMUM\_ENVIRONMENT structure contains the minimum security requirements for Windows Media DRM for Network Devices.
ms.assetid: b1bc9a8d-197e-45fe-a152-0b81add977eb
keywords:
- WMDRMNET_POLICY_MINIMUM_ENVIRONMENT structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRMNET_POLICY_MINIMUM_ENVIRONMENT
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRMNET\_POLICY\_MINIMUM\_ENVIRONMENT structure

The **WMDRMNET\_POLICY\_MINIMUM\_ENVIRONMENT** structure contains the minimum security requirements for Windows Media DRM for Network Devices.

## Syntax


```C++
typedef struct WMDRMNET_POLICY_MINIMUM_ENVIRONMENT {
  WORD  wMinimumSecurityLevel;
  DWORD dwMinimumAppRevocationListVersion;
  DWORD dwMinimumDeviceRevocationListVersion;
} ;
```



## Members

<dl> <dt>

**wMinimumSecurityLevel**
</dt> <dd>

Minimum application security level required.

</dd> <dt>

**dwMinimumAppRevocationListVersion**
</dt> <dd>

Minimum application certificate revocation list version required.

</dd> <dt>

**dwMinimumDeviceRevocationListVersion**
</dt> <dd>

Minimum device certificate revocation list required.

</dd> </dl>

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> <dt>

[**WMDRMNET\_POLICY**](wmdrmnet-policy.md)
</dt> </dl>

 

 





