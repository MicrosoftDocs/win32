---
Description: The ApplyChanges method applies any properties that have changed.
ms.assetid: dece1e61-7fe1-40f1-8d1d-89b5a334d04e
title: IDxtJpegApplyChanges method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDxtJpeg::ApplyChanges method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `ApplyChanges` method applies any properties that have changed.

## Syntax


```C++
HRESULT ApplyChanges();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IDxtJpeg Interface**](idxtjpeg.md)
</dt> </dl>

 

 




