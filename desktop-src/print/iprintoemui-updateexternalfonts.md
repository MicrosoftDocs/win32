---
Description: The IPrintOemUI::UpdateExternalFonts method allows a user interface plug-in to update a printer's Unidrv Font Format Files (.uff file).
ms.assetid: 5c501305-fa5f-4466-9a9a-83f072d904b3
title: IPrintOemUI::UpdateExternalFonts method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUI::UpdateExternalFonts method

The `IPrintOemUI::UpdateExternalFonts` method allows a user interface plug-in to update a printer's [Unidrv Font Format Files](https://www.bing.com/search?q=Unidrv+Font+Format+Files) (.uff file).

## Syntax


```C++
HRESULT UpdateExternalFonts(
   HANDLE hPrinter,
   HANDLE hHeap,
   PWSTR  pwstrCartridges
);
```



## Parameters

<dl> <dt>

*hPrinter* 
</dt> <dd>

Caller-supplied printer handle.

</dd> <dt>

*hHeap* 
</dt> <dd>

Caller-supplied handle to heap memory the method can use for local storage.

</dd> <dt>

*pwstrCartridges* 
</dt> <dd>

Caller-supplied pointer to an array of strings representing the names of all cartridges currently installed on the printer.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

A user interface plug-in must implement the `IPrintOemUI::UpdateExternalFonts` method if the plug-in is replacing Unidrv's default font installer. For more information, see [Customized Font Installers for Unidrv](https://www.bing.com/search?q=Customized+Font+Installers+for+Unidrv).

The `IPrintOemUI::UpdateExternalFonts` method's purpose is to examine the list of installed cartridges (supplied by *pwstrCartridges*) and ensure that the .uff file specified by the "ExternalFontFile" registry value contains font descriptions for only the cartridge fonts contained in the installed cartridges. (This .uff file can also contain descriptions of [*PCL*](https://msdn.microsoft.com/139a10e9-203b-499b-9291-8537eae9189c)-downloadable soft fonts.)

Descriptions of cartridge fonts can be copied from the .uff file specified by the "ExtFontCartFile" registry value. For more information, see [Unidrv Font Format Files](https://www.bing.com/search?q=Unidrv+Font+Format+Files).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUI**](iprintoemui-interface.md)
</dt> <dt>

[**IPrintOemUI::FontInstallerDlgProc**](iprintoemui-fontinstallerdlgproc.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI::UpdateExternalFonts%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





