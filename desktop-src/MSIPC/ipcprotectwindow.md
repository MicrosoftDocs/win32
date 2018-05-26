---
title: IpcProtectWindow function
description: Protects a window by using mechanisms available on the current operating system.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: E77A7A5D-0516-4300-A8EE-5BDE22F61897
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcProtectWindow function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcProtectWindow
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcProtectWindow function

Protects a window by using mechanisms available on the current operating system.

## Syntax


```C++
HRESULT WINAPI IpcProtectWindow(
  _In_ HWND     hwnd
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

The window to protect.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an *HRESULT* value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Remarks

Typically, you will call **IpcProtectWindow** when your application is loading an RMS-protected document. If the user does not have rights to copy/paste the protected content hosted within a window, you need to call **IpcProtectWindow** on this window. If this call fails, you cannot display the protected content securely, and you should treat this as a failure to load the document, presenting an appropriate error message to the user.

To ensure that your application works with current and future versions of the AD RMS SDK, you should use the following code to protect a window.


```C++
hr = IpcProtectWindow(hwnd);
if (FAILED(hr) &amp;&amp; (IPCERROR_PROPERTY_ALREADY_SET != hr))
{
  // Fail to load document
}
else
{
  // Success!  Continue...
hr = S_OK;
}
```



## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**IpcUnprotectWindow**](ipcunprotectwindow.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





