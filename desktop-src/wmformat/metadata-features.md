---
title: Metadata Features
description: Metadata is used in ASF files to describe file contents and properties.
ms.assetid: 01ba09d7-11be-46b1-a0f2-4e35ca5502a8
keywords:
- Windows Media Format SDK,metadata features
- Windows Media Format SDK,features
- Advanced Systems Format (ASF),metadata features
- ASF (Advanced Systems Format),metadata features
- Advanced Systems Format (ASF),features
- ASF (Advanced Systems Format),features
- metadata,features
ms.topic: article
ms.date: 05/31/2018
---

# Metadata Features

Metadata is used in ASF files to describe file contents and properties. All ASF files you create should include appropriate metadata. (For an overview, see [Metadata](metadata.md).) The Windows Media Format SDK includes support for metadata editing through the writer object, the metadata editor object, and both the reader and synchronous reader objects. Native support for a wide variety of metadata attributes is included. See [Attributes](attributes.md) for a list of the predefined attributes.

The metadata support provided by the various objects of the Windows Media Format SDK is flexible and powerful. The main metadata features are summarized in the following list:

-   Flexible attribute size. Metadata attributes are not limited in size.
-   Stream-level attributes. Metadata in ASF files can be assigned to the file as a whole, or to a particular stream.
-   Duplicated attributes. A named attribute can be used multiple times in the same file. This feature is of particular use when assigning content descriptive attributes. For example, a song may have several authors, each requiring a separate **Author** attribute in the file.
-   Multiple languages. Every attribute has a language associated with it. You can set the supported languages and then assign one to each attribute you write. Because you can duplicate attributes, you can provide the most important attributes in several languages to reach a larger audience. If you do not specify a language, the default language (obtained from the operating system of the computer running your application) will be used.
-   Complex attributes. Some of the predefined attributes support structured data. For these attributes, the data type is binary, but the value is a structure defined in this SDK.

The following topics discuss the other supported metadata features.



| Topic                                  | Description                                                                             |
|----------------------------------------|-----------------------------------------------------------------------------------------|
| [ID3 Support](id3.md)                 | Discusses the support for ID3 frames using the objects of the Windows Media Format SDK. |
| [Custom Metadata](custom-metadata.md) | Discusses the implications of using custom metadata.                                    |



 

## Related topics

<dl> <dt>

[**Features**](features.md)
</dt> <dt>

[**IWMHeaderInfo Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo)
</dt> <dt>

[**IWMHeaderInfo2 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo2)
</dt> <dt>

[**IWMHeaderInfo3 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3)
</dt> <dt>

[**Metadata**](metadata.md)
</dt> </dl>

 

 




