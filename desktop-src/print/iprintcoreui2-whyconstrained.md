---
Description: The IPrintCoreUI2::WhyConstrained method determines why the specified feature/option selection is constrained.
ms.assetid: 3161620e-6155-4587-b978-599d526d792c
title: IPrintCoreUI2::WhyConstrained method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintCoreUI2::WhyConstrained method

The `IPrintCoreUI2::WhyConstrained` method determines why the specified feature/option selection is constrained.

## Syntax


```C++
HRESULT WhyConstrained(
  [in]  POEMUIOBJ poemuiobj,
  [in]  DWORD     dwFlags,
  [in]  PCSTR     pszFeatureKeyword,
  [in]  PCSTR     pszOptionKeyword,
  [out] PSTR      pmszReasonList,
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

*pszFeatureKeyword* \[in\]
</dt> <dd>

Pointer to a caller-supplied buffer containing the single feature keyword of interest to the caller.

</dd> <dt>

*pszOptionKeyword* \[in\]
</dt> <dd>

Pointer to a caller-supplied buffer containing the option keyword.

</dd> <dt>

*pmszReasonList* \[out\]
</dt> <dd>

Pointer to a caller-supplied buffer that receives a list of the feature/option keyword pairs that place constraints on the specified feature/option. This list is in MULTI\_SZ format with each item in the list separated from the next by a null character. The list is terminated with two null characters.

Set this parameter to **NULL** to simply query for the size (\**pcbNeeded*) of the reason list without having the list filled in.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Specifies the size, in bytes, of the buffer pointed to by *pmszReasonList*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

Pointer to a memory location that receives the actual size, in bytes, of the reason list.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                                   | Description                                                                                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                                                                                                                                                                                                                                                                                                                    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The value in *cbSize* was smaller than the number of bytes to be written to the output buffer (the buffer pointed to by *pmszReasonList*).<br/> The method was called with *pmszReasonList* set to **NULL**.<br/>                                                                                                                       |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | The method is not supported.<br/>                                                                                                                                                                                                                                                                                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *poemuiobj* parameter pointed to an invalid context object.<br/> The feature keyword or option keyword was not recognized.<br/> The feature stickiness (see [Replacing Driver-Supplied Property Sheet Pages](https://www.bing.com/search?q=Replacing+Driver-Supplied+Property+Sheet+Pages)) did not match that specified in the current context.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | The method failed<br/>                                                                                                                                                                                                                                                                                                                        |



 

## Remarks

This method is supported only for Windows XP Pscript5 UI plug-ins that fully replace the core driver's standard UI pages, and is supported only during the UI plug-in's [**IPrintOemUI::DocumentPropertySheets**](iprintoemui-documentpropertysheets.md) and [**IPrintOemUI::DevicePropertySheets**](iprintoemui-devicepropertysheets.md) functions, and their property sheet callback routines. See [Replacing Driver-Supplied Property Sheet Pages](https://www.bing.com/search?q=Replacing+Driver-Supplied+Property+Sheet+Pages) for more information.

When a user of the OEM UI attempts to select an item that is constrained, the caller can use this method to display a message explaining why the item is constrained. When this method returns, *pmszReasonList* points to a list of one or more feature/option pairs that appear in the current driver settings, but conflict with the selected feature/option keywords. If there were no conflicts, the method should return S\_OK, *pmszReasonList* should be filled in with an empty ASCII string containing only a null character, and \**pcbNeeded* should be set to 1.

To reduce the need to make two calls per data access, pass the method an output buffer of a fixed size (1 KB, for example), and then check the function return value. If the method returns S\_OK, the buffer already contains the data of interest. If the method returns E\_OUTOFMEMORY, the value in \**pcbNeeded* is the buffer size needed to hold the data of interest. The caller should then allocate a buffer of that larger size and proceed with a second call to the method.

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

[**IPrintCoreUI2::EnumConstrainedOptions**](iprintcoreui2-enumconstrainedoptions.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreUI2::WhyConstrained%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





