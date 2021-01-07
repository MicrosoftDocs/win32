---
description: Retrieves the stylus identifier.
ms.assetid: 27320a2f-1e4a-4d7d-a1f8-5244f4a03415
title: ITabletCursor::GetId method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletCursor.GetId
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletCursor::GetId method

Retrieves the stylus identifier.

## Syntax


```C++
HRESULT GetId(
  [out] CURSOR_ID *pCid
);
```



## Parameters

<dl> <dt>

*pCid* \[out\]
</dt> <dd>

The identifier of the tablet stylus.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

CURSOR\_ID is defined as a DWORD.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITabletCursor Interface**](itabletcursor.md)
</dt> </dl>

 

 




