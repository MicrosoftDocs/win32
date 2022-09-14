---
title: Synchronous Reader Object
description: Synchronous Reader Object
ms.assetid: 52a4891f-03bf-4d8a-ab7b-e9739db30bc3
keywords:
- Windows Media Format SDK,synchronous reader objects
- Advanced Systems Format (ASF),synchronous reader objects
- ASF (Advanced Systems Format),synchronous reader objects
- objects,synchronous reader objects
- synchronous readers,objects
ms.topic: article
ms.date: 05/31/2018
---

# Synchronous Reader Object

The synchronous reader object is used to read digital media files by using synchronous calls.

The synchronous reader object is created by the function [**WMCreateSyncReader**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatesyncreader), which sets a pointer to an **IWMSyncReader** interface. The other interfaces supported by the synchronous reader interface can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the synchronous reader object.



| Interface                                | Description                                                                                                                                                        |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo)   | Sets and retrieves header information, such as metadata, [*markers*](wmformat-glossary.md), and so on.                                            |
| [**IWMHeaderInfo2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo2) | Enumerates the available codec information. Inherits all of the methods of **IWMHeaderInfo**.                                                                      |
| [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3) | Supports large attribute sizes, duplicate attribute names, and multiple language support. Inherits all of the methods of **IWMHeaderInfo** and **IWMHeaderInfo2**. |
| [**IWMProfile**](iwmprofile.md)         | Provides access to the profile information of the Windows Media file loaded into the reader.                                                                       |
| [**IWMProfile2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofile2)       | Retrieves the globally unique identifier (GUID), if any, associated with the profile. Inherits all of the methods of **IWMProfile**.                               |
| [**IWMProfile3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofile3)       | Supports bandwidth sharing and stream prioritization information in the profile. Inherits all of the methods of **IWMProfile** and **IWMProfile2**.                |
| [**IWMSyncReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)   | Provides synchronous reading capabilities for digital media files.                                                                                                 |
| [**IWMSyncReader2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader2) | Provides support for seeking to SMPTE time codes and for allocating samples manually. Inherits all of the methods of **IWMSyncReader**.                            |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Reader Object**](reader-object.md)
</dt> <dt>

[**Reading Files with the Synchronous Reader**](reading-files-with-the-synchronous-reader.md)
</dt> </dl>

 

 




