---
title: ISoftKbd SetSoftKeyboardColors method (Softkbdc.h)
description: The ISoftKbd SetSoftKeyboardColors method sets the soft keyboard color for the specified color type.
ms.assetid: 1abbff35-a5ef-4119-9367-60b6e0961c59
keywords:
- SetSoftKeyboardColors method Text Services Framework
- SetSoftKeyboardColors method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , SetSoftKeyboardColors method
topic_type:
- apiref
api_name:
- ISoftKbd.SetSoftKeyboardColors
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::SetSoftKeyboardColors method

The **ISoftKbd::SetSoftKeyboardColors** method sets the soft keyboard color for the specified color type.

## Syntax


```C++
HRESULT SetSoftKeyboardColors(
  [in] COLORTYPE colorType,
  [in] COLORREF  Color
);
```



## Parameters

<dl> <dt>

*colorType* \[in\]
</dt> <dd>

A value specifying the color type for the soft keyboard. Possible values are defined for the [**COLORTYPE**](/windows/win32/api/icm/ne-icm-colortype) enumeration.

</dd> <dt>

*Color* \[in\]
</dt> <dd>

A 32-bit [**COLORREF**](/windows/desktop/gdi/colorref) value specifying an RGB color.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                  |
|----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One of the parameters is invalid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Softkbd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ISoftKbd**](isoftkbd.md)
</dt> <dt>

[**ISoftKbd::GetSoftKeyboardColors**](isoftkbd-getsoftkeyboardcolors.md)
</dt> <dt>

[**COLORTYPE**](/windows/win32/api/icm/ne-icm-colortype)
</dt> <dt>

[**COLORREF**](/windows/desktop/gdi/colorref)
</dt> </dl>

 

