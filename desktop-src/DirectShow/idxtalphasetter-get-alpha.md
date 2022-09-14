---
description: The get\_Alpha method retrieves the alpha value for the entire image.
ms.assetid: ce891149-e964-4239-aeef-c9f4a8354563
title: IDxtAlphaSetter::get_Alpha method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtAlphaSetter.get_Alpha
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtAlphaSetter::get\_Alpha method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_Alpha` method retrieves the alpha value for the entire image.

## Syntax


```C++
HRESULT get_Alpha(
  [out, retval] long *pAlpha
);
```



## Parameters

<dl> <dt>

*pAlpha* \[out, retval\]
</dt> <dd>

Receives the alpha value. This alpha value will be applied to the entire target image. A negative value indicates that no alpha value is set.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                               | Description                          |
|-------------------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | Success<br/>                   |



 

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

[**IDxtAlphaSetter Interface**](idxtalphasetter.md)
</dt> </dl>

 

 




