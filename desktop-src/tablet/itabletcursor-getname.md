---
description: Retrieves the name of the tablet stylus.
ms.assetid: 94955c04-f699-428b-b4bf-53919b61b1ab
title: ITabletCursor::GetName method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletCursor.GetName
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletCursor::GetName method

Retrieves the name of the tablet stylus.

## Syntax


```C++
HRESULT GetName(
  [out] LPWSTR *ppwszName
);
```



## Parameters

<dl> <dt>

*ppwszName* \[out\]
</dt> <dd>

The name of the tablet stylus.

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

[**ITabletCursor**](itabletcursor.md)
</dt> <dt>

[**ITabletCursorButton Interface**](itabletcursorbutton.md)
</dt> </dl>

 

