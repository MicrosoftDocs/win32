---
title: ISoftKbd GetSoftKeyboardTextFont method
description: The ISoftKbd GetSoftKeyboardTextFont method retrieves the text font used by a soft keyboard.
ms.assetid: 73239359-70b4-47d6-abc5-9fee279ed3a6
keywords:
- GetSoftKeyboardTextFont method Text Services Framework
- GetSoftKeyboardTextFont method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , GetSoftKeyboardTextFont method
topic_type:
- apiref
api_name:
- ISoftKbd.GetSoftKeyboardTextFont
api_location:
- Softkbd.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISoftKbd::GetSoftKeyboardTextFont method

The **ISoftKbd::GetSoftKeyboardTextFont** method retrieves the text font used by a soft keyboard.

## Syntax


```C++
HRESULT GetSoftKeyboardTextFont(
  [out] LOGFONTW *pLogFont
);
```



## Parameters

<dl> <dt>

*pLogFont* \[out\]
</dt> <dd>

Pointer to a buffer in which this method retrieves a [**LOGFONTW**](https://msdn.microsoft.com/library/windows/desktop/dd145037) structure defining the text font for the soft keyboard.

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

[**ISoftKbd::SetSoftKeyboardTextFont**](isoftkbd-setsoftkeyboardtextfont.md)
</dt> </dl>

 

 





