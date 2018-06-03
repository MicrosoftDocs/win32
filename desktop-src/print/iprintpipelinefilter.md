---
Description: The methods in the IPrintPipelineFilter interface are called for initialization and shutdown. A filter must implement these methods.
ms.assetid: e8841091-1d62-4770-aa85-993b49efbd48
title: IPrintPipelineFilter interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintPipelineFilter interface

The methods in the `IPrintPipelineFilter` interface are called for initialization and shutdown. A filter must implement these methods.

## Members

The **IPrintPipelineFilter** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintPipelineFilter** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPrintPipelineFilter** interface has these methods.



| Method                                                                                    | Description                                                                                                                                |
|:------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPrintPipelineFilter::InitializeFilter**](iprintpipelinefilter-initializefilter.md)   | The `InitializeFilter` method initializes a filter.<br/>                                                                             |
| [**IPrintPipelineFilter::ShutdownOperation**](iprintpipelinefilter-shutdownoperation.md) | The Pipeline Manager uses the `ShutdownOperation` method to shut down a filter if the print job is canceled or an error occurs.<br/> |
| [**IPrintPipelineFilter::StartOperation**](iprintpipelinefilter-startoperation.md)       | The `StartOperation` method starts the operation of a filter. The filter reads, processes, and writes data in this method.<br/>      |



 

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintPipelineFilter%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




