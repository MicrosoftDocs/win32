---
title: IMediaTransform interface
description: The IMediaTransform interface is implemented by the transform and called by Windows Movie Maker.
ms.assetid: 'ef828d2f-5c2f-4a8b-85a1-185df9248e80'
keywords: ["IMediaTransform interface Windows Movie Maker and DVD Maker", "IMediaTransform interface Windows Movie Maker and DVD Maker , described"]
topic_type:
- apiref
api_name:
- IMediaTransform
api_type:
- COM
---

# IMediaTransform interface

The **IMediaTransform** interface is implemented by the transform and called by Windows Movie Maker. This is the main point of communication between your object and the application.

All data processing is done in the [**Process**](imediatransform-process.md) method. Windows Movie Maker calls the [**InitBufferManager**](imediatransform-initbuffermanager.md) method before the first data is sent, to let the object initialize any data structures it needs. Windows Movie Maker calls this method again any time the underlying device is changed.

## Members

The **IMediaTransform** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IMediaTransform** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMediaTransform** interface has these methods.



| Method                                                                     | Description                                                                                                                 |
|:---------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**get\_InputCount**](imediatransform-get-inputcount.md)                  | Enables your transform to report the number of source input streams that it can handle.<br/>                          |
| [**get\_MediaType**](imediatransform-get-mediatype.md)                    | Enables your transform to report the media type that it can handle.<br/>                                              |
| [**InitBufferManager**](imediatransform-initbuffermanager.md)             | Passes a Direct3D device to your transform and enables your transform to perform any initialization it requires.<br/> |
| [**Process**](imediatransform-process.md)                                 | Enables your transform to process a block of data.<br/>                                                               |
| [**QueryBufferRequirements**](imediatransform-querybufferrequirements.md) | On startup, allows Windows Movie Maker to learn any special buffer requirements of the transform.<br/>                |



 

## See also

<dl> <dt>

[**Transform Interfaces**](transform-interfaces.md)
</dt> </dl>

 

 





