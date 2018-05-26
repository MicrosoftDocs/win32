---
title: Structures
description: Structures
ms.assetid: 794de1b7-d60c-435e-9f77-c4df109b5372
keywords:
- Windows Media Format SDK,structures
- Advanced Systems Format (ASF),structures
- ASF (Advanced Systems Format),structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Structures

The Windows Media Format SDK implements the following structures.



| Structure                                                                                | Description                                                                                                                                                               |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRM\_COPY\_OPL**](/windows/win32/wmsdkidl/ns-wmsdkidl-__tagdrm_copy_opl?branch=master)                                                   | Holds output protection level information that applies to the copy action in a DRM license.                                                                               |
| [**DRM\_LICENSE\_STATE\_DATA**](drm-license-state-data.md)                              | Contains [*license*](wmformat-glossary.md#wmformat-license) information about a specified [*DRM*](wmformat-glossary.md#wmformat-digital-rights-management--drm-) right. |
| [**DRM\_MINIMUM\_OUTPUT\_PROTECTION\_LEVELS**](/windows/win32/wmsdkidl/ns-wmsdkidl-__tagdrm_minimum_output_protection_levels?branch=master) | Holds minimum output protection levels required by a DRM license to play content in various formats.                                                                      |
| [**DRM\_OPL\_OUTPUT\_IDS**](/windows/win32/wmsdkidl/ns-wmsdkidl-__tagdrm_opl_output_ids?branch=master)                                      | Holds an array of DRM technology identifiers. This structure is used to define groups of technologies in other DRM structures.                                            |
| [**DRM\_PLAY\_OPL**](/windows/win32/wmsdkidl/ns-wmsdkidl-__tagdrm_play_opl?branch=master)                                                   | Holds output protection level information that applies to the play action in a DRM license.                                                                               |
| [**DRM\_PLAYLIST\_CONTENT\_ID**](drm-playlist-content-id.md)                            | Contains information about content that is to be copied to CD as part of a playlist burn.                                                                                 |
| [**DRM\_VAL16**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_drm_val16?branch=master)                                                          | Stores a 128-bit value used as a device identifier.                                                                                                                       |
| [**DRM\_VIDEO\_OUTPUT\_PROTECTION**](/windows/win32/wmsdkidl/ns-wmsdkidl-__tagdrm_output_protection?branch=master)                    | Holds the identifier of a video protection technology and the configuration data required by that technology.                                                             |
| [**DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS**](/windows/win32/wmsdkidl/ns-wmsdkidl-__tagdrm_video_output_protection_ids?branch=master)           | Holds an array of **DRM\_VIDEO\_OUTPUT\_PROTECTION** structures.                                                                                                          |
| [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/desktop/dd757720)                                                | Defines the format of waveform-audio data.                                                                                                                                |
| [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/desktop/dd757721)                                | Defines the format of waveform-audio data for formats having more than two channels.                                                                                      |
| [**WM\_ADDRESS\_ACCESSENTRY**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmaddressaccessentry?branch=master)                               | Specifies an entry in an IP address access list.                                                                                                                          |
| [**WM\_CLIENT\_PROPERTIES**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmclientproperties?branch=master)                                   | Records information about the client.                                                                                                                                     |
| [**WM\_CLIENT\_PROPERTIES\_EX**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmclientpropertiesex?branch=master)                            | Records extended information about the client.                                                                                                                            |
| [**WM\_GET\_LICENSE\_DATA**](wm-get-license-data.md)                                    | Contains information about a DRM license.                                                                                                                                 |
| [**WM\_INDIVIDUALIZE\_STATUS**](wm-individualize-status.md)                             | Records the status of the [*individualization*](wmformat-glossary.md#wmformat-individualization) process.                                                                |
| [**WM\_LEAKY\_BUCKET\_PAIR**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmleakybucketpair?branch=master)                                  | Describes the buffering requirements for a variable-bit-rate (VBR) file.                                                                                                  |
| [**WM\_LICENSE\_STATE\_DATA**](/windows/win32/Wmsdkidl/?branch=master)                                | Encapsulates a [**DRM\_LICENSE\_STATE\_DATA**](drm-license-state-data.md) structure which describes DRM license state data.                                              |
| [**WM\_MEDIA\_TYPE**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmmediatype?branch=master)                                                 | Describes a media sample.                                                                                                                                                 |
| [**WMMPEG2VIDEOINFO**](/windows/win32/Wmsdkidl/ns-wmsdkidl-tagwmmpeg2videoinfo?branch=master)                                             | Describes an MPEG-2 video stream.                                                                                                                                         |
| [**WM\_PICTURE**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmpicture?branch=master)                                                        | Contains the data for the [**WM/Picture**](wmpicture.md) complex metadata attribute.                                                                                     |
| [**WM\_PORT\_NUMBER\_RANGE**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmportnumberrange?branch=master)                                  | Describes the range of port numbers used by the **IWMReaderNetworkConfig** interface.                                                                                     |
| [**WM\_READER\_CLIENTINFO**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmreaderclientinfo?branch=master)                                   | Describes the client reader (player) accessing the media stream.                                                                                                          |
| [**WM\_READER\_STATISTICS**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmreaderstatistics?branch=master)                                   | Describes the performance of a reading operation.                                                                                                                         |
| [**WMSCRIPTFORMAT**](/windows/win32/Wmsdkidl/ns-wmsdkidl-tagwmscriptformat?branch=master)                                                 | Defines the format of a script stream.                                                                                                                                    |
| [**WM\_STREAM\_PRIORITY\_RECORD**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmstreamprioritizationrecord?branch=master)                        | Contains a stream number and specifies whether delivery of that stream is mandatory.                                                                                      |
| [**WM\_STREAM\_TYPE\_INFO**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmstreamtypeinfo?branch=master)                                    | Contains the data for the [**WM/StreamTypeInfo**](wm-streamtypeinfo.md) complex metadata attribute.                                                                      |
| [**WM\_SYNCHRONISED\_LYRICS**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmsynchronisedlyrics?branch=master)                               | Contains the data for the [**WM/Lyrics\_Synchronised**](wm-lyrics-synchronised.md) complex metadata attribute.                                                           |
| [**WM\_USER\_TEXT**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmusertext?branch=master)                                                   | Contains the data for the [**WM/Text**](wm-text.md) complex metadata attribute.                                                                                          |
| [**WM\_USER\_WEB\_URL**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmuserweburl?branch=master)                                            | Contains the data for the [**WM/UserWebURL**](wm-userweburl.md) complex metadata attribute.                                                                              |
| [**WM\_WRITER\_STATISTICS**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmwriterstatistics?branch=master)                                   | Describes the performance of a writing operation.                                                                                                                         |
| [**WM\_WRITER\_STATISTICS\_EX**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmwriterstatisticsex?branch=master)                            | Contains extended writer statistics.                                                                                                                                      |
| [**WMDRM\_IMPORT\_CONTENT\_KEY**](wmdrm-import-content-key.md)                          | Holds the content key used in importing protected content.                                                                                                                |
| [**WMDRM\_IMPORT\_INIT\_STRUCT**](/windows/win32/wmsdkidl/ns-wmsdkidl-wmdrm_import_init_struct?branch=master)                          | Holds the encrypted session key and content key used in importing protected content.                                                                                      |
| [**WMDRM\_IMPORT\_SESSION\_KEY**](wmdrm-import-session-key.md)                          | Holds the session key for importing protected content.                                                                                                                    |
| [**WMT\_BUFFER\_SEGMENT**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmt_buffer_segment?branch=master)                                       | Contains the information necessary to specify a segment in a packet.                                                                                                      |
| [**WMT\_COLORSPACEINFO\_EXTENSION\_DATA**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmt_colorspaceinfo_extension_data?branch=master)        | Contains the data for the WM\_SampleExtensionGUID\_ColorSpaceInfo data unit extension.                                                                                    |
| [**WMT\_FILESINK\_DATA\_UNIT**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmt_filesink_data_unit?branch=master)                              | Contains information about a packet.                                                                                                                                      |
| [**WMT\_PAYLOAD\_FRAGMENT**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmt_payload_fragment?branch=master)                                   | Contains the information necessary to extract a payload fragment from a packet.                                                                                           |
| [**WMT\_TIMECODE\_EXTENSION\_DATA**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmt_timecode_extension_data?branch=master)                    | Contains a single SMPTE time code and related information.                                                                                                                |
| [**WMT\_VIDEOIMAGE\_SAMPLE**](/windows/win32/Wmsdkidl/ns-wmsdkidl-__wmt_videoimage_sample?branch=master)                                 | Contains information about a Video Image sample.                                                                                                                          |
| [**WMT\_WATERMARK\_ENTRY**](/windows/win32/Wmsdkidl/ns-wmsdkidl-__wmt_watermark_entry?branch=master)                                     | Contains information about a watermarking system.                                                                                                                         |
| [**WMT\_WEBSTREAM\_FORMAT**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmt_webstream_format?branch=master)                                   | Contains information about a Web stream.                                                                                                                                  |
| [**WMT\_WEBSTREAM\_SAMPLE\_HEADER**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmt_webstream_sample_header?branch=master)                    | Contains header information for Web stream samples.                                                                                                                       |
| [**WMVIDEOINFOHEADER**](/windows/win32/Wmsdkidl/ns-wmsdkidl-tagwmvideoinfoheader?branch=master)                                           | Describes the bitmap and color information for a video image.                                                                                                             |
| [**WMVIDEOINFOHEADER2**](/windows/win32/Wmsdkidl/ns-wmsdkidl-tagwmvideoinfoheader2?branch=master)                                         | Describes the bitmap and color information for a video image, including [*interlace*](wmformat-glossary.md#wmformat-interlace), copy protection, and aspect ratio.       |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 




