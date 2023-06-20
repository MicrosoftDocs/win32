---
title: Editing Metadata Attributes
description: Editing Metadata Attributes
ms.assetid: 96c979e2-c616-45e3-9c60-a24f03e29dc4
keywords:
- Windows Media Format SDK,editing metadata attributes
- Advanced Systems Format (ASF),editing metadata attributes
- ASF (Advanced Systems Format),editing metadata attributes
- metadata,editing attributes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Editing Metadata Attributes

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Editing metadata attributes is very similar to setting new ones. Instead of using [**IWMHeaderInfo3::AddAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-addattribute), use [**IWMHeaderInfo3::ModifyAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-modifyattribute). **ModifyAttribute** is identical to **AddAttribute** except that you do not specify an attribute name, and the index number is an input parameter instead of an output.

You can use stream number 0xFFFF to specify an attribute to modify using its global index.

## Related topics

<dl> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




