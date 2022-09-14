---
description: Moves a tablet context to the front or back of the input queue.
ms.assetid: ef4521b5-776b-46dc-864a-625bc221054a
title: ITabletContextP::Overlap method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletContextP.Overlap
api_type: 
- COM
api_location: 
- Wisptis.exe
- Wisptis.exe.dll
---

# ITabletContextP::Overlap method

Moves a tablet context to the front or back of the input queue.

## Syntax


```C++
HRESULT Overlap(
  [in]  BOOL  bTop,
  [out] DWORD *pdwtcid
);
```



## Parameters

<dl> <dt>

*bTop* \[in\]
</dt> <dd>

Indicates if the tablet context should be moved to the top or bottom of the input queue.

</dd> <dt>

*pdwtcid* \[out\]
</dt> <dd>

The tablet context identifier.

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

[**ITabletContextP Interface**](itabletcontextp.md)
</dt> </dl>

 

 




