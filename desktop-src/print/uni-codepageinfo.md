---
Description: The UNI\_CODEPAGEINFO structure is one of the structures used to define the contents of glyph translation table files (.gtt files).
ms.assetid: 042362d3-d5bf-47af-957f-8f1eb7a9ca7a
title: UNI\_CODEPAGEINFO structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UNI\_CODEPAGEINFO structure

The UNI\_CODEPAGEINFO structure is one of the structures used to define the contents of [glyph translation table files](print.customized_font_management#ddk-glyph-translation-table-files-gg) (.gtt files).

## Syntax


```C++
typedef struct _UNI_CODEPAGEINFO {
  DWORD dwCodePage;
  INVOC SelectSymbolSet;
  INVOC UnSelectSymbolSet;
} UNI_CODEPAGEINFO, *PUNI_CODEPAGEINFO;
```



## Members

<dl> <dt>

**dwCodePage**
</dt> <dd>

Identifies a Windows code page.

</dd> <dt>

**SelectSymbolSet**
</dt> <dd>

Is an [**INVOC**](invoc.md) structure containing the printer command to select the code page's symbol set.

</dd> <dt>

**UnSelectSymbolSet**
</dt> <dd>

Is an [**INVOC**](invoc.md) structure containing the printer command to deselect the code page's symbol set.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**INVOC**](invoc.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20UNI_CODEPAGEINFO%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





