---
title: SetPartnerID function
description: Sets the value of the partner ID used for reporting Windows Genuine Advantage (WGA) status.
ms.assetid: 1aad675c-6950-4b1d-addf-ef9577241eb5
keywords:
- SetPartnerID function Windows Genuine
topic_type:
- apiref
api_name:
- SetPartnerID
api_location:
- LegitLib.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetPartnerID function

\[This function is no longer available for use as of Windows 7.\]

Sets the value of the partner ID used for reporting Windows Genuine Advantage (WGA) status.

The **SetPartnerID** function is not declared in a public header and has no associated import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to LegitLib.dll.

## Syntax


```C++
HRESULT __stdcall SetPartnerID(
   int nPartnerID
);
```



## Parameters

<dl> <dt>

*nPartnerID* 
</dt> <dd>

The partner ID to be set.

</dd> </dl>

## Return value

If the method succeeds, it returns **S\_OK**.

If the method fails, it returns an error code. For a list of common error codes, see [Common HRESULT Values](https://msdn.microsoft.com/library/windows/desktop/aa378137).

## Remarks

The Windows Genuine Advantage (WGA) functions are available only on Windows Vista and Windows XP installations that have been validated by clicking **Validate Windows** on [http://www.microsoft.com/genuine](http://go.microsoft.com/fwlink/p/?linkid=157937).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | None supported<br/>                                                               |
| End of client support<br/>    | Windows Vista<br/>                                                                |
| End of server support<br/>    | None supported<br/>                                                               |
| DLL<br/>                      | <dl> <dt>LegitLib.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Genuine Advantage API Functions](windows-genuine-advantage-api-functions.md)
</dt> </dl>

 

 





