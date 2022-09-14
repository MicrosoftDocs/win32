---
title: Inserting Native Stream Formats Into ASF Files (QASF)
description: Inserting Native Stream Formats Into ASF Files (QASF)
ms.assetid: ec7a69f3-0d4c-43dd-8d4b-fe066329a98f
keywords:
- Windows Media Format SDK,native stream formats (QASF)
- Windows Media Format SDK,inserting native stream formats into ASF files (QASF)
- Windows Media Format SDK,DirectShow
- Advanced Systems Format (ASF),inserting native stream formats (QASF)
- ASF (Advanced Systems Format),inserting native stream formats (QASF)
- Advanced Systems Format (ASF),native stream formats (QASF)
- ASF (Advanced Systems Format),native stream formats (QASF)
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- DirectShow,native stream formats (QASF)
- DirectShow,inserting native stream formats into ASF files (QASF)
- Windows Media Format SDK,QASF
- Advanced Systems Format (ASF),QASF
- ASF (Advanced Systems Format),QASF
- DirectShow,QASF
ms.topic: article
ms.date: 05/31/2018
---

# Inserting Native Stream Formats Into ASF Files (QASF)

By default, the [WM ASF Writer](wm-asf-writer-filter.md) expects uncompressed audio and video streams on its input pins, and uses the Windows Media Format SDK to access the Windows Media Audio and Windows Media Video codecs, which compress the streams. But the ASF file container can be used for any type of data. By placing digital media data into an ASF file container, you can add features provided by ASF, such as metadata and digital rights management (DRM), without having to transcode your content.

To create an ASF file that contains content that is not Windows Media–based, the application must compress the stream in the filter graph upstream of the WM ASF Writer and bypass the WM ASF Writer's compression mechanism by calling [**IConfigAsfWriter2::SetParam**](iconfigasfwriter2-setparam.md) as follows:


```C++
pConfigAsfWriter2->SetParam(AM_CONFIGASFWRITER_PARAM_DONTCOMPRESS,TRUE,0)

```



Then configure the filter with the desired profile. It is essential that the media type of the input stream exactly matches the format in the profile. In some cases, it may be necessary to examine the input stream's format, and create a custom profile to match it. For more information, see [To Create ASF Files Using Third-Party Codecs](to-create-asf-files-using-third-party-codecs.md).

When you connect the WM ASF Writer to the upstream filter, use the **IGraphBuilder::ConnectDirect** method. Do not use any "intelligent connect" methods such as **IGraphBuilder::Connect** or **IGraphBuilder::RenderFile** to connect the filter because this will disable the filter's "bypass compression" mode.

 

 




