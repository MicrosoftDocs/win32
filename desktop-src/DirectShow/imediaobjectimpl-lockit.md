---
description: The LockIt class is an internal class that locks and unlocks the DMO.
ms.assetid: f516ce22-17ad-488e-a768-3f3849c56087
title: IMediaObjectImpl::LockIt Class (Dmoimpl.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IMediaObjectImpl::LockIt Class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `LockIt` class is an internal class that locks and unlocks the DMO.

``` syntax
LockIt(
    _DERIVED_ *p
);
```

## Parameters

<dl> <dt>

<span id="p"></span><span id="P"></span>*p*
</dt> <dd>

Pointer to the derived object.

</dd> </dl>

## Remarks

The `LockIt` constructor locks the DMO, and the destructor unlocks the DMO. To lock the object from inside your derived class, declare a local variable of type `LockIt`. The DMO is locked while the `LockIt` object remains in scope:


```C++
void SomeMethod()
{
    // The DMO is not locked.
    {
        LockIt dmoLock(this); // Locks the DMO.
        /* ... */
    } 
    // dmoLock goes out of scope, DMO is unlocked.
}
```



The methods in **IMediaObjectImpl** automatically lock the DMO.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dmoimpl.h</dt> </dl>                                                                     |
| Library<br/> | <dl> <dt>Dmoguids.lib; </dt> <dt>Msdmo.lib</dt> </dl> |



## See also

<dl> <dt>

[**IMediaObjectImpl Class Template**](imediaobjectimpl-class-template.md)
</dt> </dl>

 

 




