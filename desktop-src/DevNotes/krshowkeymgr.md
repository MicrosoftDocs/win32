---
Description: Brings up the key manager dialog into the user interface.
ms.assetid: 65c2763f-42d5-4534-94f7-e753f6486014
title: KRShowKeyMgr function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# KRShowKeyMgr function

\[This function is included only in Windows XP. It is not currently included in any other version of Windows, nor is it expected to be included in any future versions of Windows.\]

Brings up the key manager dialog into the user interface.

## Syntax


```C++
void KRShowKeyMgr(
   HWND      hwParent,
   HINSTANCE hInstance,
   LPWSTR    pszCmdLine,
   int       CmdShow
);
```



## Parameters

<dl> <dt>

*hwParent* 
</dt> <dd>

A handle to the parent window of the dialog. This parameter can be **NULL**.

</dd> <dt>

*hInstance* 
</dt> <dd>

This parameter is not used and should be set to **NULL**.

</dd> <dt>

*pszCmdLine* 
</dt> <dd>

This parameter is not used and should be set to **NULL**.

</dd> <dt>

*CmdShow* 
</dt> <dd>

This parameter is not used and should be set to **NULL**.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Keymgr.dll</dt> </dl> |



 

 




