---
title: ISoftKbd GetSoftKeyboardColors method
description: The ISoftKbd GetSoftKeyboardColors method retrieves the soft keyboard color corresponding to the supplied color type.
ms.assetid: d59d249c-a1c4-4d6a-add6-632be55a7549
keywords:
- GetSoftKeyboardColors method Text Services Framework
- GetSoftKeyboardColors method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , GetSoftKeyboardColors method
topic_type:
- apiref
api_name:
- ISoftKbd.GetSoftKeyboardColors
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# ISoftKbd::GetSoftKeyboardColors method

The **ISoftKbd::GetSoftKeyboardColors** method retrieves the soft keyboard color corresponding to the supplied color type.

## Syntax


```C++
HRESULT GetSoftKeyboardColors(
  [in]  COLORTYPE colorType,
  [out] COLORREF  *lpColor
);
```



## Parameters

<dl> <dt>

*colorType* \[in\]
</dt> <dd>

A value specifying the color type to retrieve for the soft keyboard. Possible values are defined for the [**COLORTYPE**](colortype.md) enumeration.

</dd> <dt>

*lpColor* \[out\]
</dt> <dd>

Pointer to a buffer in which this method retrieves a 32-bit [**COLORREF**](https://msdn.microsoft.com/library/windows/desktop/dd183449) value specifying an RGB color.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                  |
|----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One of the parameters is invalid.<br/> |



 

## Requirements



|                                     |                                                                                        |
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

[**ISoftKbd::SetSoftKeyboardColors**](https://msdn.microsoft.com/library/windows/desktop/dd369166)
</dt> <dt>

[**COLORTYPE**](colortype.md)
</dt> <dt>

[**COLORREF**](https://msdn.microsoft.com/library/windows/desktop/dd183449)
</dt> </dl>

 

 





