---
title: DRM_LICENSE_STATE_CATEGORY enumeration (Wmdrmsdk.h)
description: The DRM\_LICENSE\_STATE\_CATEGORY enumeration type specifies the type of license restriction that is described by a DRM\_LICENSE\_STATE\_DATA structure.
ms.assetid: 51258be9-2f4d-4f25-97f7-2cac6c155ade
keywords:
- DRM_LICENSE_STATE_CATEGORY enumeration windows Media Format
topic_type:
- apiref
api_name:
- DRM_LICENSE_STATE_CATEGORY
api_location:
- Wmdrmsdk.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM_LICENSE_STATE_CATEGORY enumeration (Wmdrmsdk.h)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_LICENSE\_STATE\_CATEGORY** enumeration type specifies the type of license restriction that is described by a [**DRM\_LICENSE\_STATE\_DATA**](drmdrm-license-state-data.md) structure.

## Syntax


```C++
typedef enum DRM_LICENSE_STATE_CATEGORY { 
  WM_DRM_LICENSE_STATE_NORIGHT                    = 0,
  WM_DRM_LICENSE_STATE_UNLIM,
  WM_DRM_LICENSE_STATE_COUNT,
  WM_DRM_LICENSE_STATE_FROM,
  WM_DRM_LICENSE_STATE_UNTIL,
  WM_DRM_LICENSE_STATE_FROM_UNTIL,
  WM_DRM_LICENSE_STATE_COUNT_FROM,
  WM_DRM_LICENSE_STATE_COUNT_UNTIL,
  WM_DRM_LICENSE_STATE_COUNT_FROM_UNTIL,
  WM_DRM_LICENSE_STATE_EXPIRATION_AFTER_FIRSTUSE
} DRM_LICENSE_STATE_CATEGORY;
```



## Constants

<dl> <dt>

<span id="WM_DRM_LICENSE_STATE_NORIGHT"></span><span id="wm_drm_license_state_noright"></span>**WM\_DRM\_LICENSE\_STATE\_NORIGHT**
</dt> <dd>

Specifies that the action for which the **DRM\_LICENSE\_STATE\_DATA** was received is not allowed.

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_UNLIM"></span><span id="wm_drm_license_state_unlim"></span>**WM\_DRM\_LICENSE\_STATE\_UNLIM**
</dt> <dd>

Specifies that the action for which the **DRM\_LICENSE\_STATE\_DATA** was received is allowed without restriction.

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_COUNT"></span><span id="wm_drm_license_state_count"></span>**WM\_DRM\_LICENSE\_STATE\_COUNT**
</dt> <dd>

Specifies that the action for which the **DRM\_LICENSE\_STATE\_DATA** was received is allowed, but only a set number of times.

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_FROM"></span><span id="wm_drm_license_state_from"></span>**WM\_DRM\_LICENSE\_STATE\_FROM**
</dt> <dd>

Specifies that the action for which the **DRM\_LICENSE\_STATE\_DATA** was received is allowed after a set date.

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_UNTIL"></span><span id="wm_drm_license_state_until"></span>**WM\_DRM\_LICENSE\_STATE\_UNTIL**
</dt> <dd>

Specifies that the action for which the **DRM\_LICENSE\_STATE\_DATA** was received is allowed until a set date.

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_FROM_UNTIL"></span><span id="wm_drm_license_state_from_until"></span>**WM\_DRM\_LICENSE\_STATE\_FROM\_UNTIL**
</dt> <dd>

Specifies that the action for which the **DRM\_LICENSE\_STATE\_DATA** was received is allowed between two set dates.

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_COUNT_FROM"></span><span id="wm_drm_license_state_count_from"></span>**WM\_DRM\_LICENSE\_STATE\_COUNT\_FROM**
</dt> <dd>

Specifies that the action for which the **DRM\_LICENSE\_STATE\_DATA** was received is allowed, but only a set number of times after a set date.

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_COUNT_UNTIL"></span><span id="wm_drm_license_state_count_until"></span>**WM\_DRM\_LICENSE\_STATE\_COUNT\_UNTIL**
</dt> <dd>

Specifies that the action for which the **DRM\_LICENSE\_STATE\_DATA** was received is allowed, but only a set number of times until a set date.

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_COUNT_FROM_UNTIL"></span><span id="wm_drm_license_state_count_from_until"></span>**WM\_DRM\_LICENSE\_STATE\_COUNT\_FROM\_UNTIL**
</dt> <dd>

Specifies that the action for which the **DRM\_LICENSE\_STATE\_DATA** was received is allowed, but only a set number of times between two set dates.

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_EXPIRATION_AFTER_FIRSTUSE"></span><span id="wm_drm_license_state_expiration_after_firstuse"></span>**WM\_DRM\_LICENSE\_STATE\_EXPIRATION\_AFTER\_FIRSTUSE**
</dt> <dd>

Specifies that the action for which the **DRM\_LICENSE\_STATE\_DATA** was received is allowed for a set amount of time beginning with the first use of the action.

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
</dt> </dl>

 

 





