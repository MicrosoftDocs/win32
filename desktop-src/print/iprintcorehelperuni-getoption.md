---
Description: The IPrintCoreHelperUniGetOption method gets a specified option for a given feature.
ms.assetid: 0850ba08-089a-4715-bee4-a44a95e6dee6
title: IPrintCoreHelperUniGetOption method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintCoreHelperUni::GetOption method

The `IPrintCoreHelperUni::GetOption` method gets a specified option for a given feature.

## Syntax


```C++
STDMETHOD GetOption(
  [in, optional] CONST DEVMODE *pDevmode,
  [in]           DWORD         cbSize,
  [in]           PCSTR         pszFeatureRequested,
  [out]          PCSTR         *ppszOption
);
```



## Parameters

<dl> <dt>

*pDevmode* \[in, optional\]
</dt> <dd>

A pointer to a [**DEVMODEW**](display.devmodew) structure. If this pointer is provided, `IPrintCoreHelperUni::GetOption` should use the DEVMODEW structure that is pointed to by *pDevmode* instead of the default or current DEVMODEW structure. If this method is called from the plug-in provider or from [**IPrintOemUni::DevMode**](iprintoemuni-devmode.md), this parameter is required. In most other situations, the parameter should be **NULL**. When the core driver sets *pDevmode* to **NULL**, it modifies its internal state rather than that of the passed-in DEVMODEW structure. This is required during operations such as full UI replacement, where the DEVMODEW structure returned by a DDI, such as [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md), is being serviced by the core driver's UI module.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

The size, in bytes, of the DEVMODEW structure that is pointed to by the *pDevmode* parameter.

</dd> <dt>

*pszFeatureRequested* \[in\]
</dt> <dd>

A pointer to the ANSI string that contains the name of the feature as it appears in the GPD file.

</dd> <dt>

*ppszOption* \[out\]
</dt> <dd>

A pointer to a variable that contains the address of an ANSI string. When `IPrintCoreHelperUni::GetOption` returns, the string should contain the keyword for the currently selected option as it appears in the configuration file. The caller should not modify this string and should not free the memory that is associated with this string.

</dd> </dl>

## Return value

`IPrintCoreHelperUni::GetOption` should return one of the following values.



| Return code                                                                                                                         | Description                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                                | The method read the option for the specified feature.<br/>                                                                                        |
| <dl> <dt>**E\_FAIL**</dt> </dl>                                              | The caller provided information that resulted in an invalid request. For example, the feature that was requested does not exist.<br/>             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                                        | The arguments were invalid. This value might mean that the feature is not supported or that too many options were requested for the feature.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                                       | The core driver was not able to service the request because there was insufficient memory.<br/>                                                   |
| <dl> <dt>**E\_UNEXPECTED, or other return codes not listed here**</dt> </dl> | The core driver seems to be in an invalid state. The caller should return a failure code.<br/>                                                    |



 

## Remarks

`IPrintCoreHelperUni::GetOption` cannot be used for features that allow multiple options to be set simultaneously.

Feature keywords are as defined in the GPD file. In addition, the Unidrv driver supports several reserved keywords for options that are stored in its private [**DEVMODEW**](display.devmodew) structure. For the list of Unidrv features, see [Keyword Mapping](print.keyword_mapping).

The caller should not free the string that is pointed to by *ppszOption* and should not modify the string in any way.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreHelperUni**](iprintcorehelperuni-interface.md)
</dt> <dt>

[**IPrintCoreHelperUni::SetOptions**](iprintcorehelperuni-setoptions.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperUni::GetOption%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





