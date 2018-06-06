---
title: Structures
description: Structures
ms.assetid: 794de1b7-d60c-435e-9f77-c4df109b5372
keywords:
- Windows Media Format SDK,structures
- Advanced Systems Format (ASF),structures
- ASF (Advanced Systems Format),structures
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Structures

The Windows Media Format SDK implements the following structures.



| Structure                                                                                | Description                                                                                                                                                               |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRM\_COPY\_OPL**](/windows/desktop/api/wmsdkidl/ns-wmsdkidl-__tagdrm_copy_opl)                                                   | Holds output protection level information that applies to the copy action in a DRM license.                                                                               |
| [**DRM\_LICENSE\_STATE\_DATA**](drm-license-state-data.md)                              | Contains [*license*](wmformat-glossary.md) information about a specified [*DRM*](wmformat-glossary.md) right. |
| [**DRM\_MINIMUM\_OUTPUT\_PROTECTION\_LEVELS**](/windows/desktop/api/wmsdkidl/ns-wmsdkidl-__tagdrm_minimum_output_protection_levels) | Holds minimum output protection levels required by a DRM license to play content in various formats.                                                                      |
| [**DRM\_OPL\_OUTPUT\_IDS**](/windows/desktop/api/wmsdkidl/ns-wmsdkidl-__tagdrm_opl_output_ids)                                      | Holds an array of DRM technology identifiers. This structure is used to define groups of technologies in other DRM structures.                                            |
| [**DRM\_PLAY\_OPL**](/windows/desktop/api/wmsdkidl/ns-wmsdkidl-__tagdrm_play_opl)                                                   | Holds output protection level information that applies to the play action in a DRM license.                                                                               |
| [**DRM\_PLAYLIST\_CONTENT\_ID**](drm-playlist-content-id.md)                            | Contains information about content that is to be copied to CD as part of a playlist burn.                                                                                 |
| [**DRM\_VAL16**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_drm_val16)                                                          | Stores a 128-bit value used as a device identifier.                                                                                                                       |
| [**DRM\_VIDEO\_OUTPUT\_PROTECTION**](/windows/desktop/api/wmsdkidl/ns-wmsdkidl-__tagdrm_output_protection)                    | Holds the identifier of a video protection technology and the configuration data required by that technology.                                                             |
| [**DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS**](/windows/desktop/api/wmsdkidl/ns-wmsdkidl-__tagdrm_video_output_protection_ids)           | Holds an array of **DRM\_VIDEO\_OUTPUT\_PROTECTION** structures.                                                                                                          |
| [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/desktop/dd757720)                                                | Defines the format of waveform-audio data.                                                                                                                                |
| [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/desktop/dd757721)                                | Defines the format of waveform-audio data for formats having more than two channels.                                                                                      |
| [**WM\_ADDRESS\_ACCESSENTRY**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmaddressaccessentry)                               | Specifies an entry in an IP address access list.                                                                                                                          |
| [**WM\_CLIENT\_PROPERTIES**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmclientproperties)                                   | Records information about the client.                                                                                                                                     |
| [**WM\_CLIENT\_PROPERTIES\_EX**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmclientpropertiesex)                            | Records extended information about the client.                                                                                                                            |
| [**WM\_GET\_LICENSE\_DATA**](wm-get-license-data.md)                                    | Contains information about a DRM license.                                                                                                                                 |
| [**WM\_INDIVIDUALIZE\_STATUS**](wm-individualize-status.md)                             | Records the status of the [*individualization*](wmformat-glossary.md) process.                                                                |
| [**WM\_LEAKY\_BUCKET\_PAIR**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmleakybucketpair)                                  | Describes the buffering requirements for a variable-bit-rate (VBR) file.                                                                                                  |
| [**WM\_LICENSE\_STATE\_DATA**](/windows/desktop/api/Wmsdkidl/)                                | Encapsulates a [**DRM\_LICENSE\_STATE\_DATA**](drm-license-state-data.md) structure which describes DRM license state data.                                              |
| [**WM\_MEDIA\_TYPE**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmmediatype)                                                 | Describes a media sample.                                                                                                                                                 |
| [**WMMPEG2VIDEOINFO**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-tagwmmpeg2videoinfo)                                             | Describes an MPEG-2 video stream.                                                                                                                                         |
| [**WM\_PICTURE**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmpicture)                                                        | Contains the data for the [**WM/Picture**](wmpicture.md) complex metadata attribute.                                                                                     |
| [**WM\_PORT\_NUMBER\_RANGE**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmportnumberrange)                                  | Describes the range of port numbers used by the **IWMReaderNetworkConfig** interface.                                                                                     |
| [**WM\_READER\_CLIENTINFO**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmreaderclientinfo)                                   | Describes the client reader (player) accessing the media stream.                                                                                                          |
| [**WM\_READER\_STATISTICS**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmreaderstatistics)                                   | Describes the performance of a reading operation.                                                                                                                         |
| [**WMSCRIPTFORMAT**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-tagwmscriptformat)                                                 | Defines the format of a script stream.                                                                                                                                    |
| [**WM\_STREAM\_PRIORITY\_RECORD**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmstreamprioritizationrecord)                        | Contains a stream number and specifies whether delivery of that stream is mandatory.                                                                                      |
| [**WM\_STREAM\_TYPE\_INFO**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmstreamtypeinfo)                                    | Contains the data for the [**WM/StreamTypeInfo**](wm-streamtypeinfo.md) complex metadata attribute.                                                                      |
| [**WM\_SYNCHRONISED\_LYRICS**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmsynchronisedlyrics)                               | Contains the data for the [**WM/Lyrics\_Synchronised**](wm-lyrics-synchronised.md) complex metadata attribute.                                                           |
| [**WM\_USER\_TEXT**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmusertext)                                                   | Contains the data for the [**WM/Text**](wm-text.md) complex metadata attribute.                                                                                          |
| [**WM\_USER\_WEB\_URL**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmuserweburl)                                            | Contains the data for the [**WM/UserWebURL**](wm-userweburl.md) complex metadata attribute.                                                                              |
| [**WM\_WRITER\_STATISTICS**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmwriterstatistics)                                   | Describes the performance of a writing operation.                                                                                                                         |
| [**WM\_WRITER\_STATISTICS\_EX**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmwriterstatisticsex)                            | Contains extended writer statistics.                                                                                                                                      |
| [**WMDRM\_IMPORT\_CONTENT\_KEY**](wmdrm-import-content-key.md)                          | Holds the content key used in importing protected content.                                                                                                                |
| [**WMDRM\_IMPORT\_INIT\_STRUCT**](/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmdrm_import_init_struct)                          | Holds the encrypted session key and content key used in importing protected content.                                                                                      |
| [**WMDRM\_IMPORT\_SESSION\_KEY**](wmdrm-import-session-key.md)                          | Holds the session key for importing protected content.                                                                                                                    |
| [**WMT\_BUFFER\_SEGMENT**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmt_buffer_segment)                                       | Contains the information necessary to specify a segment in a packet.                                                                                                      |
| [**WMT\_COLORSPACEINFO\_EXTENSION\_DATA**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmt_colorspaceinfo_extension_data)        | Contains the data for the WM\_SampleExtensionGUID\_ColorSpaceInfo data unit extension.                                                                                    |
| [**WMT\_FILESINK\_DATA\_UNIT**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmt_filesink_data_unit)                              | Contains information about a packet.                                                                                                                                      |
| [**WMT\_PAYLOAD\_FRAGMENT**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmt_payload_fragment)                                   | Contains the information necessary to extract a payload fragment from a packet.                                                                                           |
| [**WMT\_TIMECODE\_EXTENSION\_DATA**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmt_timecode_extension_data)                    | Contains a single SMPTE time code and related information.                                                                                                                |
| [**WMT\_VIDEOIMAGE\_SAMPLE**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-__wmt_videoimage_sample)                                 | Contains information about a Video Image sample.                                                                                                                          |
| [**WMT\_WATERMARK\_ENTRY**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-__wmt_watermark_entry)                                     | Contains information about a watermarking system.                                                                                                                         |
| [**WMT\_WEBSTREAM\_FORMAT**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmt_webstream_format)                                   | Contains information about a Web stream.                                                                                                                                  |
| [**WMT\_WEBSTREAM\_SAMPLE\_HEADER**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmt_webstream_sample_header)                    | Contains header information for Web stream samples.                                                                                                                       |
| [**WMVIDEOINFOHEADER**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-tagwmvideoinfoheader)                                           | Describes the bitmap and color information for a video image.                                                                                                             |
| [**WMVIDEOINFOHEADER2**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-tagwmvideoinfoheader2)                                         | Describes the bitmap and color information for a video image, including [*interlace*](wmformat-glossary.md), copy protection, and aspect ratio.       |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 




