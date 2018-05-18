---
Description: 'The RequestShutdown method requests that a pipeline be shut down.'
ms.assetid: 'dfb0d7d1-4e82-4471-814b-4b8c4929c709'
title: 'IPrintPipelineManagerControl::RequestShutdown method'
---

# IPrintPipelineManagerControl::RequestShutdown method

The `RequestShutdown` method requests that a pipeline be shut down.

## Syntax


```C++
HRESULT RequestShutdown(
  [in] HRESULT       hrReason,
  [in] IImgErrorInfo *pReason
);
```



## Parameters

<dl> <dt>

*hrReason* \[in\]
</dt> <dd>

An **HRESULT** value that indicates the reason for the lack of memory.

</dd> <dt>

*pReason* \[in\]
</dt> <dd>

Not used. Set to **NULL**.

</dd> </dl>

## Return value

`RequestShutdown` returns an **HRESULT** value.

## Remarks

A filter that uses the [IXpsDocumentConsumer](ixpsdocumentconsumer.md) interface must call `IPrintPipelineManagerControl::RequestShutdown` before it calls [**IXpsDocumentConsumer::CloseSender**](ixpsdocumentconsumer-closesender.md) to shut down the pipeline. Calling **IXpsDocumentConsumer::CloseSender** first can produce an invalid XPS document and cause an error.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintPipelineManagerControl::RequestShutdown%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




