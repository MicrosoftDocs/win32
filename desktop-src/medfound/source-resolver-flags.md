---
description: Defines the behavior of the source resolver. These flags are also used by scheme handlers and byte stream handlers.
ms.assetid: fe0b9090-5d2a-41a4-a806-57c874d3b3a2
title: Source Resolver Flags (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Source Resolver Flags

Defines the behavior of the source resolver. These flags are also used by scheme handlers and byte stream handlers.



| Constant/value                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MF_RESOLUTION_MEDIASOURCE"></span><span id="mf_resolution_mediasource"></span><dl> <dt>**MF\_RESOLUTION\_MEDIASOURCE**</dt> <dt>0x00000001</dt> </dl>                                                                                                                                           | Attempt to create a media source.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <span id="MF_RESOLUTION_BYTESTREAM"></span><span id="mf_resolution_bytestream"></span><dl> <dt>**MF\_RESOLUTION\_BYTESTREAM**</dt> <dt>0x00000002</dt> </dl>                                                                                                                                              | Attempt to create a byte stream.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="MF_RESOLUTION_CONTENT_DOES_NOT_HAVE_TO_MATCH_EXTENSION_OR_MIME_TYPE_"></span><span id="mf_resolution_content_does_not_have_to_match_extension_or_mime_type_"></span><dl> <dt>**MF\_RESOLUTION\_CONTENT\_DOES\_NOT\_HAVE\_TO\_MATCH\_EXTENSION\_OR\_MIME\_TYPE** </dt> <dt>0x00000010</dt> </dl> | If source resolution fails using the byte-stream handler that is registered for the MIME type or file name extension, the source resolver enumerates through all of the registered byte-stream handlers.<br/> Byte-stream handlers are registered by file name extension or MIME type. Initially, the source resolver attempts to use a handler that matches the file name extension or the MIME type. If that fails, then by default the entire source resolution fails and the source resolver returns an error code to the application. If this flag is specified, however, the source resolver continues to enumerates through all of the registered byte-stream handlers. Possibly a mis-matched handler can successfully create the media source.<br/> This flag cannot be combined with the MF\_RESOLUTION\_KEEP\_BYTE\_STREAM\_ALIVE\_ON\_FAIL flag. See Remarks for more information.<br/> |
| <span id="MF_RESOLUTION_KEEP_BYTE_STREAM_ALIVE_ON_FAIL"></span><span id="mf_resolution_keep_byte_stream_alive_on_fail"></span><dl> <dt>**MF\_RESOLUTION\_KEEP\_BYTE\_STREAM\_ALIVE\_ON\_FAIL**</dt> <dt>0x00000020</dt> </dl>                                                                             | If the source resolution fails, the source resolver does not close the byte stream. By default, the source resolver closes the byte stream on failure.<br/> If this flag is used and the source resolution fails, the caller should call the method again and set the MF\_RESOLUTION\_CONTENT\_DOES\_NOT\_HAVE\_TO\_MATCH\_EXTENSION\_OR\_MIME\_TYPE flag.<br/> This flag cannot be combined with the MF\_RESOLUTION\_CONTENT\_DOES\_NOT\_HAVE\_TO\_MATCH\_EXTENSION\_OR\_MIME\_TYPE flag. See Remarks for more information.<br/>                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="MF_RESOLUTION_READ"></span><span id="mf_resolution_read"></span><dl> <dt>**MF\_RESOLUTION\_READ**</dt> <dt>0x00010000</dt> </dl>                                                                                                                                                                | Requests read access to the source.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <span id="MF_RESOLUTION_WRITE"></span><span id="mf_resolution_write"></span><dl> <dt>**MF\_RESOLUTION\_WRITE**</dt> <dt>0x00020000</dt> </dl>                                                                                                                                                             | Requests write access to the source.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="MF_RESOLUTION_DISABLE_LOCAL_PLUGINS"></span><span id="mf_resolution_disable_local_plugins"></span><dl> <dt>**MF\_RESOLUTION\_DISABLE\_LOCAL\_PLUGINS**</dt> <dt>0x00000040</dt> </dl>                                                                                                           | The source resolver will not use locally registered scheme or bytestream handler plugins.<br/> Requires Windows 8.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |



## Remarks

The application sets these flags when it uses the [**IMFSourceResolver**](/windows/desktop/api/mfidl/nn-mfidl-imfsourceresolver) interface. The source resolver passes the same flags to the [**IMFByteStreamHandler::BeginCreateObject**](/windows/desktop/api/mfidl/nf-mfidl-imfbytestreamhandler-begincreateobject) and [**IMFSchemeHandler::BeginCreateObject**](/windows/desktop/api/mfidl/nf-mfidl-imfschemehandler-begincreateobject) methods.

You must specify one of the MF\_RESOLUTION\_MEDIASOURCE or MF\_RESOLUTION\_BYTESTREAM flags. The remaining flags are all optional.

The MF\_RESOLUTION\_KEEP\_BYTE\_STREAM\_ALIVE\_ON\_FAIL flag is defined for the following scenario:

1.  The application attempts to open a source over the network. The application sets the MF\_RESOLUTION\_KEEP\_BYTE\_STREAM\_ALIVE\_ON\_FAIL flag.

2.  The source's URL contains the wrong file name extension. Because the file name extension is wrong, the default byte-stream handler cannot create the media source. Because the application set the MF\_RESOLUTION\_KEEP\_BYTE\_STREAM\_ALIVE\_ON\_FAIL flag, the source resolver caches the byte stream.

3.  The source resolver returns an error code to the application.

4.  The client opens the source again, this time setting the MF\_RESOLUTION\_CONTENT\_DOES\_NOT\_HAVE\_TO\_MATCH\_EXTENSION\_OR\_MIME\_TYPE flag. This flag causes the source resolver to try all of the registered handlers instead of just the default handler. Because the byte stream was cached, the source resolver does not have to open the byte stream again.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Constants](media-foundation-constants.md)
</dt> <dt>

[**IMFByteStreamHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfbytestreamhandler)
</dt> <dt>

[**IMFSchemeHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfschemehandler)
</dt> <dt>

[**IMFSourceResolver**](/windows/desktop/api/mfidl/nn-mfidl-imfsourceresolver)
</dt> <dt>

[Source Resolver](source-resolver.md)
</dt> </dl>

 

 




