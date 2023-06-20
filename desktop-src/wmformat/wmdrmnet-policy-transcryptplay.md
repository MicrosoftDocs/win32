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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMDRMNET\_POLICY\_TRANSCRYPTPLAY structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





