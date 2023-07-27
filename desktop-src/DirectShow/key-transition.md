---
description: Key Transition
ms.assetid: 5d1ed2e4-82c2-4364-b8f0-22bba974bc22
title: Key Transition
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Key Transition

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Key transition performs keying based on RGB value, alpha value, hue or luminance.

The following image shows the key transition:

![key transition](images/trans-key.png)

Class ID (CLSID): {C5B19592-145E-11D3-9F04-006008039E37}

CLSID Variable Name: CLSID\_DxtKey

Friendly Name: "DxtKey"

Properties



| Property   | Type  | Valid range           | Description                                                                                                                                                                                                                                                | Applies To                     |
|------------|-------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| Hue        | int   | 0–360                 | The hue value on which to key.                                                                                                                                                                                                                             | Hue                            |
| Invert     | BOOL  | **FALSE** or **TRUE** | Boolean value indicating whether to invert the default operation of the key. If **FALSE**, pixels in the overlying image are made transparent in the default manner. If **TRUE**, the operation inverts.                                                   | Chroma, Hue, Luminance, Nonred |
| KeyType    | int   | See Remarks           | Specifies the type of key. For more information, see Remarks.                                                                                                                                                                                              | All                            |
| Luminance  | int   | 0–100                 | The luminance value on which to key.                                                                                                                                                                                                                       | Luminance                      |
| RGB        | DWORD | 0x0 – 0xFFFFFF        | The color on which to key. The value is a hexadecimal number with the format 0x*RRGGBB*, where *RR* is the red value, *GG* is the green value, and *BB* is the blue value. (Pure red, green, and blue are 0xFF0000, 0x00FF00, and 0x0000FF, respectively.) | Chroma                         |
| Similarity | int   | 0–100                 | The range of color data that becomes transparent. At higher values, a wider range of similar colors is transparent.                                                                                                                                        | Chroma, Nonred                 |



 

## Remarks

The type of key that is performed depends on the value of the **KeyType** property, which must be one of the following:



| Value | Enumeration       | Description                                           |
|-------|-------------------|-------------------------------------------------------|
| 0     | DXTKEY\_RGB       | Chroma key (key by RGB value).                        |
| 1     | DXTKEY\_NONRED    | Nonred key. (Makes blue and green areas transparent.) |
| 2     | DXTKEY\_LUMINANCE | Luminance key.                                        |
| 3     | DXTKEY\_ALPHA     | Key by alpha value.                                   |
| 4     | DXTKEY\_HUE       | Key by hue.                                           |



 

The key type defaults to DXTKEY\_ALPHA.

 

 



