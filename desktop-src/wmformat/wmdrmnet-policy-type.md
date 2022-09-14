---
title: WMDRMNET_POLICY_TYPE enumeration (Wmdrmsdk.h)
description: The WMDRMNET\_POLICY\_TYPE enumeration type lists the types of policies that are available for Windows Media DRM for Network Devices operations.
ms.assetid: 83e9e247-3bd8-4857-97b6-95b3cd5ad25c
keywords:
- WMDRMNET_POLICY_TYPE enumeration windows Media Format
- enumeration windows Media Format
topic_type:
- apiref
api_name:
- WMDRMNET_POLICY_TYPE
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRMNET\_POLICY\_TYPE enumeration

The **WMDRMNET\_POLICY\_TYPE** enumeration type lists the types of policies that are available for Windows Media DRM for Network Devices operations.

## Syntax


```C++
typedef enum WMDRMNET_POLICY_TYPE { 
  WMDRMNET_POLICY_TYPE_UNDEFINED       = 0x0000,
  WMDRMNET_POLICY_TYPE_TRANSCRYPTPLAY  = 0x0001
} ;
```



## Constants

<dl> <dt>

<span id="WMDRMNET_POLICY_TYPE_UNDEFINED"></span><span id="wmdrmnet_policy_type_undefined"></span>**WMDRMNET\_POLICY\_TYPE\_UNDEFINED**
</dt> <dd>

Undefined policy types are not supported.

</dd> <dt>

<span id="WMDRMNET_POLICY_TYPE_TRANSCRYPTPLAY"></span><span id="wmdrmnet_policy_type_transcryptplay"></span>**WMDRMNET\_POLICY\_TYPE\_TRANSCRYPTPLAY**
</dt> <dd>

The policy governs the ability to convert content protected by Windows Media DRM into protected Windows Media DRM for Network Devices data and play it back on a networked device.

</dd> </dl>

## Remarks

None.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](drm-enumeration-types.md)
</dt> <dt>

[**WMDRMNET\_POLICY**](wmdrmnet-policy.md)
</dt> </dl>

 

 





