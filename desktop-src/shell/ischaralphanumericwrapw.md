---
Description: Determines whether a character is either an alphabetical or a numeric character.
ms.assetid: d4b01ba5-e42a-4040-a763-ecef0c73977f
title: IsCharAlphaNumericWrapW function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IsCharAlphaNumericWrapW function

\[**IsCharAlphaNumericWrapW** is available for use in Windows XP. It will not be available in subsequent versions. You should use [**IsCharAlphaNumericW**](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\resources\strings\stringreference\stringfunctions\ischaralphanumeric.htm) in its place.\]

Determines whether a character is either an alphabetical or a numeric character. This determination is based on the semantics of the language selected by the user during setup or through Control Panel.

> [!Note]  
> **IsCharAlphaNumericWrapW** is a wrapper for the **IsCharAlphaNumericW** function. See the [**IsCharAlphaNumeric**](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\resources\strings\stringreference\stringfunctions\ischaralphanumeric.htm) page for further usage notes.

 

## Syntax


```C++
BOOL IsCharAlphaNumericWrapW(
  _In_ WCHAR ch
);
```



## Parameters

<dl> <dt>

*ch* \[in\]
</dt> <dd>

Type: **WCHAR**

The Unicode character to be tested.

</dd> </dl>

## Return value

Type: **BOOL**

If the character is alphanumeric, the return value is nonzero.

If the character is not alphanumeric, the return value is zero. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/d852e148-985c-416f-a5a7-27b6914b45d4).

## Remarks

**IsCharAlphaNumericWrapW** provides the ability to use Unicode strings in operating systems earlier than Windows XP. The preferred method is to use [**IsCharAlphaNumericW**](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\resources\strings\stringreference\stringfunctions\ischaralphanumeric.htm) in conjunction with the Microsoft Layer for Unicode (MSLU).

**IsCharAlphaNumericWrapW** must be called directly from Shlwapi.dll, using ordinal 28.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shlwapi.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IsCharAlphaNumeric**](https://msdn.microsoft.com/VS|winui|~\winui\windowsuserinterface\resources\strings\stringreference\stringfunctions\ischaralphanumeric.htm)
</dt> </dl>

 

 




