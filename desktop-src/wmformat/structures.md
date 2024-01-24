---
title: Windows Media Format SDK Structures
description: Windows Media Format SDK Structures
ms.assetid: '118ef278-ca4f-4c30-9633-a2d851f5c758'
keywords:
- Windows Media Format SDK,structures
- Advanced Systems Format (ASF),structures
- ASF (Advanced Systems Format),structures
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Windows Media Format SDK Structures

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK implements the following structures.



| Structure                                                                                | Description                                                                                                                                                               |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRM\_COPY\_OPL**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-drm_copy_opl)                                                   | Holds output protection level information that applies to the copy action in a DRM license.                                                                               |
| [**DRM\_LICENSE\_STATE\_DATA**](drm-license-state-data.md)                              | Contains [*license*](wmformat-glossary.md) information about a specified [*DRM*](wmformat-glossary.md) right. |
| [**DRM\_MINIMUM\_OUTPUT\_PROTECTION\_LEVELS**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-drm_minimum_output_protection_levels) | Holds minimum output protection levels required by a DRM license to play content in various formats.                                                                      |
| [**DRM\_OPL\_OUTPUT\_IDS**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-drm_opl_output_ids)                                      | Holds an array of DRM technology identifiers. This structure is used to define groups of technologies in other DRM structures.                                            |
| [**DRM\_PLAY\_OPL**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-drm_play_opl)                                                   | Holds output protection level information that applies to the play action in a DRM license.                                                                               |
| [**DRM\_PLAYLIST\_CONTENT\_ID**](drm-playlist-content-id.md)                            | Contains information about content that is to be copied to CD as part of a playlist burn.                                                                                 |
| [**DRM\_VAL16**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-drm_val16)                                                          | Stores a 128-bit value used as a device identifier.                                                                                                                       |
| [**DRM\_VIDEO\_OUTPUT\_PROTECTION**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-drm_output_protection)                    | Holds the identifier of a video protection technology and the configuration data required by that technology.                                                             |
| [**DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-drm_video_output_protection_ids)           | Holds an array of **DRM\_VIDEO\_OUTPUT\_PROTECTION** structures.                                                                                                          |
| [**WAVEFORMATEX**](/previous-versions/windows/desktop/legacy/dd757720(v=vs.85))                                                | Defines the format of waveform-audio data.                                                                                                                                |
| [**WAVEFORMATEXTENSIBLE**](/previous-versions/windows/desktop/legacy/dd757721(v=vs.85))                                | Defines the format of waveform-audio data for formats having more than two channels.                                                                                      |
| [**WM\_ADDRESS\_ACCESSENTRY**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_address_accessentry)                               | Specifies an entry in an IP address access list.                                                                                                                          |
| [**WM\_CLIENT\_PROPERTIES**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_client_properties)                                   | Records information about the client.                                                                                                                                     |
| [**WM\_CLIENT\_PROPERTIES\_EX**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_client_properties_ex)                            | Records extended information about the client.                                                                                                                            |
| [**WM\_GET\_LICENSE\_DATA**](wm-get-license-data.md)                                    | Contains information about a DRM license.                                                                                                                                 |
| [**WM\_INDIVIDUALIZE\_STATUS**](wm-individualize-status.md)                             | Records the status of the [*individualization*](wmformat-glossary.md) process.                                                                |
| [**WM\_LEAKY\_BUCKET\_PAIR**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_leaky_bucket_pair)                                  | Describes the buffering requirements for a variable-bit-rate (VBR) file.                                                                                                  |
| [**WM\_LICENSE\_STATE\_DATA**](/previous-versions/windows/desktop/legacy/dd757942(v=vs.85))                                | Encapsulates a [**DRM\_LICENSE\_STATE\_DATA**](drm-license-state-data.md) structure which describes DRM license state data.                                              |
| [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type)                                                 | Describes a media sample.                                                                                                                                                 |
| [**WMMPEG2VIDEOINFO**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmmpeg2videoinfo)                                             | Describes an MPEG-2 video stream.                                                                                                                                         |
| [**WM\_PICTURE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_picture)                                                        | Contains the data for the [**WM/Picture**](wmpicture.md) complex metadata attribute.                                                                                     |
| [**WM\_PORT\_NUMBER\_RANGE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_port_number_range)                                  | Describes the range of port numbers used by the **IWMReaderNetworkConfig** interface.                                                                                     |
| [**WM\_READER\_CLIENTINFO**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_reader_clientinfo)                                   | Describes the client reader (player) accessing the media stream.                                                                                                          |
| [**WM\_READER\_STATISTICS**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_reader_statistics)                                   | Describes the performance of a reading operation.                                                                                                                         |
| [**WMSCRIPTFORMAT**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmscriptformat)                                                 | Defines the format of a script stream.                                                                                                                                    |
| [**WM\_STREAM\_PRIORITY\_RECORD**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_stream_priority_record)                        | Contains a stream number and specifies whether delivery of that stream is mandatory.                                                                                      |
| [**WM\_STREAM\_TYPE\_INFO**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_stream_type_info)                                    | Contains the data for the [**WM/StreamTypeInfo**](wm-streamtypeinfo.md) complex metadata attribute.                                                                      |
| [**WM\_SYNCHRONISED\_LYRICS**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_synchronised_lyrics)                               | Contains the data for the [**WM/Lyrics\_Synchronised**](wm-lyrics-synchronised.md) complex metadata attribute.                                                           |
| [**WM\_USER\_TEXT**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_user_text)                                                   | Contains the data for the [**WM/Text**](wm-text.md) complex metadata attribute.                                                                                          |
| [**WM\_USER\_WEB\_URL**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_user_web_url)                                            | Contains the data for the [**WM/UserWebURL**](wm-userweburl.md) complex metadata attribute.                                                                              |
| [**WM\_WRITER\_STATISTICS**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_writer_statistics)                                   | Describes the performance of a writing operation.                                                                                                                         |
| [**WM\_WRITER\_STATISTICS\_EX**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_writer_statistics_ex)                            | Contains extended writer statistics.                                                                                                                                      |
| [**WMDRM\_IMPORT\_CONTENT\_KEY**](wmdrm-import-content-key.md)                          | Holds the content key used in importing protected content.                                                                                                                |
| [**WMDRM\_IMPORT\_INIT\_STRUCT**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmdrm_import_init_struct)                          | Holds the encrypted session key and content key used in importing protected content.                                                                                      |
| [**WMDRM\_IMPORT\_SESSION\_KEY**](wmdrm-import-session-key.md)                          | Holds the session key for importing protected content.                                                                                                                    |
| [**WMT\_BUFFER\_SEGMENT**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_buffer_segment)                                       | Contains the information necessary to specify a segment in a packet.                                                                                                      |
| [**WMT\_COLORSPACEINFO\_EXTENSION\_DATA**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_colorspaceinfo_extension_data)        | Contains the data for the WM\_SampleExtensionGUID\_ColorSpaceInfo data unit extension.                                                                                    |
| [**WMT\_FILESINK\_DATA\_UNIT**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_filesink_data_unit)                              | Contains information about a packet.                                                                                                                                      |
| [**WMT\_PAYLOAD\_FRAGMENT**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_payload_fragment)                                   | Contains the information necessary to extract a payload fragment from a packet.                                                                                           |
| [**WMT\_TIMECODE\_EXTENSION\_DATA**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_timecode_extension_data)                    | Contains a single SMPTE time code and related information.                                                                                                                |
| [**WMT\_VIDEOIMAGE\_SAMPLE**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample)                                 | Contains information about a Video Image sample.                                                                                                                          |
| [**WMT\_WATERMARK\_ENTRY**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_watermark_entry)                                     | Contains information about a watermarking system.                                                                                                                         |
| [**WMT\_WEBSTREAM\_FORMAT**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_webstream_format)                                   | Contains information about a Web stream.                                                                                                                                  |
| [**WMT\_WEBSTREAM\_SAMPLE\_HEADER**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_webstream_sample_header)                    | Contains header information for Web stream samples.                                                                                                                       |
| [**WMVIDEOINFOHEADER**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmvideoinfoheader)                                           | Describes the bitmap and color information for a video image.                                                                                                             |
| [**WMVIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmvideoinfoheader2)                                         | Describes the bitmap and color information for a video image, including [*interlace*](wmformat-glossary.md), copy protection, and aspect ratio.       |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 
