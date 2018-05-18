---
title: Structures
description: Structures
ms.assetid: '794de1b7-d60c-435e-9f77-c4df109b5372'
keywords: ["Windows Media Format SDK,structures", "Advanced Systems Format (ASF),structures", "ASF (Advanced Systems Format),structures"]
---

# Structures

The Windows Media Format SDK implements the following structures.



| Structure                                                                                | Description                                                                                                                                                               |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DRM\_COPY\_OPL**](drm-copy-opl.md)                                                   | Holds output protection level information that applies to the copy action in a DRM license.                                                                               |
| [**DRM\_LICENSE\_STATE\_DATA**](drm-license-state-data.md)                              | Contains [*license*](wmformat-glossary.md#wmformat-license) information about a specified [*DRM*](wmformat-glossary.md#wmformat-digital-rights-management--drm-) right. |
| [**DRM\_MINIMUM\_OUTPUT\_PROTECTION\_LEVELS**](drm-minimum-output-protection-levels.md) | Holds minimum output protection levels required by a DRM license to play content in various formats.                                                                      |
| [**DRM\_OPL\_OUTPUT\_IDS**](drm-opl-output-ids.md)                                      | Holds an array of DRM technology identifiers. This structure is used to define groups of technologies in other DRM structures.                                            |
| [**DRM\_PLAY\_OPL**](drm-play-opl.md)                                                   | Holds output protection level information that applies to the play action in a DRM license.                                                                               |
| [**DRM\_PLAYLIST\_CONTENT\_ID**](drm-playlist-content-id.md)                            | Contains information about content that is to be copied to CD as part of a playlist burn.                                                                                 |
| [**DRM\_VAL16**](drm-val16.md)                                                          | Stores a 128-bit value used as a device identifier.                                                                                                                       |
| [**DRM\_VIDEO\_OUTPUT\_PROTECTION**](drm-video-output-protection.md)                    | Holds the identifier of a video protection technology and the configuration data required by that technology.                                                             |
| [**DRM\_VIDEO\_OUTPUT\_PROTECTION\_IDS**](drm-video-output-protection-ids.md)           | Holds an array of **DRM\_VIDEO\_OUTPUT\_PROTECTION** structures.                                                                                                          |
| [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/desktop/dd757720)                                                | Defines the format of waveform-audio data.                                                                                                                                |
| [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/desktop/dd757721)                                | Defines the format of waveform-audio data for formats having more than two channels.                                                                                      |
| [**WM\_ADDRESS\_ACCESSENTRY**](wm-address-accessentry.md)                               | Specifies an entry in an IP address access list.                                                                                                                          |
| [**WM\_CLIENT\_PROPERTIES**](wm-client-properties.md)                                   | Records information about the client.                                                                                                                                     |
| [**WM\_CLIENT\_PROPERTIES\_EX**](wm-client-properties-ex.md)                            | Records extended information about the client.                                                                                                                            |
| [**WM\_GET\_LICENSE\_DATA**](wm-get-license-data.md)                                    | Contains information about a DRM license.                                                                                                                                 |
| [**WM\_INDIVIDUALIZE\_STATUS**](wm-individualize-status.md)                             | Records the status of the [*individualization*](wmformat-glossary.md#wmformat-individualization) process.                                                                |
| [**WM\_LEAKY\_BUCKET\_PAIR**](wm-leaky-bucket-pair.md)                                  | Describes the buffering requirements for a variable-bit-rate (VBR) file.                                                                                                  |
| [**WM\_LICENSE\_STATE\_DATA**](wm-license-state-data.md)                                | Encapsulates a [**DRM\_LICENSE\_STATE\_DATA**](drm-license-state-data.md) structure which describes DRM license state data.                                              |
| [**WM\_MEDIA\_TYPE**](wm-media-type.md)                                                 | Describes a media sample.                                                                                                                                                 |
| [**WMMPEG2VIDEOINFO**](wmmpeg2videoinfo.md)                                             | Describes an MPEG-2 video stream.                                                                                                                                         |
| [**WM\_PICTURE**](wm-picture.md)                                                        | Contains the data for the [**WM/Picture**](wmpicture.md) complex metadata attribute.                                                                                     |
| [**WM\_PORT\_NUMBER\_RANGE**](wm-port-number-range.md)                                  | Describes the range of port numbers used by the **IWMReaderNetworkConfig** interface.                                                                                     |
| [**WM\_READER\_CLIENTINFO**](wm-reader-clientinfo.md)                                   | Describes the client reader (player) accessing the media stream.                                                                                                          |
| [**WM\_READER\_STATISTICS**](wm-reader-statistics.md)                                   | Describes the performance of a reading operation.                                                                                                                         |
| [**WMSCRIPTFORMAT**](wmscriptformat.md)                                                 | Defines the format of a script stream.                                                                                                                                    |
| [**WM\_STREAM\_PRIORITY\_RECORD**](wm-stream-priority-record.md)                        | Contains a stream number and specifies whether delivery of that stream is mandatory.                                                                                      |
| [**WM\_STREAM\_TYPE\_INFO**](wm-stream-type-info.md)                                    | Contains the data for the [**WM/StreamTypeInfo**](wm-streamtypeinfo.md) complex metadata attribute.                                                                      |
| [**WM\_SYNCHRONISED\_LYRICS**](wm-synchronised-lyrics.md)                               | Contains the data for the [**WM/Lyrics\_Synchronised**](wm-lyrics-synchronised.md) complex metadata attribute.                                                           |
| [**WM\_USER\_TEXT**](wm-user-text.md)                                                   | Contains the data for the [**WM/Text**](wm-text.md) complex metadata attribute.                                                                                          |
| [**WM\_USER\_WEB\_URL**](wm-user-web-url.md)                                            | Contains the data for the [**WM/UserWebURL**](wm-userweburl.md) complex metadata attribute.                                                                              |
| [**WM\_WRITER\_STATISTICS**](wm-writer-statistics.md)                                   | Describes the performance of a writing operation.                                                                                                                         |
| [**WM\_WRITER\_STATISTICS\_EX**](wm-writer-statistics-ex.md)                            | Contains extended writer statistics.                                                                                                                                      |
| [**WMDRM\_IMPORT\_CONTENT\_KEY**](wmdrm-import-content-key.md)                          | Holds the content key used in importing protected content.                                                                                                                |
| [**WMDRM\_IMPORT\_INIT\_STRUCT**](wmdrm-import-init-struct.md)                          | Holds the encrypted session key and content key used in importing protected content.                                                                                      |
| [**WMDRM\_IMPORT\_SESSION\_KEY**](wmdrm-import-session-key.md)                          | Holds the session key for importing protected content.                                                                                                                    |
| [**WMT\_BUFFER\_SEGMENT**](wmt-buffer-segment.md)                                       | Contains the information necessary to specify a segment in a packet.                                                                                                      |
| [**WMT\_COLORSPACEINFO\_EXTENSION\_DATA**](wmt-colorspaceinfo-extension-data.md)        | Contains the data for the WM\_SampleExtensionGUID\_ColorSpaceInfo data unit extension.                                                                                    |
| [**WMT\_FILESINK\_DATA\_UNIT**](wmt-filesink-data-unit.md)                              | Contains information about a packet.                                                                                                                                      |
| [**WMT\_PAYLOAD\_FRAGMENT**](wmt-payload-fragment.md)                                   | Contains the information necessary to extract a payload fragment from a packet.                                                                                           |
| [**WMT\_TIMECODE\_EXTENSION\_DATA**](wmt-timecode-extension-data.md)                    | Contains a single SMPTE time code and related information.                                                                                                                |
| [**WMT\_VIDEOIMAGE\_SAMPLE**](wmt-videoimage-sample.md)                                 | Contains information about a Video Image sample.                                                                                                                          |
| [**WMT\_WATERMARK\_ENTRY**](wmt-watermark-entry.md)                                     | Contains information about a watermarking system.                                                                                                                         |
| [**WMT\_WEBSTREAM\_FORMAT**](wmt-webstream-format.md)                                   | Contains information about a Web stream.                                                                                                                                  |
| [**WMT\_WEBSTREAM\_SAMPLE\_HEADER**](wmt-webstream-sample-header.md)                    | Contains header information for Web stream samples.                                                                                                                       |
| [**WMVIDEOINFOHEADER**](wmvideoinfoheader.md)                                           | Describes the bitmap and color information for a video image.                                                                                                             |
| [**WMVIDEOINFOHEADER2**](wmvideoinfoheader2.md)                                         | Describes the bitmap and color information for a video image, including [*interlace*](wmformat-glossary.md#wmformat-interlace), copy protection, and aspect ratio.       |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 




