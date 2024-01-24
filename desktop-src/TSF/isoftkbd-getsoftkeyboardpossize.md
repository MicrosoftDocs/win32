---
title: ISoftKbd GetSoftKeyboardPosSize method (Softkbdc.h)
description: The ISoftKbd GetSoftKeyboardPosSize method retrieves the starting position and size of a soft keyboard.
ms.assetid: d4482e34-1723-4fe2-a488-e7c18eb3f68e
keywords:
- GetSoftKeyboardPosSize method Text Services Framework
- GetSoftKeyboardPosSize method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , GetSoftKeyboardPosSize method
topic_type:
- apiref
api_name:
- ISoftKbd.GetSoftKeyboardPosSize
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::GetSoftKeyboardPosSize method

The **ISoftKbd::GetSoftKeyboardPosSize** method retrieves the starting position and size of a soft keyboard.

## Syntax


```C++
HRESULT GetSoftKeyboardPosSize(
  [out] POINT *lpStartPoint,
  [out] WORD  *lpwidth,
  [out] WORD  *lpheight
);
```



## Parameters

<dl> <dt>

*lpStartPoint* \[out\]
</dt> <dd>

Pointer to a buffer in which this method retrieves a [POINT](/windows/win32/api/windef/ns-windef-point) structure indicating the coordinates of the upper left position of the soft keyboard.

</dd> <dt>

*lpwidth* \[out\]
</dt> <dd>

Pointer to a buffer in which this method retrieves the width of the soft keyboard.

</dd> <dt>

*lpheight* \[out\]
</dt> <dd>

Pointer to a buffer in which this method retrieves the height of the soft keyboard.

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

[**ISoftKbd::SetSoftKeyboardPosSize**](isoftkbd-setsoftkeyboardpossize.md)
</dt> </dl>

 

