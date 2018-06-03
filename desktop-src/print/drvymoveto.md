---
Description: The DrvYMoveTo function is obsolete.
ms.assetid: 0d8539eb-0b9c-4aae-abbe-bb7ddd6231f5
title: PFN\_DrvYMoveTo callback function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PFN\_DrvYMoveTo callback function

The **DrvYMoveTo** function is obsolete.

Windows 2000 and later Unidrv plug-ins should use [**IPrintOemDriverUni::DrvYMoveTo**](iprintoemdriveruni-drvymoveto.md).

This function pointer prototype defines the type of the **DrvYMoveTo** member of the [**DRVPROCS**](drvprocs.md) structure.

## Syntax


```C++
PFN_DrvYMoveTo DrvYMoveTo;

 INT APIENTRY* DrvYMoveTo(
   PDEVOBJ pdevobj,
   INT     y,
   DWORD   dwFlags
)
{ ... }
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd></dd> <dt>

*y* 
</dt> <dd></dd> <dt>

*dwFlags* 
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PFN_DrvYMoveTo%20callback%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




