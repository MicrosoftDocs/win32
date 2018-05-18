---
title: WEBPAGEOPTIONS structure
description: Do not use. Holds the options that affect the behavior of the CreateWebPage method.
ms.assetid: 'c8f7e0e0-a186-4296-9824-93fc2290ea26'
keywords: ["WEBPAGEOPTIONS structure Windows Mail (formerly Outlook Express)", "LPWEBPAGEOPTIONS structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- WEBPAGEOPTIONS
api_location:
- Mimeole.h
api_type:
- HeaderDef
---

# WEBPAGEOPTIONS structure

Do not use. Holds the options that affect the behavior of the [**CreateWebPage**](oe-imimemessage-createwebpage.md) method.

## Syntax


```C++
typedef struct tagWEBPAGEOPTIONS {
  DWORD cbSize;
  DWORD dwFlags;
  DWORD dwDelay;
  WCHAR wchQuote;
} WEBPAGEOPTIONS, *LPWEBPAGEOPTIONS;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the size, in bytes, of this structure.

</dd> <dt>

**dwFlags**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a bitmask that indicates the behavior of the method.



| Value                                                                                                                                                                                                                                     | Meaning                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span id="WPF_HTML"></span><span id="wpf_html"></span><dl> <dt>**WPF\_HTML**</dt> <dt>0x00000001</dt> </dl>                            | Indicates that the webpage should generate HTML. If not set, MimeOLE uses plain text. <br/> |
| <span id="WPF_AUTOINLINE"></span><span id="wpf_autoinline"></span><dl> <dt>**WPF\_AUTOINLINE**</dt> <dt>0x00000002</dt> </dl>          | Indicates that images should be inline in the HTML. <br/>                                   |
| <span id="WPF_SLIDESHOW"></span><span id="wpf_slideshow"></span><dl> <dt>**WPF\_SLIDESHOW**</dt> <dt>0x00000004</dt> </dl>             | Indicates that images should be presented as an inline slide show. <br/>                    |
| <span id="WPF_ATTACHLINKS"></span><span id="wpf_attachlinks"></span><dl> <dt>**WPF\_ATTACHLINKS**</dt> <dt>0x00000008</dt> </dl>       | Indicates that links to attachments should be generated. <br/>                              |
| <span id="WPF_IMAGESONLY"></span><span id="wpf_imagesonly"></span><dl> <dt>**WPF\_IMAGESONLY**</dt> <dt>0x00000010</dt> </dl>          | Indicates that only image attachments should be displayed. <br/>                            |
| <span id="WPF_NOMETACHARSET"></span><span id="wpf_nometacharset"></span><dl> <dt>**WPF\_NOMETACHARSET**</dt> <dt>0x00000020</dt> </dl> | Indicates that MimeOLE should not prefix the HTML with a meta-charset tag. <br/>            |



 

</dd> <dt>

**dwDelay**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the delay time, in milliseconds, between images in a slide show.

</dd> <dt>

**wchQuote**
</dt> <dd>

Type: **WCHAR**

</dd> <dd>

Contains the quoting character for a reply.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





