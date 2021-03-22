---
description: The put\_Height method specifies the height of the target rectangle.
ms.assetid: 032b5468-bce8-4492-abbe-e442131ebe3a
title: IDxtCompositor::put_Height method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtCompositor.put_Height
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtCompositor::put\_Height method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_Height` method specifies the height of the target rectangle.

## Syntax


```C++
HRESULT put_Height(
  [in] long newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

The height of the target rectangle, in pixels.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IDxtCompositor Interface**](idxtcompositor.md)
</dt> </dl>

 

 




