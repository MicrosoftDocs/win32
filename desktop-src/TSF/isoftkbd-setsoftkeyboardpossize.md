---
title: ISoftKbd SetSoftKeyboardPosSize method (Softkbdc.h)
description: The ISoftKbd SetSoftKeyboardPosSize method sets the starting position and size of a soft keyboard.
ms.assetid: bf827b07-0e8b-4d5a-8178-45d75af83551
keywords:
- SetSoftKeyboardPosSize method Text Services Framework
- SetSoftKeyboardPosSize method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , SetSoftKeyboardPosSize method
topic_type:
- apiref
api_name:
- ISoftKbd.SetSoftKeyboardPosSize
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::SetSoftKeyboardPosSize method

The **ISoftKbd::SetSoftKeyboardPosSize** method sets the starting position and size of a soft keyboard.

## Syntax


```C++
HRESULT SetSoftKeyboardPosSize(
  [in] POINT StartPoint,
  [in] WORD  width,
  [in] WORD  height
);
```



## Parameters

<dl> <dt>

*StartPoint* \[in\]
</dt> <dd>

A [POINT](/windows/win32/api/windef/ns-windef-point) structure indicating the coordinates of the upper left position of the soft keyboard.

</dd> <dt>

*width* \[in\]
</dt> <dd>

Width of the soft keyboard.

</dd> <dt>

*height* \[in\]
</dt> <dd>

Height of the soft keyboard.

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
</dt> </dl>

 

