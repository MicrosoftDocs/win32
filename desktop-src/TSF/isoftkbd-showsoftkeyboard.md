---
title: ISoftKbd ShowSoftKeyboard method (Softkbdc.h)
description: The ISoftKbd ShowSoftKeyboard method displays a soft keyboard.
ms.assetid: 7e24bef1-accb-40f6-a549-fb676abf9971
keywords:
- ShowSoftKeyboard method Text Services Framework
- ShowSoftKeyboard method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , ShowSoftKeyboard method
topic_type:
- apiref
api_name:
- ISoftKbd.ShowSoftKeyboard
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::ShowSoftKeyboard method

The **ISoftKbd::ShowSoftKeyboard** method displays a soft keyboard.

## Syntax


```C++
HRESULT ShowSoftKeyboard(
  [in] INT iShow
);
```



## Parameters

<dl> <dt>

*iShow* \[in\]
</dt> <dd>

Integer indicating the type of soft keyboard to display.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                | Description                           |
|--------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method was successful.<br/> |



 

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

 

 





