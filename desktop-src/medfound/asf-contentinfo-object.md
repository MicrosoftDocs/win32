---
description: ASF ContentInfo Object
ms.assetid: 6b7f8b68-fe98-4aeb-9842-a80ac6235999
title: ASF ContentInfo Object
ms.topic: article
ms.date: 05/31/2018
---

# ASF ContentInfo Object

The ASF *ContentInfo* object stores information from the ASF Header Object of a file. An application can use the ContentInfo object for the following purposes:

-   Read the Header Object for an existing media file. In this case, the ContentInfo object parses the Header Object and stores information about the characteristics file. Media Foundation exposes several of these properties through attributes and interfaces. These are described in [Media Foundation Attributes for ASF Header Objects](media-foundation-attributes-for-asf-header-objects.md).
-   Write header information and construct a Header Object for a new file.
-   Initialize other ASF objects such as the [ASF Splitter](asf-splitter.md), [ASF Multiplexer](asf-multiplexer.md), and the ASF Indexer, while reading or writing a media file.

For information about the structure of an ASF file, see [ASF File Structure](asf-file-structure.md).

## Creating the ContentInfo Object

To create a new instance of the ContentInfo object, call the [**MFCreateASFContentInfo**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfcontentinfo) function. This method returns a pointer to an empty ContentInfo object that must be initialized to work with a specific ASF file. Depending on whether the application is reading an existing file or writing a new ASF file, it must call [**IMFASFContentInfo::ParseHeader**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-parseheader) or [**IMFASFContentInfo::SetProfile**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-setprofile) to populate the empty object.

For more information about these method calls, see the following topics:

-   [Reading the ASF Header Object of an Existing File](reading-the-asf-header-object-of-an-existing-file.md)
-   [Getting Information from ASF Header Objects](getting-information-from-asf-header-objects.md)
-   [Writing an ASF Header Object for a New File](writing-an-asf-header-object-for-a-new-file.md)
-   [Media Foundation Attributes for ASF Header Objects](media-foundation-attributes-for-asf-header-objects.md)

## Related topics

<dl> <dt>

[WMContainer ASF Components](wmcontainer-asf-components.md)
</dt> </dl>

 

 



