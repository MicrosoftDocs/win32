---
title: WMDRMNET_POLICY structure (Wmdrmsdk.h)
description: The WMDRMNET\_POLICY structure contains the policy to be used for Windows Media DRM for Network Devices operations.
ms.assetid: 11eaaeb2-3470-4f58-ae1c-53ee0f60bdce
keywords:
- WMDRMNET_POLICY structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRMNET_POLICY
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRMNET\_POLICY structure

The **WMDRMNET\_POLICY** structure contains the policy to be used for Windows Media DRM for Network Devices operations.

## Syntax


```C++
typedef struct WMDRMNET_POLICY {
  WMDRMNET_POLICY_TYPE ePolicyType;
  BYTE                 *pbPolicy;
} ;
```



## Members

<dl> <dt>

**ePolicyType**
</dt> <dd>

Member of the [**WMDRMNET\_POLICY\_TYPE**](wmdrmnet-policy-type.md) enumeration that specifies the type of policy.

</dd> <dt>

**pbPolicy**
</dt> <dd>

Buffer containing the policy. The only type of policy currently supported is **WMDRMNET\_POLICY\_TYPE\_TRANSCRYPTPLAY**. This member is a pointer to a **WMDRMNET\_POLICY\_TRANSCRYPTPLAY** structure.

</dd> </dl>

## Remarks

This structure is used as a parameter for the [**IWMDRMNetTransmitter::GetLeafLicenseResponse**](iwmdrmnettransmitter-getleaflicenseresponse.md) method.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](drm-structures.md)
</dt> <dt>

[**WMDRMNET\_POLICY\_GLOBAL\_REQUIREMENTS**](wmdrmnet-policy-global-requirements.md)
</dt> <dt>

[**WMDRMNET\_POLICY\_MINIMUM\_ENVIRONMENT**](wmdrmnet-policy-minimum-environment.md)
</dt> <dt>

[**WMDRMNET\_POLICY\_TRANSCRYPTPLAY**](wmdrmnet-policy-transcryptplay.md)
</dt> <dt>

[**WMDRMNET\_POLICY\_TYPE**](wmdrmnet-policy-type.md)
</dt> </dl>

 

 





