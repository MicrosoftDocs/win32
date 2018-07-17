---
Description: The tables in this document list wrapper functions from Shlwapi.dll that provide limited Unicode functionality to Windows 95, Windows 98, and Windows Millennium Edition (Windows Me).
title: SHLWAPI Wrapper Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SHLWAPI Wrapper Functions

\[These functions are available through Windows XP Service Pack 2 (SP2) and Windows Server 2003. They might be altered or unavailable in subsequent versions of Windows.\]

The tables in this document list wrapper functions from Shlwapi.dll that provide limited Unicode functionality to Windows 95, Windows 98, and Windows Millennium Edition (Windows Me).

Windows 95, Windows 98, and Windows Millennium Edition (Windows Me) are referred to here as "native ANSI platforms". On native ANSI platforms, these wrapper functions convert the Unicode input string parameters to ANSI and call ANSI versions of functions in the **Forwards To** column. For example, **AppendMenuWrapW** calls **AppendMenuA**, which is the ANSI version of [**AppendMenu**](https://msdn.microsoft.com/en-us/library/ms647616(v=VS.85).aspx). The other functions follow the same pattern. Any strings returned by the ANSI function are converted to Unicode and returned to the calling application. Aside from the exceptions noted in the **Remarks** column, the wrapper function has the same syntax and provides the same functionality as the function in the **Forwards To** column. You should refer to that reference page for detailed usage information.

**Security Warning:** Multiple Unicode strings can convert to the same ANSI string. Unexpected collisions after conversion could result in unexpected behavior. For example, if **CreateEventWrapW** is used to create two differently-named events whose names match after conversion from Unicode to ANSI, the second call will return a handle to the same event as the first call, even though the original Unicode strings were different.

Microsoft Windows NT, Windows 2000, Windows XP, Windows Server 2003, and later operating systems are referred to here as "native Unicode platforms". For the most part, on native Unicode platforms, these wrapper functions simply forward input string parameters to the Unicode version of the function in the **Forwards To** column. For example, **AppendMenuWrapW** forwards to **AppendMenuW**, which is the Unicode version of [**AppendMenu**](https://msdn.microsoft.com/en-us/library/ms647616(v=VS.85).aspx). The other functions follow the same pattern. Any strings that are returned by the Unicode function are returned to the calling application. Aside from the exceptions noted in the **Remarks** column, the wrapper function has the same syntax and provides the same functionality as the function in the **Forwards To** column. You should refer to that reference page for detailed usage information.

**Security Warning:** The security issues noted for the functions in the **Forwards To** column also apply to the corresponding wrapper functions. For details, see the reference documentation for the function in the **Forwards To** column.

The wrapper functions in this table are all contained in Shlwapi.dll. To call them, you must use the ordinal listed in the table.

> [!Note]  
> These wrapper functions are available on Windows XP but do not provide any wrapper functionality in Windows XP Service Pack 2 (SP2) and later. They also do not provide wrapper functionality in Windows Server 2003. You should use the functions listed in the **Forwards To** column instead.

 



| Function                  | Ordinal | Forwards To                                             | DLL      | Remarks                                                                                                                             |
|---------------------------|---------|---------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------|
| AppendMenuWrapW           | 36      | [**AppendMenu**](https://msdn.microsoft.com/en-us/library/ms647616(v=VS.85).aspx)                     | USER32   | [(a)](#shlwapi-wrapper-functions), [(f)](#dragqueryfile), [(Menu)](#menu)                                                           |
| CallWindowProcWrapW       | 37      | [**CallWindowProc**](https://msdn.microsoft.com/en-us/library/ms633571(v=VS.85).aspx)             | USER32   | [(i)](#shlwapi-wrapper-functions)                                                                                                   |
| CharLowerWrapW            | 38      | [**CharLower**](https://msdn.microsoft.com/en-us/library/ms647467(v=VS.85).aspx)                       | KERNEL32 | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| CharUpperBufWrapW         | 44      | [**CharUpperBuff**](https://msdn.microsoft.com/en-us/library/ms647475(v=VS.85).aspx)               | KERNEL32 | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| CharUpperWrapW            | 43      | [**CharUpper**](https://msdn.microsoft.com/en-us/library/ms647474(v=VS.85).aspx)                       | KERNEL32 | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| CompareStringWrapW        | 45      | [**CompareString**](https://msdn.microsoft.com/en-us/library/Dd317759(v=VS.85).aspx)                 | KERNEL32 | [(CompareString)](#comparestring)                                                                                                   |
| CopyFileWrapW             | 112     | [**CopyFile**](https://msdn.microsoft.com/en-us/library/Aa363851(v=VS.85).aspx)                             | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| CreateEventWrapW          | 51      | [**CreateEvent**](https://msdn.microsoft.com/en-us/library/ms682396(v=VS.85).aspx)                     | KERNEL32 | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| CreateFileWrapW           | 52      | [**CreateFile**](https://msdn.microsoft.com/en-us/library/Aa363858(v=VS.85).aspx)                         | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| CreateWindowExWrapW       | 55      | [**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx)             | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| DefWindowProcWrapW        | 56      | [**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx)               | USER32   | [(i)](#shlwapi-wrapper-functions)                                                                                                   |
| DeleteFileWrapW           | 57      | [**DeleteFile**](https://msdn.microsoft.com/en-us/library/Aa363915(v=VS.85).aspx)                         | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| DialogBoxParamWrapW       | 59      | [**DialogBoxParam**](https://msdn.microsoft.com/en-us/library/ms645465(v=VS.85).aspx)             | USER32   | [(f)](#dragqueryfile), [(i)](#shlwapi-wrapper-functions), [(DialogBoxParam)](#dialogboxparam)                                       |
| DispatchMessageWrapW      | 60      | [**DispatchMessage**](https://msdn.microsoft.com/en-us/library/ms644934(v=VS.85).aspx)           | USER32   | [(i)](#shlwapi-wrapper-functions)                                                                                                   |
| DragQueryFileWrapW        | 318     | [**DragQueryFile**](/windows/desktop/api/Shellapi/nf-shellapi-dragqueryfilea)                  | SHELL32  | [(b)](#dialogboxparam), [(c)](#shlwapi-wrapper-functions), [(g)](#compareexchange), [(DragQueryFile)](#dragqueryfile)               |
| DrawTextExWrapW           | 301     | [**DrawTextEx**](https://msdn.microsoft.com/en-us/library/Dd162499(v=VS.85).aspx)                        | USER32   | [(a)](#shlwapi-wrapper-functions), [(d)](#shlwapi-wrapper-functions)                                                                |
| DrawTextWrapW             | 61      | [**DrawText**](https://msdn.microsoft.com/en-us/library/Dd162498(v=VS.85).aspx)                            | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| ExtTextOutWrapW           | 299     | [**ExtTextOut**](https://msdn.microsoft.com/en-us/library/Dd162713(v=VS.85).aspx)                        | GDI32    | [(d)](#shlwapi-wrapper-functions), [(f)](#dragqueryfile), [(ExtTextOut)](#exttextout)                                               |
| FormatMessageWrapW        | 68      | [**FormatMessage**](https://msdn.microsoft.com/en-us/library/ms679351(v=VS.85).aspx)                 | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(g)](#compareexchange), [(FormatMessage)](#formatmessage)                                       |
| GetClassInfoWrapW         | 69      | [**GetClassInfo**](https://msdn.microsoft.com/en-us/library/ms633578(v=VS.85).aspx)                 | USER32   | [(GetClassInfo)](#getclassinfo)                                                                                                     |
| GetDateFormatWrapW        | 311     | [**GetDateFormat**](https://msdn.microsoft.com/en-us/library/Dd318086(v=VS.85).aspx)                 | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(g)](#compareexchange), [(DateTime)](#datetime)                                                 |
| GetDlgItemTextWrapW       | 74      | [**GetDlgItemText**](https://msdn.microsoft.com/en-us/library/ms645489(v=VS.85).aspx)             | USER32   | [(g)](#compareexchange)                                                                                                             |
| GetFileAttributesWrapW    | 75      | [**GetFileAttributes**](https://msdn.microsoft.com/en-us/library/Aa364944(v=VS.85).aspx)           | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| GetLocaleInfoWrapW        | 77      | [**GetLocaleInfo**](https://msdn.microsoft.com/en-us/library/Dd318101(v=VS.85).aspx)                 | KERNEL32 | [(g)](#compareexchange)                                                                                                             |
| GetMenuItemInfoWrapW      | 302     | [**GetMenuItemInfo**](https://msdn.microsoft.com/en-us/library/ms647980(v=VS.85).aspx)           | USER32   | [(f)](#dragqueryfile), [(g)](#compareexchange), [(MenuItemInfo)](#menuiteminfo)                                                     |
| GetModuleFileNameWrapW    | 80      | [**GetModuleFileName**](https://msdn.microsoft.com/en-us/library/ms683197(v=VS.85).aspx)         | KERNEL32 | [(c)](#shlwapi-wrapper-functions), [(g)](#compareexchange)                                                                          |
| GetModuleHandleWrapW      | 83      | [**GetModuleHandle**](https://msdn.microsoft.com/en-us/library/ms683199(v=VS.85).aspx)             | KERNEL32 | [(c)](#shlwapi-wrapper-functions), [(g)](#compareexchange)                                                                          |
| GetObjectWrapW            | 84      | [**GetObject**](https://msdn.microsoft.com/en-us/library/Dd144904(v=VS.85).aspx)                          | GDI32    | [(g)](#compareexchange)                                                                                                             |
| GetOpenFileNameWrapW      | 403     | [**GetOpenFileName**](https://msdn.microsoft.com/en-us/library/ms646927(v=VS.85).aspx)           | COMDLG32 | [(a)](#shlwapi-wrapper-functions), [(b)](#dialogboxparam), [(g)](#compareexchange), [(OpenFileName)](#openfilename)                 |
| GetSaveFileNameWrapW      | 389     | [**GetSaveFileName**](https://msdn.microsoft.com/en-us/library/ms646928(v=VS.85).aspx)           | COMDLG32 | [(a)](#shlwapi-wrapper-functions), [(b)](#dialogboxparam), [(g)](#compareexchange), [(OpenFileName)](#openfilename)                 |
| GetSystemDirectoryWrapW   | 81      | [**GetSystemDirectory**](https://msdn.microsoft.com/en-us/library/ms724373(v=VS.85).aspx)       | KERNEL32 | [(c)](#shlwapi-wrapper-functions), [(g)](#compareexchange)                                                                          |
| GetTimeFormatWrapW        | 310     | [**GetTimeFormat**](https://msdn.microsoft.com/en-us/library/Dd318130(v=VS.85).aspx)                 | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(g)](#compareexchange), [(DateTime)](#datetime)                                                 |
| GetWindowLongWrapW        | 94      | [**GetWindowLong**](https://msdn.microsoft.com/en-us/library/ms633584(v=VS.85).aspx)               | USER32   | [(WindowLong)](#windowlong)                                                                                                         |
| GetWindowsDirectoryWrapW  | 97      | [**GetWindowsDirectory**](https://msdn.microsoft.com/en-us/library/ms724454(v=VS.85).aspx)     | KERNEL32 | [(c)](#shlwapi-wrapper-functions), [(g)](#compareexchange)                                                                          |
| GetWindowTextLengthWrapW  | 96      | [**GetWindowTextLength**](https://msdn.microsoft.com/en-us/library/ms633521(v=VS.85).aspx)   | USER32   | [(j)](#j)                                                                                                                           |
| GetWindowTextWrapW        | 95      | [**GetWindowText**](https://msdn.microsoft.com/en-us/library/ms633520(v=VS.85).aspx)               | USER32   | [(f)](#dragqueryfile), [(g)](#compareexchange)                                                                                      |
| InsertMenuItemWrapW       | 98      | [**InsertMenuItem**](https://msdn.microsoft.com/en-us/library/ms647988(v=VS.85).aspx)             | USER32   | [(a)](#shlwapi-wrapper-functions), [(f)](#dragqueryfile), [(Menu)](#menu), [(MenuItemInfo)](#menuiteminfo)                          |
| IsCharAlphaWrapW          | 25      | [**IsCharAlpha**](https://msdn.microsoft.com/en-us/library/ms647482(v=VS.85).aspx)                   | USER32   | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| IsCharAlphaNumericWrapW   | 28      | [**IsCharAlphaNumeric**](https://msdn.microsoft.com/en-us/library/ms647483(v=VS.85).aspx)     | KERNEL32 | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| IsCharUpperWrapW          | 26      | [**IsCharUpper**](https://msdn.microsoft.com/en-us/library/ms647485(v=VS.85).aspx)                   | USER32   | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| LoadLibraryWrapW          | 105     | [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx)                     | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| LoadStringWrapW           | 107     | [**LoadString**](https://msdn.microsoft.com/en-us/library/ms647486(v=VS.85).aspx)                     | KERNEL32 | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| MessageBoxWrapW           | 340     | [**MessageBox**](https://msdn.microsoft.com/en-us/library/ms645505(v=VS.85).aspx)                     | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| MoveFileWrapW             | 113     | [**MoveFile**](https://msdn.microsoft.com/en-us/library/Aa365239(v=VS.85).aspx)                             | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| OutputDebugStringWrapW    | 115     | [**OutputDebugString**](https://msdn.microsoft.com/en-us/library/Aa363362(v=VS.85).aspx)         | KERNEL32 | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| PeekMessageWrapW          | 116     | [**PeekMessage**](https://msdn.microsoft.com/en-us/library/ms644943(v=VS.85).aspx)                   | USER32   | [(PeekMessage and PostMessage)](#peekmessage-and-postmessage)                                                                       |
| PostMessageWrapW          | 117     | [**PostMessage**](https://msdn.microsoft.com/en-us/library/ms644944(v=VS.85).aspx)                   | USER32   | [(PeekMessage and PostMessage)](#peekmessage-and-postmessage)                                                                       |
| RegCreateKeyExWrapW       | 120     | [**RegCreateKeyEx**](https://msdn.microsoft.com/en-us/library/ms724844(v=VS.85).aspx)               | ADVAPI32 | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| RegisterClassWrapW        | 131     | [**RegisterClass**](https://msdn.microsoft.com/en-us/library/ms633586(v=VS.85).aspx)               | USER32   | [(a)](#shlwapi-wrapper-functions), [(RegisterClass)](#registerclass)                                                                |
| RegOpenKeyExWrapW         | 125     | [**RegOpenKeyEx**](https://msdn.microsoft.com/en-us/library/ms724897(v=VS.85).aspx)                   | ADVAPI32 | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| RegQueryValueExWrapW      | 128     | [**RegQueryValueEx**](https://msdn.microsoft.com/en-us/library/ms724911(v=VS.85).aspx)             | ADVAPI32 | [(a)](#shlwapi-wrapper-functions), [(g)](#compareexchange), [(ValueEx)](#regqueryvalueexw), [(RegQueryValueExW)](#regqueryvalueexw) |
| RegQueryValueWrapW        | 127     | [**RegQueryValue**](https://msdn.microsoft.com/en-us/library/ms724909(v=VS.85).aspx)                 | ADVAPI32 | [(a)](#shlwapi-wrapper-functions), [(g)](#compareexchange)                                                                          |
| RegSetValueExWrapW        | 130     | [**RegSetValueEx**](https://msdn.microsoft.com/en-us/library/ms724923(v=VS.85).aspx)                 | ADVAPI32 | [(a)](#shlwapi-wrapper-functions), [(ValueEx)](#regqueryvalueexw)                                                                   |
| SendMessageWrapW          | 136     | [**SendMessage**](https://msdn.microsoft.com/en-us/library/ms644950(v=VS.85).aspx)                   | USER32   | [(SendMessage)](#sendmessage)                                                                                                       |
| SetDlgItemTextWrapW       | 138     | [**SetDlgItemText**](https://msdn.microsoft.com/en-us/library/ms645521(v=VS.85).aspx)             | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| SetWindowLongWrapW        | 141     | [**SetWindowLong**](https://msdn.microsoft.com/en-us/library/ms633591(v=VS.85).aspx)               | USER32   | [(WindowLong)](#windowlong)                                                                                                         |
| SetWindowTextWrapW        | 143     | [**SetWindowText**](https://msdn.microsoft.com/en-us/library/ms633546(v=VS.85).aspx)               | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| ShellExecuteExWrapW       | 35      | [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa)                | SHELL32  | [(a)](#shlwapi-wrapper-functions), [(b)](#dialogboxparam), [(ShellExecuteEx)](#shellexecuteex)                                      |
| ShellMessageBoxWrapW      | 388     | [**ShellMessageBox**](/windows/desktop/api/Shellapi/nf-shellapi-shellmessageboxa)              | SHLWAPI  | [(a)](#shlwapi-wrapper-functions), [(FormatMessage)](#formatmessage)                                                                |
| SHGetFileInfoWrapW        | 313     | [**SHGetFileInfo**](/windows/desktop/api/Shellapi/nf-shellapi-shgetfileinfoa)                  | SHELL32  | [(a)](#shlwapi-wrapper-functions), [(b)](#dialogboxparam), [(g)](#compareexchange)                                                  |
| SHGetPathFromIDListWrapW  | 334     | [**SHGetPathFromIDList**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetpathfromidlista)      | USER32   | [(g)](#compareexchange)                                                                                                             |
| TranslateAcceleratorWrapW | 146     | [**TranslateAccelerator**](https://msdn.microsoft.com/en-us/library/ms646373(v=VS.85).aspx) | USER32   | [(i)](#shlwapi-wrapper-functions)                                                                                                   |
| UnregisterClassWrapW      | 147     | [**UnregisterClass**](https://msdn.microsoft.com/en-us/library/ms644899(v=VS.85).aspx)           | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |



 

The wrapper functions in the following table do not perform any character set conversion. Instead, they provide limited support for operating system features not available on earlier platforms.



| Function                     | Ordinal | Forwards To                                                                     | DLL      | Remarks                                                                        |
|------------------------------|---------|---------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------|
| MLGetUILanguage              | 376     | [**GetUserDefaultUILanguage**](https://msdn.microsoft.com/en-us/library/Dd318137(v=VS.85).aspx)                   | KERNEL32 | [(h)](#shlwapi-wrapper-functions)                                              |
| SHCancelTimerQueueTimer      | 265     | [**DeleteTimerQueueTimer**](https://msdn.microsoft.com/en-us/library/ms682569(v=VS.85).aspx)                         | KERNEL32 | [(h)](#shlwapi-wrapper-functions)                                              |
| SHDeleteTimerQueue           | 262     | [**DeleteTimerQueue**](https://msdn.microsoft.com/en-us/library/ms682565(v=VS.85).aspx)                                   | KERNEL32 | [(h)](#shlwapi-wrapper-functions)                                              |
| SHInterlockedCompareExchange | 342     | [**InterlockedCompareExchangePointer**](https://msdn.microsoft.com/en-us/library/ms683568(v=VS.85).aspx) | KERNEL32 | [(CompareExchange)](#compareexchange)                                          |
| SHQueueUserWorkItem          | 260     | [**QueueUserWorkItem**](https://msdn.microsoft.com/en-us/library/ms684957(v=VS.85).aspx)                                 | KERNEL32 | [(QueueUserWorkItem)](#queueuserworkitem), [(h)](#shlwapi-wrapper-functions)   |
| SHSetTimerQueueTimer         | 263     | [**CreateTimerQueueTimer**](https://msdn.microsoft.com/en-us/library/ms682485(v=VS.85).aspx)                         | KERNEL32 | [(SetTimerQueueTimer)](#settimerqueuetimer), [(h)](#shlwapi-wrapper-functions) |



 

## Remarks

### (a)

If string conversion is necessary, all strings are converted through the CP\_ACP code page.

These functions employ best-fit characters and do not perform default checking when converting from Unicode to ANSI. Furthermore, if the string cannot be converted from Unicode to ANSI, the wrapper function passes a **NULL** string to the underlying ANSI function. This can occur, for example, when there is insufficient memory. Passing a **NULL** string may cause some functions to fail with an invalid parameter error, but other functions accept the **NULL** string and treat it as the intended parameter. For example, an error occurs when the **CreateWindowExWrapW** function attempts to convert the *lpWindowName* parameter to ANSI, and [**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx) creates a window with an empty caption. The wrapper does not notify you when these problems have occurred.

The Microsoft Layer for Unicode (MSLU) checks for errors during conversion from Unicode to ANSI and returns appropriate error values. For example, the [**AppendMenu**](https://msdn.microsoft.com/en-us/library/ms647616(v=VS.85).aspx) wrapper function in the MSLU returns 0 if the item was not successfully appended.

### (b)

These functions use a delay-loaded link to the appropriate function. This means that the DLL that contains the function in the "Forwards To" column is not loaded by the Shlwapi.dll until a function in that DLL is called. The Microsoft Visual C++ linker supports this functionality more generally via the /DELAYLOAD option.

### (c)

This function manipulates filenames. As noted in [(a)](#shlwapi-wrapper-functions), the functions convert all strings through the CP\_ACP code page. They do not check whether the file I/O functions have been set to ANSI mode. If the file I/O functions are in OEM mode, the strings will be converted to and from the wrong character set. An application can set the file I/O functions to OEM mode explicitly by calling the [**SetFileApisToOEM**](https://msdn.microsoft.com/en-us/library/Aa365534(v=VS.85).aspx) function.

**Security Warning:  ** Using these wrapper functions for file names can compromise the security of your application. Since no default checking is performed and best-fit characters are employed, filename characters can be converted in unexpected ways. This could result in file system spoofing attacks. Also, silent data loss can occur during the conversion from Unicode to ANSI.

The MSLU does not have these limitations.

### (d)

If the string being drawn requires a character set that is not available in the font that is selected into the device context, these wrapper functions use the [Font Linking](https://msdn.microsoft.com/en-us/library/Aa767872(v=VS.85).aspx) feature of the [MLang](https://msdn.microsoft.com/en-us/library/Aa767865(v=VS.85).aspx) library to render each character in an appropriate font. Unlike most other wrapper functions, these are functional on Microsoft Windows NT 4.0 in addition to native ANSI platforms.

### (e)

Full Unicode implementations of these functions are available on native ANSI platforms. These functions do not call the related ANSI function.

### (f)

If the user-default UI language uses a different character set than the system-default UI language, the system attempts to rewrite dialog templates and subclass controls and convert menu items to owner-draw, so that strings in the user-default UI language continue to display correctly. The only controls supported by the dialog template rewrite rules are static, button, listbox, and combobox controls. These controls are subclassed such that the **SendMessageWrapW** function can obtain the original Unicode string without being translated through the ANSI character set. Unlike most of the other wrapper functions, these are functional on Microsoft Windows NT 4.0 as well as native ANSI platforms. See the remarks in the documentation of the [**MLLoadLibrary**](https://msdn.microsoft.com/en-us/library/Bb773822(v=VS.85).aspx) function for further discussion of how the user-default UI language and system-default UI language are determined.

### (g)

If string conversion is necessary, all strings are converted through the CP\_ACP code page.

When converting from ANSI to Unicode for output, if the returned string does not fit in the buffer that was provided, the wrapper functions truncate the string. Those functions that return the number of characters copied to the buffer or the number of characters necessary to avoid truncation do not return the number of Unicode characters copied to the buffer provided by or required from the caller of the wrapper function. They return the number of ANSI characters copied to the buffer or required by the underlying ANSI function. The MSLU does not have these limitations.

### (h)

On systems prior to Windows XP, these functions implement a simplified thread pool and timer queue. On Windows XP and later, these functions use the system thread pool and system timer queue. For the timer queue functions, the *hQueue* parameter must be set to **NULL** to indicate that the operation is to be performed on the default timer queue.

### (i)

On Unicode platforms, these functions translate the message from Unicode to ANSI if the destination window is ANSI. These functions do not perform message translation on native ANSI platforms. Therefore, calling applications calling this function must ensure that the message is in Unicode format on Unicode platforms and in ANSI format on ANSI platforms. For instance, in the following function call, the *wParam* must be a Unicode code point if the program is running on a Unicode platform and must be an ANSI character if the program is running on an ANSI platform.

``` syntax
CallWindowProcWrapW(prevWndProc, hwnd, WM_CHAR, wParam, lParam);
```

The MSLU tracks the character set of the destination window procedure and converts the message as necessary.

### (j)

On ANSI platforms, these functions return the length of the underlying ANSI string, not the length of the translated Unicode string. The MSLU does not have these limitations.

### (CompareExchange)

The syntax for **SHInterlockedCompareExchange** is somewhat different from that of [**InterlockedCompareExchangePointer**](https://msdn.microsoft.com/en-us/library/ms683568(v=VS.85).aspx), but it functions identically.

``` syntax
void* SHInterlockedCompareExchange(void **ppDest, void *pExch, void *pComp);
```

### (CompareString)

Remember that on native ANSI platforms, both strings are converted to ANSI and compared as ANSI strings. If the Unicode strings contain characters that cannot be represented in ANSI, the results may be unexpected. For example, if the default ANSI code page does not support CJK characters, then the strings L"\\x66F0" and L"\\x6708" would compare as equal on native ANSI platforms because they both map to the ANSI string "?".

### (DateTime)

On Shlwapi.dll version 5.0, which shipped with Windows 2000, the code page of the locale identifier that you pass as the first parameter of **GetDateFormatWrapW** and **GetTimeFormatWrapW** must match the current ANSI codepage. Otherwise, the returned string may be converted incorrectly. This limitation does not apply to Shlwapi.dll versions 5.5 or higher. This means that Windows XP and later systems are not subject to this limitation. The MSLU does not have this limitation.

### (DialogBoxParam)

The *lpTemplateName* parameter for the **DialogBoxParamWrapW** function cannot be a string. It must be an ordinal created by the [**MAKEINTRESOURCE**](https://msdn.microsoft.com/en-us/library/ms648029(v=VS.85).aspx) macro. The dialog procedure specified by the *lpDialogFunc* parameter receives ANSI messages on native ANSI platforms and Unicode messages on native Unicode platforms. The dialog procedure must be prepared to handle both cases. The MSLU does not have these limitations.

### (ExtTextOut)

Native ANSI platforms implement the [**ExtTextOutW**](https://msdn.microsoft.com/en-us/library/Dd162713(v=VS.85).aspx) function as well as native Unicode platforms. The purpose of **ExtTextOutWrapW** is to perform font linking, as described in a separate remark.

### (DragQueryFile)

The **DragQueryFileWrapW** function does not allow you to query for the length of a file in the drop handle by passing **NULL** as the *lpszFile* parameter. The MSLU does not have these limitations.

### (FormatMessage)

On native ANSI platforms, the formats in the string are not converted from Unicode to ANSI. For example, the following code example is in error.


```
WCHAR szBuffer[MAX_PATH];
DWORD_PTR Arguments[2] = { L"String1", L"String2" };

FormatMessageWrapW(FORMAT_MESSAGE_FROM_STRING, 
               L"%1!s! %2", 
               0, 0, 
               szBuffer, 
               MAX_PATH, 
               (va_list*)Arguments);
```



This code example uses the "!s!" format. On native ANSI platforms, this string is passed to the ANSI version of the [**FormatMessage**](https://msdn.microsoft.com/en-us/library/ms679351(v=VS.85).aspx) function. Consequently, an ANSI string is expected instead of a Unicode string. Similarly, the "%2" format implies a string argument. When it is passed to the ANSI **FormatMessage** function, it is interpreted as an ANSI string rather than a Unicode string. The correct format string is L"%1!ws! %2!ws!". This prints strings correctly on both ANSI and Unicode platforms.

The function does not support the "%0" special format string.

The MSLU does not have these limitations.

### (GetClassInfo)

On native ANSI platforms, the **lpszMenuName** and **lpszClassName** members of the [**WNDCLASS**](https://msdn.microsoft.com/en-us/library/ms633576(v=VS.85).aspx) structure are not translated to Unicode and are always set to **NULL**. Furthermore, the window procedure returned in the **lpfnWndProc** member of the **WNDCLASS** structure is not translated to Unicode, and refers to an ANSI window procedure. The MSLU does not have these limitations.

### (Menu)

On Shlwapi.dll version 5.0, which shipped with Windows 2000, menu item strings that contain tab characters (\\t) may not display correctly. This limitation does not apply to Shlwapi.dll versions 5.5 or higher. This means that Windows XP and later systems are not subject to this limitation. The MSLU does not have this limitation.

### (MenuItemInfo)

This function only supports the Microsoft Windows NT 4.0 version of the [**MENUITEMINFOW**](_win32_MENUITEMINFO_str) structure. This structure lacks an **hbmpItem** member. In addition, the function does not support the MIIM\_BITMAP flag. The MSLU does not have these limitations.

### (OpenFileName)

The **cbSize** member of the [**OPENFILENAMEW**](_win32_openfilename_str) structure must be set to sizeof(OPENFILENAME\_NT4W).

The **lpstrCustomFilter** member of the [**OPENFILENAMEW**](_win32_openfilename_str) structure must be set to **NULL**.

The values of the **nMaxFile** and **nMaxFileTitle** members of the [**OPENFILENAMEW**](_win32_openfilename_str) structure must not exceed MAX\_PATH.

If the **lpfnHook** member of the [**OPENFILENAMEW**](_win32_openfilename_str) structure is not **NULL**, it must refer to an ANSI hook procedure on native ANSI platforms and a Unicode hook procedure on native Unicode platforms.

The MSLU does not have these limitations.

### (PeekMessage and PostMessage)

On native ANSI platforms, no translation is performed on the transmitted or retrieved message. The transmitted/retrieved message is ANSI on native ANSI platforms and Unicode on native Unicode platforms. The calling application must be prepared to handle both cases. For example, if the retrieved message is WM\_CHAR, then the *wParam* is an ANSI character code on native ANSI platforms but it is a Unicode code point on native Unicode platforms. The MSLU does not have these limitations.

### (QueueUserWorkItem)

The **SHQueueUserWorkItem** function is slightly different from the corresponding [**QueueUserWorkItem**](https://msdn.microsoft.com/en-us/library/ms684957(v=VS.85).aspx) function. The syntax for **SHQueueUserWorkItem** is shown here.

``` syntax
BOOL SHQueueUserWorkItem(LPTHREAD_START_ROUTINE pfnCallback,
                     LPVOID pContext,
                     LONG lPriority,
                     DWORD_PTR dwTag,
                     DWORD_PTR * pdwId,
                     LPCSTR pszModule,
                     DWORD dwFlags);
```

The parameters should be set as follows:

-   The *pfnCallback* and *pContext* parameters have the same meanings as the *Function* and *Context* parameters, respectively, of [**QueueUserWorkItem**](https://msdn.microsoft.com/en-us/library/ms684957(v=VS.85).aspx).
-   The *dwTag* parameter is unused and must be set to 0.
-   The *pdwld* parameter is unused and must be set to **NULL**.
-   The *pszModule* parameter points to an optional null-terminated ANSI string that specifies the name of a library to be loaded before the work item begins and unloaded after the work item completes. This parameter can be **NULL**.
-   The *dwFlags* parameter supports only a subset of the values supported by [**QueueUserWorkItem**](https://msdn.microsoft.com/en-us/library/ms684957(v=VS.85).aspx). The following flags are recognized.

    

    | Name              | Value      | Meaning                          |
    |-------------------|------------|----------------------------------|
    | TPS\_EXECUTEIO    | 0x00000001 | Same as WT\_EXECUTEINIOTHREAD.   |
    | TPS\_LONGEXECTIME | 0x00000008 | Same as WT\_EXECUTELONGFUNCTION. |

    

     

    > [!Note]  
    > The TPS\_LONGEXECTIME flag does not have the same numerical value as the WT\_EXECUTELONGFUNCTION flag. When using **SHQueueUserWorkItem**, the dwFlags parameter must be a combination of TPS\_\* values, not WT\_\* values.

     

**SHQueueUserWorkItem** returns a nonzero value if the work item was successfully queued and 0 otherwise. If the function fails, you can use [**GetLastError**](https://msdn.microsoft.com/en-us/library/ms679360(v=VS.85).aspx) to obtain additional information.

### (RegisterClass)

On native ANSI platforms, no translation is performed on the **lpfnWndProc** member of the [**WNDCLASSW**](_win32_WNDCLASS_str) structure. The window will receive ANSI window messages on native ANSI platforms and Unicode window messages on native Unicode platforms. The window procedure must be prepared to handle both cases. The MSLU does not have these limitations.

### (RegQueryValueExW)

**RegQueryValueExWrapW** has also been called under the name **RegQueryValueExW**. As with any unnamed function exported strictly by ordinal, you can choose the name that the function is known by in your code.

### (SendMessage)

On native Unicode platforms, the **SendMessageWrapW** function forwards to the [**SendMessageW**](_win32_SendMessage) function. On native ANSI platforms, **SendMessageWrapW** provides limited support for translating Unicode messages to ANSI. The list of supported messages is given in the following table. The function will not translate any other messages.

The MSLU does not have these limitations.



|                      |                                                                                                           |
|----------------------|-----------------------------------------------------------------------------------------------------------|
| CB\_ADDSTRING        | (b) (f) (c)                                                                                               |
| CB\_FINDSTRING       | (b) (f) (c)                                                                                               |
| CB\_FINDSTRINGEXACT  | (a) (f) (c)                                                                                               |
| CB\_GETLBTEXT        | (b) (f) (c) (o) The buffer passed in the *lParam* parameter must have room for at least 256 characters.   |
| CB\_GETLBTEXTLEN     | (a)                                                                                                       |
| CB\_INSERTSTRING     | (b) (f) (c)                                                                                               |
| CB\_SELECTSTRING     | (b) (f) (c)                                                                                               |
| EM\_CHARFROMPOS      |                                                                                                           |
| EM\_GETLINE          | (e) The return value is the number of ANSI characters copied.                                             |
| EM\_GETSEL           |                                                                                                           |
| EM\_REPLACESEL       | (b) (f)                                                                                                   |
| EM\_SETPASSWORDCHAR  | (a)                                                                                                       |
| EM\_SETSEL           |                                                                                                           |
| EM\_SETWORDBREAKPROC | This message has no effect. The word break procedure is not set.                                          |
| LB\_ADDSTRING        | (b) (f) (d)                                                                                               |
| LB\_FINDSTRING       | (b) (f) (d)                                                                                               |
| LB\_FINDSTRINGEXACT  | (b) (f) (lbs)                                                                                             |
| LB\_GETTEXT          | (b) (f) (lbs) (o) The buffer passed in the *lParam* parameter must have room for at least 256 characters. |
| LB\_GETTEXTLEN       | (a)                                                                                                       |
| LB\_INSERTSTRING     | (b) (f) (d)                                                                                               |
| LB\_SELECTSTRING     | (b) (f) (d)                                                                                               |
| WM\_GETTEXT          | (b) (f)                                                                                                   |
| WM\_GETTEXTLENGTH    | (a)                                                                                                       |
| WM\_SETTEXT          | (b) (f)                                                                                                   |
| WM\_SETTINGCHANGE    | (a) The message is sent with a timeout of three seconds.                                                  |



 

### 

-   (a) The ANSI string being measured or retrieved must satisfy the following condition: the length of the corresponding Unicode version of the string cannot exceed the length of the ANSI version of the string. If this condition is not met, the returned length will be short. If there is insufficient memory to determine the length of the Unicode string, the function returns zero, not LB\_ERR or CB\_ERR as might be expected.
-   (b) If string conversion is necessary, all strings are converted through the CP\_ACP code page.

    This function employs best-fit characters and does not perform default checking when converting from Unicode to ANSI. Furthermore, if the string cannot be converted from Unicode to ANSI, the function passes a null string to the underlying ANSI function. This can occur, for example, when there is insufficient memory. Passing a null string may cause some functions to fail with an invalid parameter error, but other functions accept the null string and treat it as the intended parameter. For example, if an error occurs when the WM\_SETTEXT wrapper attempts to convert the window title to ANSI, the window will have an empty caption. The function does not notify you when these problems occur. The MSLU does not have these limitations.

-   (c) The specified window handle must be the handle to a [ComboBox](_win32_Combo_Boxes) or [ComboBoxEx](_win32_ComboBoxEx_Controls) control. If the handle is to a combobox control that is owner-draw and was not created with the [List Box Styles](_win32_List_Box_Styles) style, then the translation of this message will fail and may even crash.
-   (d) The specified window handle must be the handle to a listbox control. If the listbox is owner-draw and was not created with the [List Box Styles](_win32_List_Box_Styles) style, then the translation of this message will fail and may even crash.
-   (e) If string conversion is necessary, all strings are converted through the CP\_ACP code page.

    When converting from ANSI to Unicode for output, the wrapper functions truncate the returned string if it does not fit in the provided buffer. The return value for functions that return the number of characters copied to the buffer or the number of characters necessary to avoid truncation refers to the number of ANSI characters copied to the buffer or required by the underlying ANSI function, not the number of Unicode characters copied to the buffer provided by or required from the calling application that called the wrapper function. The MSLU does not have this limitation. For further details, see [Microsoft Layer for Unicode on Windows 95/98/Me Systems](http://go.microsoft.com/fwlink/p/?linkid=198351).

### (SetTimerQueueTimer)

The **SHSetTimerQueueTimer** function is slightly different from the corresponding [**CreateTimerQueueTimer**](https://msdn.microsoft.com/en-us/library/ms682485(v=VS.85).aspx) function. Its syntax is as follows:

``` syntax
HANDLE SHSetTimerQueueTimer(HANDLE hQueue,
                        WAITORTIMERCALLBACK pfnCallback,
                        LPVOID pContext,
                        DWORD dwDueTime,
                        DWORD dwPeriod,
                        LPCSTR lpszLibrary,
                        DWORD dwFlags);
```

The parameters should be set as follows:

-   The *hQueue* parameter must be set to **NULL**, specifying the default timer queue.
-   The *pfnCallback*, *pContext*, *dwDueTime*, and *dwPeriod* parameters have the same meanings as the *Callback*, *Parameter*, *DueTime*, and *Period* parameters, respectively, of [**CreateTimerQueueTimer**](https://msdn.microsoft.com/en-us/library/ms682485(v=VS.85).aspx).
-   The *lpszLibrary* parameter is unused and must be set to **NULL**.
-   The *Flags* parameter supports only a subset of the values supported by [**CreateTimerQueueTimer**](https://msdn.microsoft.com/en-us/library/ms682485(v=VS.85).aspx).

    

    | Name              | Value      | Meaning                         |
    |-------------------|------------|---------------------------------|
    | TPS\_EXECUTEIO    | 0x00000001 | Same as WT\_EXECUTEINIOTHREAD   |
    | TPS\_LONGEXECTIME | 0x00000008 | Same as WT\_EXECUTELONGFUNCTION |

    

     

    > [!Note]  
    > The TPS\_LONGEXECTIME flag does not have the same numerical value as the WT\_EXECUTELONGFUNCTION flag. When using **SHSetTimerQueueTimer**, the *dwFlags* parameter must be a combination of TPS\_\* values, not WT\_\* values.

     

**SHSetTimerQueueTimer** returns the handle of the created timer on success and **NULL** otherwise.

### (ShellExecuteEx)

The **lpFile** member of the [**SHELLEXECUTEINFO**](/windows/desktop/api/Shellapi/ns-shellapi-_shellexecuteinfoa) structure passed in this function's only parameter may not exceed INTERNET\_MAX\_URL\_LENGTH characters. If the SEE\_MASK\_CLASSNAME flag is omitted, the **lpClass** member must be initialized to **NULL**.

### (ValueEx)

Only the following registry data types are supported: REG\_SZ, REG\_EXPAND\_SZ, REG\_BINARY, and REG\_DWORD. Unlike these wrapper functions, the MSLU also supports REG\_MULTI\_EXPAND\_SZ.

### (WindowLong)

On native ANSI platforms, the function performs no translation on any of the window longs. For example, if you pass GWLP\_WNDPROC, the function returns the ANSI window procedure, not a thunk. The MSLU does not have these limitations.

 

 



