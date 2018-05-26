---
Description: The IPrintOemDriverUniDrvGetDriverSetting method is provided by the Unidrv driver so that rendering plug-ins can obtain the current status of printer features and other internal information.
ms.assetid: 29ccd7e6-60eb-4a8e-9a71-9fbed4b2bdcf
title: IPrintOemDriverUniDrvGetDriverSetting method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemDriverUni::DrvGetDriverSetting method

The `IPrintOemDriverUni::DrvGetDriverSetting` method is provided by the Unidrv driver so that rendering plug-ins can obtain the current status of printer features and other internal information.

## Syntax


```C++
HRESULT DrvGetDriverSetting(
   PVOID  pdriverobj,
   PCSTR  Feature,
   PVOID  pOutput,
   DWORD  cbSize,
   PDWORD pcbNeeded,
   PDWORD pdwOptionsReturned
);
```



## Parameters

<dl> <dt>

*pdriverobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*Feature* 
</dt> <dd>

Caller supplied value identifying the printer feature for which option settings will be returned. This can be either a string pointer or a constant, as described in the following Remarks section.

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

When the `IPrintOemDriverUni::DrvGetDriverSetting` method is called, either a string pointer or a constant value can be specified for *pFeatureKeyword*.

-   If *pFeatureKeyword* is a string, it must represent a feature name specified in a [Unidrv minidriver](print.unidrv_minidrivers) GPD file

    The method should return one or more NULL-terminated strings in the buffer pointed to by *pOutput*. Each string should represent the name of a currently selected option. The number of strings should be returned in *pdwOptionsReturned*.

-   If *pFeatureKeyword* is a constant, it must be one of the **OEMGDS\_**-prefixed constants defined in printoem.h. The method should return the value indicated by the specified constant by placing it in the buffer pointed to by *pOutput*. The value returned in *pdwOptionsReturned* must be 1.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUni::DrvGetDriverSetting%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




