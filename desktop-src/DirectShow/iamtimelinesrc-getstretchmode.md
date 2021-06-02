---
description: The GetStretchMode method retrieves the stretch mode. The stretch mode determines how a video source is rendered if its size does not match the output dimensions.
ms.assetid: d9a3d283-edb5-40be-b877-69cb23462afa
title: IAMTimelineSrc::GetStretchMode method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.GetStretchMode
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::GetStretchMode method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetStretchMode` method retrieves the stretch mode. The stretch mode determines how a video source is rendered if its size does not match the output dimensions.

## Syntax


```C++
HRESULT GetStretchMode(
   int *pnStretchMode
);
```



## Parameters

<dl> <dt>

*pnStretchMode* 
</dt> <dd>

Receives a flag indicating the current stretch mode. For a list of possible values, see [**Resize Flags**](resize-flags.md).

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

[**IAMTimelineSrc Interface**](iamtimelinesrc.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




