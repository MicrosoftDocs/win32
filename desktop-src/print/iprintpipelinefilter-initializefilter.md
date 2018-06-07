---
Description: The InitializeFilter method initializes a filter.
ms.assetid: a28a8ee0-24df-45b5-8850-f3b3984b3b64
title: IPrintPipelineFilter::InitializeFilter method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintPipelineFilter::InitializeFilter method

The `InitializeFilter` method initializes a filter.

## Syntax


```C++
HRESULT InitializeFilter(
  [in] IInterFilterCommunicator     *pICommunicator,
  [in] IPrintPipelinePropertyBag    *pIPropertyBag,
  [in] IPrintPipelineManagerControl *pIPipelineControl
);
```



## Parameters

<dl> <dt>

*pICommunicator* \[in\]
</dt> <dd>

A pointer to the [IInterFilterCommunicator](iinterfiltercommunicator.md) interface.

</dd> <dt>

*pIPropertyBag* \[in\]
</dt> <dd>

A pointer to the[IPrintPipelinePropertyBag](iprintpipelinepropertybag.md) interface.

</dd> <dt>

*pIPipelineControl* \[in\]
</dt> <dd>

A pointer to the [IPrintPipelineManagerControl](iprintpipelinemanagercontrol.md) interface.

</dd> </dl>

## Return value

`InitializeFilter` returns an **HRESULT** value. The method should return a value other than "S\_OK" or "S\_FALSE" if the necessary operations are not performed inside `InitializeFilter`.

## Remarks

When the `InitializeFilter` method is called, the filters should:

-   Get, add, or delete properties from the property bag.

-   Get the read and write interfaces.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



## See also

<dl> <dt>

[**IPrintPipelineFilter**](iprintpipelinefilter.md)
</dt> <dt>

[IInterFilterCommunicator](iinterfiltercommunicator.md)
</dt> <dt>

[IPrintPipelineManagerControl](iprintpipelinemanagercontrol.md)
</dt> <dt>

[IPrintPipelinePropertyBag](iprintpipelinepropertybag.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintPipelineFilter::InitializeFilter%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





