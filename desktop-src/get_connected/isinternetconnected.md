---
title: IsInternetConnected function
description: Determines whether the current user is connected to the Internet.
ms.assetid: a83556bc-09a3-4671-9d97-3b86da6d8ccf
keywords:
- IsInternetConnected function Get Connected Wizard API
topic_type:
- apiref
api_name:
- IsInternetConnected
api_location:
- connect.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IsInternetConnected function

The **IsInternetConnected** function determines whether the current user is connected to the Internet.

## Syntax


```C++
HRESULT WINAPI IsInternetConnected(void);
```



## Parameters

This function has no parameters.

## Return value

If the function succeeds, it returns S\_OK or S\_FALSE. The return value S\_OK indicates that the user is connected to the Internet. The return value S\_FALSE indicates that the user is not currently connected to the Internet.

If the function fails, the return value is one of the standard error codes.

## Remarks

This API uses NCSI and the Network Location Manager (NLM) to determine a "best guess" regarding the Internet connectivity of the current user. Even if S\_OK is returned, there is no guarantee that the user will be able to contact a specific Internet address.

An import library containing the **IsInternetConnected** function is not included in the Microsoft Windows Software Development Kit (SDK). Applications must use the [**GetModuleHandle**](https://msdn.microsoft.com/library/windows/desktop/ms683199) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to retrieve the function pointer from the corresponding DLL and call this function.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Connect.dll</dt> </dl> |



 

 





