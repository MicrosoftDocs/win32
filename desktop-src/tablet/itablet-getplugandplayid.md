---
description: Returns a string containing the Plug and Play ID for the tablet device.
ms.assetid: a0b6619b-f80c-470b-aa3f-f0b30a9dbda8
title: ITablet::GetPlugAndPlayId method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITablet.GetPlugAndPlayId
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITablet::GetPlugAndPlayId method

Returns a string containing the Plug and Play ID for the tablet device.

## Syntax


```C++
HRESULT GetPlugAndPlayId(
  [out] LPWSTR *ppwszPPId
);
```



## Parameters

<dl> <dt>

*ppwszPPId* \[out\]
</dt> <dd>

Pointer to a string containing the Plug and Play ID for the tablet device.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

It is the caller's responsibility to free the memory returned from this method by using [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITablet Interface**](itablet.md)
</dt> </dl>

 

