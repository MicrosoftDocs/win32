---
Description: This section contains reference topics for the Audiomediatype.h header.
ms.assetid: C675D989-6A0D-4B0E-9CE1-B068425B55F9
title: Audiomediatype.h
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Audiomediatype.h

This section contains reference topics for the Audiomediatype.h header.

## In this section



<table>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>CreateAudioMediaType</strong>](/windows/win32/audiomediatype/nf-audiomediatype-createaudiomediatype?branch=master)<br/></td>
<td>The <code>CreateAudioMediaType</code> function uses the format specified by the caller to create a media type object that describes the audio format. <br/></td>
</tr>
<tr class="even">
<td>[<strong>CreateAudioMediaTypeFromUncompressedAudioFormat</strong>](/windows/win32/audiomediatype/nf-audiomediatype-createaudiomediatypefromuncompressedaudioformat?branch=master)<br/></td>
<td>The <code>CreateAudioMediaTypeFromUncompressedAudioFormat</code> function uses the information provided in the [<strong>UNCOMPRESSEDAUDIOFORMAT</strong>](/windows/win32/Audiomediatype/ns-audiomediatype-_uncompressedaudioformat?branch=master) structure to create a media type object that describes the audio format.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAudioMediaType</strong>](/windows/win32/Audiomediatype/nn-audiomediatype-iaudiomediatype?branch=master)<br/></td>
<td>The <code>IAudioMediaType</code> interface exposes methods that allow an sAPO to get information that is used to negotiate with the audio engine for the appropriate audio data format. An sAPO also returns this interface in response to a call to [<strong>IAudioSystemEffectsCustomFormats::GetFormat</strong>](/windows/win32/audioenginebaseapo/nf-audioenginebaseapo-iaudiosystemeffectscustomformats-getformat?branch=master).<br/> <code>IAudioMediaType</code> inherits from <strong>IUnknown</strong> and also supports the following methods:<br/> <dl>[<strong>IAudioMediaType::GetAudioFormat</strong>](/windows/win32/Audiomediatype/nf-audiomediatype-iaudiomediatype-getaudioformat?branch=master) <br/><br />
[<strong>IAudioMediaType::GetUncompressedAudioFormat</strong>](/windows/win32/audiomediatype/nf-audiomediatype-iaudiomediatype-getuncompressedaudioformat?branch=master) <br/><br />
[<strong>IAudioMediaType::IsCompressedFormat</strong>](/windows/win32/audiomediatype/nf-audiomediatype-iaudiomediatype-iscompressedformat?branch=master) <br/><br />
[<strong>IAudioMediaType::IsEqual</strong>](/windows/win32/audiomediatype/nf-audiomediatype-iaudiomediatype-isequal?branch=master) <br/><br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>UNCOMPRESSEDAUUDIOFORMAT</strong>](/windows/win32/Audiomediatype/ns-audiomediatype-_uncompressedaudioformat?branch=master)<br/></td>
<td>The UNCOMPRESSEDAUDIOFORMAT structure specifies the frame rate, channel mask, and other attributes of the uncompressed audio data format.<br/></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Baudio\audio%5D:%20Audiomediatype.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




