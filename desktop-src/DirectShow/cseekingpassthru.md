---
Description: The CSeekingPassThru class is a helper object that creates CPosPassThru and CRendererPosPassThru objects.
ms.assetid: a748ea5c-d93f-4f80-9d2f-bef5a5c1c2fb
title: CSeekingPassThru class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSeekingPassThru class

The `CSeekingPassThru` class is a helper object that creates [**CPosPassThru**](cpospassthru.md) and [**CRendererPosPassThru**](crendererpospassthru.md) objects.

The **CPosPassThru** and **CRendererPosPassThru** classes are helper objects that pass seeking commands upstream, so the `CSeekingPassThru` class is a helper object for creating helper objects.

It is not necessary to use this class directly. Instead, use the [**CreatePosPassThru**](createpospassthru.md) function, which handles all of the details of using this class. It has the further advantage of loading the object from Quartz.dll, which reduces the code size of your filter somewhat. For more information, see [**CPosPassThru**](cpospassthru.md).

The `CSeekingPassThru` class exposes the [**ISeekingPassThru**](/windows/win32/Strmif/nn-strmif-iseekingpassthru?branch=master) interface. The [**ISeekingPassThru::Init**](/windows/win32/Strmif/nf-strmif-iseekingpassthru-init?branch=master) method initializes the object. After the object is initialized, the filter can query it for the [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master) and [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master) interfaces.



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



 

 




