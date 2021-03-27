---
title: WMDRMNET_POLICY_TRANSCRYPTPLAY structure (Wmdrmsdk.h)
description: The WMDRMNET\_POLICY\_TRANSCRYPTPLAY structure holds the policy information for playing content using Windows Media DRM for Network Devices.
ms.assetid: 95671c58-a593-40bb-856e-28ad1cba340e
keywords:
- WMDRMNET_POLICY_TRANSCRYPTPLAY structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRMNET_POLICY_TRANSCRYPTPLAY
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRMNET\_POLICY\_TRANSCRYPTPLAY structure

The **WMDRMNET\_POLICY\_TRANSCRYPTPLAY** structure holds the policy information for playing content using Windows Media DRM for Network Devices.

## Syntax


```C++
typedef struct WMDRMNET_POLICY_TRANSCRYPTPLAY {
  WMDRMNET_POLICY_GLOBAL_REQUIREMENTS globals;
  WMDRMNET_POLICY_PLAY_OPL            playOPLs;
} ;
```



## Members

<dl> <dt>

**globals**
</dt> <dd>

Global policy structure.

</dd> <dt>

**playOPLs**
</dt> <dd>

Output protection levels for playback. **WMDRMNET\_POLICY\_PLAY\_OPL** is a type defined as [**DRM\_PLAY\_OPL\_EX**](drm-play-opl-ex.md).

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

 

 





