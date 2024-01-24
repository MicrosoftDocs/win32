---
description: Updates the tablet digitizer to window location mapping coordinates.
ms.assetid: 2984b87b-620e-4e5d-a3cc-4c3f4c89bae3
title: ITabletContextP::TrackInputRect method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletContextP.TrackInputRect
api_type: 
- COM
api_location: 
- Wisptis.exe
- Wisptis.exe.dll
---

# ITabletContextP::TrackInputRect method

Updates the tablet digitizer to window location mapping coordinates.

## Syntax


```C++
HRESULT TrackInputRect(
  [out] RECT *prcInput
);
```



## Parameters

<dl> <dt>

*prcInput* \[out\]
</dt> <dd>

The new input window rectangle after updating the mapping between the window and digitizer coordinates.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

Call this method anytime the location of the window on the screen changes.

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

 

 




