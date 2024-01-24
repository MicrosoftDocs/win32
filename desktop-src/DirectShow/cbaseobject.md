---
description: The CBaseObject class is an abstract class for implementing DirectShow objects. To implement Component Object Model (COM) objects, use the CUnknown class, which derives from CBaseObject.
ms.assetid: 4b651d43-b177-4081-8c76-f6615ff2830c
title: CBaseObject class (Combase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseObject
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseObject class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CBaseObject** class is an abstract class for implementing DirectShow objects. To implement Component Object Model (COM) objects, use the [**CUnknown**](cunknown.md) class, which derives from **CBaseObject**.



| Class Methods                                      | Description                            |
|----------------------------------------------------|----------------------------------------|
| [**CBaseObject**](cbaseobject-cbaseobject.md)     | Constructor method.                    |
| [**~CBaseObject**](cbaseobject--cbaseobject.md)   | Destructor method.                     |
| [**ObjectsActive**](cbaseobject-objectsactive.md) | Retrieves the count of active objects. |



 

## Remarks

Most of the DirectShow base classes derive from **CBaseObject**. This class provides debugging assistance by keeping a count of all the DirectShow objects active during run time. The object count is stored in a class-static member variable:


```
class CBaseObject
{
private:
    static LONG m_cObjects;  // Total number of objects active. 
/* ... */
};
```



In debug builds, the DLL will assert if it is unloaded while the object count is greater than zero. This makes it easier to track down leaks caused by reference-counting problems.

The **CBaseObject** constructor takes one argument, a debugging name for the object. This name is stored in a global table in the DLL. The [**DbgDumpObjectRegister**](dbgdumpobjectregister.md) function formats a list of the objects active in the DLL, and sends it to the debug output.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Base Classes](directshow-base-classes.md)
</dt> </dl>

 

 




