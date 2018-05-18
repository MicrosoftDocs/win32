---
Description: 'The DrvWriteSpoolBuf function pointed to by this function pointer is obsolete.'
ms.assetid: 'a0de6757-3be8-4c8f-bc6f-93c2e097fec7'
title: 'PFN\_DrvWriteSpoolBuf callback function'
---

# PFN\_DrvWriteSpoolBuf callback function

The **DrvWriteSpoolBuf** function pointed to by this function pointer is obsolete.

Windows 2000 and later render plug-ins should use [**IPrintOemDriverUni::DrvWriteSpoolBuf**](iprintoemdriveruni-drvwritespoolbuf.md) (Unidrv plug-ins), [**IPrintOemDriverPS::DrvWriteSpoolBuf**](iprintoemdriverps-drvwritespoolbuf.md) (Pscript plug-ins), or [**IPrintCorePS2::DrvWriteSpoolBuf**](iprintcoreps2-drvwritespoolbuf.md) (Pscript plug-ins).

This function pointer prototype defines the **DrvWriteSpoolBuf** member of the [**DRVPROCS**](drvprocs.md) structure.

## Syntax


```C++
PFN_DrvWriteSpoolBuf DrvWriteSpoolBuf;

DWORD APIENTRY* DrvWriteSpoolBuf(
   PDEVOBJ                        pdevobj,
   _In_reads_bytes_(cbSize) PVOID pBuffer,
   DWORD                          cbSize
)
{ ... }
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd></dd> <dt>

*pBuffer* 
</dt> <dd></dd> <dt>

*cbSize* 
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PFN_DrvWriteSpoolBuf%20callback%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




