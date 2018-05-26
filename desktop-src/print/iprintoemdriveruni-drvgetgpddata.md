---
Description: The IPrintOemDriverUniDrvGetGPDData method is provided by the Unidrv driver so that rendering plug-ins can obtain data defined in a printers GPD file.
ms.assetid: cebe8972-4e5a-4382-ac1b-4c326dea46b1
title: IPrintOemDriverUniDrvGetGPDData method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemDriverUni::DrvGetGPDData method

The `IPrintOemDriverUni::DrvGetGPDData` method is provided by the Unidrv driver so that rendering plug-ins can obtain data defined in a printer's [*GPD*](wdkgloss.g#wdkgloss-generic-printer-description--gpd-) file.

## Syntax


```C++
HRESULT DrvGetGPDData(
   PDEVOBJ pdevobj,
   DWORD   dwType,
   PVOID   pInputData,
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

*dwType* 
</dt> <dd>

Caller-supplied flag indicating the type of GPD data being requested. Currently, the following flag is the only one defined:



| Flag                          | Definition                                                                                       |
|-------------------------------|--------------------------------------------------------------------------------------------------|
| GPD\_OEMCUSTOMDATA<br/> | The method returns the string associated with a GPD file's \***OEMCustomData** entry.<br/> |



 

</dd> <dt>

*pInputData* 
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Caller-supplied pointer to a buffer to receive the requested information.

</dd> <dt>

*cbSize* 
</dt> <dd>

Caller-supplied size, in bytes, of the buffer pointed to by *pBuffer*.

</dd> <dt>

*pcbNeeded* 
</dt> <dd>

Receives the driver-supplied minimum buffer size, in bytes, required to contain the requested information.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

If the buffer specified by *pBuffer* and *cbSize* is too small to receive the requested information, Unidrv supplies the required buffer size in the location pointed to by *pcbNeeded*, returns E\_FAIL, and sets the error code to ERROR\_INSUFFICIENT\_BUFFER.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUni::DrvGetGPDData%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




