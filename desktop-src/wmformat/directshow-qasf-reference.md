---
title: DirectShow QASF Reference
description: DirectShow QASF Reference
ms.assetid: 66f483b5-3886-48b4-bc43-7c3517abd20d
keywords:
- Windows Media Format SDK,QASF
- Windows Media Format SDK,DirectShow
- DirectShow,QASF reference
- QASF filters,reference
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DirectShow QASF Reference

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section contains programming references for the following DirectShow QASF filters, interfaces and enumerations. The DirectShow SDK documentation contains reference and programming guide materials for additional generic interfaces exposed by these filters, such as **IBaseFilter** and **IPin**, and for earlier versions of the QASF components.

For an explanation of the QASF name, see [About DirectShow](about-directshow.md).

The following filters are included with the DirectShow QASF components.



| Filter                                           | Description                                                      |
|--------------------------------------------------|------------------------------------------------------------------|
| [WM ASF Reader Filter](wm-asf-reader-filter.md) | Reads and parses local or remote ASF files.                      |
| [WM ASF Writer Filter](wm-asf-writer-filter.md) | Creates ASF files from compressed or uncompressed input streams. |



 

The following interfaces are defined for use with the DirectShow QASF components.



| Interface                                                  | Description                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IAMWMBufferPass**](/previous-versions/windows/desktop/api/dshowasf/nn-dshowasf-iamwmbufferpass)                 | Provides a method that enables applications to register for callbacks from the input pins of the [WM ASF Writer](wm-asf-writer-filter.md) or the output pins of the [WM ASF Reader](wm-asf-reader-filter.md) filter. Used in indexing and when adding data unit extensions. |
| [**IAMWMBufferPassCallback**](/previous-versions/windows/desktop/api/dshowasf/nn-dshowasf-iamwmbufferpasscallback) | Implemented by applications and called by the filters. Applications use the one method on this interface to obtain information about individual samples in the stream. Used in indexing and when adding data unit extensions.                                                 |
| [**IConfigAsfWriter**](/previous-versions/windows/desktop/legacy/dd743205(v=vs.85))               | Implemented on the WM ASF Writer. Used by applications to specify profiles and indexing parameters for the file.                                                                                                                                                              |
| [**IConfigAsfWriter2**](/previous-versions/windows/desktop/legacy/dd743206(v=vs.85))             | Provides additional configuration functions on the WM ASF Writer.                                                                                                                                                                                                             |



 

The following enumeration, structure, and events are defined for use with the DirectShow QASF components.



| Enumeration                                                               | Description                                                                                                                                                                       |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [\_AM\_ASFWRITERCONFIG\_PARAM](/previous-versions/windows/desktop/legacy/dd758054(v=vs.85)) | Defines filter configuration parameters used in the [**IConfigAsfWriter2::GetParam**](iconfigasfwriter2-getparam.md) and [**SetParam**](iconfigasfwriter2-setparam.md) methods. |



 



| Structure                                         | Description                                                                                                                                           |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AM\_WMT\_EVENT\_DATA**](/previous-versions/windows/desktop/api/evcode/ns-evcode-am_wmt_event_data) | Contains information pertaining to a [**WMT\_STATUS**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_status) event and the associated status code returned by the Windows Media Format SDK. |



 



| Event                                           | Description                                                                                                     |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [EC\_WMT\_EVENT](ec-wmt-event.md)              | Event forwarded from the Windows Media Format SDK.                                                              |
| [EC\_WMT\_INDEX\_EVENT](ec-wmt-index-event.md) | Sent when an application uses the [WM ASF Writer](wm-asf-writer-filter.md) to index Windows Media Video files. |



 

 

 