---
title: Windows Media Format SDK Enumeration Types
description: Learn about the enumeration types that the Windows Media Format SDK implements, such as DRM_HTTP_STATUS and DRM_LICENSE_STATE_CATEGORY.
ms.assetid: 'cd28f608-25ba-44a7-868b-b1cd4dfcfa45'
keywords:
- Windows Media Format SDK,enumeration types
- Advanced Systems Format (ASF),enumeration types
- ASF (Advanced Systems Format),enumeration types
- enumeration types
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Windows Media Format SDK Enumeration Types

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK implements the following enumeration types.



| Enumeration type                                                               | Description                                                                                                                      |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**DRM\_HTTP\_STATUS**](drm-http-status.md)                                   | Defines a range of states for a DRM request.                                                                                     |
| [**DRM\_LICENSE\_STATE\_CATEGORY**](drm-license-state-category.md)            | Defines the categories for DRM license strings.                                                                                  |
| [**DRM\_INDIVIDUALIZATION\_STATUS**](drm-individualization-status.md)         | Defines the valid states for DRM individualization.                                                                              |
| [**NETSOURCE\_URLCREDPOLICY\_SETTINGS**](/previous-versions/windows/desktop/api/wmsinternaladminnetsource/ne-wmsinternaladminnetsource-netsource_urlcredpolicy_settings) | Defines possible security policy settings that can exist on a client computer.                                                   |
| [**WM\_AETYPE**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wm_aetype)                                                | Specifies the permissions for an entry in an IP address access list.                                                             |
| [**WMT\_ATTR\_DATATYPE**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_attr_datatype)                               | Defines a range of basic data types. These values are used to identify the type of data returned by various methods in this SDK. |
| [**WMT\_ATTR\_IMAGETYPE**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_attr_imagetype)                             | Defines a range of image types that can be stored in an ASF file header.                                                         |
| [**WMT\_CODEC\_INFO\_TYPE**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_codec_info_type)                          | Defines a range of data sizes used by a codec.                                                                                   |
| [**WMT\_CREDENTIAL\_FLAGS**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_credential_flags)                         | Defines the flags that can be used when acquiring credentials.                                                                   |
| [**WMT\_DRMLA\_TRUST**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_drmla_trust)                                   | Defines the trust state of a DRM license acquisition URL.                                                                        |
| [**WMT\_FILESINK\_MODE**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_filesink_mode)                               | Defines the types of input accepted by the file sink.                                                                            |
| [**WMT\_IMAGE\_TYPE**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_image_type)                                     | Defines the possible image types used for banner ads.                                                                            |
| [**WMT\_INDEX\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_index_type)                                     | Defines the object with which a time-based index can be associated.                                                              |
| [**WMT\_INDEXER\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_indexer_type)                                 | Defines the types of indexing supported by the indexer.                                                                          |
| [**WMT\_NET\_PROTOCOL**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_net_protocol)                                 | Defines the types of protocols that the network sink supports.                                                                   |
| [**WMT\_MUSICSPEECH\_CLASS\_MODE**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_musicspeech_class_mode)            | Defines the compression modes available to the Windows Media Audio 9 Voice codec.                                                |
| [**WMT\_OFFSET\_FORMAT**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_offset_format)                               | Defines the types of offsets used in this SDK.                                                                                   |
| [**WMT\_PLAY\_MODE**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_play_mode)                                       | Defines the playback options of the reader.                                                                                      |
| [**WMT\_PROXY\_SETTINGS**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_proxy_settings)                             | Defines the network proxy settings for use with a reader object.                                                                 |
| [**WMT\_RIGHTS**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_rights)                                              | Defines the rights that may be specified in a DRM license.                                                                       |
| [**WMT\_STATUS**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_status)                                              | Defines a range of status flags.                                                                                                 |
| [**WMT\_STORAGE\_FORMAT**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_storage_format)                             | Defines the file types that can be manipulated with this SDK.                                                                    |
| [**WMT\_STREAM\_SELECTION**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_stream_selection)                         | Defines the status of a stream.                                                                                                  |
| [**WMT\_TRANSPORT\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_transport_type)                             | Defines the transport types supported by this SDK.                                                                               |
| [**WMT\_VERSION**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_version)                                            | Defines the version numbers of the Windows Media Format SDK.                                                                     |
| [**WMT\_WATERMARK\_ENTRY\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_watermark_entry_type)                | Defines the types of supported watermarks.                                                                                       |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 




