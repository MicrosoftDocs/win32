---
Description: This section describes the methods defined for the IPrintOemUI COM interface.
ms.assetid: 0ef635dd-9598-4356-94fc-7e5237df9bd9
title: IPrintOemUI interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemUI interface

This section describes the methods defined for the **IPrintOemUI** COM interface.

## Members

The **IPrintOemUI** interface inherits from the [**IUnknown**](com.iunknown) interface. **IPrintOemUI** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintOemUI** interface has these methods.



| Method                                                               | Description                                                                                                                                                                                                                                              |
|:---------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommonUIProp**](iprintoemui-commonuiprop.md)                     | The `IPrintOemUI::CommonUIProp` method allows a user interface plug-in to modify an existing printer property sheet page.<br/>                                                                                                                     |
| [**DeviceCapabilities**](iprintoemui-devicecapabilities.md)         | The `IPrintOemUI::DeviceCapabilities` method enables a user interface plug-in to specify customized device capabilities.<br/>                                                                                                                      |
| [**DevicePropertySheets**](iprintoemui-devicepropertysheets.md)     | The `IPrintOemUI::DevicePropertySheets` method allows a user interface plug-in to append a new page to a printer device's printer property sheet.<br/>                                                                                             |
| [**DevMode**](iprintoemui-devmode.md)                               | The `IPrintOemUI::DevMode` method, provided by user interface plug-ins, performs operations on the plug-in's private DEVMODEW members.<br/>                                                                                                        |
| [**DocumentPropertySheets**](iprintoemui-documentpropertysheets.md) | The `IPrintOemUI::DocumentPropertySheets` method allows a user interface plug-in to append a new page to a printer device's document property sheet.<br/>                                                                                          |
| [**DriverEvent**](iprintoemui-driverevent.md)                       | The printer driver's [**DrvDriverEvent**](drvdriverevent.md) function calls a user interface plug-in's `IPrintOemUI::DriverEvent` method for additional processing of printer driver events.<br/>                                                 |
| [**FontInstallerDlgProc**](iprintoemui-fontinstallerdlgproc.md)     | A user interface plug-in's `IPrintOemUI::FontInstallerDlgProc` method replaces the Unidrv font installer's user interface.<br/>                                                                                                                    |
| [**GetInfo**](iprintoemui-getinfo.md)                               | A user interface plug-in's `IPrintOemUI::GetInfo` method returns identification information.<br/>                                                                                                                                                  |
| [**PrinterEvent**](iprintoemui-printerevent.md)                     | The `IPrintOemUI::PrinterEvent` method allows a user interface plug-in to process printer events.<br/>                                                                                                                                             |
| [**PublishDriverInterface**](iprintoemui-publishdriverinterface.md) | The `IPrintOemUI::PublishDriverInterface` method allows a user interface plug-in to obtain the Unidrv or Pscript5 driver's **IPrintOemDriverUI**, **IPrintCoreUI2**, **IPrintCoreHelperPS**, or **IPrintCoreHelperUni** interface.<br/>            |
| [**QueryColorProfile**](iprintoemui-querycolorprofile.md)           | The `IPrintOemUI::QueryColorProfile` method allows a user interface plug-in to specify an ICC profile to use for color management.<br/>                                                                                                            |
| [**UpdateExternalFonts**](iprintoemui-updateexternalfonts.md)       | The `IPrintOemUI::UpdateExternalFonts` method allows a user interface plug-in to update a printer's [Unidrv Font Format Files](print.customized_font_management#ddk-unidrv-font-format-files-gg) (.uff file).<br/> |
| [**UpgradePrinter**](iprintoemui-upgradeprinter.md)                 | The `IPrintOemUI::UpgradePrinter` method allows a user interface plug-in to upgrade device option values that are stored in the registry.<br/>                                                                                                     |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




