---
Description: This section describes the methods defined for the IPrintOemUni COM interface.
ms.assetid: 097366a0-2ded-435c-9b63-2b736b716032
title: IPrintOemUni interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintOemUni interface

This section describes the methods defined for the IPrintOemUni COM interface.

## Members

The **IPrintOemUni** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintOemUni** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintOemUni** interface has these methods.



| Method                                                                | Description                                                                                                                                                                                                                                                                     |
|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CommandCallback**](iprintoemuni-commandcallback.md)               | The `IPrintOemUni::CommandCallback` method is used to provide dynamically generated printer commands for Unidrv-supported printers.<br/>                                                                                                                                  |
| [**Compression**](iprintoemuni-compression.md)                       | The `IPrintOemUni::Compression` method can be used with Unidrv-supported printers to provide a customized bitmap compression method.<br/>                                                                                                                                 |
| [**DevMode**](iprintoemuni-devmode.md)                               | The `IPrintOemUni::DevMode` method, provided by rendering plug-ins for Unidrv, performs operations on private [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) members.<br/>                                                                                                              |
| [**DisableDriver**](iprintoemuni-disabledriver.md)                   | The `IPrintOemuNI::DisableDriver` method allows a rendering plug-in for [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) to free resources that were allocated by the plug-in's [**IPrintOemUni::EnableDriver**](iprintoemuni-enabledriver.md) method.<br/>        |
| [**DisablePDEV**](iprintoemuni-disablepdev.md)                       | The `IPrintOemUni::DisablePDEV` method allows a rendering plug-in for [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) to delete the private PDEV structure that was allocated by its [**IPrintOemUni::EnablePDEV**](iprintoemuni-enablepdev.md) method.<br/>      |
| [**DownloadCharGlyph**](iprintoemuni-downloadcharglyph.md)           | The `IPrintOemUni::DownloadCharGlyph` method enables a rendering plug-in for Unidrv to send a character glyph for a specified soft font to the printer.<br/>                                                                                                              |
| [**DownloadFontHeader**](iprintoemuni-downloadfontheader.md)         | The `IPrintOemUni::DownloadFontHeader` method allows a rendering plug-in for [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) to send a font's header information to a printer.<br/>                                                                                |
| [**DriverDMS**](iprintoemuni-driverdms.md)                           | The `IPrintOemUni::DriverDMS` method allows a rendering plug-in for [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) to indicate that it uses a device-managed drawing surface.<br/>                                                                                |
| [**EnableDriver**](iprintoemuni-enabledriver.md)                     | The `IPrintOemUni::EnableDriver` method allows a rendering plug-in for [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) to hook out some graphics DDI functions.<br/>                                                                                               |
| [**EnablePDEV**](iprintoemuni-enablepdev.md)                         | The `IPrintOemUni::EnablePDEV` method allows a rendering plug-in for [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) to create its own PDEV structure.<br/>                                                                                                        |
| [**FilterGraphics**](iprintoemuni-filtergraphics.md)                 | The `IPrintOemUni::FilterGraphics` method can be used with Unidrv-supported printers to modify scan line data and send it to the spooler.<br/>                                                                                                                            |
| [**GetImplementedMethod**](iprintoemuni-getimplementedmethod.md)     | The `IPrintOemUni::GetImplementedMethod` method is used by Unidrv to determine which **IPrintOemUni** interface methods a rendering plug-in has implemented.<br/>                                                                                                         |
| [**GetInfo**](iprintoemuni-getinfo.md)                               | A rendering plug-in's `IPrintOemUni::GetInfo` method returns identification information.<br/>                                                                                                                                                                             |
| [**HalftonePattern**](iprintoemuni-halftonepattern.md)               | The `IPrintOemUni::HalftonePattern` method can be used with Unidrv-supported printers to create or modify a halftone pattern before it is used in a halftoning operation.<br/>                                                                                            |
| [**ImageProcessing**](iprintoemuni-imageprocessing.md)               | The `IPrintOemUni::ImageProcessing` method can be used with Unidrv-supported printers to modify image bitmap data, in order to perform color formatting or halftoning. The method can return the modified bitmap to Unidrv or send it directly to the print spooler.<br/> |
| [**MemoryUsage**](iprintoemuni-memoryusage.md)                       | The `IPrintOemUni::MemoryUsage` method can be used with Unidrv-supported printers to specify the amount of memory required for use by a rendering plug-in's [**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md) method.<br/>                            |
| [**OutputCharStr**](iprintoemuni-outputcharstr.md)                   | The `IPrintOemUni::OutputCharStr` method enables a rendering plug-in to control the printing of font glyphs.<br/>                                                                                                                                                         |
| [**PublishDriverInterface**](iprintoemuni-publishdriverinterface.md) | The `IPrintOemUni::PublishDriverInterface` method allows a rendering plug-in for Unidrv to obtain the Unidrv driver's **IPrintOemDriverUni** or **IPrintCoreHelperUni** interface.<br/>                                                                                   |
| [**ResetPDEV**](iprintoemuni-resetpdev.md)                           | The `IPrintOemUni::ResetPDEV` method allows a rendering plug-in for Unidrv to reset its PDEV structure.<br/>                                                                                                                                                              |
| [**SendFontCmd**](iprintoemuni-sendfontcmd.md)                       | The `IPrintOemUni::SendFontCmd` method enables a rendering plug-in to modify a printer's font selection command and then send it to the printer.<br/>                                                                                                                     |
| [**TextOutAsBitmap**](iprintoemuni-textoutasbitmap.md)               | The `IPrintOemUni::TextOutAsBitmap` method allows a rendering plug-in to create a bitmap image of a text string, in case a downloadable font is not available.<br/>                                                                                                       |
| [**TTDownloadMethod**](iprintoemuni-ttdownloadmethod.md)             | The `IPrintOemUni::TTDownloadMethod` method enables a rendering plug-in to indicate the format that Unidrv should use for a specified TrueType soft font.<br/>                                                                                                            |
| [**TTYGetInfo**](iprintoemuni-ttygetinfo.md)                         | The `IPrintOemUni::TTYGetInfo` method enables a rendering plug-in to supply Unidrv with information relevant to text-only printers.<br/>                                                                                                                                  |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




