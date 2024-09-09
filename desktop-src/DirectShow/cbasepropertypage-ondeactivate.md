---
description: The OnDeactivate method is called when the dialog box window is destroyed.
ms.assetid: 47320e61-324f-4f64-abe1-38fe70e82787
title: CBasePropertyPage.OnDeactivate method (Cprop.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePropertyPage.OnDeactivate
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePropertyPage.OnDeactivate method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `OnDeactivate` method is called when the dialog box window is destroyed.

## Syntax


```C++
virtual HRESULT OnDeactivate();
```



## Parameters

This method has no parameters.

## Return value

The base-class implementation returns S\_OK.

## Remarks

The [**CBasePropertyPage::Deactivate**](cbasepropertypage-deactivate.md) method calls the `OnDeactivate` method. Override `OnDeactivate` to release any resources that the derived class obtained in the [**CBasePropertyPage::OnActivate**](cbasepropertypage-onactivate.md) method, or to perform other tasks as needed.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




