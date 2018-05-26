---
Description: The Continue method tells the caller (the XPS rasterization service) whether to continue rasterizing the current XPS fixed page.
ms.assetid: 8136eec2-1d4b-4233-bb93-7203d932816b
title: IXpsRasterizerNotificationCallbackContinue method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IXpsRasterizerNotificationCallback::Continue method

The `Continue` method tells the caller (the XPS rasterization service) whether to continue rasterizing the current XPS fixed page.

## Syntax


```C++
HRESULT Continue();
```



## Parameters

This method has no parameters.

## Return value

`Continue` returns S\_OK to enable rasterization to continue. Otherwise, the method returns an error code to abort rasterization. Possible error return values include:



| Return code                                                                                                                  | Description                                         |
|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_PRINT\_CANCELLED)**</dt> </dl> | The current print job has been canceled.<br/> |



 

## Remarks

This method is implemented by an XPSDrv filter. During a page rasterization operation, the [XPS rasterization service](print.using_the_xps_rasterization_service) periodically calls this method to determine whether to continue the operation.

To begin a page rasterization operation, the XPSDrv filter calls the [**IXpsRasterizer::RasterizeRect**](ixpsrasterizer-rasterizerect.md) method. With this call, the filter can, as an option, supply a pointer to an [IXpsRasterizerNotificationCallback](ixpsrasterizernotificationcallback-interface.md) interface instance. If supplied, **RasterizeRect** will periodically call the `Continue` method on this interface during the processing of the **RasterizeRect** call. If `Continue` returns a success code, **RasterizeRect** continues with the rasterization operation in progress. If `Continue` returns an error code, **RasterizeRect** aborts the rasterization operation and returns immediately.

If the user cancels a print job or if an error occurs during the processing of a print job, the pipeline manager calls the XPSDrv filter's [**IPrintPipelineFilter::ShutdownOperation**](iprintpipelinefilter-shutdownoperation.md) method to shut down the filter. Typically, the filter can complete the shutdown in a more timely way if it implements the `Continue` method and supplies an **IXpsRasterizerNotificationCallback** pointer to **RasterizeRect**.

For an example implementation of the `Continue` method, see the XpsRasFilter sample in the WDK. This sample is located in the Src\\Print\\Xpsrasfilter folder in your WDK installation.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>     |
| Version<br/>         | Supported in Windows 7 and later versions of the Windows operating system.<br/>  |
| Header<br/>          | <dl> <dt>Xpsrassvc.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintPipelineFilter::ShutdownOperation**](iprintpipelinefilter-shutdownoperation.md)
</dt> <dt>

[**IXpsRasterizer::RasterizeRect**](ixpsrasterizer-rasterizerect.md)
</dt> <dt>

[IXpsRasterizerNotificationCallback](ixpsrasterizernotificationcallback-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsRasterizerNotificationCallback::Continue%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





