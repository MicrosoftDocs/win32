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

Windows 95, Windows 98, and Windows Millennium Edition (Windows Me) are referred to here as "native ANSI platforms". On native ANSI platforms, these wrapper functions convert the Unicode input string parameters to ANSI and call ANSI versions of functions in the **Forwards To** column. For example, **AppendMenuWrapW** calls **AppendMenuA**, which is the ANSI version of [**AppendMenu**](https://msdn.microsoft.com/windows/desktop/07da4d45-a816-40c1-a5c5-c7fbe954be57). The other functions follow the same pattern. Any strings returned by the ANSI function are converted to Unicode and returned to the calling application. Aside from the exceptions noted in the **Remarks** column, the wrapper function has the same syntax and provides the same functionality as the function in the **Forwards To** column. You should refer to that reference page for detailed usage information.

**Security Warning:** Multiple Unicode strings can convert to the same ANSI string. Unexpected collisions after conversion could result in unexpected behavior. For example, if **CreateEventWrapW** is used to create two differently-named events whose names match after conversion from Unicode to ANSI, the second call will return a handle to the same event as the first call, even though the original Unicode strings were different.

Microsoft Windows NT, Windows 2000, Windows XP, Windows Server 2003, and later operating systems are referred to here as "native Unicode platforms". For the most part, on native Unicode platforms, these wrapper functions simply forward input string parameters to the Unicode version of the function in the **Forwards To** column. For example, **AppendMenuWrapW** forwards to **AppendMenuW**, which is the Unicode version of [**AppendMenu**](https://msdn.microsoft.com/windows/desktop/07da4d45-a816-40c1-a5c5-c7fbe954be57). The other functions follow the same pattern. Any strings that are returned by the Unicode function are returned to the calling application. Aside from the exceptions noted in the **Remarks** column, the wrapper function has the same syntax and provides the same functionality as the function in the **Forwards To** column. You should refer to that reference page for detailed usage information.

**Security Warning:** The security issues noted for the functions in the **Forwards To** column also apply to the corresponding wrapper functions. For details, see the reference documentation for the function in the **Forwards To** column.

The wrapper functions in this table are all contained in Shlwapi.dll. To call them, you must use the ordinal listed in the table.

> [!Note]  
> These wrapper functions are available on Windows XP but do not provide any wrapper functionality in Windows XP Service Pack 2 (SP2) and later. They also do not provide wrapper functionality in Windows Server 2003. You should use the functions listed in the **Forwards To** column instead.

 



| Function                  | Ordinal | Forwards To                                             | DLL      | Remarks                                                                                                                             |
|---------------------------|---------|---------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------|
| AppendMenuWrapW           | 36      | [**AppendMenu**](https://msdn.microsoft.com/windows/desktop/07da4d45-a816-40c1-a5c5-c7fbe954be57)                     | USER32   | [(a)](#shlwapi-wrapper-functions), [(f)](#dragqueryfile), [(Menu)](#menu)                                                           |
| CallWindowProcWrapW       | 37      | [**CallWindowProc**](https://msdn.microsoft.com/windows/desktop/667449cd-1eea-43de-8268-3da73022d7ac)             | USER32   | [(i)](#shlwapi-wrapper-functions)                                                                                                   |
| CharLowerWrapW            | 38      | [**CharLower**](https://msdn.microsoft.com/windows/desktop/b67786aa-d629-4d23-b4cb-efb43282ca02)                       | KERNEL32 | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| CharUpperBufWrapW         | 44      | [**CharUpperBuff**](https://msdn.microsoft.com/windows/desktop/774619cf-ed37-4342-b265-8125693fede5)               | KERNEL32 | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| CharUpperWrapW            | 43      | [**CharUpper**](https://msdn.microsoft.com/windows/desktop/4a101fb6-8b90-479b-93dc-3f768e9b952a)                       | KERNEL32 | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| CompareStringWrapW        | 45      | [**CompareString**](https://msdn.microsoft.com/windows/desktop/4db84fa7-f3c2-48fb-ad7d-8673397c4b0e)                 | KERNEL32 | [(CompareString)](#comparestring)                                                                                                   |
| CopyFileWrapW             | 112     | [**CopyFile**](https://msdn.microsoft.com/windows/desktop/2c8ad002-cef4-499c-acda-c162205f6a8d)                             | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| CreateEventWrapW          | 51      | [**CreateEvent**](https://msdn.microsoft.com/windows/desktop/1f6d946e-c74c-4599-ac3d-b709216a0900)                     | KERNEL32 | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| CreateFileWrapW           | 52      | [**CreateFile**](https://msdn.microsoft.com/windows/desktop/80a96083-4de9-4422-9705-b8ad2b6cbd1b)                         | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| CreateWindowExWrapW       | 55      | [**CreateWindowEx**](https://msdn.microsoft.com/windows/desktop/33deeb92-6285-4c67-9338-ca2e194b9915)             | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| DefWindowProcWrapW        | 56      | [**DefWindowProc**](https://msdn.microsoft.com/windows/desktop/fcc6b242-e152-4364-a977-b0441bec425f)               | USER32   | [(i)](#shlwapi-wrapper-functions)                                                                                                   |
| DeleteFileWrapW           | 57      | [**DeleteFile**](https://msdn.microsoft.com/windows/desktop/0b947a85-816b-4374-a8f8-c369e366a17d)                         | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| DialogBoxParamWrapW       | 59      | [**DialogBoxParam**](https://msdn.microsoft.com/windows/desktop/f6d6b80b-251f-44a0-9deb-e518af170b14)             | USER32   | [(f)](#dragqueryfile), [(i)](#shlwapi-wrapper-functions), [(DialogBoxParam)](#dialogboxparam)                                       |
| DispatchMessageWrapW      | 60      | [**DispatchMessage**](https://msdn.microsoft.com/windows/desktop/6d5e2d1d-dcd2-48ce-a8ba-99bd5dbdfb21)           | USER32   | [(i)](#shlwapi-wrapper-functions)                                                                                                   |
| DragQueryFileWrapW        | 318     | [**DragQueryFile**](/windows/desktop/api/Shellapi/nf-shellapi-dragqueryfilea)                  | SHELL32  | [(b)](#dialogboxparam), [(c)](#shlwapi-wrapper-functions), [(g)](#compareexchange), [(DragQueryFile)](#dragqueryfile)               |
| DrawTextExWrapW           | 301     | [**DrawTextEx**](https://msdn.microsoft.com/windows/desktop/77b9973b-77f1-4508-a021-52d61d576c23)                        | USER32   | [(a)](#shlwapi-wrapper-functions), [(d)](#shlwapi-wrapper-functions)                                                                |
| DrawTextWrapW             | 61      | [**DrawText**](https://msdn.microsoft.com/windows/desktop/fe412280-d797-4abd-8a29-107a9cd96145)                            | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| ExtTextOutWrapW           | 299     | [**ExtTextOut**](https://msdn.microsoft.com/windows/desktop/74f8fcb8-8ad4-47f2-a330-fa56713bdb37)                        | GDI32    | [(d)](#shlwapi-wrapper-functions), [(f)](#dragqueryfile), [(ExtTextOut)](#exttextout)                                               |
| FormatMessageWrapW        | 68      | [**FormatMessage**](https://msdn.microsoft.com/windows/desktop/b9d61342-4bcf-42e9-96f1-a5993dfb6c0c)                 | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(g)](#compareexchange), [(FormatMessage)](#formatmessage)                                       |
| GetClassInfoWrapW         | 69      | [**GetClassInfo**](https://msdn.microsoft.com/windows/desktop/f7eb12c9-ff24-465d-8c6d-8ee5777c05bc)                 | USER32   | [(GetClassInfo)](#getclassinfo)                                                                                                     |
| GetDateFormatWrapW        | 311     | [**GetDateFormat**](https://msdn.microsoft.com/windows/desktop/546cede1-1702-403a-bba3-b5cd3b35a1bf)                 | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(g)](#compareexchange), [(DateTime)](#datetime)                                                 |
| GetDlgItemTextWrapW       | 74      | [**GetDlgItemText**](https://msdn.microsoft.com/windows/desktop/6cfaa693-aafe-4034-abcb-0a8364cccb4b)             | USER32   | [(g)](#compareexchange)                                                                                                             |
| GetFileAttributesWrapW    | 75      | [**GetFileAttributes**](https://msdn.microsoft.com/windows/desktop/9f9bcdbb-1ffd-49c2-92f4-181fdcc9c690)           | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| GetLocaleInfoWrapW        | 77      | [**GetLocaleInfo**](https://msdn.microsoft.com/windows/desktop/091b3f17-ccf7-493c-8992-00425f37d0ec)                 | KERNEL32 | [(g)](#compareexchange)                                                                                                             |
| GetMenuItemInfoWrapW      | 302     | [**GetMenuItemInfo**](https://msdn.microsoft.com/windows/desktop/4a2c9135-510b-4ccf-bdba-35ffabc49d5c)           | USER32   | [(f)](#dragqueryfile), [(g)](#compareexchange), [(MenuItemInfo)](#menuiteminfo)                                                     |
| GetModuleFileNameWrapW    | 80      | [**GetModuleFileName**](https://msdn.microsoft.com/windows/desktop/f124c99f-8be1-4a9c-a84c-b1b323921f1a)         | KERNEL32 | [(c)](#shlwapi-wrapper-functions), [(g)](#compareexchange)                                                                          |
| GetModuleHandleWrapW      | 83      | [**GetModuleHandle**](https://msdn.microsoft.com/windows/desktop/29514410-89fe-4888-8b34-0c30d5af237f)             | KERNEL32 | [(c)](#shlwapi-wrapper-functions), [(g)](#compareexchange)                                                                          |
| GetObjectWrapW            | 84      | [**GetObject**](https://msdn.microsoft.com/windows/desktop/555ab876-d990-426d-915c-f98df82a10aa)                          | GDI32    | [(g)](#compareexchange)                                                                                                             |
| GetOpenFileNameWrapW      | 403     | [**GetOpenFileName**](https://msdn.microsoft.com/windows/desktop/22b8f3d0-455a-4eb8-9835-e90d41924ec7)           | COMDLG32 | [(a)](#shlwapi-wrapper-functions), [(b)](#dialogboxparam), [(g)](#compareexchange), [(OpenFileName)](#openfilename)                 |
| GetSaveFileNameWrapW      | 389     | [**GetSaveFileName**](https://msdn.microsoft.com/windows/desktop/424e9d85-853b-4dc6-a29a-c532a8bb23f7)           | COMDLG32 | [(a)](#shlwapi-wrapper-functions), [(b)](#dialogboxparam), [(g)](#compareexchange), [(OpenFileName)](#openfilename)                 |
| GetSystemDirectoryWrapW   | 81      | [**GetSystemDirectory**](https://msdn.microsoft.com/windows/desktop/79f045b2-40d9-498a-b720-e729c92bf50b)       | KERNEL32 | [(c)](#shlwapi-wrapper-functions), [(g)](#compareexchange)                                                                          |
| GetTimeFormatWrapW        | 310     | [**GetTimeFormat**](https://msdn.microsoft.com/windows/desktop/3db91d29-df97-4660-b3cd-0db5b42cfd01)                 | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(g)](#compareexchange), [(DateTime)](#datetime)                                                 |
| GetWindowLongWrapW        | 94      | [**GetWindowLong**](https://msdn.microsoft.com/windows/desktop/4c2b634d-1df8-44bb-825c-261eb13045ce)               | USER32   | [(WindowLong)](#windowlong)                                                                                                         |
| GetWindowsDirectoryWrapW  | 97      | [**GetWindowsDirectory**](https://msdn.microsoft.com/windows/desktop/8c9b55e1-121a-4405-9f83-043752dd48ed)     | KERNEL32 | [(c)](#shlwapi-wrapper-functions), [(g)](#compareexchange)                                                                          |
| GetWindowTextLengthWrapW  | 96      | [**GetWindowTextLength**](https://msdn.microsoft.com/windows/desktop/dfd05c5b-2e60-4f4f-aa6b-53f723a048be)   | USER32   | [(j)](#j)                                                                                                                           |
| GetWindowTextWrapW        | 95      | [**GetWindowText**](https://msdn.microsoft.com/windows/desktop/461d2200-2e3a-4361-bb2e-9a29ed9f333f)               | USER32   | [(f)](#dragqueryfile), [(g)](#compareexchange)                                                                                      |
| InsertMenuItemWrapW       | 98      | [**InsertMenuItem**](https://msdn.microsoft.com/windows/desktop/be3819c2-8bdc-4a90-a188-ff8b4060eb8f)             | USER32   | [(a)](#shlwapi-wrapper-functions), [(f)](#dragqueryfile), [(Menu)](#menu), [(MenuItemInfo)](#menuiteminfo)                          |
| IsCharAlphaWrapW          | 25      | [**IsCharAlpha**](https://msdn.microsoft.com/windows/desktop/747dd0e0-2d7c-427b-807f-9d0c2de20589)                   | USER32   | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| IsCharAlphaNumericWrapW   | 28      | [**IsCharAlphaNumeric**](https://msdn.microsoft.com/windows/desktop/5c77d035-cef6-4d63-af53-3e5e32a58ed1)     | KERNEL32 | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| IsCharUpperWrapW          | 26      | [**IsCharUpper**](https://msdn.microsoft.com/windows/desktop/cc9ffea1-d14e-4cf8-b036-0b39cf0a7ae7)                   | USER32   | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| LoadLibraryWrapW          | 105     | [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65)                     | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| LoadStringWrapW           | 107     | [**LoadString**](https://msdn.microsoft.com/windows/desktop/9d878af7-a7b1-4d24-89ff-c567e4a8accd)                     | KERNEL32 | [(e)](#shlwapi-wrapper-functions)                                                                                                   |
| MessageBoxWrapW           | 340     | [**MessageBox**](https://msdn.microsoft.com/windows/desktop/4840decc-8173-4021-8d3e-bae3b0eaa956)                     | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| MoveFileWrapW             | 113     | [**MoveFile**](https://msdn.microsoft.com/windows/desktop/baa3cc02-0a61-4463-b2f1-0d7aaefa126b)                             | KERNEL32 | [(a)](#shlwapi-wrapper-functions), [(c)](#shlwapi-wrapper-functions)                                                                |
| OutputDebugStringWrapW    | 115     | [**OutputDebugString**](https://msdn.microsoft.com/windows/desktop/ca23d9a9-65b7-4a36-bd09-857a6997f482)         | KERNEL32 | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| PeekMessageWrapW          | 116     | [**PeekMessage**](https://msdn.microsoft.com/windows/desktop/b9f5baa4-8166-4d6e-b416-df023aed9bad)                   | USER32   | [(PeekMessage and PostMessage)](#peekmessage-and-postmessage)                                                                       |
| PostMessageWrapW          | 117     | [**PostMessage**](https://msdn.microsoft.com/windows/desktop/5357de37-1e44-4e4a-bdae-b5a386032dd4)                   | USER32   | [(PeekMessage and PostMessage)](#peekmessage-and-postmessage)                                                                       |
| RegCreateKeyExWrapW       | 120     | [**RegCreateKeyEx**](https://msdn.microsoft.com/windows/desktop/e9ffad7f-c0b6-44ce-bf22-fbe45ca98bf4)               | ADVAPI32 | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| RegisterClassWrapW        | 131     | [**RegisterClass**](https://msdn.microsoft.com/windows/desktop/485115e5-b4ec-4e93-89ce-eee229ccabb7)               | USER32   | [(a)](#shlwapi-wrapper-functions), [(RegisterClass)](#registerclass)                                                                |
| RegOpenKeyExWrapW         | 125     | [**RegOpenKeyEx**](https://msdn.microsoft.com/windows/desktop/c8a590f2-3249-437f-a320-c7443d42b792)                   | ADVAPI32 | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| RegQueryValueExWrapW      | 128     | [**RegQueryValueEx**](https://msdn.microsoft.com/windows/desktop/202d253a-10ff-40e7-8eec-a49717443b81)             | ADVAPI32 | [(a)](#shlwapi-wrapper-functions), [(g)](#compareexchange), [(ValueEx)](#regqueryvalueexw), [(RegQueryValueExW)](#regqueryvalueexw) |
| RegQueryValueWrapW        | 127     | [**RegQueryValue**](https://msdn.microsoft.com/windows/desktop/18f27717-3bd9-45ac-a1ea-61abc1753a52)                 | ADVAPI32 | [(a)](#shlwapi-wrapper-functions), [(g)](#compareexchange)                                                                          |
| RegSetValueExWrapW        | 130     | [**RegSetValueEx**](https://msdn.microsoft.com/windows/desktop/29b0e27c-4999-4e92-bd8b-bba74920bccc)                 | ADVAPI32 | [(a)](#shlwapi-wrapper-functions), [(ValueEx)](#regqueryvalueexw)                                                                   |
| SendMessageWrapW          | 136     | [**SendMessage**](https://msdn.microsoft.com/windows/desktop/c069c542-f854-41ff-a523-90f3855e2277)                   | USER32   | [(SendMessage)](#sendmessage)                                                                                                       |
| SetDlgItemTextWrapW       | 138     | [**SetDlgItemText**](https://msdn.microsoft.com/windows/desktop/af359c1c-f3ec-4901-97bb-3fb654f44598)             | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| SetWindowLongWrapW        | 141     | [**SetWindowLong**](https://msdn.microsoft.com/windows/desktop/75f6721f-188c-4daa-9410-6cb2d86869fc)               | USER32   | [(WindowLong)](#windowlong)                                                                                                         |
| SetWindowTextWrapW        | 143     | [**SetWindowText**](https://msdn.microsoft.com/windows/desktop/6f3e3ef8-b342-43f0-9d8b-3a72c610a940)               | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |
| ShellExecuteExWrapW       | 35      | [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa)                | SHELL32  | [(a)](#shlwapi-wrapper-functions), [(b)](#dialogboxparam), [(ShellExecuteEx)](#shellexecuteex)                                      |
| ShellMessageBoxWrapW      | 388     | [**ShellMessageBox**](/windows/desktop/api/Shellapi/nf-shellapi-shellmessageboxa)              | SHLWAPI  | [(a)](#shlwapi-wrapper-functions), [(FormatMessage)](#formatmessage)                                                                |
| SHGetFileInfoWrapW        | 313     | [**SHGetFileInfo**](/windows/desktop/api/Shellapi/nf-shellapi-shgetfileinfoa)                  | SHELL32  | [(a)](#shlwapi-wrapper-functions), [(b)](#dialogboxparam), [(g)](#compareexchange)                                                  |
| SHGetPathFromIDListWrapW  | 334     | [**SHGetPathFromIDList**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetpathfromidlista)      | USER32   | [(g)](#compareexchange)                                                                                                             |
| TranslateAcceleratorWrapW | 146     | [**TranslateAccelerator**](https://msdn.microsoft.com/windows/desktop/0d8a970c-68b2-45e6-8702-2490029c1e1d) | USER32   | [(i)](#shlwapi-wrapper-functions)                                                                                                   |
| UnregisterClassWrapW      | 147     | [**UnregisterClass**](https://msdn.microsoft.com/windows/desktop/ce0277a9-082e-49ef-b8fd-779284303ffa)           | USER32   | [(a)](#shlwapi-wrapper-functions)                                                                                                   |



 

The wrapper functions in the following table do not perform any character set conversion. Instead, they provide limited support for operating system features not available on earlier platforms.



| Function                     | Ordinal | Forwards To                                                                     | DLL      | Remarks                                                                        |
|------------------------------|---------|---------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------|
| MLGetUILanguage              | 376     | [**GetUserDefaultUILanguage**](https://msdn.microsoft.com/windows/desktop/0de3a2d8-e595-4068-805c-b9bcba7ada91)                   | KERNEL32 | [(h)](#shlwapi-wrapper-functions)                                              |
| SHCancelTimerQueueTimer      | 265     | [**DeleteTimerQueueTimer**](https://msdn.microsoft.com/windows/desktop/d830fa1f-504a-4921-865c-34dbf0256720)                         | KERNEL32 | [(h)](#shlwapi-wrapper-functions)                                              |
| SHDeleteTimerQueue           | 262     | [**DeleteTimerQueue**](https://msdn.microsoft.com/windows/desktop/29dde4ec-1c95-4417-a8bf-ab9bd56e3f6f)                                   | KERNEL32 | [(h)](#shlwapi-wrapper-functions)                                              |
| SHInterlockedCompareExchange | 342     | [**InterlockedCompareExchangePointer**](https://msdn.microsoft.com/windows/desktop/15c1fadd-9e0d-4254-ae14-82b0ce46909e) | KERNEL32 | [(CompareExchange)](#compareexchange)                                          |
| SHQueueUserWorkItem          | 260     | [**QueueUserWorkItem**](https://msdn.microsoft.com/windows/desktop/96f34b51-3784-4bb7-ae40-067f8113ff39)                                 | KERNEL32 | [(QueueUserWorkItem)](#queueuserworkitem), [(h)](#shlwapi-wrapper-functions)   |
| SHSetTimerQueueTimer         | 263     | [**CreateTimerQueueTimer**](https://msdn.microsoft.com/windows/desktop/dfcbea5c-e2b7-40e4-b1a2-3cc7446d8844)                         | KERNEL32 | [(SetTimerQueueTimer)](#settimerqueuetimer), [(h)](#shlwapi-wrapper-functions) |



 

## Remarks

### (a)

If string conversion is necessary, all strings are converted through the CP\_ACP code page.

These functions employ best-fit characters and do not perform default checking when converting from Unicode to ANSI. Furthermore, if the string cannot be converted from Unicode to ANSI, the wrapper function passes a **NULL** string to the underlying ANSI function. This can occur, for example, when there is insufficient memory. Passing a **NULL** string may cause some functions to fail with an invalid parameter error, but other functions accept the **NULL** string and treat it as the intended parameter. For example, an error occurs when the **CreateWindowExWrapW** function attempts to convert the *lpWindowName* parameter to ANSI, and [**CreateWindowEx**](https://msdn.microsoft.com/windows/desktop/33deeb92-6285-4c67-9338-ca2e194b9915) creates a window with an empty caption. The wrapper does not notify you when these problems have occurred.

The Microsoft Layer for Unicode (MSLU) checks for errors during conversion from Unicode to ANSI and returns appropriate error values. For example, the [**AppendMenu**](https://msdn.microsoft.com/windows/desktop/07da4d45-a816-40c1-a5c5-c7fbe954be57) wrapper function in the MSLU returns 0 if the item was not successfully appended.

### (b)

These functions use a delay-loaded link to the appropriate function. This means that the DLL that contains the function in the "Forwards To" column is not loaded by the Shlwapi.dll until a function in that DLL is called. The Microsoft Visual C++ linker supports this functionality more generally via the /DELAYLOAD option.

### (c)

This function manipulates filenames. As noted in [(a)](#shlwapi-wrapper-functions), the functions convert all strings through the CP\_ACP code page. They do not check whether the file I/O functions have been set to ANSI mode. If the file I/O functions are in OEM mode, the strings will be converted to and from the wrong character set. An application can set the file I/O functions to OEM mode explicitly by calling the [**SetFileApisToOEM**](https://msdn.microsoft.com/windows/desktop/15f657d8-075a-4f0c-a653-73273ea62f5f) function.

**Security Warning:  ** Using these wrapper functions for file names can compromise the security of your application. Since no default checking is performed and best-fit characters are employed, filename characters can be converted in unexpected ways. This could result in file system spoofing attacks. Also, silent data loss can occur during the conversion from Unicode to ANSI.

The MSLU does not have these limitations.

### (d)

If the string being drawn requires a character set that is not available in the font that is selected into the device context, these wrapper functions use the [Font Linking](https://www.bing.com/search?q=Font Linking) feature of the [MLang](https://www.bing.com/search?q=MLang) library to render each character in an appropriate font. Unlike most other wrapper functions, these are functional on Microsoft Windows NT 4.0 in addition to native ANSI platforms.

### (e)

Full Unicode implementations of these functions are available on native ANSI platforms. These functions do not call the related ANSI function.

### (f)

If the user-default UI language uses a different character set than the system-default UI language, the system attempts to rewrite dialog templates and subclass controls and convert menu items to owner-draw, so that strings in the user-default UI language continue to display correctly. The only controls supported by the dialog template rewrite rules are static, button, listbox, and combobox controls. These controls are subclassed such that the **SendMessageWrapW** function can obtain the original Unicode string without being translated through the ANSI character set. Unlike most of the other wrapper functions, these are functional on Microsoft Windows NT 4.0 as well as native ANSI platforms. See the remarks in the documentation of the [**MLLoadLibrary**](/windows/desktop/api/Shlwapi/) function for further discussion of how the user-default UI language and system-default UI language are determined.

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

The syntax for **SHInterlockedCompareExchange** is somewhat different from that of [**InterlockedCompareExchangePointer**](https://msdn.microsoft.com/windows/desktop/15c1fadd-9e0d-4254-ae14-82b0ce46909e), but it functions identically.

``` syntax
void* SHInterlockedCompareExchange(void **ppDest, void *pExch, void *pComp);
```

### (CompareString)

Remember that on native ANSI platforms, both strings are converted to ANSI and compared as ANSI strings. If the Unicode strings contain characters that cannot be represented in ANSI, the results may be unexpected. For example, if the default ANSI code page does not support CJK characters, then the strings L"\\x66F0" and L"\\x6708" would compare as equal on native ANSI platforms because they both map to the ANSI string "?".

### (DateTime)

On Shlwapi.dll version 5.0, which shipped with Windows 2000, the code page of the locale identifier that you pass as the first parameter of **GetDateFormatWrapW** and **GetTimeFormatWrapW** must match the current ANSI codepage. Otherwise, the returned string may be converted incorrectly. This limitation does not apply to Shlwapi.dll versions 5.5 or higher. This means that Windows XP and later systems are not subject to this limitation. The MSLU does not have this limitation.

### (DialogBoxParam)

The *lpTemplateName* parameter for the **DialogBoxParamWrapW** function cannot be a string. It must be an ordinal created by the [**MAKEINTRESOURCE**](https://msdn.microsoft.com/windows/desktop/761df981-776f-43ca-9cc9-bb82a49f66e6) macro. The dialog procedure specified by the *lpDialogFunc* parameter receives ANSI messages on native ANSI platforms and Unicode messages on native Unicode platforms. The dialog procedure must be prepared to handle both cases. The MSLU does not have these limitations.

### (ExtTextOut)

Native ANSI platforms implement the [**ExtTextOutW**](https://msdn.microsoft.com/windows/desktop/74f8fcb8-8ad4-47f2-a330-fa56713bdb37) function as well as native Unicode platforms. The purpose of **ExtTextOutWrapW** is to perform font linking, as described in a separate remark.

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



This code example uses the "!s!" format. On native ANSI platforms, this string is passed to the ANSI version of the [**FormatMessage**](https://msdn.microsoft.com/windows/desktop/b9d61342-4bcf-42e9-96f1-a5993dfb6c0c) function. Consequently, an ANSI string is expected instead of a Unicode string. Similarly, the "%2" format implies a string argument. When it is passed to the ANSI **FormatMessage** function, it is interpreted as an ANSI string rather than a Unicode string. The correct format string is L"%1!ws! %2!ws!". This prints strings correctly on both ANSI and Unicode platforms.

The function does not support the "%0" special format string.

The MSLU does not have these limitations.

### (GetClassInfo)

On native ANSI platforms, the **lpszMenuName** and **lpszClassName** members of the [**WNDCLASS**](https://msdn.microsoft.com/windows/desktop/7e2a4e89-19b6-4ef7-81dd-f44a3874e546) structure are not translated to Unicode and are always set to **NULL**. Furthermore, the window procedure returned in the **lpfnWndProc** member of the **WNDCLASS** structure is not translated to Unicode, and refers to an ANSI window procedure. The MSLU does not have these limitations.

### (Menu)

On Shlwapi.dll version 5.0, which shipped with Windows 2000, menu item strings that contain tab characters (\\t) may not display correctly. This limitation does not apply to Shlwapi.dll versions 5.5 or higher. This means that Windows XP and later systems are not subject to this limitation. The MSLU does not have this limitation.

### (MenuItemInfo)

This function only supports the Microsoft Windows NT 4.0 version of the [**MENUITEMINFOW**](https://www.bing.com/search?q=**MENUITEMINFOW**) structure. This structure lacks an **hbmpItem** member. In addition, the function does not support the MIIM\_BITMAP flag. The MSLU does not have these limitations.

### (OpenFileName)

The **cbSize** member of the [**OPENFILENAMEW**](https://www.bing.com/search?q=**OPENFILENAMEW**) structure must be set to sizeof(OPENFILENAME\_NT4W).

The **lpstrCustomFilter** member of the [**OPENFILENAMEW**](https://www.bing.com/search?q=**OPENFILENAMEW**) structure must be set to **NULL**.

The values of the **nMaxFile** and **nMaxFileTitle** members of the [**OPENFILENAMEW**](https://www.bing.com/search?q=**OPENFILENAMEW**) structure must not exceed MAX\_PATH.

If the **lpfnHook** member of the [**OPENFILENAMEW**](https://www.bing.com/search?q=**OPENFILENAMEW**) structure is not **NULL**, it must refer to an ANSI hook procedure on native ANSI platforms and a Unicode hook procedure on native Unicode platforms.

The MSLU does not have these limitations.

### (PeekMessage and PostMessage)

On native ANSI platforms, no translation is performed on the transmitted or retrieved message. The transmitted/retrieved message is ANSI on native ANSI platforms and Unicode on native Unicode platforms. The calling application must be prepared to handle both cases. For example, if the retrieved message is WM\_CHAR, then the *wParam* is an ANSI character code on native ANSI platforms but it is a Unicode code point on native Unicode platforms. The MSLU does not have these limitations.

### (QueueUserWorkItem)

The **SHQueueUserWorkItem** function is slightly different from the corresponding [**QueueUserWorkItem**](https://msdn.microsoft.com/windows/desktop/96f34b51-3784-4bb7-ae40-067f8113ff39) function. The syntax for **SHQueueUserWorkItem** is shown here.

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

-   The *pfnCallback* and *pContext* parameters have the same meanings as the *Function* and *Context* parameters, respectively, of [**QueueUserWorkItem**](https://msdn.microsoft.com/windows/desktop/96f34b51-3784-4bb7-ae40-067f8113ff39).
-   The *dwTag* parameter is unused and must be set to 0.
-   The *pdwld* parameter is unused and must be set to **NULL**.
-   The *pszModule* parameter points to an optional null-terminated ANSI string that specifies the name of a library to be loaded before the work item begins and unloaded after the work item completes. This parameter can be **NULL**.
-   The *dwFlags* parameter supports only a subset of the values supported by [**QueueUserWorkItem**](https://msdn.microsoft.com/windows/desktop/96f34b51-3784-4bb7-ae40-067f8113ff39). The following flags are recognized.

    

    | Name              | Value      | Meaning                          |
    |-------------------|------------|----------------------------------|
    | TPS\_EXECUTEIO    | 0x00000001 | Same as WT\_EXECUTEINIOTHREAD.   |
    | TPS\_LONGEXECTIME | 0x00000008 | Same as WT\_EXECUTELONGFUNCTION. |

    

     

    > [!Note]  
    > The TPS\_LONGEXECTIME flag does not have the same numerical value as the WT\_EXECUTELONGFUNCTION flag. When using **SHQueueUserWorkItem**, the dwFlags parameter must be a combination of TPS\_\* values, not WT\_\* values.

     

**SHQueueUserWorkItem** returns a nonzero value if the work item was successfully queued and 0 otherwise. If the function fails, you can use [**GetLastError**](https://msdn.microsoft.com/windows/desktop/d852e148-985c-416f-a5a7-27b6914b45d4) to obtain additional information.

### (RegisterClass)

On native ANSI platforms, no translation is performed on the **lpfnWndProc** member of the [**WNDCLASSW**](https://www.bing.com/search?q=**WNDCLASSW**) structure. The window will receive ANSI window messages on native ANSI platforms and Unicode window messages on native Unicode platforms. The window procedure must be prepared to handle both cases. The MSLU does not have these limitations.

### (RegQueryValueExW)

**RegQueryValueExWrapW** has also been called under the name **RegQueryValueExW**. As with any unnamed function exported strictly by ordinal, you can choose the name that the function is known by in your code.

### (SendMessage)

On native Unicode platforms, the **SendMessageWrapW** function forwards to the [**SendMessageW**](https://www.bing.com/search?q=**SendMessageW**) function. On native ANSI platforms, **SendMessageWrapW** provides limited support for translating Unicode messages to ANSI. The list of supported messages is given in the following table. The function will not translate any other messages.

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

-   (c) The specified window handle must be the handle to a [ComboBox](https://www.bing.com/search?q=ComboBox) or [ComboBoxEx](https://www.bing.com/search?q=ComboBoxEx) control. If the handle is to a combobox control that is owner-draw and was not created with the [List Box Styles](https://www.bing.com/search?q=List Box Styles) style, then the translation of this message will fail and may even crash.
-   (d) The specified window handle must be the handle to a listbox control. If the listbox is owner-draw and was not created with the [List Box Styles](https://www.bing.com/search?q=List Box Styles) style, then the translation of this message will fail and may even crash.
-   (e) If string conversion is necessary, all strings are converted through the CP\_ACP code page.

    When converting from ANSI to Unicode for output, the wrapper functions truncate the returned string if it does not fit in the provided buffer. The return value for functions that return the number of characters copied to the buffer or the number of characters necessary to avoid truncation refers to the number of ANSI characters copied to the buffer or required by the underlying ANSI function, not the number of Unicode characters copied to the buffer provided by or required from the calling application that called the wrapper function. The MSLU does not have this limitation. For further details, see [Microsoft Layer for Unicode on Windows 95/98/Me Systems](http://go.microsoft.com/fwlink/p/?linkid=198351).

### (SetTimerQueueTimer)

The **SHSetTimerQueueTimer** function is slightly different from the corresponding [**CreateTimerQueueTimer**](https://msdn.microsoft.com/windows/desktop/dfcbea5c-e2b7-40e4-b1a2-3cc7446d8844) function. Its syntax is as follows:

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
-   The *pfnCallback*, *pContext*, *dwDueTime*, and *dwPeriod* parameters have the same meanings as the *Callback*, *Parameter*, *DueTime*, and *Period* parameters, respectively, of [**CreateTimerQueueTimer**](https://msdn.microsoft.com/windows/desktop/dfcbea5c-e2b7-40e4-b1a2-3cc7446d8844).
-   The *lpszLibrary* parameter is unused and must be set to **NULL**.
-   The *Flags* parameter supports only a subset of the values supported by [**CreateTimerQueueTimer**](https://msdn.microsoft.com/windows/desktop/dfcbea5c-e2b7-40e4-b1a2-3cc7446d8844).

    

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

 

 



