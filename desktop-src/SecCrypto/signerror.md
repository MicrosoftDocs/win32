---
Description: Calls the GetLastError function and converts the return code to an HRESULT.
ms.assetid: 7b8eab85-212b-44bc-9d1b-60587652380d
title: SignError function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SignError
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# SignError function

> \[!Important\]  
> This API is deprecated. Microsoft may remove this API in future releases.

 

The **SignError** function calls the [**GetLastError**](https://msdn.microsoft.com/en-us/library/ms679360(v=VS.85).aspx) function and converts the return code to an **HRESULT**.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
HRESULT WINAPI SignError(void);
```



## Parameters

This function has no parameters.

## Return value

If the method succeeds, it returns **S\_OK**.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



 

 




