---
description: Indicates if the stylus is upside down.
ms.assetid: 04b05287-000d-455f-88e5-821c7fdb8119
title: ITabletCursor::IsInverted method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletCursor.IsInverted
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletCursor::IsInverted method

Indicates if the stylus is upside down.

## Syntax


```C++
HRESULT IsInverted();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                             | Description                               |
|-----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | The stylus is inverted.<br/>        |
| <dl> <dt>**S\_FALSE**</dt> </dl> | The stylus is not inverted.<br/>    |
| <dl> <dt>**E\_FAIL**</dt> </dl>  | An unspecified error occurred.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITabletCursor**](itabletcursor.md)
</dt> <dt>

[**ITabletCursorButton Interface**](itabletcursorbutton.md)
</dt> </dl>

 

 




