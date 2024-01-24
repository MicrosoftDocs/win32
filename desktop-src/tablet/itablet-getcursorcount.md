---
description: Returns the number of cursor objects associated with the tablet.
ms.assetid: 7aa5802c-1255-41a4-b1fa-23e5f56c0b80
title: ITablet::GetCursorCount method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITablet.GetCursorCount
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITablet::GetCursorCount method

Returns the number of cursor objects associated with the tablet.

## Syntax


```C++
HRESULT GetCursorCount(
  [out] ULONG *pcCurs
);
```



## Parameters

<dl> <dt>

*pcCurs* \[out\]
</dt> <dd>

The number of cursor objects associated with the tablet.

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

 

 




