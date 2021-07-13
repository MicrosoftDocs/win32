---
title: Creating ASF Files in DirectShow (Windows Media Format 11 SDK)
description: Learn about creating ASF files in DirectShow by using the Windows Media Format 11 SDK. ASF is a container format that can contain any type of data.
ms.assetid: 8b7af340-934d-43a9-88e9-7bbb2d3a38e0
keywords:
- Windows Media Format SDK,creating ASF files in DirectShow
- Windows Media Format SDK,DirectShow
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- Advanced Systems Format (ASF),creating in DirectShow
- ASF (Advanced Systems Format),creating in DirectShow
- DirectShow,creating ASF files
ms.topic: article
ms.date: 05/31/2018
---

# Creating ASF Files in DirectShow (Windows Media Format 11 SDK)

You can use DirectShow to create ASF files directly from capture sources such as DV camcorders or to transcode other files into Windows Media Format. In either scenario, applications create filter graphs that include the [WM ASF Writer](wm-asf-writer-filter.md) filter as the renderer.

The WM ASF Writer provides a partial wrapper for the Windows Media Format SDK. Applications can use the [**IConfigAsfWriter**](/previous-versions/windows/desktop/legacy/dd743205(v=vs.85)) interface of the filter to pass in a system profile (versions 4, 7, or 8), or use the Windows Media Format SDK directly to create a custom profile to pass to the filter. To add metadata and other header information, the application uses the [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo) interface, which can be obtained from the filter. After the profile and metadata have been configured, the application can simply run the filter graph. Internally, the filter uses the Windows Media Format SDK to write the file. The filter handles all the audio-video synchronization details, which would otherwise be the responsibility of the application.

This process is explained in more detail in the following sections.



| Section                                                                                                           | Description                                                                            |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [Configuring the WM ASF Writer (QASF)](configuring-the-wm-asf-writer--qasf.md)                                   | Describes how to configure the WM ASF Writer filter.                                   |
| [Building Filter Graphs to Write ASF Files (QASF)](building-filter-graphs-to-write-asf-files--qasf.md)           | Describes how to create file-transcoding and capture graphs.                           |
| [Configuring Profiles and Other File Properties (QASF)](configuring-profiles-and-other-file-properties--qasf.md) | Describes how to perform various ASF file-configuration tasks using the WM ASF Writer. |



 

 

 
