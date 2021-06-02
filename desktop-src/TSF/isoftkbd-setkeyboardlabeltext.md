---
title: ISoftKbd SetKeyboardLabelText method (Softkbdc.h)
description: The ISoftKbd SetKeyboardLabelText method sets the label text from the layout for a soft keyboard.
ms.assetid: 86c45c37-fe50-4596-b4c9-960de760a2e0
keywords:
- SetKeyboardLabelText method Text Services Framework
- SetKeyboardLabelText method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , SetKeyboardLabelText method
topic_type:
- apiref
api_name:
- ISoftKbd.SetKeyboardLabelText
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::SetKeyboardLabelText method

The **ISoftKbd::SetKeyboardLabelText** method sets the label text from the layout for a soft keyboard.

## Syntax


```C++
HRESULT SetKeyboardLabelText(
  [in] HKL hKl
);
```



## Parameters

<dl> <dt>

*hKl* \[in\]
</dt> <dd>

Handle that is used to retrieve the installed layout for the soft keyboard.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                |
|----------------------------------------------------------------------------------------------|--------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *hKl* parameter is invalid.<br/> |



 

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

[**ISoftKbd::SetKeyboardLabelTextCombination**](isoftkbd-setkeyboardlabeltextcombination.md)
</dt> </dl>

 

 





