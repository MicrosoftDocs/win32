---
Description: A rendering filter uses the IPrintPipelineProgressReport interface to send progress status to a spooler.
ms.assetid: 7a2644af-fdfe-4481-8c44-c40244b8a00e
title: IPrintPipelineProgressReport interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintPipelineProgressReport interface

A rendering filter uses the `IPrintPipelineProgressReport` interface to send progress status to a spooler.

A rendering filter should search for the **XPS\_FP\_PROGRESS\_REPORT** property in a property bag, get the progress, and then remove it from the property bag. If there are no rendering filters, the filter pipeline sends the notifications to the spooler. It is very important for a rendering filter to remove the progress and send progress status to the spooler; if progress status is not handled correctly, the spooler may get conflicting progress reports.

## Members

The **IPrintPipelineProgressReport** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintPipelineProgressReport** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintPipelineProgressReport** interface has these methods.



| Method                                                                                              | Description                                                                                                     |
|:----------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
| [**IPrintPipelineProgressReport::ReportProgress**](iprintpipelineprogressreport-reportprogress.md) | The `ReportProgress` method reports the progress of the XPS job consumption to the pipeline manager.<br/> |



 

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintPipelineProgressReport%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




