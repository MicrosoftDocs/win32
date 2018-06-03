---
Description: The IPrintCoreUI2::QuerySimulationSupport method retrieves a spooler simulation capability structure, which indicates the kinds of simulation the spooler supports.
ms.assetid: 0136df19-9491-47ea-9a8f-c9a932646686
title: IPrintCoreUI2::QuerySimulationSupport method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintCoreUI2::QuerySimulationSupport method

The `IPrintCoreUI2::QuerySimulationSupport` method retrieves a spooler simulation capability structure, which indicates the kinds of simulation the spooler supports.

## Syntax


```C++
HRESULT QuerySimulationSupport(
  [in]  HANDLE hPrinter,
  [in]  DWORD  dwLevel,
  [out] PBYTE  pCaps,
  [in]  DWORD  cbSize,
  [out] PDWORD pcbNeeded
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

Specifies a handle to the printer.

</dd> <dt>

*dwLevel* \[in\]
</dt> <dd>

Specifies the spooler simulation capability structure returned in the buffer pointed to by *pCaps*. Currently, only level 1 of spooler simulation support is provided.



| Value        | Spooler Simulation Support Structure                                            |
|--------------|---------------------------------------------------------------------------------|
| 1<br/> | [**SIMULATE\_CAPS\_1**](simulate-caps-1.md) (defined in printoem.h)<br/> |



 

</dd> <dt>

*pCaps* \[out\]
</dt> <dd>

Pointer to the output buffer, which contains a structure of the type indicated by the value in the *dwLevel* parameter.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Specifies the size, in bytes, of the output buffer, which is pointed to by *pCaps*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

Specifies the size, in bytes, of the memory needed to store a structure of the type indicated by *dwLevel*.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                                   | Description                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                                                                                                                                                                            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The value in *cbSize* was smaller than the number of bytes to be written to the output buffer (the buffer pointed to by *pCaps*).<br/> The method was called with *pCaps* set to **NULL**.<br/> |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | The method is not supported.<br/> A structure of the type specified by *dwLevel* is not supported.<br/>                                                                                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | The method failed<br/>                                                                                                                                                                                |



 

## Remarks

This method is supported only for Windows XP Pscript5 plug-ins, not for Unidrv plug-ins.

The `IPrintCoreUI2::QuerySimulationSupport` method stores a spooler simulation capability structure in the buffer pointed to by *pCaps*. This structure specifies the level of spooler support for "N-up" printing, reverse printing, the maximum number of pages that can be printed, collation, and others.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreUI2**](iprintcoreui2-interface.md)
</dt> <dt>

[**SIMULATE\_CAPS\_1**](simulate-caps-1.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreUI2::QuerySimulationSupport%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





