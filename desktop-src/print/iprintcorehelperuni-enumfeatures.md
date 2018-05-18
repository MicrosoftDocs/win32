---
Description: 'The IPrintCoreHelperUni::EnumFeatures method gets a list of all available features, including synthesized and core driver-implement features.'
ms.assetid: 'ed21e52b-13a6-4a89-8bbc-9cbf72e3d9fd'
title: 'IPrintCoreHelperUni::EnumFeatures method'
---

# IPrintCoreHelperUni::EnumFeatures method

The `IPrintCoreHelperUni::EnumFeatures` method gets a list of all available features, including synthesized and core driver-implement features.

## Syntax


```C++
STDMETHOD EnumFeatures(
  [out] PCSTR *pFeatureList[],
  [out] DWORD *pdwNumFeatures
);
```



## Parameters

<dl> <dt>

*pFeatureList\[\]* \[out\]
</dt> <dd>

A pointer to an array of ANSI character strings that contain all of the features that are available for the current device. The final array element is indicated by a **NULL** string.

</dd> <dt>

*pdwNumFeatures* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of feature keywords in the array that is pointed to by the *pFeatureList* parameter.

</dd> </dl>

## Return value

`IPrintCoreHelperUni::EnumFeatures` should return S\_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.

## Remarks

For Unidrv features, the feature list is based on the GPD view of the configuration file, so features that are surrounded by "\*Ifdef GDL\_ENABLED/\*Endif" directives cannot be configured by using this method.

## Requirements



|                            |                                                                                       |
|----------------------------|---------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>    |
| Header<br/>          | <dl> <dt>Prcomoem.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreHelperUni**](iprintcorehelperuni-interface.md)
</dt> <dt>

[**IPrintCoreHelperUni::EnumOptions**](iprintcorehelperuni-enumoptions.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperUni::EnumFeatures%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





