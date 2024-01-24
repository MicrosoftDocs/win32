---
title: Gopher Type Values (Wininet.h)
description: The following list contains the possible Gopher type values.
ms.assetid: e77a0328-d811-4c01-831a-0ead888a4988
topic_type:
- apiref
api_name:
- GOPHER_TYPE_ASK
- GOPHER_TYPE_BINARY
- GOPHER_TYPE_BITMAP
- GOPHER_TYPE_CALENDAR
- GOPHER_TYPE_CSO
- GOPHER_TYPE_DIRECTORY
- GOPHER_TYPE_DOS_ARCHIVE
- GOPHER_TYPE_ERROR
- GOPHER_TYPE_GIF
- GOPHER_TYPE_GOPHER_PLUS
- GOPHER_TYPE_HTML
- GOPHER_TYPE_IMAGE
- GOPHER_TYPE_INDEX_SERVER
- GOPHER_TYPE_INLINE
- GOPHER_TYPE_MAC_BINHEX
- GOPHER_TYPE_MOVIE
- GOPHER_TYPE_PDF
- GOPHER_TYPE_REDUNDANT
- GOPHER_TYPE_SOUND
- GOPHER_TYPE_TELNET
- GOPHER_TYPE_TEXT_FILE
- GOPHER_TYPE_TN3270
- GOPHER_TYPE_UNIX_UUENCODED
- GOPHER_TYPE_UNKNOWN
api_location:
- Wininet.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Gopher Type Values

\[These Gopher type vales are available for use in the operating systems specified in the Requirements section only.\]

The following list contains the possible Gopher type values.

<dl> <dt>

<span id="GOPHER_TYPE_ASK"></span><span id="gopher_type_ask"></span>**GOPHER\_TYPE\_ASK**
</dt> <dd> <dl> <dt>

0x40000000
</dt> <dt>



Ask+ item.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_BINARY"></span><span id="gopher_type_binary"></span>**GOPHER\_TYPE\_BINARY**
</dt> <dd> <dl> <dt>

0x00000200
</dt> <dt>



Binary file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_BITMAP"></span><span id="gopher_type_bitmap"></span>**GOPHER\_TYPE\_BITMAP**
</dt> <dd> <dl> <dt>

0x00004000
</dt> <dt>



Bitmap file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_CALENDAR"></span><span id="gopher_type_calendar"></span>**GOPHER\_TYPE\_CALENDAR**
</dt> <dd> <dl> <dt>

0x00080000
</dt> <dt>



Calendar file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_CSO"></span><span id="gopher_type_cso"></span>**GOPHER\_TYPE\_CSO**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



CSO telephone book server.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_DIRECTORY"></span><span id="gopher_type_directory"></span>**GOPHER\_TYPE\_DIRECTORY**
</dt> <dd> <dl> <dt>

0x00000002
</dt> <dt>



Directory of additional Gopher items.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_DOS_ARCHIVE"></span><span id="gopher_type_dos_archive"></span>**GOPHER\_TYPE\_DOS\_ARCHIVE**
</dt> <dd> <dl> <dt>

0x00000020
</dt> <dt>



MS-DOS archive file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_ERROR"></span><span id="gopher_type_error"></span>**GOPHER\_TYPE\_ERROR**
</dt> <dd> <dl> <dt>

0x00000008
</dt> <dt>



Indicator of an error condition.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_GIF"></span><span id="gopher_type_gif"></span>**GOPHER\_TYPE\_GIF**
</dt> <dd> <dl> <dt>

0x00001000
</dt> <dt>



GIF graphics file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_GOPHER_PLUS"></span><span id="gopher_type_gopher_plus"></span>**GOPHER\_TYPE\_GOPHER\_PLUS**
</dt> <dd> <dl> <dt>

0x80000000
</dt> <dt>



Gopher+ item.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_HTML"></span><span id="gopher_type_html"></span>**GOPHER\_TYPE\_HTML**
</dt> <dd> <dl> <dt>

0x00020000
</dt> <dt>



HTML document.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_IMAGE"></span><span id="gopher_type_image"></span>**GOPHER\_TYPE\_IMAGE**
</dt> <dd> <dl> <dt>

0x00002000
</dt> <dt>



Image file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_INDEX_SERVER"></span><span id="gopher_type_index_server"></span>**GOPHER\_TYPE\_INDEX\_SERVER**
</dt> <dd> <dl> <dt>

0x00000080
</dt> <dt>



Index server.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_INLINE"></span><span id="gopher_type_inline"></span>**GOPHER\_TYPE\_INLINE**
</dt> <dd> <dl> <dt>

0x00100000
</dt> <dt>



Inline file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_MAC_BINHEX"></span><span id="gopher_type_mac_binhex"></span>**GOPHER\_TYPE\_MAC\_BINHEX**
</dt> <dd> <dl> <dt>

0x00000010
</dt> <dt>



Macintosh file in BINHEX format.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_MOVIE"></span><span id="gopher_type_movie"></span>**GOPHER\_TYPE\_MOVIE**
</dt> <dd> <dl> <dt>

0x00008000
</dt> <dt>



Movie file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_PDF"></span><span id="gopher_type_pdf"></span>**GOPHER\_TYPE\_PDF**
</dt> <dd> <dl> <dt>

0x00040000
</dt> <dt>



PDF file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_REDUNDANT"></span><span id="gopher_type_redundant"></span>**GOPHER\_TYPE\_REDUNDANT**
</dt> <dd> <dl> <dt>

0x00000400
</dt> <dt>



Indicator of a duplicated server. The information contained within is a duplicate of the primary server. The primary server is defined as the last directory entry that did not have a GOPHER\_TYPE\_REDUNDANT type.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_SOUND"></span><span id="gopher_type_sound"></span>**GOPHER\_TYPE\_SOUND**
</dt> <dd> <dl> <dt>

0x00010000
</dt> <dt>



Sound file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_TELNET"></span><span id="gopher_type_telnet"></span>**GOPHER\_TYPE\_TELNET**
</dt> <dd> <dl> <dt>

0x00000100
</dt> <dt>



Telnet server.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_TEXT_FILE"></span><span id="gopher_type_text_file"></span>**GOPHER\_TYPE\_TEXT\_FILE**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



ASCII text file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_TN3270"></span><span id="gopher_type_tn3270"></span>**GOPHER\_TYPE\_TN3270**
</dt> <dd> <dl> <dt>

0x00000800
</dt> <dt>



TN3270 server.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_UNIX_UUENCODED"></span><span id="gopher_type_unix_uuencoded"></span>**GOPHER\_TYPE\_UNIX\_UUENCODED**
</dt> <dd> <dl> <dt>

0x00000040
</dt> <dt>



UUENCODED file.


</dt> </dl> </dd> <dt>

<span id="GOPHER_TYPE_UNKNOWN"></span><span id="gopher_type_unknown"></span>**GOPHER\_TYPE\_UNKNOWN**
</dt> <dd> <dl> <dt>

0x20000000
</dt> <dt>



Item type is unknown.


</dt> </dl> </dd> </dl>

## Remarks

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP<br/>                                                                |
| End of server support<br/>    | Windows Server 2003 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>Wininet.h</dt> </dl> |



 

