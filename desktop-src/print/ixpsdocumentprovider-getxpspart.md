---
Description: The GetXpsPart method retrieves several objects that make up an XPS document.
ms.assetid: 7e36cf90-a84a-447c-bec3-2b5175fffd7c
title: IXpsDocumentProvider::GetXpsPart method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IXpsDocumentProvider::GetXpsPart method

The `GetXpsPart` method retrieves several objects that make up an XPS document.

## Syntax


```C++
HRESULT GetXpsPart(
  [out] IUnknown **ppIXpsPart
);
```



## Parameters

<dl> <dt>

*ppIXpsPart* \[out\]
</dt> <dd>

The XPS part. This part is the **IUnknown** interface of an object that is an XPS part. If *ppIXpsPart* is NULL, there are no more XPS parts to consume and the filter is ready to finish processing.

</dd> </dl>

## Return value

`GetXpsPart` returns an **HRESULT**.

## Remarks

Use **QueryInterface** on the value that the **GetXpsPart** method returns to determine the type of object that it retrieved.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsDocumentProvider::GetXpsPart%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




