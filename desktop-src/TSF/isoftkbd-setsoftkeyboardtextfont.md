---
title: ISoftKbd SetSoftKeyboardTextFont method
description: The ISoftKbd SetSoftKeyboardTextFont method sets the text font used by a soft keyboard.
ms.assetid: '14705723-4592-40ef-9ebb-1c44c10c3cda'
keywords: ["SetSoftKeyboardTextFont method Text Services Framework", "SetSoftKeyboardTextFont method Text Services Framework , ISoftKbd interface", "ISoftKbd interface Text Services Framework , SetSoftKeyboardTextFont method"]
topic_type:
- apiref
api_name:
- ISoftKbd.SetSoftKeyboardTextFont
api_location:
- Softkbd.dll
api_type:
- COM
---

# ISoftKbd::SetSoftKeyboardTextFont method

The **ISoftKbd::SetSoftKeyboardTextFont** method sets the text font used by a soft keyboard.

## Syntax


```C++
HRESULT SetSoftKeyboardTextFont(
  [in] LOGFONTW *pLogFont
);
```



## Parameters

<dl> <dt>

*pLogFont* \[in\]
</dt> <dd>

Pointer to a [**LOGFONTW**](https://msdn.microsoft.com/library/windows/desktop/dd145037) structure defining the text font for the soft keyboard.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                     |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *pLogFont* parameter is invalid.<br/> |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Softkbd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ISoftKbd**](isoftkbd.md)
</dt> <dt>

[**ISoftKbd::GetSoftKeyboardTextFont**](isoftkbd-getsoftkeyboardtextfont.md)
</dt> </dl>

 

 





