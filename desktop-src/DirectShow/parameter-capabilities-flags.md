---
description: These flags specify which envelope curves are supported by a media parameter.
ms.assetid: 6f3b7666-d245-41fc-b6e4-9e1ed264dfdc
title: Parameter Capabilities Flags (Medparam.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Parameter Capabilities Flags

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

These flags specify which envelope curves are supported by a media parameter.



| Constant                                                                                                                                                                                      | Description                                              |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| <span id="MP_CAPS_CURVE_INVSQUARE"></span><span id="mp_caps_curve_invsquare"></span><dl> <dt>**MP\_CAPS\_CURVE\_INVSQUARE**</dt> </dl> | Inverse square curve.<br/>                         |
| <span id="MP_CAPS_CURVE_JUMP"></span><span id="mp_caps_curve_jump"></span><dl> <dt>**MP\_CAPS\_CURVE\_JUMP**</dt> </dl>                | Jump to the next point without interpolation.<br/> |
| <span id="MP_CAPS_CURVE_LINEAR"></span><span id="mp_caps_curve_linear"></span><dl> <dt>**MP\_CAPS\_CURVE\_LINEAR**</dt> </dl>          | Linear interpolation.<br/>                         |
| <span id="MP_CAPS_CURVE_SINE"></span><span id="mp_caps_curve_sine"></span><dl> <dt>**MP\_CAPS\_CURVE\_SINE**</dt> </dl>                | Sine curve.<br/>                                   |
| <span id="MP_CAPS_CURVE_SQUARE"></span><span id="mp_caps_curve_square"></span><dl> <dt>**MP\_CAPS\_CURVE\_SQUARE**</dt> </dl>          | Parabolic curve.<br/>                              |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Medparam.h</dt> </dl> |



## See also

<dl> <dt>

[DMO Constants](dmo-constants.md)
</dt> </dl>

 

 




