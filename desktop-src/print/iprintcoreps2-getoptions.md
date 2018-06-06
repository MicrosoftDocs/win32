---
Description: The IPrintCorePS2::GetOptions method retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs.
ms.assetid: 8f5df76b-57c9-4c5a-9ca2-f02c8d903a8b
title: IPrintCorePS2::GetOptions method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintCorePS2::GetOptions method

The `IPrintCorePS2::GetOptions` method retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs.

## Syntax


```C++
HRESULT GetOptions(
  [in]  PDEVOBJ pdevobj,
  [in]  DWORD   dwFlags,
  [in]  PCSTR   pmszFeaturesRequested,
  [in]  DWORD   cbIn,
  [out] PSTR    pmszFeatureOptionBuf,
  [in]  DWORD   cbSize,
  [out] PDWORD  pcbNeeded
);
```



## Parameters

<dl> <dt>

*pdevobj* \[in\]
</dt> <dd>

Pointer to a [**DEVOBJ**](devobj.md) structure.

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

Pointer to a caller-supplied buffer that receives a list of feature/option keyword pairs (in MULTI\_SZ format) obtained from the driver settings. Each feature/option keyword pair contains the feature keyword name, a null character, the option keyword name, and another null character. The list is terminated by two NULL characters.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Specifies the size, in bytes, of the buffer pointed to by *pmszFeatureOptionBuf*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

Pointer to a memory location that receives the actual size, in bytes, of the requested data.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                                   | Description                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                                                                                                                                                                                                          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The value in *cbSize* was smaller than the number of bytes to be written to the output buffer (the buffer pointed to by *pmszFeatureOptionBuf*).<br/> The method was called with *pmszFeatureOptionBuf* set to **NULL**.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The input buffer (the buffer pointed to by *pmszFeaturesRequested*) was provided, but its contents were not in MULTI\_SZ format.<br/> The *pdevobj* parameter pointed to an invalid driver context object.<br/>               |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | The method is not supported.<br/>                                                                                                                                                                                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | The method failed.<br/>                                                                                                                                                                                                             |



 

## Remarks

This method supports both [*document-sticky*](wdkgloss.d#wdkgloss-document-sticky) and [*printer-sticky*](wdkgloss.p#wdkgloss-printer-sticky) features. It is supported only after the core driver finishes its [**DrvEnablePDEV**](https://msdn.microsoft.com/9a7ed18a-f21c-486b-9261-59a3fe5aef9e) processing, which sets up all option settings. A call to `IPrintCorePS2::GetOptions` when it is not supported should cause it to return E\_NOTIMPL. For example, when the core driver calls a render plug-in's [**IPrintOemPS::EnablePDEV**](iprintoemps-enablepdev.md) method, the driver is still occupied with its **DrvEnablePDEV** processing, so if the plug-in calls `IPrintCorePS2::GetOptions` within the plug-in's **IPrintOemPS::DevMode** method, the plug-in receives the E\_NOTIMPL return value. However, because the plug-in's **IPrintOemPS::EnablePDEV** method is called after the core driver finishes its **DrvEnablePDEV** processing, the plug-in is able to call `IPrintCorePS2::GetOptions` successfully within its **IPrintOemPS::EnablePDEV** method.

If a requested feature keyword is not recognized, or the feature is recognized but there is currently no option selection for it, the feature is ignored and the feature/option keyword pair is not placed in the output buffer.

To reduce the need to make two calls per data access, pass the method an output buffer of a fixed size (1 KB, for example), and then check the function return value. If the method returns S\_OK, the buffer already contains the data of interest. If the method returns E\_OUTOFMEMORY, the value in \**pcbNeeded* is the buffer size needed to hold the data of interest. The caller should then allocate a buffer of that larger size and proceed with a second call to the method.

This method is supported for any Pscript5 render plug-in.

For more information, see [Using GetOptions and SetOptions](https://www.bing.com/search?q=Using+GetOptions+and+SetOptions).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCorePS2**](iprintcoreps2-interface.md)
</dt> <dt>

[**DEVOBJ**](devobj.md)
</dt> <dt>

[**DrvEnablePDEV**](https://msdn.microsoft.com/9a7ed18a-f21c-486b-9261-59a3fe5aef9e)
</dt> <dt>

[**IPrintOemPS::DevMode**](iprintoemps-devmode.md)
</dt> <dt>

[**IPrintOemPS::EnablePDEV**](iprintoemps-enablepdev.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCorePS2::GetOptions%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





