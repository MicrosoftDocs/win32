---
Description: The StartOperation method starts the operation of a filter. The filter reads, processes, and writes data in this method.
ms.assetid: 87139670-9b51-4ced-9624-2ec9f4726a84
title: IPrintPipelineFilterStartOperation method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintPipelineFilter::StartOperation method

The `StartOperation` method starts the operation of a filter. The filter reads, processes, and writes data in this method.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE StartOperation(
    None
);
```



## Parameters

<dl> <dt>

*None* 
</dt> <dd></dd> </dl>

## Return value

`StartOperation` returns an **HRESULT** value.

## Remarks

A filter returns the `StartOperation` call only when the filter processing is complete.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintPipelineFilter::StartOperation%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




