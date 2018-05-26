---
title: ADDRESSFORMAT enumeration
description: Do not use. Used by the GetFormat method to specify the format of a text-based representation of an address string.
ms.assetid: d11165b4-aa62-41b3-b87e-9d60ca166e35
keywords:
- ADDRESSFORMAT enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ADDRESSFORMAT enumeration

Do not use. Used by the [**GetFormat**](oe-imimeaddresstable-getformat.md) method to specify the format of a text-based representation of an address string.

## Syntax


```C++
typedef enum tagADDRESSFORMAT { 
  AFT_DISPLAY_FRIENDLY  = 0,
  AFT_DISPLAY_EMAIL     = 1,
  AFT_DISPLAY_BOTH      = 2,
  AFT_RFC822_DECODED    = 3,
  AFT_RFC822_ENCODED    = 4,
  AFT_RFC822_TRANSMIT   = 5
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="AFT_DISPLAY_FRIENDLY"></span><span id="aft_display_friendly"></span>**AFT\_DISPLAY\_FRIENDLY**
</dt> <dd>

Display only with friendly names of the addresses, for example, "Jo Brown; Mikael Sandberg".

</dd> <dt>

<span id="AFT_DISPLAY_EMAIL"></span><span id="aft_display_email"></span>**AFT\_DISPLAY\_EMAIL**
</dt> <dd>

Display only with friendly email addresses, for example, "jobrown@example.com; mikaelsandberg@example.com".

</dd> <dt>

<span id="AFT_DISPLAY_BOTH"></span><span id="aft_display_both"></span>**AFT\_DISPLAY\_BOTH**
</dt> <dd>

Display with both the friendly names and email addresses, for example, "Jo Brown &lt;jobrown@example.com&gt;; Mikael Sandberg &lt;mikaelsandberg@example.com&gt;".

</dd> <dt>

<span id="AFT_RFC822_DECODED"></span><span id="aft_rfc822_decoded"></span>**AFT\_RFC822\_DECODED**
</dt> <dd>

Display formatted according to the RFC822 standard. The friendly names are not encoded.

</dd> <dt>

<span id="AFT_RFC822_ENCODED"></span><span id="aft_rfc822_encoded"></span>**AFT\_RFC822\_ENCODED**
</dt> <dd>

Display formatted according to the RFC822 standard.

</dd> <dt>

<span id="AFT_RFC822_TRANSMIT"></span><span id="aft_rfc822_transmit"></span>**AFT\_RFC822\_TRANSMIT**
</dt> <dd>

Display formatted according to the RFC822 standard. The string can be wrapped to avoid exceeding the maximum line length.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





