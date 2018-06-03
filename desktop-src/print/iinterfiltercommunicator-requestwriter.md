---
Description: The RequestWriter method retrieves the writer interface for an IInterFilterCommunicator object.
ms.assetid: 1f0684f0-e15e-491f-ba09-314f831d7ba9
title: IInterFilterCommunicator::RequestWriter method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IInterFilterCommunicator::RequestWriter method

The **RequestWriter** method retrieves the writer interface for an **IInterFilterCommunicator** object.

## Syntax


```C++
HRESULT RequestWriter(
  [out] void **ppIWriter
);
```



## Parameters

<dl> <dt>

*ppIWriter* \[out\]
</dt> <dd>

A variable that receives the writer interface object that **RequestWriter** retrieves.

</dd> </dl>

## Return value

**RequestWriter** returns an **HRESULT** value.

## Remarks

The **IInterFilterCommunicator** object is passed to each filter in the [**IPrintPipelineFilter::InitializeFilter**](iprintpipelinefilter-initializefilter.md) method. The filter uses the **RequestWriter** method to get the writer interface for the object. The universally unique identifier (UUID) for the object is declared in the [filter pipeline configuration file](https://www.bing.com/search?q=filter pipeline configuration file).

## Requirements



|                            |                                                                                                                        |
|----------------------------|------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                     |
| Header<br/>          | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl>                          |



## See also

<dl> <dt>

[**IInterFilterCommunicator**](iinterfiltercommunicator.md)
</dt> <dt>

[**IPrintPipelineFilter::InitializeFilter**](iprintpipelinefilter-initializefilter.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IInterFilterCommunicator::RequestWriter%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





