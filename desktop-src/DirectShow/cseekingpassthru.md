---
Description: 'The CSeekingPassThru class is a helper object that creates CPosPassThru and CRendererPosPassThru objects.'
ms.assetid: 'a748ea5c-d93f-4f80-9d2f-bef5a5c1c2fb'
title: CSeekingPassThru class
---

# CSeekingPassThru class

The `CSeekingPassThru` class is a helper object that creates [**CPosPassThru**](cpospassthru.md) and [**CRendererPosPassThru**](crendererpospassthru.md) objects.

The **CPosPassThru** and **CRendererPosPassThru** classes are helper objects that pass seeking commands upstream, so the `CSeekingPassThru` class is a helper object for creating helper objects.

It is not necessary to use this class directly. Instead, use the [**CreatePosPassThru**](createpospassthru.md) function, which handles all of the details of using this class. It has the further advantage of loading the object from Quartz.dll, which reduces the code size of your filter somewhat. For more information, see [**CPosPassThru**](cpospassthru.md).

The `CSeekingPassThru` class exposes the [**ISeekingPassThru**](iseekingpassthru.md) interface. The [**ISeekingPassThru::Init**](iseekingpassthru-init.md) method initializes the object. After the object is initialized, the filter can query it for the [**IMediaSeeking**](imediaseeking.md) and [**IMediaPosition**](imediaposition.md) interfaces.



| Public Methods                                                  | Description                        |
|-----------------------------------------------------------------|------------------------------------|
| [**CSeekingPassThru**](cseekingpassthru-cseekingpassthru.md)   | Constructor method.                |
| [**~CSeekingPassThru**](cseekingpassthru--cseekingpassthru.md) | Destructor method.                 |
| [**CreateInstance**](cseekingpassthru-createinstance.md)       | Creates an instance of the object. |
| ISeekingPassThru Methods                                        | Description                        |
| [**Init**](cseekingpassthru-init.md)                           | Initializes the object.            |



 

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Seekpt.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




