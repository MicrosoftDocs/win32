---
description: Initializing the ContentInfo Object of a New ASF File
ms.assetid: a4f6c90e-1b38-4c70-8bc5-e2e16af3d87a
title: Initializing the ContentInfo Object of a New ASF File
ms.topic: article
ms.date: 05/31/2018
---

# Initializing the ContentInfo Object of a New ASF File

After creating an empty ContentInfo object by calling the [**MFCreateASFContentInfo**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfcontentinfo) function, the application must call [**IMFASFContentInfo::SetProfile**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-setprofile) to provide the encoding profile. For information about creating a profile, see [Creating an ASF Profile](creating-an-asf-profile.md).

Before information can be read from the profile, the **SetProfile** method must validate the specified profile object by checking the stream identifiers or media types. If the profile passes the validation, various header objects are generated, such as the File Properties Object, the Stream Bitrate Properties Object, the Stream Properties Object, and the Mutual Exclusion Object.

**SetProfile** computes and sets recommended values for certain properties, such as the preroll value. If this is not already set, the recommended preroll value in milliseconds depends on the maximum buffer window of the leaky bucket specified for the streams in the profile. Similarly, the minimum and maximum data packet sizes are also set. The recommended values might override the packet sizes that are set on the profile through attributes.

Because the file is in the process of being created, the file is categorized as a broadcast type, which is denoted by the Flags field of the File Properties Object. Certain unknown values such as the number of data packets, play duration, and send duration are set to zero. These values are represented by **MF\_PD\_ASF\_xxx** attributes and must be updated by the application after file creation is complete.

The specified profile object replaces any existing profile associated with the ContentInfo object, removes the referenced header objects, and resets global file properties such as preroll and data packet size.

The **SetProfile** method also creates the data object that represents the ASF Data Object. If you reuse a ContentInfo object that includes information about any data packets, **SetProfile** fails and returns the MF\_E\_ALREADY\_INITIALIZED error indicating that it is already associated with an existing ASF Data Object. By default, for a new ContentInfo object, the data packet count is set to zero and the data object size is set to 50 bytes. If you use the multiplexer to generate data packets, the multiplexer updates the ContentInfo object to reflect new values such as the data packet count. For more information about data packet generation, see [Generating New ASF Data Packets](generating-new-asf-data-packets.md).

After all the Header Objects are added to the final ASF Header Object, the total header size can be retrieved by calling [**IMFASFContentInfo::GetHeaderSize**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getheadersize). This size includes the initial data object size.

## Related topics

<dl> <dt>

[Setting Properties in the ContentInfo Object](setting-properties-in-the-contentinfo-object.md)
</dt> <dt>

[Writing an ASF Header Object for a New File](writing-an-asf-header-object-for-a-new-file.md)
</dt> </dl>

 

 



