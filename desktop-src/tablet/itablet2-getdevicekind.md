---
description: Returns the type of hardware device the tablet object represents such as mouse, pen or touch.
ms.assetid: 693cb45f-958d-42e2-a3ee-a7cfcc72e5c3
title: ITablet2::GetDeviceKind method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITablet2.GetDeviceKind
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITablet2::GetDeviceKind method

Returns the type of hardware device the tablet object represents such as mouse, pen or touch.

## Syntax


```C++
HRESULT GetDeviceKind(
  [out] TABLET_DEVICE_KIND *pKind
);
```



## Parameters

<dl> <dt>

*pKind* \[out\]
</dt> <dd>

Enumeration value that indicates the type of tablet such as mouse, pen or touch.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

This interface and method were introduced in Windows Vista.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITablet2 Interface**](itablet2.md)
</dt> <dt>

[**TABLET\_DEVICE\_KIND Enumeration**](tablet-device-kind.md)
</dt> <dt>

[**ITablet Interface**](itablet.md)
</dt> </dl>

 

 




