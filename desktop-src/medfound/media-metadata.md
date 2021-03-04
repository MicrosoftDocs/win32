---
description: Media Metadata
ms.assetid: dd7c4bc9-e2a6-49cd-8f29-865a44d5b5c9
title: Media Metadata
ms.topic: article
ms.date: 05/31/2018
---

# Media Metadata

Media files contain properties that describe the contents of the file. In Microsoft Media Foundation, these properties can be categorized as follows:

-   **Media-type attributes** specify the encoding parameters, such as the encoding algorithm (media subtype), video frame size, video frame rate, audio bit rate, and audio sample rate. For more information about media-type attributes, see [Media Types](media-types.md).
-   **Metadata** contains descriptive information for the media content, such as title, artist, composer, and genre. Metadata can also describe encoding parameters. It can be faster to access this information through metadata than through media-type attributes.
-   **DRM properties** contain information on usage restrictions. Currently Media Foundation does not support DRM properties through metadata, with the exception of the **PKEY\_DRM\_IsProtected** property.

There are two ways to read metadata in Media Foundation:

-   The [**IMFMetadata**](/windows/desktop/api/mfidl/nn-mfidl-imfmetadata) interface (Media Foundation version 1 metadata).
-   The Windows Shell [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) interface (Shell metadata).

Shell metadata pertains not only to media files but to a much wider range of files on the system.

The following table compares the features and limitations of each metadata API.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Media Foundation v1 Metadata</th>
<th>Shell Metadata</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Requires Windows Vista or later.</td>
<td>Requires Windows 7.
<blockquote>
[!Note]<br />
Shell metadata in general does not require Windows 7, but Media Foundation did not support Shell metadata prior to Windows 7.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Properties are not compatible with Shell property system.</td>
<td>Properties are compatible with the Shell property system.</td>
</tr>
<tr class="odd">
<td>Properties can apply to the entire file, or at the stream level.</td>
<td>Only file-level properties are supported. Stream-level properties are not supported.</td>
</tr>
<tr class="even">
<td>Properties can have values in multiple languages.</td>
<td>Values in multiple languages are not supported.</td>
</tr>
<tr class="odd">
<td>Property keys are wide-character strings.</td>
<td>Property keys are <a href="/windows/desktop/api/wtypes/ns-wtypes-propertykey"><strong>PROPERTYKEY</strong></a> values.</td>
</tr>
<tr class="even">
<td>Property values are <a href="/windows/win32/api/propidl/ns-propidl-propvariant"><strong>PROPVARIANT</strong></a> values.</td>
<td>Property values are <a href="/windows/win32/api/propidl/ns-propidl-propvariant"><strong>PROPVARIANT</strong></a> values.</td>
</tr>
</tbody>
</table>



 

## In this section



| Topic                                                                                     | Description                                                                                                                                |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [Shell Metadata Providers](shell-metadata-providers.md)<br/>                       | Starting in Windows 7, Media Foundation exposes metadata through the [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) interface.<br/> |
| [Metadata Properties for Media Files](metadata-properties-for-media-files.md)<br/> | This topic lists the most common metadata properties for media files.<br/>                                                           |
| [Metadata Providers in Windows Vista](metadata-providers-in-windows-vista.md)<br/> | In Windows Vista, Media Foundation exposes metadata through the [**IMFMetadata**](/windows/desktop/api/mfidl/nn-mfidl-imfmetadata) interface.<br/>                   |



 

If you are implementing a custom media source and want to expose Shell metadata, see [Custom Metadata Providers for Media Files](custom-metadata-providers-for-media-files.md).

## Related topics

<dl> <dt>

[Media Foundation Programming Guide](media-foundation-programming-guide.md)
</dt> </dl>

 

 
