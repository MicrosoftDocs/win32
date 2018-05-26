---
Description: The INVOC structure is used for describing printer command strings in Unidrv font metrics files (.ufm files) and glyph translation table files (.gtt files).
ms.assetid: 5eeaa7f7-dc99-4cf7-846c-801954cc9040
title: INVOC structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INVOC structure

The INVOC structure is used for describing printer command strings in [Unidrv font metrics files](print.customized_font_management#ddk-unidrv-font-metrics-files-gg) (.ufm files) and [glyph translation table files](print.customized_font_management#ddk-glyph-translation-table-files-gg) (.gtt files).

## Syntax


```C++
typedef struct _INVOC {
  DWORD dwCount;
  DWORD loOffset;
} INVOC, *PINVOC;
```



## Members

<dl> <dt>

**dwCount**
</dt> <dd>

Specifies the number of characters in the command.

</dd> <dt>

**loOffset**
</dt> <dd>

Indicates one of the following:

<dl> <dt>

<span id="For_.ufm_files_"></span><span id="for_.ufm_files_"></span><span id="FOR_.UFM_FILES_"></span>For .ufm files:
</dt> <dd>

Specifies the byte offset from the beginning of the .ufm file's [**UNIDRVINFO**](unidrvinfo.md) structure to beginning of the command string.

</dd> <dt>

<span id="For_.gtt_files_"></span><span id="for_.gtt_files_"></span><span id="FOR_.GTT_FILES_"></span>For .gtt files:
</dt> <dd>

Specifies the byte offset from the beginning of the .gtt file's [**UNI\_CODEPAGEINFO**](uni-codepageinfo.md) structure to beginning of the command string.

</dd> </dl> </dd> </dl>

## Remarks

INVOC structures are used within [**UNIDRVINFO**](unidrvinfo.md) structures.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prntfont.h (include Prntfont.h)</dt> </dl> |



## See also

<dl> <dt>

[**UNIDRVINFO**](unidrvinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20INVOC%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





