---
description: The CImageSample class implements a media sample that manages a GDI device-independent bitmap (DIB).
ms.assetid: 620ea791-458e-441e-8f0c-2184c44c742e
title: CImageSample class (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageSample
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageSample class

![cimagesample class hierarchy](images/wutil03.png)

The `CImageSample` class implements a media sample that manages a GDI device-independent bitmap (DIB). This class derives from the [**CMediaSample**](cmediasample.md) class. It is intended to be used with the [**CImageAllocator**](cimageallocator.md) class. The **CImageAllocator** class provides an allocator that creates `CImageSample` objects.



| Protected Member Variables                        | Description                                                       |
|---------------------------------------------------|-------------------------------------------------------------------|
| [**m\_DibData**](cimagesample-m-dibdata.md)      | Contains information about the DIB that this object is managing.  |
| [**m\_bInit**](cimagesample-m-binit.md)          | Indicates whether the object has been initialized.                |
| Public Methods                                    | Description                                                       |
| [**CImageSample**](cimagesample-cimagesample.md) | Constructor method.                                               |
| [**GetDIBData**](cimagesample-getdibdata.md)     | Retrieves information about the DIB that this object is managing. |
| [**SetDIBData**](cimagesample-setdibdata.md)     | Sets information about the DIB that this object is managing.      |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




