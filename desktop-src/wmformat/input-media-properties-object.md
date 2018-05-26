---
title: Input Media Properties Object
description: Input Media Properties Object
ms.assetid: e7aa6c99-b6b3-4e5b-869d-3387f70dad87
keywords:
- Windows Media Format SDK,input media properties objects
- Advanced Systems Format (ASF),input media properties objects
- ASF (Advanced Systems Format),input media properties objects
- objects,input media properties objects
- input media properties objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Input Media Properties Object

An input media properties object created by the writer object supports the following interfaces. These interfaces are accessed by a call to **QueryInterface** on one of the interfaces of the writer object.



| Interface                                        | Description                                                                                                |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**IWMInputMediaProps**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwminputmediaprops?branch=master) | Retrieves the properties of an input stream.                                                               |
| [**IWMMediaProps**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmmediaprops?branch=master)           | Used as the base interface for the other media-property interfaces (input, output, and video).             |
| [**IWMVideoMediaProps**](/windows/win32/Wmsdkidl/nn-wmsdkidl-iwmvideomediaprops?branch=master) | Manages the properties of a video stream. This is an optional interface, available only for video streams. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Writer Object**](writer-object.md)
</dt> </dl>

 

 




