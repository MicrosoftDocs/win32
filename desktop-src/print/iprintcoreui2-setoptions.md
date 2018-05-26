---
Description: The IPrintCoreUI2SetOptions method sets the drivers feature settings.
ms.assetid: b608e331-6b13-4b27-8bb1-00a7c2fef281
title: IPrintCoreUI2SetOptions method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintCoreUI2::SetOptions method

The `IPrintCoreUI2::SetOptions` method sets the driver's feature settings.

## Syntax


```C++
HRESULT SetOptions(
  [in]  POEMUIOBJ poemuiobj,
  [in]  DWORD     dwFlags,
  [in]  PCSTR     pmszFeatureOptionBuf,
  [in]  DWORD     cbIn,
  [out] PDWORD    pdwResult
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

Specifies whether the core driver is to resolve conflicts. This parameter must be set to one of the following values:



| Value                                          | Meaning                                                             |
|------------------------------------------------|---------------------------------------------------------------------|
| SETOPTIONS\_FLAG\_KEEP\_CONFLICT<br/>    | Ask core driver to not resolve any conflict that arises.<br/> |
| SETOPTIONS\_FLAG\_RESOLVE\_CONFLICT<br/> | Ask core driver to resolve any conflict that arises.<br/>     |



 

</dd> <dt>

*pmszFeatureOptionBuf* \[in\]
</dt> <dd>

Pointer to a caller-supplied buffer containing a list of feature/option keyword pairs in MULTI\_SZ format. Each item in this list is separated from the next by a null character, and the list is terminated with two null characters.

</dd> <dt>

*cbIn* \[in\]
</dt> <dd>

Specifies the size, in bytes, of the buffer pointed to by *pmszFeatureOptionBuf*. This size includes the last MULTI\_SZ null character.

</dd> <dt>

*pdwResult* \[out\]
</dt> <dd>

Pointer to a memory location that receives one of the following values. These constants are defined in printoem.h.



| Value                                             | Meaning                                                                   |
|---------------------------------------------------|---------------------------------------------------------------------------|
| SETOPTIONS\_RESULT\_CONFLICT\_REMAINED<br/> | The core driver found conflicts, but has left them unresolved.<br/> |
| SETOPTIONS\_RESULT\_CONFLICT\_RESOLVED<br/> | The core driver found and resolved all conflicts.<br/>              |
| SETOPTIONS\_RESULT\_NO\_CONFLICT<br/>       | The core driver did not find any conflict.<br/>                     |



 

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                                  | Description                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method succeeded.<br/>                                                                                                                                                                                            |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>    | The method is not supported.<br/> A structure of the type specified by *dwLevel* is not supported.<br/>                                                                                                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The value in *dwFlags* was incorrect.<br/> The input buffer (pointed to by *pmszFeatureOptionBuf*) was not in MULTI\_SZ format.<br/> The *poemuiobj* parameter pointed to an invalid context object.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | The method failed<br/>                                                                                                                                                                                                |



 

## Remarks

This method is supported only for Windows XP Pscript5 plug-ins, not for Unidrv plug-ins.

This method is called to set the driver's feature settings using a list of feature/option keyword pairs. The caller can access the resultant feature settings using the [**IPrintCoreUI2::GetOptions**](iprintcoreui2-getoptions.md) method.

If this method returns any value other than S\_OK, then it did not make any change in the driver's feature settings.

The *pmszFeatureOptionBuf* input buffer must be constructed in the same way as the output buffer of the **IPrintCoreUI2::GetOptions** method. That is, the feature/option keyword pairs must be in MULTI\_SZ format, and each item in the list is separated from the next by a null character. A pair of null characters terminates the list.

If the input buffer contains a feature keyword or its option keyword that is not recognized, or the feature is recognized but not supported in the current sticky mode (see [Replacing Driver-Supplied Property Sheet Pages](print.replacing_driver_supplied_property_sheet_pages)), then the feature/option pair is ignored, and the current option for that feature continues to be in effect.

This method is supported only for UI plug-ins that fully replace the core driver's standard UI pages, and is supported only during the UI plug-in's [**IPrintOemUI::DocumentPropertySheets**](iprintoemui-documentpropertysheets.md) and [**IPrintOemUI::DevicePropertySheets**](iprintoemui-devicepropertysheets.md) functions, and their property sheet callback routines.

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

[**IPrintCoreUI2::GetOptions**](iprintcoreui2-getoptions.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreUI2::SetOptions%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





