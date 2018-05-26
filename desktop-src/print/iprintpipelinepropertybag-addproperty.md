---
Description: The AddProperty method adds a property to a property bag.
ms.assetid: ba994342-c203-443e-a9fd-60fd29721dae
title: IPrintPipelinePropertyBagAddProperty method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintPipelinePropertyBag::AddProperty method

The `AddProperty` method adds a property to a property bag.

## Syntax


```C++
HRESULT AddProperty(
  [in] const wchar_t *pszName,
  [in] const VARIANT *pVar
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

The name of the property that you want to add to the property bag. You should uniquely identify this property so that it does not collide with others. For example, use a name like *MyCompanyName-MySetting*.

</dd> <dt>

*pVar* \[in\]
</dt> <dd>

The **VARIANT** value to add to the property bag.

</dd> </dl>

## Return value

`AddProperty` returns an **HRESULT** value.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintPipelinePropertyBag::AddProperty%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




