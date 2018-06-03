---
Description: The IPrintCoreHelper::WhyConstrained method provides a list of options that are constraining the specified feature-option pair in the current configuration.
ms.assetid: de3fdbd4-9647-4369-9c23-4779aa768b1b
title: IPrintCoreHelper::WhyConstrained method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintCoreHelper::WhyConstrained method

The **IPrintCoreHelper::WhyConstrained** method provides a list of options that are constraining the specified feature-option pair in the current configuration.

## Syntax


```C++
HRESULT WhyConstrained(
  [in]  const DEVMODE              *pDevmode,
  [in]        DWORD                cbSize,
  [in]        PCSTR                pszFeatureKeyword,
  [in]        PCSTR                pszOptionKeyword,
  [out] const PRINT_FEATURE_OPTION **ppFOConstraints,
  [out]       DWORD                *pdwNumOptions
);
```



## Parameters

<dl> <dt>

*pDevmode* \[in\]
</dt> <dd>

A pointer to a [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure. If this pointer is provided, **IPrintCoreHelper::WhyConstrained** should use the DEVMODEW structure that is pointed to by *pDevmode* instead of the default or current DEVMODEW structure. If this method is called from the plug-in provider or from either [**IPrintOemPS::DevMode**](iprintoemps-devmode.md) or [**IPrintOemUni::DevMode**](iprintoemuni-devmode.md), this parameter is required. In most other situations, the parameter should be **NULL**. When the core driver sets *pDevmode* to **NULL**, it modifies its internal state rather than that of the passed-in DEVMODEW structure. This is required during operations such as full UI replacement, where the DEVMODEW structure returned by a DDI, such as [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md), is being serviced by the core driver's UI module.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

The size, in bytes, of the DEVMODEW structure that is pointed to by the *pDevmode* parameter.

</dd> <dt>

*pszFeatureKeyword* \[in\]
</dt> <dd>

A pointer to an ANSI string that contains the name of the feature. The feature name should correspond to the keyword that is used in the GPD or PPD file.

</dd> <dt>

*pszOptionKeyword* \[in\]
</dt> <dd>

A pointer to an ANSI string that contains the name of the option. The option name should correspond to the keyword that is used in the GPD or PPD file.

</dd> <dt>

*ppFOConstraints* \[out\]
</dt> <dd>

A pointer to an array of [**PRINT\_FEATURE\_OPTION**](print-feature-option.md) elements. When **IPrintCoreHelper::WhyConstrained** returns, the array contains a list of feature-element pairs of the options that constrain the options that are specified in the *pszOptionKeyword* parameter.

</dd> <dt>

*pdwNumOptions* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of feature-option pairs in the array that is pointed to by the *ppFOConstraints* parameter.

</dd> </dl>

## Return value

**IPrintCoreHelper::WhyConstrained** should return one of the following values.



| Return code                                                                                   | Description                                                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The operation succeeded.<br/>                                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | One or more of the arguments is invalid, or the feature was not supported.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Memory for the result array could not be allocated.<br/>                        |



 

## Remarks

If the specified feature-option pair is not constrained, **IPrintCoreHelper::WhyConstrained** will return S\_OK but will return with \**pdwFOPairs* set to 0 and with \**ppFOConstraints*\[0\] set to **NULL**.

Note that the results from this method might not contain all of the options that affect the currently selected option. For Unidrv drivers, this list will include at least one option from each set of constraints that is active. If there are invalid combinations that list more than two feature-option pairs, however, only one option from the combination will be included in the list.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreHelper**](iprintcorehelper-interface.md)
</dt> <dt>

[**IPrintCoreHelper::EnumConstrainedOptions**](iprintcorehelper-enumconstrainedoptions.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelper::WhyConstrained%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





