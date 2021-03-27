---
description: The put\_ReplicateX method specifies the number of times the wipe pattern is replicated horizontally.
ms.assetid: 8baa641c-c063-4c22-8b00-3559c173d627
title: IDxtJpeg::put_ReplicateX method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtJpeg.put_ReplicateX
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtJpeg::put\_ReplicateX method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_ReplicateX` method specifies the number of times the wipe pattern is replicated horizontally.

## Syntax


```C++
HRESULT put_ReplicateX(
  [in] long newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

The number of times the wipe pattern is replicated horizontally.

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

[**IDxtJpeg Interface**](idxtjpeg.md)
</dt> </dl>

 

 




