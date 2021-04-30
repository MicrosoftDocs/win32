---
description: Retrieves a rectangle that represents maximum input area of the tablet.
ms.assetid: 98facd24-b019-40d1-afe1-28c9a78cae80
title: ITablet::GetMaxInputRect method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITablet.GetMaxInputRect
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITablet::GetMaxInputRect method

Retrieves a rectangle that represents maximum input area of the tablet.

## Syntax


```C++
HRESULT GetMaxInputRect(
  [out] RECT *prcInput
);
```



## Parameters

<dl> <dt>

*prcInput* \[out\]
</dt> <dd>

Pointer to rectangle that represents maximum input area of the tablet.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

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

 

 




