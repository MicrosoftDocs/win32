---
Description: The IPrintCoreHelperUni::SetFontSubstitution method specifies the device font to print in place of a given TrueType font.
ms.assetid: 73afb4e9-23c7-473c-937f-045bf5e332f7
title: IPrintCoreHelperUni::SetFontSubstitution method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintCoreHelperUni::SetFontSubstitution method

The `IPrintCoreHelperUni::SetFontSubstitution` method specifies the device font to print in place of a given TrueType font.

## Syntax


```C++
STDMETHOD SetFontSubstitution(
  [in] PCWSTR pszTrueTypeFontName,
  [in] PCWSTR pszDevFontName
);
```



## Parameters

<dl> <dt>

*pszTrueTypeFontName* \[in\]
</dt> <dd>

A pointer to a null-terminated Unicode string that contains a valid TrueType font name. This parameter must not be **NULL**.

</dd> <dt>

*pszDevFontName* \[in\]
</dt> <dd>

A pointer to a null-terminated Unicode string that contains the name of the device font.

</dd> </dl>

## Return value

`IPrintCoreHelperUni::SetFontSubstitution` should return one of the following values.



| Return code                                                                                                                         | Description                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                                | The method read the option for the specified feature.<br/>                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                                              | The font that was requested does not exist or was not a TrueType font.<br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                                        | One or more of the arguments is invalid.<br/>                                                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                                       | The core driver was not able to service the request because there was insufficient memory.<br/> |
| <dl> <dt>**E\_UNEXPECTED, or other return codes not listed here**</dt> </dl> | The core driver seems to be in an invalid state. The caller should return a failure code.<br/>  |



 

## Remarks

Setting a device font to use in place of a specified TrueType font can occur only during the device property sheets session and only if full UI replacement is enabled. The font that is represented by the *pszTrueTypeFontName* parameter must be a valid TrueType font and must be installed on the printer. The device font that is represented by the *pszDevFontName* parameter must be a valid font for this printer.

If a substitution mapping for the specified TrueType font already exists on this queue, the `SetFontSubstitution` method will silently replace the mapping. To remove a substitution mapping, call this method with the TrueType font name specified in *pszTrueTypeFontName* and with **NULL** specified in *pszDevFontName*.

To obtain a list of valid device fonts, create an information context for the current printer, and call **SetGraphicsMode**(hIC, GM\_ADVANCED). Then, enumerate device fonts by calling **EnumFontFamilies**. The callback parameter (see **EnumFontFamProc** in the Microsoft Windows SDK documentation) of **EnumFontFamilies** should filter for device fonts by incrementing a counter for each font for which the bitwise AND result (FontType & TRUETYPE\_FONTTYPE) is nonzero. The **SetGraphicsMode**, **EnumFontFamilies**, and **EnumFontFamProc** functions are described in the Windows SDK documentation.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreHelperUni**](iprintcorehelperuni-interface.md)
</dt> <dt>

[**IPrintCoreHelperUni::GetFontSubstitution**](iprintcorehelperuni-getfontsubstitution.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperUni::SetFontSubstitution%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





