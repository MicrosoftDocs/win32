---
Description: 'The IPrintCoreUI2::GetOptions method retrieves the driver''s current feature settings in the format of a list of feature/option keyword pairs.'
ms.assetid: 'd83b8520-6f31-403c-ac58-6d6a20cf8750'
title: 'IPrintCoreUI2::GetOptions method'
---

# IPrintCoreUI2::GetOptions method

The `IPrintCoreUI2::GetOptions` method retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs.

## Syntax


```C++
HRESULT GetOptions(
  [in]  POEMUIOBJ poemuiobj,
  [in]  DWORD     dwFlags,
  [in]  PCSTR     pmszFeaturesRequested,
  [in]  DWORD     cbIn,
  [out] PSTR      pmszFeatureOptionBuf,
  [in]  DWORD     cbSize,
  [out] PDWORD    pcbNeeded
);
```



## Parameters

<dl> <dt>

*poemuiobj* \[in\]
</dt> <dd>

Pointer to the current context, an [**OEMUIOBJ**](oemuiobj.md) structure.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Is reserved and must be set to zero.

</dd> <dt>

*pmszFeaturesRequested* \[in\]
</dt> <dd>

Pointer to caller-supplied buffer containing a list of feature keywords (in MULTI\_SZ format) whose settings are requested. Set this parameter to **NULL** to obtain settings for all features.

</dd> <dt>

*cbIn* \[in\]
</dt> <dd>

Specifies the size, in bytes, of the buffer pointed to by *pmszFeaturesRequested*. The size includes the last MULTI\_SZ null character.

</dd> <dt>

*pmszFeatureOptionBuf* \[out\]
</dt> <dd>

Pointer to a caller-supplied buffer that receives a list of feature/option keyword pairs (in MULTI\_SZ format) obtained from the driver settings. Each feature/option keyword pair contains the feature keyword name, a null character, the option keyword name, and another null character. The list is terminated by two null characters.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Specifies the size, in bytes, of the buffer pointed to by *pmszFeatureOptionBuf*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

Pointer to a memory location that receives the actual size, in bytes, of the feature/option keyword pairs.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                                   | Description                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                                                                                                                                                                                                          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The value in *cbSize* was smaller than the number of bytes to be written to the output buffer (the buffer pointed to by *pmszFeatureOptionBuf*).<br/> The method was called with *pmszFeatureOptionBuf* set to **NULL**.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The input buffer (the buffer pointed to by *pmszFeaturesRequested*) was provided, but its contents were not in MULTI\_SZ format.<br/> The *poemuiobj* parameter pointed to an invalid context object.<br/>                    |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | The method is not supported.<br/>                                                                                                                                                                                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | The method failed<br/>                                                                                                                                                                                                              |



 

## Remarks

This method is supported only for Windows XP Pscript5 UI plug-ins that fully replace the core driver's standard UI pages, and is supported only during the UI plug-in's [**IPrintOemUI::DocumentPropertySheets**](iprintoemui-documentpropertysheets.md) and [**IPrintOemUI::DevicePropertySheets**](iprintoemui-devicepropertysheets.md) functions, and their property sheet callback routines. See [Replacing Driver-Supplied Property Sheet Pages](print.replacing_driver_supplied_property_sheet_pages) for more information.

If a requested feature keyword is not recognized, or recognized but not supported in the current sticky mode ([*document-sticky*](wdkgloss.d#wdkgloss-document-sticky) or [*printer-sticky*](wdkgloss.p#wdkgloss-printer-sticky) -- see [Replacing Driver-Supplied Property Sheet Pages](print.replacing_driver_supplied_property_sheet_pages)), or the feature keyword is recognized but there is currently no option selection for it, the feature is simply ignored and the feature/option keyword pair is not placed in the output buffer.

To reduce the need to make two calls per data access, pass the method an output buffer of a fixed size (1 KB, for example), and then check the function return value. If the method returns S\_OK, the buffer already contains the data of interest. If the method returns E\_OUTOFMEMORY, the value in \**pcbNeeded* is the buffer size needed to hold the data of interest. The caller should then allocate a buffer of that larger size and proceed with a second call to the method.

For more information, see [Using GetOptions and SetOptions](print.using_getoptions_and_setoptions).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreUI2**](iprintcoreui2-interface.md)
</dt> <dt>

[**OEMUIOBJ**](oemuiobj.md)
</dt> <dt>

[**IPrintOemUI::DocumentPropertySheets**](iprintoemui-documentpropertysheets.md)
</dt> <dt>

[**IPrintOemUI::DevicePropertySheets**](iprintoemui-devicepropertysheets.md)
</dt> <dt>

[**IPrintCoreUI2::SetOptions**](iprintcoreui2-setoptions.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreUI2::GetOptions%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





