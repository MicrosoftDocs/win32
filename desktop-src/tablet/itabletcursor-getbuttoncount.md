---
description: Retrieves the number of buttons on the tablet stylus.
ms.assetid: ae4ce670-769a-4f00-b728-285020f09934
title: ITabletCursor::GetButtonCount method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletCursor.GetButtonCount
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletCursor::GetButtonCount method

Retrieves the number of buttons on the tablet stylus.

## Syntax


```C++
HRESULT GetButtonCount(
  [out] ULONG *pcButtons
);
```



## Parameters

<dl> <dt>

*pcButtons* \[out\]
</dt> <dd>

The count of buttons on the tablet stylus.

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

 

 




