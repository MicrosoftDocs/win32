---
description: Writing an ASF Header Object for a New File
ms.assetid: f2a76471-3d93-427b-a316-d0967cd20e77
title: Writing an ASF Header Object for a New File
ms.topic: article
ms.date: 05/31/2018
---

# Writing an ASF Header Object for a New File

The ASF ContentInfo object stores ASF Header Object information for a file. When an ASF file is created or modified, the Header Object must be generated. To do this, the application must provide the encoding profile of the content to the ContentInfo object so that it knows the characteristics of the media file to be created.

For writing a new file, you can use the ContentInfo object to:

-   Collect header information from the profile object of the file to be created,
-   Populate various Header Objects in the ASF library maintained internally by Media Foundation,
-   Initialize the [ASF Multiplexer](asf-multiplexer.md) for ASF data packet generation, and
-   Construct the top-level Header Object in binary format that can be written to a file.

For information about profiles, see [ASF Profile](asf-profile.md).

This section contains the following topics:



| Topic                                                                                                              | Description                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Initializing the ContentInfo Object of a New ASF File](initializing-the-contentinfo-object-of-a-new-asf-file.md) | Describes the [**IMFASFContentInfo::SetProfile**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-setprofile) method that initializes the ContentInfo object with header information stored in a profile object. |
| [Setting Properties in the ContentInfo Object](setting-properties-in-the-contentinfo-object.md)                   | Information about various configuration properties that must be set on the ContentInfo object.                                                                                         |
| [Generating a New ASF Header Object](generating-a-new-asf-header-object.md)                                       | How to generate a media buffer, which contains the actual ASF Header Object of the new file, from the ContentInfo object.                                                              |



 

## Related topics

<dl> <dt>

[ASF ContentInfo Object](asf-contentinfo-object.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md)
</dt> <dt>

ASF File Structure
</dt> </dl>

 

 



