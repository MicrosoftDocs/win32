---
title: Setting Metadata Attributes
description: Setting Metadata Attributes
ms.assetid: a5d99361-9919-4548-a24d-900ac65cc634
keywords:
- Windows Media Format SDK,setting metadata attributes
- Advanced Systems Format (ASF),setting metadata attributes
- ASF (Advanced Systems Format),setting metadata attributes
- metadata,setting attributes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting Metadata Attributes

Metadata attributes are set by using the [**IWMHeaderInfo3::AddAttribute**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-addattribute?branch=master) method.

All attributes are assigned a language from the language list for the file. You can access the language list by using the [**IWMLanguageList**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmlanguagelist?branch=master) interface. To get a pointer to an **IWMLanguageList** interface, call **QueryInterface** on any interface of the object from which you have obtained [**IWMHeaderInfo3**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3?branch=master).

You can add attributes with any name you like. However, using attribute names that are not standard names supported by the Windows Media Format SDK can make your metadata difficult for users to discover. Most media-playing applications will check for standard values. For more information, see [Custom Metadata](custom-metadata.md).

You cannot use stream number 0xFFFF to add an attribute globally. You must assign each attribute to a specific stream number, or stream 0 for file-level attributes.

## Related topics

<dl> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




