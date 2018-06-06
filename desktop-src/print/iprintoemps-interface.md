---
Description: This section describes the methods defined for the IPrintOemPS COM interface.
ms.assetid: 14c545b7-8080-424f-9164-f97ef8a1acc2
title: IPrintOemPS interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintOemPS interface

This section describes the methods defined for the **IPrintOemPS** COM interface.

## Members

The **IPrintOemPS** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintOemPS** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintOemPS** interface has these methods.



| Method                                                                            | Description                                                                                                                                                                                                                                                              |
|:----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPrintOemPS::Command**](iprintoemps-command.md)                               | The `IPrintOemPS::Command` method is used by rendering plug-ins for the Microsoft PostScript printer driver, in order to insert PostScript commands into the print job's data stream.<br/>                                                                         |
| [**IPrintOemPS::DevMode**](iprintoemps-devmode.md)                               | The `IPrintOemPS::DevMode` method, provided by rendering plug-ins for Pscript5, performs operations on private [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) members.<br/>                                                                                                      |
| [**IPrintOemPS::DisableDriver**](iprintoemps-disabledriver.md)                   | The `IPrintOemPS::DisableDriver` method allows a rendering plug-in for [*Pscript*](wdkgloss.p#wdkgloss-pscript) to free resources that were allocated by the plug-in's [**IPrintOemPS::EnableDriver**](iprintoemps-enabledriver.md) method.<br/> |
| [**IPrintOemPS::DisablePDEV**](iprintoemps-disablepdev.md)                       | The `IPrintOemPS::DisablePDEV` method allows a rendering plug-in for Pscript5 to delete the private PDEV structure that was allocated by its [**IPrintOemPS::EnablePDEV**](iprintoemps-enablepdev.md) method.<br/>                                                |
| [**IPrintOemPS::EnableDriver**](iprintoemps-enabledriver.md)                     | The `IPrintOemPS::EnableDriver` method allows a rendering plug-in for [*Pscript*](wdkgloss.p#wdkgloss-pscript) to hook out some graphics DDI functions.<br/>                                                                                      |
| [**IPrintOemPS::EnablePDEV**](iprintoemps-enablepdev.md)                         | The `IPrintOemPS::EnablePDEV` method allows a rendering plug-in for Pscript5 to create its own PDEV structure.<br/>                                                                                                                                                |
| [**IPrintOemPS::GetInfo**](iprintoemps-getinfo.md)                               | A rendering plug-in's `IPrintOemPS::GetInfo` method returns identification information.<br/>                                                                                                                                                                       |
| [**IPrintOemPS::PublishDriverInterface**](iprintoemps-publishdriverinterface.md) | The `IPrintOemPS::PublishDriverInterface` method allows a rendering plug-in for Pscript5 to obtain the Pscript5 driver's **IPrintCorePS2**, **IPrintOemDriverPS**, or **IPrintCoreHelperPS** interface.<br/>                                                       |
| [**IPrintOemPS::ResetPDEV**](iprintoemps-resetpdev.md)                           | The `IPrintOemPS::ResetPDEV` method allows a rendering plug-in for Pscript5 to reset its PDEV structure.<br/>                                                                                                                                                      |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPS%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




