---
description: The get\_InputSize method returns the resizer filter's current input size.
ms.assetid: 7066a044-52ea-4851-83f2-f1fb323c2251
title: IResize::get_InputSize method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IResize.get_InputSize
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IResize::get\_InputSize method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_InputSize` method returns the resizer filter's current input size.

## Syntax


```C++
HRESULT get_InputSize(
  [out] int *piHeight,
  [out] int *piWidth
);
```



## Parameters

<dl> <dt>

*piHeight* \[out\]
</dt> <dd>

Receives the video height, in pixels.

</dd> <dt>

*piWidth* \[out\]
</dt> <dd>

Receives the video width, in pixels.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the filter's input pin is not connected, return an error code. Otherwise, return the width and height of the video, as specified by the input pin's media type.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | DirectX 9.0 or later<br/>                                                         |
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**IResize Interface**](iresize.md)
</dt> </dl>

 

 




