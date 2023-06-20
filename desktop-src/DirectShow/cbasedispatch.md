---
description: The CBaseDispatch class is a base class for implementing the IDispatch interface in a DirectShow filter.
ms.assetid: 33a989be-d059-4ad7-99f8-715c55a128a2
title: CBaseDispatch class (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseDispatch
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseDispatch class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![cbasedispatch class hierarchy](images/cutil01.png)

The **CBaseDispatch** class is a base class for implementing the **IDispatch** interface in a DirectShow filter.

This class is limited to supporting the Automation-compatible interfaces exported by the DirectShow type library, QuartzTypeLib. For example, the [**CMediaControl**](cmediacontrol.md) and [**CMediaPosition**](cmediaposition.md) classes use **CBaseDispatch** to implement [**IMediaControl**](/windows/desktop/api/Control/nn-control-imediacontrol) and [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition), respectively. Because of this limitation, there is probably no reason to use **CBaseDispatch** directly in your own filters.

To use this class, do the following:

-   Declare a new class that supports **IDispatch**.
-   Give your new class a private member variable of type **CBaseDispatch**.
-   Implement the **IDispatch** methods.
-   In your **IDispatch** methods, call the **CBaseDispatch** methods.

For more details, refer to the source code for any of the sample classes declared in Ctlutil.h.



| Public Methods                                             | Description                                                                                                         |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**CBaseDispatch**](cbasedispatch-cbasedispatch.md)       | Constructor method.                                                                                                 |
| [**~CBaseDispatch**](cbasedispatch--cbasedispatch.md)     | Destructor method.                                                                                                  |
| [**GetIDsOfNames**](cbasedispatch-getidsofnames.md)       | Maps a set of names to a corresponding set of DISPIDs.                                                              |
| [**GetTypeInfo**](cbasedispatch-gettypeinfo.md)           | Retrieves the type information for the object, which can then be used to get the type information for an interface. |
| [**GetTypeInfoCount**](cbasedispatch-gettypeinfocount.md) | Retrieves the number of type information interfaces the object provides.                                            |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Base Classes](directshow-base-classes.md)
</dt> </dl>

 

 




