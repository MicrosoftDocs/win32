---
description: Starts Windows Help (Winhelp.exe) and passes additional data that indicates the nature of the help requested by the application.
ms.assetid: e7466832-f236-4567-b05d-37d25fe88ba2
title: MLWinHelp function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MLWinHelp
- MLWinHelpA
- MLWinHelpW
api_type: 
- DllExport
api_location: 
- Shlwapi.dll
---

# MLWinHelp function

\[This function is available through Windows XP and Windows Server 2003. It might be altered or unavailable in subsequent versions of Windows.\]

Starts Windows Help (Winhelp.exe) and passes additional data that indicates the nature of the help requested by the application.

## Syntax


```C++
BOOL MLWinHelp(
  _In_ HWND      hWndMain,
  _In_ LPCTSTR   lpszHelp,
  _In_ UINT      uCommand,
  _In_ DWORD_PTR dwData
);
```



## Parameters

<dl> <dt>

*hWndMain* \[in\]
</dt> <dd>

Type: **HWND**

A handle to the window requesting help. The **MLWinHelp** function uses this handle to keep track of which applications have requested help. If the *uCommand* parameter specifies HELP\_CONTEXTMENU or HELP\_WM\_HELP, *hWndMain* identifies the control requesting help.

</dd> <dt>

*lpszHelp* \[in\]
</dt> <dd>

Type: **LPCTSTR**

The address of a null-terminated string containing the path, if necessary, and the name of the help file that **MLWinHelp** is to display.

The file name can be followed by an angle bracket (>) and the name of a secondary window if the topic is to be displayed in a secondary window rather than in the primary window. You must define the name of the secondary window in the \[WINDOWS\] section of the help project (.hpj) file.

</dd> <dt>

*uCommand* \[in\]
</dt> <dd>

Type: **UINT**

The type of help requested. For a list of possible values and how they affect the value to place in the *dwData* parameter, see the Remarks section.

</dd> <dt>

*dwData* \[in\]
</dt> <dd>

Type: **DWORD\_PTR**

Additional data. The value used depends on the value of the *uCommand* parameter. For a list of possible *dwData* values, see the Remarks section.

</dd> </dl>

## Return value

Type: **BOOL**

Returns a nonzero value on success, or zero otherwise. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

This function is not included in a header file and must be called by ordinal 395 for **MLWinHelpA** and 397 for **MLWinHelpW**.

**MLWinHelp** is essentially a wrapper for [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa). It attempts to obtain the path to the help file corresponding to the current UI language setting before calling **WinHelp**. If it succeeds, it passes that path. If it fails, it passes the path pointed to by *lpszHelp*.

This function fails if called from any context but the current user.

Before closing the window that requested help, the application must call **MLWinHelp** with the *uCommand* parameter set to HELP\_QUIT. Until all applications have done this, Windows Help will not terminate. Note that calling Windows Help with the HELP\_QUIT command is not necessary if you used the HELP\_CONTEXTPOPUP command to start Windows Help.

The following table shows the possible values for the *uCommand* parameter and the corresponding formats of the *dwData* parameter.



| *uCommand*          | Action                                                                                                                                                                                                                                                               | *dwData*                                                                                                                                                                                                                                                                                                     |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HELP\_COMMAND       | Executes a help macro or macro string.                                                                                                                                                                                                                               | Address of a string that specifies the name of the help macro(s) to run. If the string specifies multiple macro names, the names must be separated by semicolons. You must use the short form of the macro name for some macros because Windows Help does not support the long name.                         |
| HELP\_CONTENTS      | Displays the topic specified by the Contents option in the \[OPTIONS\] section of the .hpj file. This command is for backward compatibility. New applications should provide a .cnt file and use the HELP\_FINDER command.                                           | Ignored; set to 0.                                                                                                                                                                                                                                                                                           |
| HELP\_CONTEXT       | Displays the topic identified by the specified context identifier defined in the \[MAP\] section of the .hpj file.                                                                                                                                                   | Contains the context identifier for the topic.                                                                                                                                                                                                                                                               |
| HELP\_CONTEXTMENU   | Displays the **Help** menu for the selected window, then displays the topic for the selected control in a pop-up window.                                                                                                                                             | Address of an array of **DWORD** pairs. The first **DWORD** in each pair is the control identifier, and the second is the context identifier for the topic. The array must be terminated by a pair of zeros {0,0}. If you do not want to add help to a particular control, set its context identifier to -1. |
| HELP\_CONTEXTPOPUP  | Displays the topic identified by the specified context identifier defined in the \[MAP\] section of the .hpj file in a pop-up window.                                                                                                                                | Contains the context identifier for a topic.                                                                                                                                                                                                                                                                 |
| HELP\_FINDER        | Displays the **Help Topics** dialog box.                                                                                                                                                                                                                             | Ignored; set to 0.                                                                                                                                                                                                                                                                                           |
| HELP\_FORCEFILE     | Ensures that Windows Help is displaying the correct help file. If the incorrect help file is being displayed, Windows Help opens the correct one; otherwise, there is no action.                                                                                     | Ignored; set to 0.                                                                                                                                                                                                                                                                                           |
| HELP\_HELPONHELP    | Displays help on how to use Windows Help, if the Winhlp32.hlp file is available.                                                                                                                                                                                     | Ignored; set to 0.                                                                                                                                                                                                                                                                                           |
| HELP\_INDEX         | Displays the topic specified by the Contents option in the \[OPTIONS\] section of the .hpj file. This command is for backward compatibility. New applications should use the HELP\_FINDER command.                                                                   | Ignored; set to 0.                                                                                                                                                                                                                                                                                           |
| HELP\_KEY           | Displays the topic in the keyword table that matches the specified keyword, if there is an exact match. If there is more than one match, displays the index with the topics listed in the **Topics Found** list box.                                                 | Address of a keyword string. Multiple keywords must be separated by semicolons.                                                                                                                                                                                                                              |
| HELP\_MULTIKEY      | Displays the topic specified by a keyword in an alternative keyword table.                                                                                                                                                                                           | Address of a [**MULTIKEYHELP**](/windows/win32/api/winuser/ns-winuser-multikeyhelpa) structure that specifies a table footnote character and a keyword.                                                                                                                                                                                     |
| HELP\_PARTIALKEY    | Displays the topic in the keyword table that matches the specified keyword, if there is an exact match. If there is more than one match, displays the **Topics Found** dialog box. To display the index without passing a keyword, use a pointer to an empty string. | Address of a keyword string. Multiple keywords must be separated by semicolons.                                                                                                                                                                                                                              |
| HELP\_QUIT          | Informs Windows Help that it is no longer needed. If no other applications have asked for help, Windows closes Windows Help.                                                                                                                                         | Ignored; set to 0.                                                                                                                                                                                                                                                                                           |
| HELP\_SETCONTENTS   | Specifies the Contents topic. Windows Help displays this topic when the user clicks the **Contents** button if the help file does not have an associated .cnt file.                                                                                                  | Contains the context identifier for the Contents topic.                                                                                                                                                                                                                                                      |
| HELP\_SETPOPUP\_POS | Sets the position of the subsequent pop-up window.                                                                                                                                                                                                                   | Contains the position data. Use the [**MAKELONG**](/previous-versions/windows/desktop/legacy/ms632660(v=vs.85)) macro to concatenate the horizontal and vertical coordinates into a single value. The pop-up window is positioned as if the mouse cursor were at the specified point when the pop-up window was invoked.                                 |
| HELP\_SETWINPOS     | Displays the Windows Help window, if it is minimized or in memory, and sets its size and position as specified.                                                                                                                                                      | Address of a [**HELPWININFO**](/windows/win32/api/winuser/ns-winuser-helpwininfoa) structure that specifies the size and position of either a primary or secondary help window.                                                                                                                                                             |
| HELP\_TCARD         | Indicates that a command is for a training card instance of Windows Help. Combine this command with other commands using the bitwise OR operator.                                                                                                                    | Depends on the command with which this command is combined.                                                                                                                                                                                                                                                  |
| HELP\_WM\_HELP      | Displays the topic for the control identified by the *hWndMain* parameter in a pop-up window.                                                                                                                                                                        | Address of an array of **DWORD** pairs. The first **DWORD** in each pair is a control identifier, and the second is a context identifier for a topic. The array must be terminated by a pair of zeros {0,0}. If you do not want to add Help to a particular control, set its context identifier to -1.       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>None</dt> </dl>                               |
| DLL<br/>                      | <dl> <dt>Shlwapi.dll (version 5.0 or later)</dt> </dl> |
| Unicode and ANSI names<br/>   | **MLWinHelpW** (Unicode) and **MLWinHelpA** (ANSI)<br/>                                                 |



## See also

<dl> <dt>

[**HELPWININFO**](/windows/win32/api/winuser/ns-winuser-helpwininfoa)
</dt> <dt>

[**MULTIKEYHELP**](/windows/win32/api/winuser/ns-winuser-multikeyhelpa)
</dt> </dl>

 

 
