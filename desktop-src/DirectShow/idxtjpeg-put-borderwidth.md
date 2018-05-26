---
Description: The put\_BorderWidth method specifies the width of the solid border along the edges of the wipe pattern.
ms.assetid: a618926a-efa4-47a2-9ce9-ae298ed41083
title: IDxtJpegput\_BorderWidth method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDxtJpeg::put\_BorderWidth method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_BorderWidth` method specifies the width of the solid border along the edges of the wipe pattern.

## Syntax


```C++
HRESULT put_BorderWidth(
  [in] long newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

The width of the border, in pixels.

</dd> </dl>

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

 

 




