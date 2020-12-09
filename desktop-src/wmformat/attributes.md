---
title: Attributes (Windows Media Format 11 SDK)
description: Attributes
ms.assetid: 1e9392b4-4fff-41ad-9d80-23c1c7f9e9a4
keywords:
- Windows Media Format SDK,attributes
- Advanced Systems Format (ASF),attributes
- ASF (Advanced Systems Format),attributes
- attributes,about
ms.topic: article
ms.date: 05/31/2018
---

# Attributes (Windows Media Format 11 SDK)

An attribute is an individual item of metadata. Most of the attributes can be set by your application and are written to the header of an ASF file.

Some of the predefined attributes are coded attributes. These attributes are not stored in the header of an ASF file, but are computed by the objects of the Windows Media Format SDK when the file is loaded. Because coded attributes are always computed, they are inherently read-only.

This SDK includes many attribute definitions that you can use. You can also create attributes of your own to describe content.

The following sections describe the predefined attributes.



| Section                                                                | Description                                                                                                                                                                                           |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Attribute List](attribute-list.md)                                   | Provides an alphabetical list of all of the predefined attributes. After the list, each attribute is described individually.                                                                          |
| [Attributes with Multiple Values](attributes-with-multiple-values.md) | Lists the attributes that can be added to a file more than once.                                                                                                                                      |
| [Attributes By Type](attributes-by-type.md)                           | Contains lists of attributes sorted by type. These include lists of special-purpose attributes (like those dealing with digital rights management) and lists of suggested attributes by content type. |
| [ID3 Tag Support](id3-tag-support.md)                                 | Lists the attributes that are compatible with ID3 tags.                                                                                                                                               |



 

## Related topics

<dl> <dt>

[**IWMHeaderInfo::GetAttributeByIndex**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-getattributebyindex)
</dt> <dt>

[**IWMHeaderInfo::GetAttributeByName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-getattributebyname)
</dt> <dt>

[**IWMHeaderInfo::SetAttribute**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-setattribute)
</dt> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




