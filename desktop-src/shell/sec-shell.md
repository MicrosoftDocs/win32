---
description: This topic provides information about security considerations related to the Windows Shell.
ms.assetid: eca31652-2659-456d-b082-c84d6fd39094
title: 'Security Considerations: Microsoft Windows Shell'
ms.topic: article
ms.date: 05/31/2018
---

# Security Considerations: Microsoft Windows Shell

This topic provides information about security considerations related to the Windows Shell. This document cannot provide all you need to know about security issues—instead, use it as a starting point and reference for this specific technology area.

The Shell controls a number of important aspects of the system, including several that present potential security risks if they are not properly handled. This topic outlines some of the more common issues and how to address them in your applications. Remember that security is not limited to Internet-based exploits. On shared systems, including systems that are accessible through Terminal Services, you must also ensure that users cannot do anything that could harm others who share the system.

-   [Installing Your Application Properly](#installing-your-application-properly)
-   [Shlwapi](#shlwapi)
-   [Autocomplete](#autocomplete)
-   [ShellExecute, ShellExecuteEx, and Related Functions](#shellexecute-shellexecuteex-and-related-functions)
-   [Moving and Copying Files](#moving-and-copying-files)
-   [Writing Secure Namespace Extensions](#writing-secure-namespace-extensions)
-   [Security Alerts](#security-alerts)
-   [Related topics](#related-topics)

## Installing Your Application Properly

The majority of potential Shell security issues can be mitigated by correctly installing your application.

-   Install the application under the Program Files folder. 

    | Operating System                             | Location                                                                                                                                                                                                                                   |
    |----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Windows XP, Windows Server 2003, and earlier | CSIDL\_PROGRAM\_FILES                                                                                                                                                                                                                      |
    | Windows Vista and later                      | FOLDERID\_ProgramFiles, FOLDERID\_ProgramFilesX86, FOLDERID\_ProgramFilesX64, FOLDERID\_ProgramFilesCommon, FOLDERID\_ProgramFilesCommonX86, or FOLDERID\_ProgramFilesCommonX64. See [**KNOWNFOLDERID**](knownfolderid.md) for specifics. |

    

     

-   Do not store user data under the Program Files folder.

    Use the appropriate data folder for data that is common to all users.

    

    | Operating System                             | Location               |
    |----------------------------------------------|------------------------|
    | Windows XP, Windows Server 2003, and earlier | CSIDL\_COMMON\_APPDATA |
    | Windows Vista and later                      | FOLDERID\_ProgramData  |

    

     

    Use the appropriate user data folder for data that belongs to a particular user.

    

    | Operating System                             | Location                                                   |
    |----------------------------------------------|------------------------------------------------------------|
    | Windows XP, Windows Server 2003, and earlier | CSIDL\_APPDATA, CSIDL\_PERSONAL, and others.               |
    | Windows Vista and later                      | FOLDERID\_RoamingAppData, FOLDERID\_Documents, and others. |

    

     

-   If you must install to a location other than the Program Files folder, make sure that you set access control lists (ACLs) properly so that users do not have access to inappropriate parts of the file system. Any data that is specific to a particular user should have an ACL that prevents any other user from accessing it.
-   When you set up file associations, be sure to properly specify the command line. Use a fully qualified path and wrap any elements that contain white space in quotation marks. Wrap command parameters in separate quotation marks. Otherwise, the string might be incorrectly parsed and the application will not launch properly. Two examples of properly formed command lines are shown here.

    ```
    "C:\Program Files\MyApp\MyApp.exe" "%1" "%2"
    C:\MyAppDir\MyApp\MyApp.exe "%1"
    ```

    

> [!Note]  
> The location of the standard installation folders might vary from system to system. To get the location of a standard folder on a particular Windows Vista or later system, call [**SHGetKnownFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetknownfolderpath) with the appropriate [**KNOWNFOLDERID**](knownfolderid.md) value. In Windows XP, Windows Server 2003, or earlier systems, call [**SHGetFolderLocation**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderlocation) or [**SHGetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha) with the appropriate [**CSIDL**](csidl.md) value.

 

## Shlwapi

The Shell Lightweight API (Shlwapi) includes a number of string manipulation functions. Using these functions incorrectly can lead to unexpectedly truncated strings with no notification of the truncation being returned. In the following cases, the Shlwapi functions should not be used. The listed alternative functions, which pose fewer risks, should be used in their place.



| Shlwapi Function                                                 | Alternative Function                                                                                             |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**StrCat**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcatw),[**StrNCat**](/windows/desktop/api/Shlwapi/nf-shlwapi-strncata)              | [**StringCchCat**](/windows/win32/api/strsafe/nf-strsafe-stringcchcata), [**StringCbCat**](/windows/win32/api/strsafe/nf-strsafe-stringcbcata) and related functions             |
| [**StrCpy**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcpyw), [**StrCpyN**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcpynw)             | [**StringCchCopy**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopya), [**StringCbCopy**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopya) and related functions         |
| [**wnsprintf**](/windows/desktop/api/Shlwapi/nf-shlwapi-wnsprintfa), [**wvnsprintf**](/windows/desktop/api/Shlwapi/nf-shlwapi-wvnsprintfa) | [**StringCchPrintf**](/windows/win32/api/strsafe/nf-strsafe-stringcchprintfa), [**StringCbPrintf**](/windows/win32/api/strsafe/nf-strsafe-stringcbprintfa) and related functions |



 

With functions such as [**PathRelativePathTo**](/windows/desktop/api/Shlwapi/nf-shlwapi-pathrelativepathtoa) that return a file path, always set the size of the buffer to MAX\_PATH characters. Doing so ensures that the buffer is large enough to hold the largest possible file path, plus a terminating null character.

For more information on the alternative string functions, see [About Strsafe.h](../menurc/strsafe-ovw.md).

## Autocomplete

Do not use the Autocomplete feature for passwords.

## ShellExecute, ShellExecuteEx, and Related Functions

There are several Shell functions that you can use to launch applications: [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea), [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa), [**WinExec**](/windows/win32/api/winbase/nf-winbase-winexec), and [**SHCreateProcessAsUserW**](/windows/desktop/api/Shellapi/nf-shellapi-shcreateprocessasuserw). Make sure you provide an unambiguous definition of the application that is to be executed.

-   When providing the executable file's path, provide the fully qualified path. Do not depend on the Shell to locate the file.
-   If you provide a command-line string that contains white space, wrap the string in quotation marks. Otherwise, the parser might interpret a single element that contains spaces as multiple elements.

## Moving and Copying Files

One key to system security is properly assigning ACLs. You also might use encrypted files. Make sure that when you move or copy files, that they are assigned the correct ACL and that they have not been accidentally decrypted. This includes moving files to the **Recycle Bin**, as well as within the file system. Use [**IFileOperation**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileoperation) (Windows Vista or later) or [**SHFileOperation**](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa) (Windows XP and earlier). Do not use [**MoveFile**](/windows/win32/api/winbase/nf-winbase-movefile), which might not set the expected ACL for the destination file.

## Writing Secure Namespace Extensions

Shell namespace extensions are a powerful and flexible way to present data to the user. However, they can cause system failure if they are not correctly written. Some key points to keep in mind:

-   Do not assume that data such as images are formatted correctly.
-   Do not assume that MAX\_PATH is equivalent to the number of *bytes* in a string. It is the number of *characters*.

## Security Alerts

The following table lists some features that can, if used incorrectly, compromise the security of your applications.



| Feature                                                                        | Mitigation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea), [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) | Searches that depend on checking a series of default locations to find a specific file can be used in a spoofing attack. Use a fully qualified path to ensure that you access the desired file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**StrCat**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcatw)                                                       | The first argument, *psz1*, must be large enough to hold *psz2* and the closing '\\0', otherwise a buffer overrun might occur. Use one of the following alternatives instead. [**StringCbCat**](/windows/win32/api/strsafe/nf-strsafe-stringcbcata), [**StringCbCatEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcatexa), [**StringCbCatN**](/windows/win32/api/strsafe/nf-strsafe-stringcbcatna), [**StringCbCatNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcatnexa), [**StringCchCat**](/windows/win32/api/strsafe/nf-strsafe-stringcchcata), [**StringCchCatEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcatexa), [**StringCchCatN**](/windows/win32/api/strsafe/nf-strsafe-stringcchcatna), or [**StringCchCatNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcatnexa).                                                                                                                                                             |
| [**StrCatBuff**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcatbuffa)                                               | The final string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCat**](/windows/win32/api/strsafe/nf-strsafe-stringcbcata), [**StringCbCatEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcatexa), [**StringCbCatN**](/windows/win32/api/strsafe/nf-strsafe-stringcbcatna), [**StringCbCatNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcatnexa), [**StringCchCat**](/windows/win32/api/strsafe/nf-strsafe-stringcchcata), [**StringCchCatEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcatexa), [**StringCchCatN**](/windows/win32/api/strsafe/nf-strsafe-stringcchcatna), or [**StringCchCatNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcatnexa).                                                                                                                                                                                                                                  |
| [**StrCatChainW**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcatchainw)                                           | The final string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCatEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcatexa), [**StringCbCatNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcatnexa), [**StringCchCatEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcatexa), or [**StringCchCatNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcatnexa).                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**StrCpy**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcpyw)                                                       | The first argument, *psz1*, must be large enough to hold *psz2* and the closing '\\0', otherwise a buffer overrun might occur. Use one of the following alternatives instead. [**StringCbCopy**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopya), [**StringCbCopyEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopyexa), [**StringCbCopyN**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopyna), [**StringCbCopyNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopynexa), [**StringCchCopy**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopya), [**StringCchCopyEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopyexa), [**StringCchCopyN**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopyna), or [**StringCchCopyNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopynexa).                                                                                                                                             |
| [**StrCpyN**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcpynw)                                                     | The copied string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCopy**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopya), [**StringCbCopyEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopyexa), [**StringCbCopyN**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopyna), [**StringCbCopyNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopynexa), [**StringCchCopy**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopya), [**StringCchCopyEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopyexa), [**StringCchCopyN**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopyna), [**StringCchCopyNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopynexa).                                                                                                                                                                                                                    |
| [**StrDup**](/windows/desktop/api/Shlwapi/nf-shlwapi-strdupa)                                                       | [**StrDup**](/windows/desktop/api/Shlwapi/nf-shlwapi-strdupa) assumes that *lpsz* is a null-terminated string. Further, the returned string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCat**](/windows/win32/api/strsafe/nf-strsafe-stringcbcata), [**StringCbCopyEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopyexa), [**StringCbCopyN**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopyna), [**StringCbCopyNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopynexa), [**StringCchCopy**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopya), [**StringCchCopyEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopyexa), [**StringCchCopyN**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopyna), or [**StringCchCopyNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcopynexa).                                                                                                                              |
| [**StrNCat**](/windows/desktop/api/Shlwapi/nf-shlwapi-strncata)                                                     | The first argument, *pszFront*, must be large enough to hold *pszBack* and the closing '\\0', otherwise a buffer overrun might occur. Be aware that the last argument, *cchMax*, is the number of characters to copy into *pszFront*, not necessarily the size of the *pszFront* in bytes. Use one of the following alternatives instead. [**StringCbCat**](/windows/win32/api/strsafe/nf-strsafe-stringcbcata), [**StringCbCatEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcatexa), [**StringCbCatN**](/windows/win32/api/strsafe/nf-strsafe-stringcbcatna), [**StringCbCatNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbcatnexa), [**StringCchCat**](/windows/win32/api/strsafe/nf-strsafe-stringcchcata), [**StringCchCatEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcatexa), [**StringCchCatN**](/windows/win32/api/strsafe/nf-strsafe-stringcchcatna), or [**StringCchCatNEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchcatnexa). |
| [**wnsprintf**](/windows/desktop/api/Shlwapi/nf-shlwapi-wnsprintfa)                                                 | The copied string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbPrintf**](/windows/win32/api/strsafe/nf-strsafe-stringcbprintfa), [**StringCbPrintfEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbprintfexa), [**StringCbVPrintf**](/windows/win32/api/strsafe/nf-strsafe-stringcbvprintfa), [**StringCbVPrintfEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbvprintfexa), [**StringCchPrintf**](/windows/win32/api/strsafe/nf-strsafe-stringcchprintfa), [**StringCchPrintfEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchprintfexa), [**StringCchVPrintf**](/windows/win32/api/strsafe/nf-strsafe-stringcchvprintfa), or [**StringCchVPrintfEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchvprintfexa).                                                                                                                                                                                 |
| [**wvnsprintf**](/windows/desktop/api/Shlwapi/nf-shlwapi-wvnsprintfa)                                               | The copied string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbPrintf**](/windows/win32/api/strsafe/nf-strsafe-stringcbprintfa), [**StringCbPrintfEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbprintfexa), [**StringCbVPrintf**](/windows/win32/api/strsafe/nf-strsafe-stringcbvprintfa), [**StringCbVPrintfEx**](/windows/win32/api/strsafe/nf-strsafe-stringcbvprintfexa), [**StringCchPrintf**](/windows/win32/api/strsafe/nf-strsafe-stringcchprintfa), [**StringCchPrintfEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchprintfexa), [**StringCchVPrintf**](/windows/win32/api/strsafe/nf-strsafe-stringcchvprintfa), or [**StringCchVPrintfEx**](/windows/win32/api/strsafe/nf-strsafe-stringcchvprintfexa).                                                                                                                                                                                 |



 

## Related topics

<dl> <dt>

[Microsoft Security](https://www.microsoft.com/security/default.aspx)
</dt> <dt>

[Security Developer Center](https://msdn.microsoft.com/security/)
</dt> <dt>

[Microsoft Solution Accelerators](/previous-versions/tn-archive/cc936627(v=technet.10))
</dt> <dt>

[Security TechCenter](https://technet.microsoft.com/security/default.aspx)
</dt> <dt>

[About Strsafe.h](../menurc/strsafe-ovw.md)
</dt> </dl>

 

 
