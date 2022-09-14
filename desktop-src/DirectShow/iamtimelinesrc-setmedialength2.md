---
description: The SetMediaLength2 method specifies the duration of the source file. This method is equivalent to IAMTimelineSrc::SetMediaLength, but takes a REFTIME value.
ms.assetid: 1a1dcf23-2041-4791-bce7-0ecbe33df592
title: IAMTimelineSrc::SetMediaLength2 method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.SetMediaLength2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::SetMediaLength2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetMediaLength2` method specifies the duration of the source file. This method is equivalent to [**IAMTimelineSrc::SetMediaLength**](iamtimelinesrc-setmedialength.md), but takes a [**REFTIME**](reftime.md) value.

## Syntax


```C++
HRESULT SetMediaLength2(
   REFTIME Length
);
```



## Parameters

<dl> <dt>

*Length* 
</dt> <dd>

Media length, in seconds.

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

 

 




