---
title: ISoftKbd SetKeyboardLabelTextCombination method (Softkbdc.h)
description: The ISoftKbd SetKeyboardLabelTextCombination method sets a combination of label and text used to describe a soft keyboard.
ms.assetid: fe054eae-1a44-41ad-9a44-bc0b46df7c7b
keywords:
- SetKeyboardLabelTextCombination method Text Services Framework
- SetKeyboardLabelTextCombination method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , SetKeyboardLabelTextCombination method
topic_type:
- apiref
api_name:
- ISoftKbd.SetKeyboardLabelTextCombination
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::SetKeyboardLabelTextCombination method

The **ISoftKbd::SetKeyboardLabelTextCombination** method sets a combination of label and text used to describe a soft keyboard.

## Syntax


```C++
HRESULT SetKeyboardLabelTextCombination(
  [in] DWORD nModifierCombination
);
```



## Parameters

<dl> <dt>

*nModifierCombination* \[in\]
</dt> <dd>

Combination of label and text used to describe the soft keyboard.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                                 |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *nModifierCombination* parameter is invalid.<br/> |



 

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

[**ISoftKbd::SetKeyboardLabelText**](isoftkbd-setkeyboardlabeltext.md)
</dt> </dl>

 

 





