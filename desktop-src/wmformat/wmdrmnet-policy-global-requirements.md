---
title: WMDRMNET_POLICY_GLOBAL_REQUIREMENTS structure (Wmdrmsdk.h)
description: The WMDRMNET\_POLICY\_GLOBAL\_REQUIREMENTS structure holds global requirements for Windows Media DRM for Network Devices.
ms.assetid: 140b3a6f-ccba-4735-b48a-2e990f5ec570
keywords:
- WMDRMNET_POLICY_GLOBAL_REQUIREMENTS structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRMNET_POLICY_GLOBAL_REQUIREMENTS
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRMNET\_POLICY\_GLOBAL\_REQUIREMENTS structure

The **WMDRMNET\_POLICY\_GLOBAL\_REQUIREMENTS** structure holds global requirements for Windows Media DRM for Network Devices.

## Syntax


```C++
typedef struct WMDRMNET_POLICY_GLOBAL_REQUIREMENTS {
  WMDRMNET_POLICY_MINIMUM_ENVIRONMENT MinimumEnvironment;
} ;
```



## Members

<dl> <dt>

**MinimumEnvironment**
</dt> <dd>

[**WMDRMNET\_POLICY\_MINIMUM\_ENVIRONMENT**](wmdrmnet-policy-minimum-environment.md) structure containing the minimum security requirements for Windows Media DRM for Network Devices.

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

 

 





