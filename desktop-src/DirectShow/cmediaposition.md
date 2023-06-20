---
description: The CMediaPosition class handles the IDispatch methods of the IMediaPosition dual interface.
ms.assetid: 5e84a2b6-39d4-47a4-93b4-690df12e2d19
title: CMediaPosition class (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaPosition
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaPosition class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![cmediaposition class hierarchy](images/cutil14.png)

The **CMediaPosition** class handles the **IDispatch** methods of the [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition) dual interface.

This class inherits the [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition) interface but does not implement it. It implements **IDispatch** through the [**CBaseDispatch**](cbasedispatch.md) class and the DirectShow type library. Do not use this class directly. Instead, use one of the following classes:

-   Source filters: Use the [**CSourceSeeking**](csourceseeking.md) base class to implement seeking.
-   Transform filters: Use the [**CPosPassThru**](cpospassthru.md) class to pass seeking commands upstream.
-   Renderers: Use the [**CRendererPosPassThru**](crendererpospassthru.md) class to pass seeking commands upstream.



| Public Methods                                              | Description                                                                                                         |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**CMediaPosition**](cmediaposition-cmediaposition.md)     | Constructor method.                                                                                                 |
| IDispatch Methods                                           | Description                                                                                                         |
| [**GetIDsOfNames**](cmediaposition-getidsofnames.md)       | Maps a set of names to a corresponding set of DISPIDs.                                                              |
| [**GetTypeInfo**](cmediaposition-gettypeinfo.md)           | Retrieves the type information for the object, which can then be used to get the type information for an interface. |
| [**GetTypeInfoCount**](cmediaposition-gettypeinfocount.md) | Retrieves the number of type information interfaces the object provides.                                            |
| [**Invoke**](cmediaposition-invoke.md)                     | Provides access to properties and methods exposed by the object.                                                    |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Base Classes](directshow-base-classes.md)
</dt> </dl>

 

 




