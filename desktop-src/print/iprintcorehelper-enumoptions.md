---
Description: The IPrintCoreHelperEnumOptions method gets a list of available options for the given feature.
ms.assetid: 2e46e8cd-b5e5-4116-b42c-b7adcee9d520
title: IPrintCoreHelperEnumOptions method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintCoreHelper::EnumOptions method

The **IPrintCoreHelper::EnumOptions** method gets a list of available options for the given feature.

## Syntax


```C++
STDMETHOD EnumOptions(
  [in]  PCSTR pszFeatureKeyword,
  [out] PCSTR *pOptionList[],
  [out] DWORD *pdwNumOptions
);
```



## Parameters

<dl> <dt>

*pszFeatureKeyword* \[in\]
</dt> <dd>

An ANSI character string that contains the feature whose options are requested.

</dd> <dt>

*pOptionList\[\]* \[out\]
</dt> <dd>

A pointer to an array of ANSI character strings that contain all of the options for the feature that is specified in the *pszFeatureKeyword* parameter. **IPrintCoreHelper::EnumOptions** is responsible for allocating the memory for the array. The last element of the array must be a **NULL** string.

</dd> <dt>

*pdwNumOptions* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of options in the option array that is pointed to by the *pOptionList* parameter.

</dd> </dl>

## Return value

**IPrintCoreHelper::EnumOptions** should return S\_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.

## Remarks

When **IPrintCoreHelper::EnumOptions** returns, the option list contains all options, regardless of constraints or other factors.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreHelper**](iprintcorehelper-interface.md)
</dt> <dt>

[**IPrintCoreHelper::EnumFeatures**](iprintcorehelper-enumfeatures.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelper::EnumOptions%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





