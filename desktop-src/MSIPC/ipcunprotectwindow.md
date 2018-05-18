---
title: IpcUnprotectWindow function
description: Removes the protection from a window protected using IpcProtectWindow.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'FC84133C-52B8-4A63-8F0D-9B1762742C3F'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IpcUnprotectWindow function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IpcUnprotectWindow
api_location:
- Msipc.dll
api_type:
- DllExport
---

# IpcUnprotectWindow function

Removes the protection from a window protected using [**IpcProtectWindow**](ipcprotectwindow.md).

## Syntax


```C++
HRESULT WINAPI IpcUnprotectWindow(
  _In_ HWND     hwnd
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

The window to unprotect.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Remarks

To ensure that your application works with current and future versions of the RMS SDK 2.1, you should use the following code to unprotect a window.


```C++
hr = IpcUnprotectWindow(hwnd);
if (FAILED(hr) &amp;&amp; (IPCERROR_PROPERTY_ALREADY_SET != hr)) 
{ 

// Failed to unprotect the window. 
// Your application code must determine whether to treat this condition as fatal. 

} 

else 
{ 
// Success! Continue... 
hr = S_OK;
}
```



## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**IpcProtectWindow**](ipcprotectwindow.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





