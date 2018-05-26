---
Description: The IPrintOemDriverUniDrvGetStandardVariable method is provided by the Unidrv driver so that rendering plug-ins can obtain the current value of Unidrvs standard variables.
ms.assetid: d55d3130-14e7-438f-bfb5-18927466bd60
title: IPrintOemDriverUniDrvGetStandardVariable method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemDriverUni::DrvGetStandardVariable method

The `IPrintOemDriverUni::DrvGetStandardVariable` method is provided by the Unidrv driver so that rendering plug-ins can obtain the current value of Unidrv's [standard variables](print.standard_variables).

## Syntax


```C++
HRESULT DrvGetStandardVariable(
   PDEVOBJ pdevobj,
   DWORD   dwIndex,
   PVOID   pBuffer,
   DWORD   cbSize,
   PDWORD  pcbNeeded
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*dwIndex* 
</dt> <dd>

Caller-supplied, SVI\_-prefixed index into the list of Unidrv's standard variables. The SVI\_-prefixed index values are defined in printoem.h.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Caller-supplied pointer to a DWORD to receive the standard variable's current value.

</dd> <dt>

*cbSize* 
</dt> <dd>

Caller-supplied size of the buffer pointed to by *pBuffer*.

</dd> <dt>

*pcbNeeded* 
</dt> <dd>

Caller-supplied pointer to a location to receive the minimum buffer size required to contain the requested information.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUni::DrvGetStandardVariable%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




