---
Description: The Current method provides the current URI and part.
ms.assetid: ccc8125a-c571-4267-860a-11fc313e395c
title: IXpsPartIterator::Current method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IXpsPartIterator::Current method

The `Current` method provides the current URI and part.

## Syntax


```C++
HRESULT Current(
  [out] BSTR     *pUri,
  [out] IUnknown **ppXpsPart
);
```



## Parameters

<dl> <dt>

*pUri* \[out\]
</dt> <dd>

A pointer to the URI of the part. If **NULL**, the *ppXpsPartparameter* might still be valid.

</dd> <dt>

*ppXpsPart* \[out\]
</dt> <dd>

The current part in the iterator. If **NULL**, the *pUri* parameter might still be valid.

</dd> </dl>

## Return value

`Current` returns an **HRESULT** value.

## Remarks

Filters should call the [**IXpsPartIterator::IsDone**](ixpspartiterator-isdone.md) method before calling `Current`. One or both parameters can be **NULL**.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IXpsPartIterator::Current%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




