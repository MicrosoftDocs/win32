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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMDRMNET\_POLICY\_MINIMUM\_ENVIRONMENT structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





