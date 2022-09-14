---
description: The get\_MaskNum method retrieves the SMPTE wipe code of the wipe.
ms.assetid: 49710d40-acc0-453e-ac9c-882794a0b82d
title: IDxtJpeg::get_MaskNum method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtJpeg.get_MaskNum
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtJpeg::get\_MaskNum method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_MaskNum` method retrieves the SMPTE wipe code of the wipe.

## Syntax


```C++
HRESULT get_MaskNum(
  [out, retval] long *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives the SMPTE wipe code. For a list of supported SMPTE wipes, see [SMPTE Wipe Transition](smpte-wipe-transition.md).

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

 

 




