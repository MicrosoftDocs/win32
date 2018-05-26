---
Description: The SendXpsUnknown method sends an XPS document part that cannot be identified to the filter pipeline.
ms.assetid: 5e2880c6-0f5a-4098-a97e-809ad75ddfd0
title: IXpsDocumentConsumerSendXpsUnknown method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IXpsDocumentConsumer::SendXpsUnknown method

The `SendXpsUnknown` method sends an XPS document part that cannot be identified to the filter pipeline.

## Syntax


```C++
HRESULT SendXpsUnknown(
  [in] IUnknown *pUnknown
);
```



## Parameters

<dl> <dt>

*pUnknown* \[in\]
</dt> <dd>

A pointer to an unrecognized document part interface.

</dd> </dl>

## Return value

`SendXpsUnknown` returns an HRESULT value.

## Remarks

If the [**IXpsDocumentProvider::GetXpsPart**](ixpsdocumentprovider-getxpspart.md) method returns an object that the filter cannot identify, the filter should forward the unrecognized object to the next filter in the filter pipeline by calling `SendXpsUnknown`. Passing unrecognized objects to the next filter helps the filter maintain compatibility with future document formats.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsDocumentConsumer::SendXpsUnknown%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




