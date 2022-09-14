---
description: Returns a value that represents the capabilities of the tablet hardware.
ms.assetid: 68936dab-3df4-42c4-9945-bcd525c996f3
title: ITablet::GetHardwareCaps method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITablet.GetHardwareCaps
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITablet::GetHardwareCaps method

Returns a value that represents the capabilities of the tablet hardware.

## Syntax


```C++
HRESULT GetHardwareCaps(
  [out] DWORD *pdwCaps
);
```



## Parameters

<dl> <dt>

*pdwCaps* \[out\]
</dt> <dd>

Bit flags that represent the capabilities of the tablet hardware.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

The *pdwCaps* parameter is a set of bit flags that describe tablet hardware capabilities. The following table describes these flags.



| Flag Name                         | Value                 | Description                                                                                                                    |
|-----------------------------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------|
| THWC\_INTEGRATED<br/>       | 0x00000001<br/> | Indicates that the display and digitizer share the same surface.<br/>                                                    |
| THWC\_CSR\_MUST\_TOUCH<br/> | 0x00000002<br/> | Indicates that the cursor must be in physical contact with the device to report position.<br/>                           |
| THWC\_HARD\_PROXIMITY<br/>  | 0x00000004<br/> | Indicates that the device can generate events when the cursor is entering and leaving the physical detection range.<br/> |
| THWC\_PHYSID\_CSRS<br/>     | 0x00000008<br/> | Indicates that the device can uniquely identify the active cursor in hardware.<br/>                                      |



 

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

 

 




