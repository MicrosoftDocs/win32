---
description: The get\_KeyType method retrieves the type of key.
ms.assetid: 902cbd46-529a-45d8-afa2-a8dd9439769a
title: IDxtKey::get_KeyType method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtKey.get_KeyType
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtKey::get\_KeyType method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_KeyType` method retrieves the type of key.

## Syntax


```C++
HRESULT get_KeyType(
  [out, retval] int *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives one of the following enumeration values.



| Value             | Description                                           |
|-------------------|-------------------------------------------------------|
| DXTKEY\_RGB       | Chroma key. (Key on RGB value.)                       |
| DXTKEY\_NONRED    | Nonred key. (Makes blue and green areas transparent.) |
| DXTKEY\_LUMINANCE | Luminance key.                                        |
| DXTKEY\_ALPHA     | Key by alpha value.                                   |
| DXTKEY\_HUE       | Key by hue.                                           |



 

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

[**IDxtKey Interface**](idxtkey.md)
</dt> </dl>

 

 




