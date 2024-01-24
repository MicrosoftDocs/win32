---
description: The ReadyState property retrieves the ReadyState of the MSWebDVD object.
ms.assetid: e43b0fa4-4a5a-4492-a6a9-bf271f58e11b
title: ReadyState Property (Ocidl.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- READYSTATE
api_type: 
- HeaderDef
api_location: 
- ocidl.h
ms.custom: UpdateFrequency5
---

# ReadyState Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `ReadyState` property retrieves the ReadyState of the **MSWebDVD** object.

``` syntax
[ iReadyState = ] MSWebDVD.ReadyState
```

## Return Value

Returns an integer value representing the control's ReadyState.



| Return code | Description                                               |
|-------------|-----------------------------------------------------------|
| 0           | Default initialization state.                             |
| 1           | Object is loading its properties.                         |
| 2           | Object has been initialized.                              |
| 3           | Object is interactive, but not all its data is available. |
| 4           | Object has received all its data.                         |



 

## Remarks

This property is read-only with no default value.

Any object embedded in a Web page exposes the `ReadyState` property.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ocidl.h</dt> </dl> |



 

 




