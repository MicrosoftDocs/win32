---
title: Using Version Information
description: This topic discusses how to use the version information functions.
ms.assetid: 447b57c9-9e94-4a28-897e-f7b87d9cb25a
keywords:
- resources,version information
- version information
- installation file information
ms.topic: article
ms.date: 05/31/2018
---

# Using Version Information

An installation program typically has the following goals:

-   To place files in the correct location.
-   To notify the user if the installation program is replacing an existing file with a version that is significantly different—for example, replacing a German-language file with an English-language file, or replacing a newer file with an older file.

When writing the installation program, you must have the following information for each file:

-   The name and location of the file (referred to as the source file).
-   The name of the equivalent file on the user's hard disk (referred to as the destination file). This name is usually the same as the filename on the installation disk.
-   The sharing status of the file—that is, whether the file is private to the application being installed or could be shared by multiple applications.

The installation program can use the [**VerFindFile**](/windows/desktop/api/Winver/nf-winver-verfindfilea) function to determine where the file should be copied on the disk. This function can also be used to specify whether the file is private to the application or can be shared. If a problem occurs in finding the file, **VerFindFile** returns an error value. For example, if the system is using the destination file, **VerFindFile** returns **VFF\_FILEINUSE**. The installation program must notify the user of the problem and respond to the user's decision to continue or to end the installation.

The [**VerInstallFile**](/windows/desktop/api/Winver/nf-winver-verinstallfilea) function copies the source file to a temporary file in the directory specified by [**VerFindFile**](/windows/desktop/api/Winver/nf-winver-verfindfilea). If necessary, **VerInstallFile** expands the file by using the functions in the data decompression library.

[**VerInstallFile**](/windows/desktop/api/Winver/nf-winver-verinstallfilea) compares the version information of the temporary file to that of the destination file. If the two differ, **VerInstallFile** returns one or more error values. For example, it returns **VIF\_SRCOLD** if the temporary file is older than the destination file and **VIF\_DIFFLANG** if the files have different language identifiers or code-page values. The installation program must notify the user of the problem and respond to the user's decision to continue or to end the installation.

Some [**VerInstallFile**](/windows/desktop/api/Winver/nf-winver-verinstallfilea) errors are recoverable. That is, the installation program can call **VerInstallFile** again, specifying the **VIFF\_FORCEINSTALL** option, to install the file regardless of the version conflict. If **VerInstallFile** returns **VIF\_TEMPFILE** and the user chooses not to force the installation, the installation program should delete the temporary file.

[**VerInstallFile**](/windows/desktop/api/Winver/nf-winver-verinstallfilea) could encounter a nonrecoverable error when attempting to force installation, even though the error did not exist previously. For example, the file could be locked by another user before the installation program attempted to force installation. If an installation program attempts to force installation after a non-recoverable error, **VerInstallFile** fails. The installation program must contain routines to recover from this type of error.

The recommended solution is to display a dialog box with the buttons **Install**, **Skip**, and **Install All**. (Another solution is a dialog box with the buttons **Yes**, **Yes to All**, **Skip**, and **Cancel**.) The **Install All** button should prevent the installation program from prompting the user about similar errors by including the **VIFF\_FORCEINSTALL** option in all subsequent uses of [**VerInstallFile**](/windows/desktop/api/Winver/nf-winver-verinstallfilea). For nonrecoverable errors, the **Install** and **Install All** buttons should be disabled.

To display a useful error message to the user, the installation program usually must retrieve information from the version resources of the conflicting files. There are four functions the installation program can use for this purpose:

-   [**GetFileVersionInfoSize**](/windows/desktop/api/Winver/nf-winver-getfileversioninfosizea)
-   [**GetFileVersionInfo**](/windows/desktop/api/Winver/nf-winver-getfileversioninfoa)
-   [**VerQueryValue**](/windows/desktop/api/Winver/nf-winver-verqueryvaluea)
-   [**VerLanguageName**](/windows/desktop/api/Winver/nf-winver-verlanguagenamea)

[**GetFileVersionInfoSize**](/windows/desktop/api/Winver/nf-winver-getfileversioninfosizea) returns the size of the version information. [**GetFileVersionInfo**](/windows/desktop/api/Winver/nf-winver-getfileversioninfoa) uses information retrieved by **GetFileVersionInfoSize** to retrieve a structure that contains the version information. [**VerQueryValue**](/windows/desktop/api/Winver/nf-winver-verqueryvaluea) retrieves a specific member from that structure.

For example, if [**VerInstallFile**](/windows/desktop/api/Winver/nf-winver-verinstallfilea) returns the **VIF\_DIFFTYPE** error, the installation program should use the [**GetFileVersionInfoSize**](/windows/desktop/api/Winver/nf-winver-getfileversioninfosizea), [**GetFileVersionInfo**](/windows/desktop/api/Winver/nf-winver-getfileversioninfoa), and [**VerQueryValue**](/windows/desktop/api/Winver/nf-winver-verqueryvaluea) functions on the temporary and destination files to obtain the general type of each file. If the languages of the files conflict, the installation program should also use [**VerLanguageName**](/windows/desktop/api/Winver/nf-winver-verlanguagenamea) to translate the binary language identifier into a text representation of the language. (For example, 0x040C translates to the string "French.")

If [**VerInstallFile**](/windows/desktop/api/Winver/nf-winver-verinstallfilea) returns a file error, such as **VIF\_ACCESSVIOLATION**, the installation program should use the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function to retrieve the most recent error value. The program should translate this value into an informative message to display to the user. The program must not yield control between the calls to **VerInstallFile** and **GetLastError**.

 

 