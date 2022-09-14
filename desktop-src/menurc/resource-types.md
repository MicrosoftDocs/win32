---
title: Resource Types (Winuser.h)
description: The following are the predefined resource types.
ms.assetid: 8d27f79a-8165-4565-a975-f25b2344efdc
topic_type:
- apiref
api_name:
- RT_ACCELERATOR
- RT_ANICURSOR
- RT_ANIICON
- RT_BITMAP
- RT_CURSOR
- RT_DIALOG
- RT_DLGINCLUDE
- RT_FONT
- RT_FONTDIR
- RT_GROUP_CURSOR
- RT_GROUP_ICON
- RT_HTML
- RT_ICON
- RT_MANIFEST
- RT_MENU
- RT_MESSAGETABLE
- RT_PLUGPLAY
- RT_RCDATA
- RT_STRING
- RT_VERSION
- RT_VXD
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Resource Types

The following are the predefined resource types.



| Constant/value                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                      |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RT_ACCELERATOR"></span><span id="rt_accelerator"></span><dl> <dt>**RT\_ACCELERATOR**</dt> <dt>MAKEINTRESOURCE(9)</dt> </dl>                                 | Accelerator table.<br/>                                                                                                                                                                                                                                                                    |
| <span id="RT_ANICURSOR"></span><span id="rt_anicursor"></span><dl> <dt>**RT\_ANICURSOR**</dt> <dt>MAKEINTRESOURCE(21)</dt> </dl>                                      | Animated cursor.<br/>                                                                                                                                                                                                                                                                      |
| <span id="RT_ANIICON"></span><span id="rt_aniicon"></span><dl> <dt>**RT\_ANIICON**</dt> <dt>MAKEINTRESOURCE(22)</dt> </dl>                                            | Animated icon.<br/>                                                                                                                                                                                                                                                                        |
| <span id="RT_BITMAP"></span><span id="rt_bitmap"></span><dl> <dt>**RT\_BITMAP**</dt> <dt>MAKEINTRESOURCE(2)</dt> </dl>                                                | Bitmap resource.<br/>                                                                                                                                                                                                                                                                      |
| <span id="RT_CURSOR"></span><span id="rt_cursor"></span><dl> <dt>**RT\_CURSOR**</dt> <dt>MAKEINTRESOURCE(1)</dt> </dl>                                                | Hardware-dependent cursor resource.<br/>                                                                                                                                                                                                                                                   |
| <span id="RT_DIALOG"></span><span id="rt_dialog"></span><dl> <dt>**RT\_DIALOG**</dt> <dt>MAKEINTRESOURCE(5)</dt> </dl>                                                | Dialog box.<br/>                                                                                                                                                                                                                                                                           |
| <span id="RT_DLGINCLUDE"></span><span id="rt_dlginclude"></span><dl> <dt>**RT\_DLGINCLUDE**</dt> <dt>MAKEINTRESOURCE(17)</dt> </dl>                                   | Allows a resource editing tool to associate a string with an .rc file. Typically, the string is the name of the header file that provides symbolic names. The resource compiler parses the string but otherwise ignores the value. For example, <br/> `1 DLGINCLUDE "MyFile.h"`<br/> |
| <span id="RT_FONT"></span><span id="rt_font"></span><dl> <dt>**RT\_FONT**</dt> <dt>MAKEINTRESOURCE(8)</dt> </dl>                                                      | Font resource.<br/>                                                                                                                                                                                                                                                                        |
| <span id="RT_FONTDIR"></span><span id="rt_fontdir"></span><dl> <dt>**RT\_FONTDIR**</dt> <dt>MAKEINTRESOURCE(7)</dt> </dl>                                             | Font directory resource.<br/>                                                                                                                                                                                                                                                              |
| <span id="RT_GROUP_CURSOR"></span><span id="rt_group_cursor"></span><dl> <dt>**RT\_GROUP\_CURSOR**</dt> <dt>MAKEINTRESOURCE((ULONG\_PTR)(RT\_CURSOR) + 11)</dt> </dl> | Hardware-independent cursor resource.<br/>                                                                                                                                                                                                                                                 |
| <span id="RT_GROUP_ICON"></span><span id="rt_group_icon"></span><dl> <dt>**RT\_GROUP\_ICON**</dt> <dt>MAKEINTRESOURCE((ULONG\_PTR)(RT\_ICON) + 11)</dt> </dl>         | Hardware-independent icon resource.<br/>                                                                                                                                                                                                                                                   |
| <span id="RT_HTML"></span><span id="rt_html"></span><dl> <dt>**RT\_HTML**</dt> <dt>MAKEINTRESOURCE(23)</dt> </dl>                                                     | HTML resource.<br/>                                                                                                                                                                                                                                                                        |
| <span id="RT_ICON"></span><span id="rt_icon"></span><dl> <dt>**RT\_ICON**</dt> <dt>MAKEINTRESOURCE(3)</dt> </dl>                                                      | Hardware-dependent icon resource.<br/>                                                                                                                                                                                                                                                     |
| <span id="RT_MANIFEST"></span><span id="rt_manifest"></span><dl> <dt>**RT\_MANIFEST**</dt> <dt>MAKEINTRESOURCE(24)</dt> </dl>                                         | Side-by-Side Assembly Manifest.<br/>                                                                                                                                                                                                                                                       |
| <span id="RT_MENU"></span><span id="rt_menu"></span><dl> <dt>**RT\_MENU**</dt> <dt>MAKEINTRESOURCE(4)</dt> </dl>                                                      | Menu resource.<br/>                                                                                                                                                                                                                                                                        |
| <span id="RT_MESSAGETABLE"></span><span id="rt_messagetable"></span><dl> <dt>**RT\_MESSAGETABLE**</dt> <dt>MAKEINTRESOURCE(11)</dt> </dl>                             | Message-table entry.<br/>                                                                                                                                                                                                                                                                  |
| <span id="RT_PLUGPLAY"></span><span id="rt_plugplay"></span><dl> <dt>**RT\_PLUGPLAY**</dt> <dt>MAKEINTRESOURCE(19)</dt> </dl>                                         | Plug and Play resource.<br/>                                                                                                                                                                                                                                                               |
| <span id="RT_RCDATA"></span><span id="rt_rcdata"></span><dl> <dt>**RT\_RCDATA**</dt> <dt>MAKEINTRESOURCE(10)</dt> </dl>                                               | Application-defined resource (raw data).<br/>                                                                                                                                                                                                                                              |
| <span id="RT_STRING"></span><span id="rt_string"></span><dl> <dt>**RT\_STRING**</dt> <dt>MAKEINTRESOURCE(6)</dt> </dl>                                                | String-table entry.<br/>                                                                                                                                                                                                                                                                   |
| <span id="RT_VERSION"></span><span id="rt_version"></span><dl> <dt>**RT\_VERSION**</dt> <dt>MAKEINTRESOURCE(16)</dt> </dl>                                            | Version resource.<br/>                                                                                                                                                                                                                                                                     |
| <span id="RT_VXD"></span><span id="rt_vxd"></span><dl> <dt>**RT\_VXD**</dt> <dt>MAKEINTRESOURCE(20)</dt> </dl>                                                        | VXD.<br/>                                                                                                                                                                                                                                                                                  |



## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winuser.h</dt> </dl> |



 

 





