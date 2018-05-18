---
Description: 'Used to determine whether to show the Share this folder option in web view.'
title: CanShareFolderW function
---

# CanShareFolderW function

\[This function is available through Windows XP with Service Pack 2 (SP2) and Windows Server 2003. It might be altered or unavailable in subsequent versions of Windows.\]

Used to determine whether to show the **Share this folder** option in web view.

## Syntax


```C++
STDAPI CanShareFolderW(
  _In_ LPCWSTR pszPath
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a string that specifies the path of the folder to test.

</dd> </dl>

## Return value

Type: **STDAPI**

Return values include the following.



| Return code/value                                                                        | Description                                                                           |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>     | The path pointed to by *pszPath* specifies a folder that can be shared.<br/>    |
| <dl> <dt>**S\_FALSE**</dt> </dl>  | The path pointed to by *pszPath* specifies a folder that cannot be shared.<br/> |
| <dl> <dt>HRESULT error</dt> </dl> | An error has occurred.<br/>                                                     |



 

## Remarks

This function has no associated .lib file. You must use [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) to use it.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Ntshrui.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **CanShareFolderW** (Unicode)<br/>                                               |



## See also

<dl> <dt>

[**ShowShareFolderUI**](shell.showsharefolderui)
</dt> </dl>

 

 




