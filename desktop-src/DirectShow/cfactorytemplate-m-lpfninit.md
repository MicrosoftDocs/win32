---
description: Pointer to a function that gets called from the DLL entry point. Can be NULL.
ms.assetid: 0769f55b-6f0d-4a89-9d3f-64f211426342
title: CFactoryTemplate::m_lpfnInit member (Combase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_lpfnInit
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CFactoryTemplate::m\_lpfnInit member

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Pointer to a function that gets called from the DLL entry point. Can be **NULL**.

## Syntax


```C++
LPFNInitRoutine m_lpfnInit;
```



## Remarks

The function pointer type is [**LPFNInitRoutine**](lpfninitroutine.md). If you provide this function in your DLL, the DLL entry-point function calls it with following parameters:

-   *bLoading*: **TRUE** when the DLL is loaded, **FALSE** when the DLL is unloaded.
-   *rclsid*: Pointer to the object's CLISD, specified in the [**CFactoryTemplate::m\_ClsID**](cfactorytemplate-m-clsid.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CFactoryTemplate Class**](cfactorytemplate.md)
</dt> </dl>

 

 




