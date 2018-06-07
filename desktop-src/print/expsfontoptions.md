---
Description: The EXpsFontOptions enumeration describes the font options for an XPS part.
ms.assetid: 3a92b219-91ee-4c11-b5c1-8e2e0cbff406
title: EXpsFontOptions enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# EXpsFontOptions enumeration

The EXpsFontOptions enumeration describes the font options for an XPS part.

## Syntax


```C++
typedef enum  { 
  Font_Normal,
  Font_Obfusticate
} EXpsFontOptions;
```



## Constants

<dl> <dt>

<span id="Font_Normal"></span><span id="font_normal"></span><span id="FONT_NORMAL"></span>**Font\_Normal**
</dt> <dd>

The font code is human-readable.

</dd> <dt>

<span id="Font_Obfusticate"></span><span id="font_obfusticate"></span><span id="FONT_OBFUSTICATE"></span>**Font\_Obfusticate**
</dt> <dd>

The font code is obfusticated (that is, the internal structure of the font is scrambled in such a way to prevent someone from understaning how the structure works).

</dd> </dl>

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |
| IDL<br/>    | <dl> <dt>Filterpipeline.idl</dt> </dl>                          |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20EXpsFontOptions%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




