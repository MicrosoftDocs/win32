---
Description: The ReportProgress method reports the progress of the XPS job consumption to the pipeline manager.
ms.assetid: 989e8888-3494-4355-a41f-2ed774a060d2
title: IPrintPipelineProgressReport::ReportProgress method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintPipelineProgressReport::ReportProgress method

The `ReportProgress` method reports the progress of the XPS job consumption to the pipeline manager.

## Syntax


```C++
HRESULT ReportProgress(
  [in] EXpsJobConsumption update
);
```



## Parameters

<dl> <dt>

*update* \[in\]
</dt> <dd>

An [**EXpsJobConsumption**](expsjobconsumption.md)-typed value that describes the progress to the pipeline manager.

</dd> </dl>

## Return value

`ReportProgress` returns an **HRESULT** value.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



## See also

<dl> <dt>

[**IPrintPipelineProgressReport**](iprintpipelineprogressreport.md)
</dt> <dt>

[**EXpsJobConsumption**](expsjobconsumption.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintPipelineProgressReport::ReportProgress%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





