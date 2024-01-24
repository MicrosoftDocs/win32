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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMDRMNET\_POLICY structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





