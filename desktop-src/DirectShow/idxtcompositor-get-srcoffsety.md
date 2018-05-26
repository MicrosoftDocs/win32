---
Description: The get\_SrcOffsetY method retrieves the vertical offset of the source rectangle.
ms.assetid: b692e71b-c7a9-437c-9127-fa517e817883
title: IDxtCompositorget\_SrcOffsetY method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDxtCompositor::get\_SrcOffsetY method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_SrcOffsetY` method retrieves the vertical offset of the source rectangle.

## Syntax


```C++
HRESULT get_SrcOffsetY(
  [out, retval] long *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives the vertical offset of the source rectangle, in pixels.

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

[**IDxtCompositor Interface**](idxtcompositor.md)
</dt> </dl>

 

 




