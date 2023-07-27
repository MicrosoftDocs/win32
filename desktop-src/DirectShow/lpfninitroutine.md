---
description: Pointer to a function that gets called from the DLL entry point.
ms.assetid: 30196657-38ab-42ca-b673-b0894999e566
title: LPFNInitRoutine function pointer (Combase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LPFNInitRoutine
api_type: 
- UserDefined
api_location: 
- Combase.h
ms.custom: UpdateFrequency5
---

# LPFNInitRoutine function pointer

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Pointer to a function that gets called from the DLL entry point.

## Syntax


```C++
typedef void ( CALLBACK *LPFNInitRoutine)(
         BOOL  bLoading,
   const CLSID *rclsid
);
```



## Parameters

<dl> <dt>

*bLoading* 
</dt> <dd>

**TRUE** when the DLL is loaded, **FALSE** when the DLL is unloaded.

</dd> <dt>

*rclsid* 
</dt> <dd>

Pointer to the object's CLISD, specified in the [**CFactoryTemplate::m\_ClsID**](cfactorytemplate-m-clsid.md) member variable.

</dd> </dl>

## Return value

This function pointer does not return a value.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Combase.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[**CFactoryTemplate Class**](cfactorytemplate.md)
</dt> </dl>

 

 




