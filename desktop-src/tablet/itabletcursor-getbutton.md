---
description: Retrieves the specified button object from a tablet stylus.
ms.assetid: 83a26703-4501-4f43-9e86-c5c753347012
title: ITabletCursor::GetButton method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletCursor.GetButton
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletCursor::GetButton method

Retrieves the specified button object from a tablet stylus.

## Syntax


```C++
HRESULT GetButton(
  [in]  ULONG               iButton,
  [out] ITabletCursorButton **ppButton
);
```



## Parameters

<dl> <dt>

*iButton* \[in\]
</dt> <dd>

Identifier of the button to retrieve.

</dd> <dt>

*ppButton* \[out\]
</dt> <dd>

The button object specified by the *iButton* parameter.

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

[**ITabletCursor Interface**](itabletcursor.md)
</dt> </dl>

 

 




