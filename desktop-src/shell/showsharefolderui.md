---
Description: Displays the Folder Sharing tab on the properties sheet for the specified folder.
ms.assetid: e622e4bb-eaf7-494f-b2a2-78ba1311a496
title: ShowShareFolderUI function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ShowShareFolderUI function

Displays the **Folder Sharing** tab on the properties sheet for the specified folder.

## Syntax


```C++
HRESULT ShowShareFolderUI(
  _In_ HWND    hwndParent,
  _In_ LPCWSTR pszPath
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **HWND**

A handle to the parent window for the property sheet.

</dd> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a string that specifies the path to the folder that displays its **Folder Sharing** tab.

</dd> </dl>

## Return value

Type: **HRESULT**

This function always returns S\_OK.

## Remarks

This function has no associated .lib file. You must use [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) to use it.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Ntshrui.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **ShowShareFolderUIW** (Unicode)<br/>                                            |



## See also

<dl> <dt>

[**CanShareFolderW**](cansharefolderw.md)
</dt> </dl>

 

 




