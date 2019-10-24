---
Description: Performs an operation on a specified file.
ms.assetid: ce652565-40b6-4f69-bd2a-9e05e3f360ac
title: WOWShellExecute function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WOWShellExecute
api_type: 
- DllExport
api_location: 
- Shell32.dll
---

# WOWShellExecute function

\[This function is available through Windows XP with Service Pack 2 (SP2) and Windows Server 2003. It might be altered or unavailable in subsequent versions of Windows.\]

Performs an operation on a specified file. **WOWShellExecute** exists only for use with the Microsoft Windows NT Virtual DOS Machine (Ntvdm.exe), which allows disk operating system (DOS) and 16-bit software to run on a Windows system, and should not be used by anyone else. Use [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea) instead.

## Syntax


```C++
HINSTANCE WOWShellExecute(
  _In_ HWND    hwnd,
  _In_ LPCTSTR lpOperation,
  _In_ LPCTSTR lpFile,
  _In_ LPCTSTR lpParameters,
  _In_ LPCTSTR lpDirectory,
  _In_ INT     nShowCmd,
       void    *lpfnCBWinExec
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

Type: **HWND**

A handle to the owner window used for displaying a UI or error messages. This value can be **NULL** if the operation is not associated with a window.

</dd> <dt>

*lpOperation* \[in\]
</dt> <dd>

Type: **LPCTSTR**

A pointer to a **null**-terminated string, referred to in this case as a *verb*, that specifies the action to be performed. The set of available verbs depends on the particular file or folder. Generally, the actions available from an object's shortcut menu are available verbs. For more information about verbs and their availability, see the *Object Verbs* section of [Launching Applications](launch.md). See [Extending Shortcut Menus](context.md) for further discussion of shortcut menus. The following verbs are commonly used.

<dt>

<span id="edit"></span><span id="EDIT"></span>

<span id="edit"></span><span id="EDIT"></span>**edit**


</dt> <dd>

Launches an editor and opens the document for editing. If *lpFile* is not a document file, the function will fail.

</dd> <dt>

<span id="explore"></span><span id="EXPLORE"></span>

<span id="explore"></span><span id="EXPLORE"></span>**explore**


</dt> <dd>

Explores the folder specified by *lpFile*.

</dd> <dt>

<span id="find"></span><span id="FIND"></span>

<span id="find"></span><span id="FIND"></span>**find**


</dt> <dd>

Initiates a search starting from the specified directory.

</dd> <dt>

<span id="open"></span><span id="OPEN"></span>

<span id="open"></span><span id="OPEN"></span>**open**


</dt> <dd>

Opens the file specified by the *lpFile* parameter. The file can be an executable file, a document file, or a folder.

</dd> <dt>

<span id="print"></span><span id="PRINT"></span>

<span id="print"></span><span id="PRINT"></span>**print**


</dt> <dd>

Prints the document file specified by *lpFile*. If *lpFile* is not a document file, the function will fail.

</dd> <dt>

<span id="NULL"></span><span id="null"></span>

<span id="NULL"></span><span id="null"></span>**NULL**


</dt> <dd>

For systems prior to Windows 2000, the default verb is used if it is valid and available in the registry. If not, the "open" verb is used.

For Windows 2000 and later systems, the default verb is used if available. If not, the "open" verb is used. If neither verb is available, the system uses the first verb listed in the registry.

</dd> </dl> </dd> <dt>

*lpFile* \[in\]
</dt> <dd>

Type: **LPCTSTR**

A pointer to a **null**-terminated string that specifies the file or object on which to execute the specified verb. To specify a Shell namespace object, pass the fully qualified parse name. Note that not all verbs are supported on all objects. For example, not all document types support the "print" verb.

</dd> <dt>

*lpParameters* \[in\]
</dt> <dd>

Type: **LPCTSTR**

If the *lpFile* parameter specifies an executable file, *lpParameters* is a pointer to a **null**-terminated string that specifies the parameters to be passed to the application. The format of this string is determined by the verb that is to be invoked. If *lpFile* specifies a document file, *lpParameters* should be **NULL**.

</dd> <dt>

*lpDirectory* \[in\]
</dt> <dd>

Type: **LPCTSTR**

A pointer to a **null**-terminated string that specifies the default directory.

</dd> <dt>

*nShowCmd* \[in\]
</dt> <dd>

Type: **INT**

The flags that specify how an application is to be displayed when it is opened. If *lpFile* specifies a document file, the flag is simply passed to the associated application. It is up to the application to decide how to handle it.

<dt>

<span id="SW_HIDE"></span><span id="sw_hide"></span>

<span id="SW_HIDE"></span><span id="sw_hide"></span>**SW\_HIDE**


</dt> <dd>

Hides the window and activates another window.

</dd> <dt>

<span id="SW_MAXIMIZE"></span><span id="sw_maximize"></span>

<span id="SW_MAXIMIZE"></span><span id="sw_maximize"></span>**SW\_MAXIMIZE**


</dt> <dd>

Maximizes the specified window.

</dd> <dt>

<span id="SW_MINIMIZE"></span><span id="sw_minimize"></span>

<span id="SW_MINIMIZE"></span><span id="sw_minimize"></span>**SW\_MINIMIZE**


</dt> <dd>

Minimizes the specified window and activates the next top-level window in the z-order.

</dd> <dt>

<span id="SW_RESTORE"></span><span id="sw_restore"></span>

<span id="SW_RESTORE"></span><span id="sw_restore"></span>**SW\_RESTORE**


</dt> <dd>

Activates and displays the window. If the window is minimized or maximized, Windows restores it to its original size and position. An application should specify this flag when restoring a minimized window.

</dd> <dt>

<span id="SW_SHOW"></span><span id="sw_show"></span>

<span id="SW_SHOW"></span><span id="sw_show"></span>**SW\_SHOW**


</dt> <dd>

Activates the window and displays it in its current size and position.

</dd> <dt>

<span id="SW_SHOWDEFAULT"></span><span id="sw_showdefault"></span>

<span id="SW_SHOWDEFAULT"></span><span id="sw_showdefault"></span>**SW\_SHOWDEFAULT**


</dt> <dd>

Sets the show state based on the SW\_ flag specified in the [**STARTUPINFO**](https://msdn.microsoft.com/en-us/library/ms686331(v=VS.85).aspx) structure passed to the [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) function by the program that started the application. An application should call [**ShowWindow**](https://msdn.microsoft.com/en-us/library/ms633548(v=VS.85).aspx) with this flag to set the initial show state of its main window.

</dd> <dt>

<span id="SW_SHOWMAXIMIZED"></span><span id="sw_showmaximized"></span>

<span id="SW_SHOWMAXIMIZED"></span><span id="sw_showmaximized"></span>**SW\_SHOWMAXIMIZED**


</dt> <dd>

Activates the window and displays it as a maximized window.

</dd> <dt>

<span id="SW_SHOWMINIMIZED"></span><span id="sw_showminimized"></span>

<span id="SW_SHOWMINIMIZED"></span><span id="sw_showminimized"></span>**SW\_SHOWMINIMIZED**


</dt> <dd>

Activates the window and displays it as a minimized window.

</dd> <dt>

<span id="SW_SHOWMINNOACTIVE"></span><span id="sw_showminnoactive"></span>

<span id="SW_SHOWMINNOACTIVE"></span><span id="sw_showminnoactive"></span>**SW\_SHOWMINNOACTIVE**


</dt> <dd>

Displays the window as a minimized window. The active window remains active.

</dd> <dt>

<span id="SW_SHOWNA"></span><span id="sw_showna"></span>

<span id="SW_SHOWNA"></span><span id="sw_showna"></span>**SW\_SHOWNA**


</dt> <dd>

Displays the window in its current state. The active window remains active.

</dd> <dt>

<span id="SW_SHOWNOACTIVATE"></span><span id="sw_shownoactivate"></span>

<span id="SW_SHOWNOACTIVATE"></span><span id="sw_shownoactivate"></span>**SW\_SHOWNOACTIVATE**


</dt> <dd>

Displays a window in its most recent size and position. The active window remains active.

</dd> <dt>

<span id="SW_SHOWNORMAL"></span><span id="sw_shownormal"></span>

<span id="SW_SHOWNORMAL"></span><span id="sw_shownormal"></span>**SW\_SHOWNORMAL**


</dt> <dd>

Activates and displays a window. If the window is minimized or maximized, Windows restores it to its original size and position. An application should specify this flag when displaying the window for the first time.

</dd> </dl> </dd> <dt>

*lpfnCBWinExec* 
</dt> <dd>

Type: **void\***

Callback function used to call [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) in the 16-bit kernel.

</dd> </dl>

## Return value

Type: **HINSTANCE**

Returns a value greater than 32 if successful, or an error value that is less than or equal to 32 otherwise. The following table lists the error values. The return value is cast as an HINSTANCE for backward compatibility with 16-bit Windows applications. It is not a true HINSTANCE, however. The only thing that can be done with the returned HINSTANCE is to cast it to an **int** and compare it with the value 32 or one of the error codes below.



| Return code                                                                                             | Description                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl>                        | The operating system is out of memory or resources.<br/>                                                                                                           |
| <dl> <dt>**ERROR\_FILE\_NOT\_FOUND**</dt> </dl>  | The specified file was not found.<br/>                                                                                                                             |
| <dl> <dt>**ERROR\_PATH\_NOT\_FOUND**</dt> </dl>  | The specified path was not found.<br/>                                                                                                                             |
| <dl> <dt>**ERROR\_BAD\_FORMAT**</dt> </dl>       | The .exe file is invalid (non-Win32 .exe or error in .exe image).<br/>                                                                                             |
| <dl> <dt>**SE\_ERR\_ACCESSDENIED**</dt> </dl>    | The operating system denied access to the specified file.<br/>                                                                                                     |
| <dl> <dt>**SE\_ERR\_ASSOCINCOMPLETE**</dt> </dl> | The file name association is incomplete or invalid.<br/>                                                                                                           |
| <dl> <dt>**SE\_ERR\_DDEBUSY**</dt> </dl>         | The DDE transaction could not be completed because other DDE transactions were being processed.<br/>                                                               |
| <dl> <dt>**SE\_ERR\_DDEFAIL**</dt> </dl>         | The DDE transaction failed.<br/>                                                                                                                                   |
| <dl> <dt>**SE\_ERR\_DDETIMEOUT**</dt> </dl>      | The DDE transaction could not be completed because the request timed out.<br/>                                                                                     |
| <dl> <dt>**SE\_ERR\_DLLNOTFOUND**</dt> </dl>     | The specified DLL was not found.<br/>                                                                                                                              |
| <dl> <dt>**SE\_ERR\_FNF**</dt> </dl>             | The specified file was not found.<br/>                                                                                                                             |
| <dl> <dt>**SE\_ERR\_NOASSOC**</dt> </dl>         | There is no application associated with the given file name extension. This error will also be returned if you attempt to print a file that is not printable.<br/> |
| <dl> <dt>**SE\_ERR\_OOM**</dt> </dl>             | There was not enough memory to complete the operation.<br/>                                                                                                        |
| <dl> <dt>**SE\_ERR\_PNF**</dt> </dl>             | The specified path was not found.<br/>                                                                                                                             |
| <dl> <dt>**SE\_ERR\_SHARE**</dt> </dl>           | A sharing violation occurred.<br/>                                                                                                                                 |



 

## Remarks

**WOWShellExecute** is not included in a header or .lib file. It is exported from Shell32.dll by name.

This method allows you to execute any commands in a folder's shortcut menu or stored in the registry.

If *lpOperation* is **NULL**, the function opens the file specified by *lpFile*. If *lpOperation* is "open" or "explore", the function attempts to open or explore the folder.

To obtain information about the application that is launched as a result of calling **WOWShellExecute**, use [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa).

> [!Note]  
> The **Launch folder windows in a separate process** setting in Folder Options affects **WOWShellExecute**. If that option is disabled (the default setting), **WOWShellExecute** uses an open Explorer window rather than launch a new one. If no Explorer window is open, **WOWShellExecute** launches a new one.

 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



## See also

<dl> <dt>

[**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea)
</dt> </dl>

 

 




