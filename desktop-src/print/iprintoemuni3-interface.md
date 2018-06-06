---
Description: This section describes the methods defined for the IPrintOemUni3 COM interface.
ms.assetid: cf5705fb-8420-4eec-99d4-d56f192da581
title: IPrintOemUni3 interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintOemUni3 interface

This section describes the methods defined for the **IPrintOemUni3** COM interface.

The **IPrintOemUni3** COM interface includes its own methods as well as those that belong to [**IPrintOemUni**](iprintoemuni-interface.md) COM interface and the [**IPrintOemUni2**](iprintoemuni2-interface.md) COM interface.

The **IPrintOemUni3** COM interface is available in Windows Vista and later.

## Members

The **IPrintOemUni3** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintOemUni3** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintOemUni3** interface has these methods.



| Method                                                             | Description                                                                                                                                                              |
|:-------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DownloadPattern**](iprintoemuni3-downloadpattern.md)           | The `IPrintOemUni3::DownloadPattern` method downloads a pattern to a printer.<br/>                                                                                 |
| [**GetImplementedMethod**](iprintoemuni3-getimplementedmethod.md) | The `IPrintOemUni3::GetImplementedMethod` method is used by Unidrv to determine which **IPrintOemUni** interface methods a rendering plug-in has implemented.<br/> |
| [**GetPDEVAdjustment**](iprintoemuni3-getpdevadjustment.md)       | The `IPrintOemUni3::GetPDEVAdjustment` method enables a plug-in to override specific [*PDEV*](https://msdn.microsoft.com/139a10e9-203b-499b-9291-8537eae9189c) settings.<br/>               |
| [**SetBandSize**](iprintoemuni3-setbandsize.md)                   | The `IPrintOemUni3::SetBandSize` method can be used with Unidrv-supported printers to specify the desired band size on the printed output.<br/>                    |



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni3%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




