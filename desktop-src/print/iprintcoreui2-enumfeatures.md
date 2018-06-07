---
Description: The IPrintCoreUI2::EnumFeatures method enumerates a printer's available features.
ms.assetid: e5c16b6d-555d-4360-b781-4d22be81ab56
title: IPrintCoreUI2::EnumFeatures method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintCoreUI2::EnumFeatures method

The `IPrintCoreUI2::EnumFeatures` method enumerates a printer's available features.

## Syntax


```C++
HRESULT EnumFeatures(
  [in]  POEMUIOBJ poemuiobj,
  [in]  DWORD     dwFlags,
  [out] PSTR      pmszFeatureList,
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

*pmszFeatureList* \[out\]
</dt> <dd>

Pointer to a caller-supplied buffer that receives a null-delimited list of feature keywords in MULTI\_SZ format. The list is terminated with two null characters.

Set this parameter to **NULL** to simply query for the size (\**pcbNeeded*) of the feature list without having the list filled in.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Specifies the size, in bytes, of the buffer pointed to by *pmszFeatureList*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

Pointer to a memory location that receives the actual size, in bytes, of the feature list.

</dd> </dl>

## Return value

This method must return one of the following values.



| Return code                                                                                   | Description                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                                                                                                                                                                                                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The value in *cbSize* was smaller than the number of bytes to be written to the output buffer (the buffer pointed to by *pmszFeatureList*).<br/> The method was called with *pmszFeatureList* set to **NULL**.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *poemuiobj* parameter pointed to an invalid context object.<br/>                                                                                                                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | The method failed<br/>                                                                                                                                                                                                    |



 

## Remarks

This method is supported only for Windows XP Pscript5 plug-ins, not for Unidrv plug-ins.

[*printer-sticky*](https://msdn.microsoft.com/139a10e9-203b-499b-9291-8537eae9189c) features (see [Replacing Driver-Supplied Property Sheet Pages](https://www.bing.com/search?q=Replacing+Driver-Supplied+Property+Sheet+Pages)), such as those that determine installable memory and the presence of optional accessories, are included in the feature keyword list, which appears in the output buffer pointed to by *pmszFeatureList* when the method returns. For Pscript5, such features have the **OpenGroupType** feature attribute set to "InstallableOptions".

To reduce the need to make two calls per data access, pass the method an output buffer of a fixed size (1 KB, for example), and then check the function return value. If the method returns S\_OK, the buffer already contains the data of interest. If the method returns E\_OUTOFMEMORY, the value in \**pcbNeeded* is the buffer size needed to hold the data of interest. The caller should then allocate a buffer of that larger size and proceed with a second call to the method.

For more information, see [Using EnumFeatures](https://www.bing.com/search?q=Using+EnumFeatures).

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

[**IPrintCoreUI2::EnumOptions**](iprintcoreui2-enumoptions.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreUI2::EnumFeatures%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





