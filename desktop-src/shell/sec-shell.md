---
Description: This topic provides information about security considerations related to the Windows Shell.
ms.assetid: eca31652-2659-456d-b082-c84d6fd39094
title: 'Security Considerations: Microsoft Windows Shell'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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
| [**StrCat**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcatw),[**StrNCat**](/windows/desktop/api/Shlwapi/nf-shlwapi-strncata)              | [**StringCchCat**](https://msdn.microsoft.com/windows/desktop/72ddb6ab-8167-4213-815b-bd15b62d6123), [**StringCbCat**](https://msdn.microsoft.com/windows/desktop/6330483b-dc61-4bbf-8ee7-e91a93495bb2) and related functions             |
| [**StrCpy**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcpyw), [**StrCpyN**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcpynw)             | [**StringCchCopy**](https://msdn.microsoft.com/windows/desktop/9cbf6ce6-ef45-4bb9-bc1f-a55db399d34f), [**StringCbCopy**](https://msdn.microsoft.com/windows/desktop/00c99f3e-106b-46a2-afae-517b32b7a960) and related functions         |
| [**wnsprintf**](/windows/desktop/api/Shlwapi/nf-shlwapi-wnsprintfa), [**wvnsprintf**](/windows/desktop/api/Shlwapi/nf-shlwapi-wvnsprintfa) | [**StringCchPrintf**](https://msdn.microsoft.com/windows/desktop/9eaafe87-04da-4273-babb-b16d26bfdf70), [**StringCbPrintf**](https://msdn.microsoft.com/windows/desktop/224c8840-06c6-4144-8f23-8705ac8ef887) and related functions |



 

With functions such as [**PathRelativePathTo**](/windows/desktop/api/Shlwapi/nf-shlwapi-pathrelativepathtoa) that return a file path, always set the size of the buffer to MAX\_PATH characters. Doing so ensures that the buffer is large enough to hold the largest possible file path, plus a terminating null character.

For more information on the alternative string functions, see [About Strsafe.h](https://msdn.microsoft.com/windows/desktop/a104a260-1edb-441a-acf8-e2bd3a7d8235).

## Autocomplete

Do not use the Autocomplete feature for passwords.

## ShellExecute, ShellExecuteEx, and Related Functions

There are several Shell functions that you can use to launch applications: [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea), [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa), [**WinExec**](https://msdn.microsoft.com/windows/desktop/00ac3bd8-59d3-4f7f-8720-e57d05cee056), and [**SHCreateProcessAsUserW**](/windows/desktop/api/Shellapi/nf-shellapi-shcreateprocessasuserw). Make sure you provide an unambiguous definition of the application that is to be executed.

-   When providing the executable file's path, provide the fully qualified path. Do not depend on the Shell to locate the file.
-   If you provide a command-line string that contains white space, wrap the string in quotation marks. Otherwise, the parser might interpret a single element that contains spaces as multiple elements.

## Moving and Copying Files

One key to system security is properly assigning ACLs. You also might use encrypted files. Make sure that when you move or copy files, that they are assigned the correct ACL and that they have not been accidentally decrypted. This includes moving files to the **Recycle Bin**, as well as within the file system. Use [**IFileOperation**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileoperation) (Windows Vista or later) or [**SHFileOperation**](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa) (Windows XP and earlier). Do not use [**MoveFile**](https://msdn.microsoft.com/windows/desktop/baa3cc02-0a61-4463-b2f1-0d7aaefa126b), which might not set the expected ACL for the destination file.

## Writing Secure Namespace Extensions

Shell namespace extensions are a powerful and flexible way to present data to the user. However, they can cause system failure if they are not correctly written. Some key points to keep in mind:

-   Do not assume that data such as images are formatted correctly.
-   Do not assume that MAX\_PATH is equivalent to the number of *bytes* in a string. It is the number of *characters*.

## Security Alerts

The following table lists some features that can, if used incorrectly, compromise the security of your applications.



| Feature                                                                        | Mitigation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea), [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) | Searches that depend on checking a series of default locations to find a specific file can be used in a spoofing attack. Use a fully qualified path to ensure that you access the desired file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**StrCat**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcatw)                                                       | The first argument, *psz1*, must be large enough to hold *psz2* and the closing '\\0', otherwise a buffer overrun might occur. Use one of the following alternatives instead. [**StringCbCat**](https://msdn.microsoft.com/windows/desktop/6330483b-dc61-4bbf-8ee7-e91a93495bb2), [**StringCbCatEx**](https://msdn.microsoft.com/windows/desktop/db9f0731-0f7b-4018-ad07-1abe0bfe71e8), [**StringCbCatN**](https://msdn.microsoft.com/windows/desktop/56ef4ada-52df-48dd-a5e1-f62311be7592), [**StringCbCatNEx**](https://msdn.microsoft.com/windows/desktop/ad1cad70-c548-4b2f-b253-b0af5000df08), [**StringCchCat**](https://msdn.microsoft.com/windows/desktop/72ddb6ab-8167-4213-815b-bd15b62d6123), [**StringCchCatEx**](https://msdn.microsoft.com/windows/desktop/3b829dfa-6ede-47bd-b4d7-fcbf94a26c50), [**StringCchCatN**](https://msdn.microsoft.com/windows/desktop/516b67f9-ab6e-4c23-b04a-01848de09115), or [**StringCchCatNEx**](https://msdn.microsoft.com/windows/desktop/63c9f437-b769-4c5a-9168-d0c458947abc).                                                                                                                                                             |
| [**StrCatBuff**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcatbuffa)                                               | The final string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCat**](https://msdn.microsoft.com/windows/desktop/6330483b-dc61-4bbf-8ee7-e91a93495bb2), [**StringCbCatEx**](https://msdn.microsoft.com/windows/desktop/db9f0731-0f7b-4018-ad07-1abe0bfe71e8), [**StringCbCatN**](https://msdn.microsoft.com/windows/desktop/56ef4ada-52df-48dd-a5e1-f62311be7592), [**StringCbCatNEx**](https://msdn.microsoft.com/windows/desktop/ad1cad70-c548-4b2f-b253-b0af5000df08), [**StringCchCat**](https://msdn.microsoft.com/windows/desktop/72ddb6ab-8167-4213-815b-bd15b62d6123), [**StringCchCatEx**](https://msdn.microsoft.com/windows/desktop/3b829dfa-6ede-47bd-b4d7-fcbf94a26c50), [**StringCchCatN**](https://msdn.microsoft.com/windows/desktop/516b67f9-ab6e-4c23-b04a-01848de09115), or [**StringCchCatNEx**](https://msdn.microsoft.com/windows/desktop/63c9f437-b769-4c5a-9168-d0c458947abc).                                                                                                                                                                                                                                  |
| [**StrCatChainW**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcatchainw)                                           | The final string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCatEx**](https://msdn.microsoft.com/windows/desktop/db9f0731-0f7b-4018-ad07-1abe0bfe71e8), [**StringCbCatNEx**](https://msdn.microsoft.com/windows/desktop/ad1cad70-c548-4b2f-b253-b0af5000df08), [**StringCchCatEx**](https://msdn.microsoft.com/windows/desktop/3b829dfa-6ede-47bd-b4d7-fcbf94a26c50), or [**StringCchCatNEx**](https://msdn.microsoft.com/windows/desktop/63c9f437-b769-4c5a-9168-d0c458947abc).                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**StrCpy**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcpyw)                                                       | The first argument, *psz1*, must be large enough to hold *psz2* and the closing '\\0', otherwise a buffer overrun might occur. Use one of the following alternatives instead. [**StringCbCopy**](https://msdn.microsoft.com/windows/desktop/00c99f3e-106b-46a2-afae-517b32b7a960), [**StringCbCopyEx**](https://msdn.microsoft.com/windows/desktop/28750482-a0ba-43e1-b433-2c850feef051), [**StringCbCopyN**](https://msdn.microsoft.com/windows/desktop/4b97de2a-c8bb-423e-8765-a7f20e6fc61c), [**StringCbCopyNEx**](https://msdn.microsoft.com/windows/desktop/0ef55f41-000c-475a-8227-66df352366fb), [**StringCchCopy**](https://msdn.microsoft.com/windows/desktop/9cbf6ce6-ef45-4bb9-bc1f-a55db399d34f), [**StringCchCopyEx**](https://msdn.microsoft.com/windows/desktop/0965b0f6-9588-4944-98d8-3aca3a3029fc), [**StringCchCopyN**](https://msdn.microsoft.com/windows/desktop/5803c6fa-d1ae-4c3b-8627-162039e8c31f), or [**StringCchCopyNEx**](https://msdn.microsoft.com/windows/desktop/228ddd78-9747-4a9a-b936-abfba6ff2940).                                                                                                                                             |
| [**StrCpyN**](/windows/desktop/api/Shlwapi/nf-shlwapi-strcpynw)                                                     | The copied string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCopy**](https://msdn.microsoft.com/windows/desktop/00c99f3e-106b-46a2-afae-517b32b7a960), [**StringCbCopyEx**](https://msdn.microsoft.com/windows/desktop/28750482-a0ba-43e1-b433-2c850feef051), [**StringCbCopyN**](https://msdn.microsoft.com/windows/desktop/4b97de2a-c8bb-423e-8765-a7f20e6fc61c), [**StringCbCopyNEx**](https://msdn.microsoft.com/windows/desktop/0ef55f41-000c-475a-8227-66df352366fb), [**StringCchCopy**](https://msdn.microsoft.com/windows/desktop/9cbf6ce6-ef45-4bb9-bc1f-a55db399d34f), [**StringCchCopyEx**](https://msdn.microsoft.com/windows/desktop/0965b0f6-9588-4944-98d8-3aca3a3029fc), [**StringCchCopyN**](https://msdn.microsoft.com/windows/desktop/5803c6fa-d1ae-4c3b-8627-162039e8c31f), [**StringCchCopyNEx**](https://msdn.microsoft.com/windows/desktop/228ddd78-9747-4a9a-b936-abfba6ff2940).                                                                                                                                                                                                                    |
| [**StrDup**](/windows/desktop/api/Shlwapi/nf-shlwapi-strdupa)                                                       | [**StrDup**](/windows/desktop/api/Shlwapi/nf-shlwapi-strdupa) assumes that *lpsz* is a null-terminated string. Further, the returned string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCat**](https://msdn.microsoft.com/windows/desktop/6330483b-dc61-4bbf-8ee7-e91a93495bb2), [**StringCbCopyEx**](https://msdn.microsoft.com/windows/desktop/28750482-a0ba-43e1-b433-2c850feef051), [**StringCbCopyN**](https://msdn.microsoft.com/windows/desktop/4b97de2a-c8bb-423e-8765-a7f20e6fc61c), [**StringCbCopyNEx**](https://msdn.microsoft.com/windows/desktop/0ef55f41-000c-475a-8227-66df352366fb), [**StringCchCopy**](https://msdn.microsoft.com/windows/desktop/9cbf6ce6-ef45-4bb9-bc1f-a55db399d34f), [**StringCchCopyEx**](https://msdn.microsoft.com/windows/desktop/0965b0f6-9588-4944-98d8-3aca3a3029fc), [**StringCchCopyN**](https://msdn.microsoft.com/windows/desktop/5803c6fa-d1ae-4c3b-8627-162039e8c31f), or [**StringCchCopyNEx**](https://msdn.microsoft.com/windows/desktop/228ddd78-9747-4a9a-b936-abfba6ff2940).                                                                                                                              |
| [**StrNCat**](/windows/desktop/api/Shlwapi/nf-shlwapi-strncata)                                                     | The first argument, *pszFront*, must be large enough to hold *pszBack* and the closing '\\0', otherwise a buffer overrun might occur. Be aware that the last argument, *cchMax*, is the number of characters to copy into *pszFront*, not necessarily the size of the *pszFront* in bytes. Use one of the following alternatives instead. [**StringCbCat**](https://msdn.microsoft.com/windows/desktop/6330483b-dc61-4bbf-8ee7-e91a93495bb2), [**StringCbCatEx**](https://msdn.microsoft.com/windows/desktop/db9f0731-0f7b-4018-ad07-1abe0bfe71e8), [**StringCbCatN**](https://msdn.microsoft.com/windows/desktop/56ef4ada-52df-48dd-a5e1-f62311be7592), [**StringCbCatNEx**](https://msdn.microsoft.com/windows/desktop/ad1cad70-c548-4b2f-b253-b0af5000df08), [**StringCchCat**](https://msdn.microsoft.com/windows/desktop/72ddb6ab-8167-4213-815b-bd15b62d6123), [**StringCchCatEx**](https://msdn.microsoft.com/windows/desktop/3b829dfa-6ede-47bd-b4d7-fcbf94a26c50), [**StringCchCatN**](https://msdn.microsoft.com/windows/desktop/516b67f9-ab6e-4c23-b04a-01848de09115), or [**StringCchCatNEx**](https://msdn.microsoft.com/windows/desktop/63c9f437-b769-4c5a-9168-d0c458947abc). |
| [**wnsprintf**](/windows/desktop/api/Shlwapi/nf-shlwapi-wnsprintfa)                                                 | The copied string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbPrintf**](https://msdn.microsoft.com/windows/desktop/224c8840-06c6-4144-8f23-8705ac8ef887), [**StringCbPrintfEx**](https://msdn.microsoft.com/windows/desktop/525e1fb5-9dfd-4ec2-a4af-9b9e198b6e17), [**StringCbVPrintf**](https://msdn.microsoft.com/windows/desktop/d6985910-65be-4b68-b410-026cef66c651), [**StringCbVPrintfEx**](https://msdn.microsoft.com/windows/desktop/36f77c17-6244-4357-9361-a04118fcd820), [**StringCchPrintf**](https://msdn.microsoft.com/windows/desktop/9eaafe87-04da-4273-babb-b16d26bfdf70), [**StringCchPrintfEx**](https://msdn.microsoft.com/windows/desktop/e3904cd0-fcb9-4b54-9895-513a95f4a6f7), [**StringCchVPrintf**](https://msdn.microsoft.com/windows/desktop/82cc5a7c-e4c5-4a88-9bb5-d3f02dc3d7f5), or [**StringCchVPrintfEx**](https://msdn.microsoft.com/windows/desktop/07b4eb68-2b50-4c66-af1a-13cc57144e3a).                                                                                                                                                                                 |
| [**wvnsprintf**](/windows/desktop/api/Shlwapi/nf-shlwapi-wvnsprintfa)                                               | The copied string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbPrintf**](https://msdn.microsoft.com/windows/desktop/224c8840-06c6-4144-8f23-8705ac8ef887), [**StringCbPrintfEx**](https://msdn.microsoft.com/windows/desktop/525e1fb5-9dfd-4ec2-a4af-9b9e198b6e17), [**StringCbVPrintf**](https://msdn.microsoft.com/windows/desktop/d6985910-65be-4b68-b410-026cef66c651), [**StringCbVPrintfEx**](https://msdn.microsoft.com/windows/desktop/36f77c17-6244-4357-9361-a04118fcd820), [**StringCchPrintf**](https://msdn.microsoft.com/windows/desktop/9eaafe87-04da-4273-babb-b16d26bfdf70), [**StringCchPrintfEx**](https://msdn.microsoft.com/windows/desktop/e3904cd0-fcb9-4b54-9895-513a95f4a6f7), [**StringCchVPrintf**](https://msdn.microsoft.com/windows/desktop/82cc5a7c-e4c5-4a88-9bb5-d3f02dc3d7f5), or [**StringCchVPrintfEx**](https://msdn.microsoft.com/windows/desktop/07b4eb68-2b50-4c66-af1a-13cc57144e3a).                                                                                                                                                                                 |



 

## Related topics

<dl> <dt>

[Microsoft Security](http://go.microsoft.com/fwlink/p/?linkid=193968)
</dt> <dt>

[Security Developer Center](http://go.microsoft.com/fwlink/p/?linkid=182493)
</dt> <dt>

[Microsoft Solution Accelerators](http://go.microsoft.com/fwlink/p/?linkid=190371)
</dt> <dt>

[Security TechCenter](http://go.microsoft.com/fwlink/p/?linkid=181548)
</dt> <dt>

[About Strsafe.h](https://msdn.microsoft.com/windows/desktop/a104a260-1edb-441a-acf8-e2bd3a7d8235)
</dt> </dl>

 

 



