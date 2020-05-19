---
title: Output Media Properties Object
description: Output Media Properties Object
ms.assetid: 96fa7c66-59a0-4eb3-ace4-a827b139f978
keywords:
- Windows Media Format SDK,output media properties objects
- Advanced Systems Format (ASF),output media properties objects
- ASF (Advanced Systems Format),output media properties objects
- objects,output media properties objects
- output media properties objects
ms.topic: article
ms.date: 05/31/2018
---

# Output Media Properties Object

An output media properties object is used to retrieve and set an output property. Output media properties objects are created for supported output formats of streams in a file that is loaded into a reader object. For compressed streams, the output properties are determined by the possible outputs of the decompressing codec.

An output media properties object is created by [**IWMReader::GetOutputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-getoutputprops) This method creates an output media properties object that contains the properties of the default output format. Other formats may be supported for an output. To obtain additional output formats, you can call [**IWMReader::GetOutputFormatCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreader-getoutputformatcount) to get the number of supported output formats and then loop through them using calls to [**IWMReader::GetOutputFormat**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-getoutputformat). **GetOutputFormat** creates an output media properties object populated with the data for the selected output format.

Output media properties objects can also be created with the synchronous reader. All of the method names are identical to those in the reader and they are all exposed by the [**IWMSyncReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader) interface.

**GetOutputProps** and **GetOutputFormat** both set a pointer to an [**IWMOutputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmoutputmediaprops) interface. The other interfaces of the output media properties object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by every output media properties object.



| Interface                                          | Description                                                                                                |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**IWMMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmediaprops)             | Used as the base interface for the other media-property interfaces (input, output, and video).             |
| [**IWMOutputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmoutputmediaprops) | Retrieves the properties of an output.                                                                     |
| [**IWMVideoMediaProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nn-wmsdkidl-iwmvideomediaprops)   | Manages the properties of a video stream. This is an optional interface, available only for video streams. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Reader Object**](reader-object.md)
</dt> </dl>

 

 




