---
title: Custom Metadata
description: Custom Metadata
ms.assetid: 86132163-da56-416a-9539-874d18972932
keywords:
- Windows Media Format SDK,custom metadata
- Advanced Systems Format (ASF),custom metadata
- ASF (Advanced Systems Format),custom metadata
- Windows Media Format SDK,IWMHeaderInfo3 interface
- Advanced Systems Format (ASF),IWMHeaderInfo3 interface
- ASF (Advanced Systems Format),IWMHeaderInfo3 interface
- metadata,customizing
- IWMHeaderInfo3
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Custom Metadata

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

In addition to the many supported attributes provided with the Windows Media Format SDK, you can create metadata attributes to your own specifications. When creating custom metadata attributes, you should use an easily identifiable naming convention to avoid possible conflict with attributes created by others.

It is recommended that you use the methods of [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3) to create your metadata because of the added flexibility they provide over the methods of [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo).

## Related topics

<dl> <dt>

[**Attributes**](attributes.md)
</dt> <dt>

[**Metadata Features**](metadata-features.md)
</dt> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




