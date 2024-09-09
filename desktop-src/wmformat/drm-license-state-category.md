---
title: DRM_LICENSE_STATE_CATEGORY enumeration (Drmexternals.h)
description: The DRM\_LICENSE\_STATE\_CATEGORY enumeration type defines the categories for DRM license strings that are displayed to the user.
ms.assetid: 'f5c5aa78-84f9-4ee4-b551-05bf864243ab'
keywords:
- DRM_LICENSE_STATE_CATEGORY enumeration windows Media Format
- enumeration windows Media Format
topic_type:
- apiref
api_name:
- DRM_LICENSE_STATE_CATEGORY
api_location:
- Drmexternals.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DRM_LICENSE_STATE_CATEGORY enumeration (Drmexternals.h)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DRM\_LICENSE\_STATE\_CATEGORY** enumeration type defines the categories for DRM [*license*](wmformat-glossary.md) strings that are displayed to the user.

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
} ;
```



## Constants

<dl> <dt>

<span id="WM_DRM_LICENSE_STATE_NORIGHT"></span><span id="wm_drm_license_state_noright"></span>**WM\_DRM\_LICENSE\_STATE\_NORIGHT**
</dt> <dd>

Indicates the string will take the form "Playback not permitted."

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_UNLIM"></span><span id="wm_drm_license_state_unlim"></span>**WM\_DRM\_LICENSE\_STATE\_UNLIM**
</dt> <dd>

Indicates the string will take the form "Playback unlimited."

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_COUNT"></span><span id="wm_drm_license_state_count"></span>**WM\_DRM\_LICENSE\_STATE\_COUNT**
</dt> <dd>

Indicates the string will take the form "Playback valid 5 times."

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_FROM"></span><span id="wm_drm_license_state_from"></span>**WM\_DRM\_LICENSE\_STATE\_FROM**
</dt> <dd>

Indicates the string will take the form "Playback valid from 7/12/00."

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_UNTIL"></span><span id="wm_drm_license_state_until"></span>**WM\_DRM\_LICENSE\_STATE\_UNTIL**
</dt> <dd>

Indicates the string will take the form "Playback valid until 7/12/00."

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_FROM_UNTIL"></span><span id="wm_drm_license_state_from_until"></span>**WM\_DRM\_LICENSE\_STATE\_FROM\_UNTIL**
</dt> <dd>

Indicates the string will take the form "Playback valid from 5/12 to 9/12."

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_COUNT_FROM"></span><span id="wm_drm_license_state_count_from"></span>**WM\_DRM\_LICENSE\_STATE\_COUNT\_FROM**
</dt> <dd>

Indicates the string will take the form "Playback valid 5 times from 5/12 to 9/12."

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_COUNT_UNTIL"></span><span id="wm_drm_license_state_count_until"></span>**WM\_DRM\_LICENSE\_STATE\_COUNT\_UNTIL**
</dt> <dd>

Indicates the string will take the form "Playback valid 5 times until 7/12/00."

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_COUNT_FROM_UNTIL"></span><span id="wm_drm_license_state_count_from_until"></span>**WM\_DRM\_LICENSE\_STATE\_COUNT\_FROM\_UNTIL**
</dt> <dd>

Indicates the string will take the form "Playback valid 5 times from 5/12 to 9/12."

</dd> <dt>

<span id="WM_DRM_LICENSE_STATE_EXPIRATION_AFTER_FIRSTUSE"></span><span id="wm_drm_license_state_expiration_after_firstuse"></span>**WM\_DRM\_LICENSE\_STATE\_EXPIRATION\_AFTER\_FIRSTUSE**
</dt> <dd>

Indicates the string will take the form "Playback valid for 24 hours from first use."

</dd> </dl>

## Remarks

This enumeration indicates the category for each possible output string to be displayed. It is a member of the [**DRM\_LICENSE\_STATE\_DATA**](drm-license-state-data.md) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                      |
| Version<br/>                  | Windows Media Format 7 SDK, or later versions of the SDK<br/>                       |
| Header<br/>                   | <dl> <dt>Drmexternals.h</dt> </dl> |



## See also

<dl> <dt>

[**Enumeration Types**](enumeration-types.md)
</dt> </dl>

 

 





