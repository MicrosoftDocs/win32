---
description: Retrieves the unique identifier of the stylus button.
ms.assetid: 06bd6a84-46cd-4c62-92d6-50caae359e43
title: ITabletCursorButton::GetGuid method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletCursorButton.GetGuid
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletCursorButton::GetGuid method

Retrieves the unique identifier of the stylus button.

## Syntax


```C++
HRESULT GetGuid(
  [out] GUID *pguidBtn
);
```



## Parameters

<dl> <dt>

*pguidBtn* \[out\]
</dt> <dd>

A unique value that identifies the stylus button.

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

[**ITabletCursorButton Interface**](itabletcursorbutton.md)
</dt> </dl>

 

 




