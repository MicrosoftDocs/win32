---
Description: 'This topic provides information about security considerations related to the Windows Shell.'
ms.assetid: 'eca31652-2659-456d-b082-c84d6fd39094'
title: 'Security Considerations: Microsoft Windows Shell'
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
> The location of the standard installation folders might vary from system to system. To get the location of a standard folder on a particular Windows Vista or later system, call [**SHGetKnownFolderPath**](shgetknownfolderpath.md) with the appropriate [**KNOWNFOLDERID**](knownfolderid.md) value. In Windows XP, Windows Server 2003, or earlier systems, call [**SHGetFolderLocation**](shgetfolderlocation.md) or [**SHGetFolderPath**](shgetfolderpath.md) with the appropriate [**CSIDL**](csidl.md) value.

 

## Shlwapi

The Shell Lightweight API (Shlwapi) includes a number of string manipulation functions. Using these functions incorrectly can lead to unexpectedly truncated strings with no notification of the truncation being returned. In the following cases, the Shlwapi functions should not be used. The listed alternative functions, which pose fewer risks, should be used in their place.



| Shlwapi Function                                                 | Alternative Function                                                                                             |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**StrCat**](strcat.md),[**StrNCat**](strncat.md)              | [**StringCchCat**](menurc.stringcchcat), [**StringCbCat**](menurc.stringcbcat) and related functions             |
| [**StrCpy**](strcpy.md), [**StrCpyN**](strcpyn.md)             | [**StringCchCopy**](menurc.stringcchcopy), [**StringCbCopy**](menurc.stringcbcopy) and related functions         |
| [**wnsprintf**](wnsprintf.md), [**wvnsprintf**](wvnsprintf.md) | [**StringCchPrintf**](menurc.stringcchprintf), [**StringCbPrintf**](menurc.stringcbprintf) and related functions |



 

With functions such as [**PathRelativePathTo**](pathrelativepathto.md) that return a file path, always set the size of the buffer to MAX\_PATH characters. Doing so ensures that the buffer is large enough to hold the largest possible file path, plus a terminating null character.

For more information on the alternative string functions, see [About Strsafe.h](menurc.strsafe_ovw).

## Autocomplete

Do not use the Autocomplete feature for passwords.

## ShellExecute, ShellExecuteEx, and Related Functions

There are several Shell functions that you can use to launch applications: [**ShellExecute**](shellexecute.md), [**ShellExecuteEx**](shellexecuteex.md), [**WinExec**](base.winexec), and [**SHCreateProcessAsUserW**](shcreateprocessasuserw.md). Make sure you provide an unambiguous definition of the application that is to be executed.

-   When providing the executable file's path, provide the fully qualified path. Do not depend on the Shell to locate the file.
-   If you provide a command-line string that contains white space, wrap the string in quotation marks. Otherwise, the parser might interpret a single element that contains spaces as multiple elements.

## Moving and Copying Files

One key to system security is properly assigning ACLs. You also might use encrypted files. Make sure that when you move or copy files, that they are assigned the correct ACL and that they have not been accidentally decrypted. This includes moving files to the **Recycle Bin**, as well as within the file system. Use [**IFileOperation**](ifileoperation.md) (Windows Vista or later) or [**SHFileOperation**](shfileoperation.md) (Windows XP and earlier). Do not use [**MoveFile**](fs.movefile), which might not set the expected ACL for the destination file.

## Writing Secure Namespace Extensions

Shell namespace extensions are a powerful and flexible way to present data to the user. However, they can cause system failure if they are not correctly written. Some key points to keep in mind:

-   Do not assume that data such as images are formatted correctly.
-   Do not assume that MAX\_PATH is equivalent to the number of *bytes* in a string. It is the number of *characters*.

## Security Alerts

The following table lists some features that can, if used incorrectly, compromise the security of your applications.



| Feature                                                                        | Mitigation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ShellExecute**](shellexecute.md), [**ShellExecuteEx**](shellexecuteex.md) | Searches that depend on checking a series of default locations to find a specific file can be used in a spoofing attack. Use a fully qualified path to ensure that you access the desired file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**StrCat**](strcat.md)                                                       | The first argument, *psz1*, must be large enough to hold *psz2* and the closing '\\0', otherwise a buffer overrun might occur. Use one of the following alternatives instead. [**StringCbCat**](menurc.stringcbcat), [**StringCbCatEx**](menurc.stringcbcatex), [**StringCbCatN**](menurc.stringcbcatn), [**StringCbCatNEx**](menurc.stringcbcatnex), [**StringCchCat**](menurc.stringcchcat), [**StringCchCatEx**](menurc.stringcchcatex), [**StringCchCatN**](menurc.stringcchcatn), or [**StringCchCatNEx**](menurc.stringcchcatnex).                                                                                                                                                             |
| [**StrCatBuff**](strcatbuff.md)                                               | The final string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCat**](menurc.stringcbcat), [**StringCbCatEx**](menurc.stringcbcatex), [**StringCbCatN**](menurc.stringcbcatn), [**StringCbCatNEx**](menurc.stringcbcatnex), [**StringCchCat**](menurc.stringcchcat), [**StringCchCatEx**](menurc.stringcchcatex), [**StringCchCatN**](menurc.stringcchcatn), or [**StringCchCatNEx**](menurc.stringcchcatnex).                                                                                                                                                                                                                                  |
| [**StrCatChainW**](strcatchainw.md)                                           | The final string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCatEx**](menurc.stringcbcatex), [**StringCbCatNEx**](menurc.stringcbcatnex), [**StringCchCatEx**](menurc.stringcchcatex), or [**StringCchCatNEx**](menurc.stringcchcatnex).                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**StrCpy**](strcpy.md)                                                       | The first argument, *psz1*, must be large enough to hold *psz2* and the closing '\\0', otherwise a buffer overrun might occur. Use one of the following alternatives instead. [**StringCbCopy**](menurc.stringcbcopy), [**StringCbCopyEx**](menurc.stringcbcopyex), [**StringCbCopyN**](menurc.stringcbcopyn), [**StringCbCopyNEx**](menurc.stringcbcopynex), [**StringCchCopy**](menurc.stringcchcopy), [**StringCchCopyEx**](menurc.stringcchcopyex), [**StringCchCopyN**](menurc.stringcchcopyn), or [**StringCchCopyNEx**](menurc.stringcchcopynex).                                                                                                                                             |
| [**StrCpyN**](strcpyn.md)                                                     | The copied string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCopy**](menurc.stringcbcopy), [**StringCbCopyEx**](menurc.stringcbcopyex), [**StringCbCopyN**](menurc.stringcbcopyn), [**StringCbCopyNEx**](menurc.stringcbcopynex), [**StringCchCopy**](menurc.stringcchcopy), [**StringCchCopyEx**](menurc.stringcchcopyex), [**StringCchCopyN**](menurc.stringcchcopyn), [**StringCchCopyNEx**](menurc.stringcchcopynex).                                                                                                                                                                                                                    |
| [**StrDup**](strdup.md)                                                       | [**StrDup**](strdup.md) assumes that *lpsz* is a null-terminated string. Further, the returned string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbCat**](menurc.stringcbcat), [**StringCbCopyEx**](menurc.stringcbcopyex), [**StringCbCopyN**](menurc.stringcbcopyn), [**StringCbCopyNEx**](menurc.stringcbcopynex), [**StringCchCopy**](menurc.stringcchcopy), [**StringCchCopyEx**](menurc.stringcchcopyex), [**StringCchCopyN**](menurc.stringcchcopyn), or [**StringCchCopyNEx**](menurc.stringcchcopynex).                                                                                                                              |
| [**StrNCat**](strncat.md)                                                     | The first argument, *pszFront*, must be large enough to hold *pszBack* and the closing '\\0', otherwise a buffer overrun might occur. Be aware that the last argument, *cchMax*, is the number of characters to copy into *pszFront*, not necessarily the size of the *pszFront* in bytes. Use one of the following alternatives instead. [**StringCbCat**](menurc.stringcbcat), [**StringCbCatEx**](menurc.stringcbcatex), [**StringCbCatN**](menurc.stringcbcatn), [**StringCbCatNEx**](menurc.stringcbcatnex), [**StringCchCat**](menurc.stringcchcat), [**StringCchCatEx**](menurc.stringcchcatex), [**StringCchCatN**](menurc.stringcchcatn), or [**StringCchCatNEx**](menurc.stringcchcatnex). |
| [**wnsprintf**](wnsprintf.md)                                                 | The copied string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbPrintf**](menurc.stringcbprintf), [**StringCbPrintfEx**](menurc.stringcbprintfex), [**StringCbVPrintf**](menurc.stringcbvprintf), [**StringCbVPrintfEx**](menurc.stringcbvprintfex), [**StringCchPrintf**](menurc.stringcchprintf), [**StringCchPrintfEx**](menurc.stringcchprintfex), [**StringCchVPrintf**](menurc.stringcchvprintf), or [**StringCchVPrintfEx**](menurc.stringcchvprintfex).                                                                                                                                                                                 |
| [**wvnsprintf**](wvnsprintf.md)                                               | The copied string is not guaranteed to be null-terminated. Use one of the following alternatives instead. [**StringCbPrintf**](menurc.stringcbprintf), [**StringCbPrintfEx**](menurc.stringcbprintfex), [**StringCbVPrintf**](menurc.stringcbvprintf), [**StringCbVPrintfEx**](menurc.stringcbvprintfex), [**StringCchPrintf**](menurc.stringcchprintf), [**StringCchPrintfEx**](menurc.stringcchprintfex), [**StringCchVPrintf**](menurc.stringcchvprintf), or [**StringCchVPrintfEx**](menurc.stringcchvprintfex).                                                                                                                                                                                 |



 

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

[About Strsafe.h](menurc.strsafe_ovw)
</dt> </dl>

 

 



