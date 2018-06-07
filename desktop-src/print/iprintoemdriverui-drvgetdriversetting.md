---
Description: The IPrintOemDriverUI::DrvGetDriverSetting method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can obtain the current status of printer features and other internal information.
ms.assetid: 25e8aec7-86af-4753-83d7-e7df5435f602
title: IPrintOemDriverUI::DrvGetDriverSetting method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemDriverUI::DrvGetDriverSetting method

The `IPrintOemDriverUI::DrvGetDriverSetting` method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can obtain the current status of printer features and other internal information.

## Syntax


```C++
HRESULT DrvGetDriverSetting(
   PVOID  pci,
   PCSTR  Feature,
   PVOID  pOutput,
   DWORD  cbSize,
   PDWORD pcbNeeded,
   PDWORD pdwOptionsReturned
);
```



## Parameters

<dl> <dt>

*pci* 
</dt> <dd>

Caller-supplied pointer to an [**OEMUIOBJ**](oemuiobj.md) structure.

</dd> <dt>

*Feature* 
</dt> <dd>

Caller-supplied value identifying the printer feature for which option settings are returned. This can be either a string pointer or a constant, as described in the following Remarks section.

</dd> <dt>

*pOutput* 
</dt> <dd>

Caller-supplied pointer to a buffer to receive the specified information.

</dd> <dt>

*cbSize* 
</dt> <dd>

Caller-supplied size, in bytes, of the buffer pointed to by *pOutput*.

</dd> <dt>

*pcbNeeded* 
</dt> <dd>

Caller-supplied pointer to a location to receive the minimum buffer size required to contain the requested information.

</dd> <dt>

*pdwOptionsReturned* 
</dt> <dd>

Caller-supplied pointer to a location to receive the number of option strings placed in *pOutput*.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

When calling the `IPrintOemDriverUI::DrvGetDriverSetting` method, a user interface plug-in can specify either a string pointer or a constant value for *pFeatureKeyword*.

-   If *pFeatureKeyword* is a string, it must represent one of the following:

    -   A feature name specified in a [Unidrv minidriver](https://www.bing.com/search?q=Unidrv+minidriver) GPD file, or,
    -   A keyword argument to an \***OpenUI** entry in a Pscript5 minidriver's PPD file.

    The method returns one or more NULL-terminated strings in the buffer pointed to by *pOutput*. Each string represents the name of a currently selected option.The number of strings is returned in *pdwOptionsReturned*.

-   If *pFeatureKeyword* is a constant, it must be one of the **OEMGDS\_**-prefixed constants defined in printoem.h. The method returns the value indicated by the specified constant by placing it in the buffer pointed to by *pOutput*. The value returned in *pdwOptionsReturned* is always 1.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUI::DrvGetDriverSetting%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




