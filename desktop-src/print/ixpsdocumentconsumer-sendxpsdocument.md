---
Description: The SendXpsDocument method sends an XPS document to the pipeline.
ms.assetid: ad9f0f6b-19a6-4c99-9350-7ca249cf4774
title: IXpsDocumentConsumer::SendXpsDocument method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IXpsDocumentConsumer::SendXpsDocument method

The `SendXpsDocument` method sends an XPS document to the pipeline.

## Syntax


```C++
HRESULT SendXpsDocument(
  [in] IXpsDocument *pIXpsDocument
);
```



## Parameters

<dl> <dt>

*pIXpsDocument* \[in\]
</dt> <dd>

A pointer to the XPS document object to send.

</dd> </dl>

## Return value

`SendXpsDocument` returns an **HRESULT** value.

## Remarks

The [IXpsDocument](ixpsdocument.md) interface is the root for a tree view of an XPS document. The tree also contains one fixed document sequence and any number of fixed documents and fixed pages.

Only one XpsDocument interface can be sent. The `SendXpsDocument` method will fail if a filter submits more than one XpsDocument interface for the same print job.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



## See also

<dl> <dt>

[**IXpsDocumentConsumer**](ixpsdocumentconsumer.md)
</dt> <dt>

[IXpsDocument](ixpsdocument.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsDocumentConsumer::SendXpsDocument%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





