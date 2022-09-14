---
title: GetProcessHandleFromHwnd function
description: Retrieves a process handle from a window handle.
ms.assetid: 173579d2-c930-402c-81c7-761b063b5b51
keywords:
- GetProcessHandleFromHwnd function Windows Accessibility
topic_type:
- apiref
api_name:
- GetProcessHandleFromHwnd
api_location:
- Oleacc.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# GetProcessHandleFromHwnd function

Retrieves a process handle from a window handle.

## Syntax


```C++
HANDLE WINAPI GetProcessHandleFromHwnd(
  _In_ HWND hwnd
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

Type: **[**HWND**](/windows/desktop/WinProg/windows-data-types)**

The window handle.

</dd> </dl>

## Return value

Type: **[**HANDLE**](/windows/desktop/WinProg/windows-data-types)**

If successful, returns the handle of the process that owns the window.

If not successful, returns **NULL**.

## Remarks

In previous versions of the operating system, a process could open another process (to access its memory, for example) using [**OpenProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-openprocess). This function succeeds if the caller has appropriate privileges; usually the caller and target process must be the same user.

On Windows Vista, however, [**OpenProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-openprocess) fails in the scenario where the caller has UIAccess, and the target process is elevated. In this case, the owner of the target process is in the Administrators group, but the calling process is running with the restricted token, so does not have membership in this group, and is denied access to the elevated process. If the caller has UIAccess, however, they can use a windows hook to inject code into the target process, and from within the target process, send a handle back to the caller.

**GetProcessHandleFromHwnd** is a convenience function that uses this technique to obtain the handle of the process that owns the specified HWND. Note that it only succeeds in cases where the caller and target process are running as the same user. The returned handle has the following privileges: PROCESS\_DUP\_HANDLE \| PROCESS\_VM\_OPERATION \| PROCESS\_VM\_READ \| PROCESS\_VM\_WRITE \| SYNCHRONIZE. If other privileges are required, it may be necessary to implement the hooking technique explicitly instead of using this function.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Oleacc.dll</dt> </dl> |



 

