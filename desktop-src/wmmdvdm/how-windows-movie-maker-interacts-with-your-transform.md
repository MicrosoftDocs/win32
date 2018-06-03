---
title: How Windows Movie Maker Interacts with Your Transform
description: How Windows Movie Maker Interacts with Your Transform
ms.assetid: 0b594967-cf6a-4b76-83de-569487f85887
keywords:
- Windows Movie Maker,transform interaction
- Movie Maker,transform interaction
- programming guide,Windows Movie Maker and transform interaction
- transforms,Windows Movie Maker interaction
- custom transforms,Windows Movie Maker interaction
- IMediaTransform interface
- INotifySeek interface
- IControlOutputSize interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How Windows Movie Maker Interacts with Your Transform

All transforms must implement the [**IMediaTransform**](imediatransform.md) interface, which is the main communication channel between Windows Movie Maker and the transform. In addition, transforms can optionally implement the [**INotifySeek**](inotifyseek.md) interface to receive seek notifications from Windows Movie Maker, and the [**IControlOutputSize**](icontroloutputsize.md) interface to enable Windows Movie Maker to alternate output buffer sizes when producing output frames.

On startup, Windows Movie Maker looks in specially designated folders for all third-party XML initialization files, and then loads them. Each XML file specifies one or more effects or transitions loaded from one or more registered DLLs, and specifies a name, image, and zero or more parameters for each. These images and names are shown in the lists of available effects and transitions in Windows Movie Maker's user interface. The transform DLL is not actually loaded at this time. For more information on the contents of the XML initialization files, see [Creating Custom Transforms Using XML](creating-custom-transforms-using-xml.md).

When a user chooses a transform in the Windows Movie Maker user interface and then previews or renders video, Windows Movie Maker loads the appropriate DLL and makes the following calls on the transform:

1.  Windows Movie Maker calls the transform's constructor. If the transform needs to get any parameters from an initialization XML file, it should call the [**CreateTransformProperties**](createtransformproperties.md) function with the [**ITransformProperties**](itransformproperties.md) member it implements.
2.  Windows Movie Maker calls [**IMediaTransform::get\_InputCount**](imediatransform-get-inputcount.md) and [**IMediaTransform::get\_MediaType**](imediatransform-get-mediatype.md) to get the number of input streams and the media types that will be accepted by the transform. A transform can have either one or two input streams, but only one output stream.
3.  Windows Movie Maker calls [**IMediaTransform::QueryBufferRequirements**](imediatransform-querybufferrequirements.md) to get the transform's requirements for the input and output buffers that Windows Movie Maker will send to it.
4.  Windows Movie Maker calls [**IMediaTransform::InitBufferManager**](imediatransform-initbuffermanager.md) to let the transform perform any setup it needs to on a device.
5.  Windows Movie Maker calls [**IMediaTransform::Process**](imediatransform-process.md) repeatedly. This method passes in the data from the input streams and waits for the transform to modify and send out the new data. A transform receives either one or two streams, depending on the type, and returns only one stream. All input and output buffers are allocated by Windows Movie Maker. For more information on this method, see the reference page for **IMediaTransform::Process**.
6.  If the device changes, for some reason (for example, if the user locks the desktop or if system resources are taken away), Windows Movie Maker will call **IMediaTransform::InitBufferManager** again with the new device.

## Related topics

<dl> <dt>

[**Creating Custom Transforms Using COM and DirectX**](creating-custom-transforms-using-com-and-directx.md)
</dt> </dl>

 

 




