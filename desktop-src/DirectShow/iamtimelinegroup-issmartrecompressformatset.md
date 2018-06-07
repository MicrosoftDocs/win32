---
Description: The IsSmartRecompressFormatSet method determines whether a smart recompression format was set for the group.
ms.assetid: d2b7ecc7-2348-402d-8d96-e0922e06a685
title: IAMTimelineGroup::IsSmartRecompressFormatSet method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAMTimelineGroup::IsSmartRecompressFormatSet method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IsSmartRecompressFormatSet` method determines whether a smart recompression format was set for the group.

## Syntax


```C++
HRESULT IsSmartRecompressFormatSet(
   BOOL *pVal
);
```



## Parameters

<dl> <dt>

*pVal* 
</dt> <dd>

Receives a Boolean value indicating whether a compression format was set. If **TRUE**, a compression format was set.

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

[**IAMTimelineGroup Interface**](iamtimelinegroup.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




