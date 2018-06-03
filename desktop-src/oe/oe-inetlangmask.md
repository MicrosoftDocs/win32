---
title: INETLANGMASK enumeration
description: Do not use. Specifies the validity of a member of the CODEPAGEINFO structure.
ms.assetid: fabe6728-d0c0-48bd-acc8-e60fe2c77637
keywords:
- INETLANGMASK enumeration Windows Mail (formerly Outlook Express)
- ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Mimeole.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# INETLANGMASK enumeration

Do not use. Specifies the validity of a member of the [**CODEPAGEINFO**](oe-codepageinfo.md) structure.

## Syntax


```C++
typedef enum tagINETLANGMASK { 
  ILM_FAMILY        = 0x00000001,
  ILM_NAME          = 0x00000002,
  ILM_BODYCSET      = 0x00000004,
  ILM_HEADERCSET    = 0x00000008,
  ILM_WEBCSET       = 0x00000010,
  ILM_FIXEDFONT     = 0x00000020,
  ILM_VARIABLEFONT  = 0x00000040
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="ILM_FAMILY"></span><span id="ilm_family"></span>**ILM\_FAMILY**
</dt> <dd>

Indicates that **dwFamily** is valid.

</dd> <dt>

<span id="ILM_NAME"></span><span id="ilm_name"></span>**ILM\_NAME**
</dt> <dd>

Indicates that **szName** is valid.

</dd> <dt>

<span id="ILM_BODYCSET"></span><span id="ilm_bodycset"></span>**ILM\_BODYCSET**
</dt> <dd>

Indicates that **szBodyCset** is valid.

</dd> <dt>

<span id="ILM_HEADERCSET"></span><span id="ilm_headercset"></span>**ILM\_HEADERCSET**
</dt> <dd>

Indicates that **szHeadCset** is valid.

</dd> <dt>

<span id="ILM_WEBCSET"></span><span id="ilm_webcset"></span>**ILM\_WEBCSET**
</dt> <dd>

Indicates that **szWebCset** is valid.

</dd> <dt>

<span id="ILM_FIXEDFONT"></span><span id="ilm_fixedfont"></span>**ILM\_FIXEDFONT**
</dt> <dd>

Indicates that **szFixedFont** is valid.

</dd> <dt>

<span id="ILM_VARIABLEFONT"></span><span id="ilm_variablefont"></span>**ILM\_VARIABLEFONT**
</dt> <dd>

Indicates that **szVariableFont** is valid.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





