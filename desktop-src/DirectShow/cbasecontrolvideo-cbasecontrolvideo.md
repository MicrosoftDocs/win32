---
description: CBaseControlVideo.CBaseControlVideo constructor - Constructor method.
ms.assetid: 925c6c45-0990-4044-aca1-34f343f438b5
title: CBaseControlVideo.CBaseControlVideo constructor (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.CBaseControlVideo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlVideo.CBaseControlVideo constructor

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
CBaseControlVideo(
   CBaseFilter *pFilter,
   CCritSec    *pInterfaceLock,
   TCHAR       *pName,
   LPUNKNOWN   pUnk,
   HRESULT     *phr
);
```



## Parameters

<dl> <dt>

*pFilter* 
</dt> <dd>

Pointer to the owning media filter object.

</dd> <dt>

*pInterfaceLock* 
</dt> <dd>

Pointer to the critical section to use for locking.

</dd> <dt>

*pName* 
</dt> <dd>

Pointer to the object description.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the controlling **IUnknown** interface, if the object is part of an aggregate; otherwise, must be **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that receives an HRESULT value indicating the success or failure of the constructor method.

</dd> </dl>

## Remarks

The object implements the [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) control interface.

All the interface methods from [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) that this class implements require that the filter be connected correctly. For this reason, the class is passed a pin with which it should synchronize with. Whenever an interface method is called, the object determines that the pin is still connected.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




