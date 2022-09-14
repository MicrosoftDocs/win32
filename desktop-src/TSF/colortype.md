---
title: COLORTYPE enumeration (Softkbdc.h)
description: Elements of the COLORTYPE enumeration are used to specify types of colors that are available for a soft keyboard.
ms.assetid: 63a51f67-d85c-4017-a569-03df164198db
keywords:
- COLORTYPE enumeration Text Services Framework
topic_type:
- apiref
api_name:
- COLORTYPE
api_location:
- Softkbdc.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# COLORTYPE enumeration

Elements of the **COLORTYPE** enumeration are used to specify types of colors that are available for a soft keyboard.

## Syntax


```C++
typedef enum tagCOLORTYPE { 
  bkcolor         = 0,
  UnSelForeColor  = 1,
  UnSelTextColor  = 2,
  SelForeColor    = 3,
  SelTextColor    = 4,
  Max_color_Type  = 5
} COLORTYPE;
```



## Constants

<dl> <dt>

<span id="bkcolor"></span><span id="BKCOLOR"></span>**bkcolor**
</dt> <dd>

Background color.

</dd> <dt>

<span id="UnSelForeColor"></span><span id="unselforecolor"></span><span id="UNSELFORECOLOR"></span>**UnSelForeColor**
</dt> <dd>

Unselected foreground color.

</dd> <dt>

<span id="UnSelTextColor"></span><span id="unseltextcolor"></span><span id="UNSELTEXTCOLOR"></span>**UnSelTextColor**
</dt> <dd>

Unselected text color.

</dd> <dt>

<span id="SelForeColor"></span><span id="selforecolor"></span><span id="SELFORECOLOR"></span>**SelForeColor**
</dt> <dd>

Selected foreground color.

</dd> <dt>

<span id="SelTextColor"></span><span id="seltextcolor"></span><span id="SELTEXTCOLOR"></span>**SelTextColor**
</dt> <dd>

Selected text color.

</dd> <dt>

<span id="Max_color_Type"></span><span id="max_color_type"></span><span id="MAX_COLOR_TYPE"></span>**Max\_color\_Type**
</dt> <dd>

Maximum color type.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |



 

 





