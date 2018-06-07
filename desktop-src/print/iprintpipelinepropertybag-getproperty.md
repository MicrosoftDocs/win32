---
Description: The GetProperty method gets a property from a property bag.
ms.assetid: 10a5ada8-98ab-4e1c-a4b5-2f6d60674952
title: IPrintPipelinePropertyBag::GetProperty method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintPipelinePropertyBag::GetProperty method

The `GetProperty` method gets a property from a property bag.

## Syntax


```C++
HRESULT GetProperty(
  [in]  const wchar_t *pszName,
  [out]       VARIANT *pVar
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

The name of the property that you want to get from the property bag.

</dd> <dt>

*pVar* \[out\]
</dt> <dd>

The **VARIANT** value to get from the property bag.

</dd> </dl>

## Return value

`GetProperty` returns an **HRESULT** value.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintPipelinePropertyBag::GetProperty%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




