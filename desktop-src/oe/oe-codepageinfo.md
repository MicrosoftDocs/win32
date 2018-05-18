---
title: CODEPAGEINFO structure
description: Do not use. Holds information about a code page. A client can use an IMimeInternational object to look up a CODEPAGEINFO for a given CODEPAGEID.
ms.assetid: 'd5946880-3fe9-4a61-93a0-09c4ae916723'
keywords: ["CODEPAGEINFO structure Windows Mail (formerly Outlook Express)", "LPCODEPAGEINFO structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- CODEPAGEINFO
api_location:
- Mimeole.h
api_type:
- HeaderDef
---

# CODEPAGEINFO structure

Do not use. Holds information about a code page. A client can use an [**IMimeInternational**](oe-imimeinternational.md) object to look up a **CODEPAGEINFO** for a given CODEPAGEID.

## Syntax


```C++
typedef struct tagCODEPAGEINFO {
  DWORD        dwMask;
  CODEPAGEID   cpiCodePage;
  BOOL         fIsValidCodePage;
  ULONG        ulMaxCharSize;
  BOOL         fInternetCP;
  CODEPAGEID   cpiFamily;
  CHAR         szName[CCHMAX_LANG_NAME];
  CHAR         szBodyCset[CCHMAX_CSET_NAME];
  CHAR         szHeaderCset[CCHMAX_CSET_NAME];
  CHAR         szWebCset[CCHMAX_CSET_NAME];
  CHAR         szFixedFont[CCHMAX_FACE_NAME];
  CHAR         szVariableFont[CCHMAX_FACE_NAME];
  ENCODINGTYPE ietNewsDefault;
  ENCODINGTYPE ietMailDefault;
  DWORD        dwReserved1;
} CODEPAGEINFO, *LPCODEPAGEINFO;
```



## Members

<dl> <dt>

**dwMask**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a bitmask that indicates the valid fields in this structure. (INETLANGMASK)



| Value                                                                                                                                                                                                                                  | Meaning                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <span id="ILM_FAMILY"></span><span id="ilm_family"></span><dl> <dt>**ILM\_FAMILY**</dt> <dt>0x00000001</dt> </dl>                   | Indicates that **cpiFamily** is valid. <br/>      |
| <span id="ILM_NAME"></span><span id="ilm_name"></span><dl> <dt>**ILM\_NAME**</dt> <dt>0x00000002</dt> </dl>                         | Indicates that **szName** is valid. <br/>         |
| <span id="ILM_BODYCSET"></span><span id="ilm_bodycset"></span><dl> <dt>**ILM\_BODYCSET**</dt> <dt>0x00000004</dt> </dl>             | Indicates that **szBodyCset** is valid. <br/>     |
| <span id="ILM_HEADERCSET"></span><span id="ilm_headercset"></span><dl> <dt>**ILM\_HEADERCSET**</dt> <dt>0x00000008</dt> </dl>       | Indicates that **szHeaderCset** is valid. <br/>   |
| <span id="ILM_WEBCSET"></span><span id="ilm_webcset"></span><dl> <dt>**ILM\_WEBCSET**</dt> <dt>0x00000010</dt> </dl>                | Indicates that **szWebCset** is valid. <br/>      |
| <span id="ILM_FIXEDFONT"></span><span id="ilm_fixedfont"></span><dl> <dt>**ILM\_FIXEDFONT**</dt> <dt>0x00000020</dt> </dl>          | Indicates that **szFixedFont** is valid. <br/>    |
| <span id="ILM_VARIABLEFONT"></span><span id="ilm_variablefont"></span><dl> <dt>**ILM\_VARIABLEFONT**</dt> <dt>0x00000040</dt> </dl> | Indicates that **szVariableFont** is valid. <br/> |



 

</dd> <dt>

**cpiCodePage**
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

</dd> <dd>

Contains the ID of this code page. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

**fIsValidCodePage**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains the result of IsValidCodePage(**cpiCodePage**). This member is **TRUE** when this code page is a valid Windows code page.

</dd> <dt>

**ulMaxCharSize**
</dt> <dd>

Type: **ULONG**

</dd> <dd>

Contains the size, in bytes, of the largest character in the code page.

</dd> <dt>

**fInternetCP**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a value that indicates whether this is an Internet code page. When this member is **TRUE**, text encoded in this code page can be transmitted over the Internet.

</dd> <dt>

**cpiFamily**
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

</dd> <dd>

Contains the Windows code page ID when **fInternetCP** is **TRUE**. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

**szName**
</dt> <dd>

Type: **CHAR\[CCHMAX\_LANG\_NAME\]**

</dd> <dd>

Contains the name or description of this code page.

</dd> <dt>

**szBodyCset**
</dt> <dd>

Type: **CHAR\[CCHMAX\_CSET\_NAME\]**

</dd> <dd>

Contains the name of the default body character set that corresponds to [**CHARSET\_BODY**](oe-charsettype.md).

</dd> <dt>

**szHeaderCset**
</dt> <dd>

Type: **CHAR\[CCHMAX\_CSET\_NAME\]**

</dd> <dd>

Contains the name of the default header character set that corresponds to [**CHARSET\_HEADER**](oe-charsettype.md).

</dd> <dt>

**szWebCset**
</dt> <dd>

Type: **CHAR\[CCHMAX\_CSET\_NAME\]**

</dd> <dd>

Contains the name of the default Web character set that corresponds to [**CHARSET\_WEB**](oe-charsettype.md).

</dd> <dt>

**szFixedFont**
</dt> <dd>

Type: **CHAR\[CCHMAX\_FACE\_NAME\]**

</dd> <dd>

Contains the name of the default typeface to use as the fixed width font.

</dd> <dt>

**szVariableFont**
</dt> <dd>

Type: **CHAR\[CCHMAX\_FACE\_NAME\]**

</dd> <dd>

Contains the name of the default typeface to use as the variable width font.

</dd> <dt>

**ietNewsDefault**
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

</dd> <dd>

Contains the default [**ENCODINGTYPE**](oe-encodingtype.md) for News messages (**IET\_QP** or **IET\_BASE64**).

</dd> <dt>

**ietMailDefault**
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

</dd> <dd>

Contains the default [**ENCODINGTYPE**](oe-encodingtype.md) for Mail messages (**IET\_QP** or **IET\_BASE64**).

</dd> <dt>

**dwReserved1**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Do not use.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





