---
title: Setting Metadata Attributes
description: Setting Metadata Attributes
ms.assetid: a5d99361-9919-4548-a24d-900ac65cc634
keywords:
- Windows Media Format SDK,setting metadata attributes
- Advanced Systems Format (ASF),setting metadata attributes
- ASF (Advanced Systems Format),setting metadata attributes
- metadata,setting attributes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Setting Metadata Attributes

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Metadata attributes are set by using the [**IWMHeaderInfo3::AddAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-addattribute) method.

All attributes are assigned a language from the language list for the file. You can access the language list by using the [**IWMLanguageList**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlanguagelist) interface. To get a pointer to an **IWMLanguageList** interface, call **QueryInterface** on any interface of the object from which you have obtained [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3).

You can add attributes with any name you like. However, using attribute names that are not standard names supported by the Windows Media Format SDK can make your metadata difficult for users to discover. Most media-playing applications will check for standard values. For more information, see [Custom Metadata](custom-metadata.md).

You cannot use stream number 0xFFFF to add an attribute globally. You must assign each attribute to a specific stream number, or stream 0 for file-level attributes.

## Related topics

<dl> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




