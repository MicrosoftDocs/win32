---
Description: The IPrintCoreHelperPS::EnumConstrainedOptions method provides a list of all of the options that are constrained in a particular feature, based on current settings.
ms.assetid: 106119cd-80ed-4d26-a7c1-fda5a49b080c
title: IPrintCoreHelperPS::EnumConstrainedOptions method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintCoreHelperPS::EnumConstrainedOptions method

The **IPrintCoreHelperPS::EnumConstrainedOptions** method provides a list of all of the options that are constrained in a particular feature, based on current settings.

## Syntax


```C++
STDMETHOD EnumConstrainedOptions(
  [in, optional] CONST DEVMODE *pDevmode,
  [in]           DWORD         cbSize,
  [in]           PCSTR         pszFeatureKeyword,
  [out]          PCSTR         *pConstrainedOptionList[],
  [out]          DWORD         *pdwNumOptions
);
```



## Parameters

<dl> <dt>

*pDevmode* \[in, optional\]
</dt> <dd>

A pointer to a [**DEVMODEW**](https://www.bing.com/search?q=**DEVMODEW**) structure. If this pointer is provided, **IPrintCoreHelperPS::EnumConstrainedOptions** should use the DEVMODEW structure that is pointed to by *pDevmode* instead of the default or current DEVMODEW structure. If this method is called from the plug-in provider or from [**IPrintOemPS::DevMode**](iprintoemps-devmode.md), this parameter is required. In most other situations, the parameter should be **NULL**. When the core driver sets *pDevmode* to **NULL**, it modifies its internal state rather than that of the passed-in DEVMODEW structure. This is required during operations such as full UI replacement, where the DEVMODEW structure returned by a DDI, such as [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md), is being serviced by the core driver's UI module.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

The size, in bytes, of the DEVMODEW structure that is pointed to by the *pDevmode* parameter.

</dd> <dt>

*pszFeatureKeyword* \[in\]
</dt> <dd>

A string of ANSI characters that contains the feature name.

</dd> <dt>

*pConstrainedOptionList\[\]* \[out\]
</dt> <dd>

A pointer to an array of ANSI character strings. When **IPrintCoreHelperPS::EnumConstrainedOptions** returns, these strings will contain the names of all of the options that are constrained within the specified feature. The caller is not responsible for freeing the array or the individual strings in the array.

</dd> <dt>

*pdwNumOptions* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of constrained options in the array that is pointed to by the *pConstrainedOptionList* parameter.

</dd> </dl>

## Return value

**IPrintCoreHelperPS::EnumConstrainedOptions** should return one of the following values.



| Return code                                                                                                                     | Description                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                            | The constrained options were set for the specified feature.<br/>                                                                          |
| <dl> <dt>**E\_FAIL**</dt> </dl>                                          | The caller provided information that resulted in an invalid request, such as a request for a feature that does not exist.<br/>            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                                    | One or more of the arguments were invalid. This value might mean that the feature is not supported.<br/>                                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                                   | There was not enough memory to create the options array or the core driver could not service the request because of lack of memory. <br/> |
| <dl> <dt>**E\_UNEXPECTED, or other failures not listed here**</dt> </dl> | An unexpected condition occurred. The core driver is probably in an invalid state. The caller should exit with a failure code.<br/>       |



 

## Remarks

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreHelperPS**](iprintcorehelperps-interface.md)
</dt> <dt>

[**IPrintCoreHelperPS::EnumOptions**](iprintcorehelperps-enumoptions.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperPS::EnumConstrainedOptions%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





