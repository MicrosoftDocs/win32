---
description: The following list are recommended best practices you should use when working with file associations.
title: Best Practices for File Associations
ms.topic: article
ms.date: 05/31/2018
ms.assetid: d4d0edf9-3475-4164-b0fa-15006e05e242
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Best Practices for File Associations

The following list are recommended best practices you should use when working with file associations.

- [Do Not Copy File Associations from the Registry](#do-not-copy-file-associations-from-the-registry)
- [Avoid Hard-Coding Paths into the Registry Where Possible](#avoid-hard-coding-paths-into-the-registry-where-possible)
- [Always Wrap Expanding Strings in Quotation Marks](#always-wrap-expanding-strings-in-quotation-marks)
- [Do Not Confuse Autoplay/Autorun with File Associations](#do-not-confuse-autoplayautorun-with-file-associations)
- [Do Not Confuse the Internet Explorer MIME Database with File Associations](#do-not-confuse-the-internet-explorer-mime-database-with-file-associations)
- [Use Properly Formed and Versioned ProgIDs](#use-properly-formed-and-versioned-progids)
- [Do Not Use Short File Name Extensions](#do-not-use-short-file-name-extensions)
- [Register New File Types in the IANA MIME Database](#register-new-file-types-in-the-iana-mime-database)
- [Sign Up with the Windows Web Service for File Associations](#sign-up-with-the-windows-web-service-for-file-associations)
- [Related topics](#related-topics)

## Do Not Copy File Associations from the Registry

We recommended that you do not copy existing file associations from the registry. This often leads to the propagation of poorly formed file associations. Instead, you should follow the steps outlined in [File Association Sample Scenario](fa-sample-scenarios.md).

## Avoid Hard-Coding Paths into the Registry Where Possible

Just as hard-coding paths into programs can cause problems, hard-coding paths into the registry can also lead to problems. Instead, you should use registry expansion strings (REG\_EXPAND\_SZ) to provide path independence where applicable. For example, instead of using this method:

```
HKEY_CLASSES_ROOT
   MyVendor.MyProgram.1
      DefaultIcon
         (Default) = C:\WINNT\hta.exe,1
```

You should use this method:

```
HKEY_CLASSES_ROOT
   MyVendor.MyProgram.1
      DefaultIcon
         (Default) = "%SYSTEMROOT%\hta.exe,1"
```

## Always Wrap Expanding Strings in Quotation Marks

Expanding strings can contain spaces when they expand. Because spaces are often interpreted as argument delimiters, they cause problems under certain circumstances. For example, a command to invoke MyProgram can be stored in the registry as:

`%SYSTEMROOT%\MyProgram %1 %2`

MyProgram expects that %1 is the full path to a file name, and %2 is a switch to indicate some action. If this command is executed with arguments **C:\\Program Files\\My Documents\\document.txt** and **/print**, and assuming a SYSTEMROOT of C:\\WINNT, it expands to:

`C:\WINNT\MyProgram C:\Program Files\My Documents\document.txt /print`

In this case, MyProgram interprets that the first argument is C:\\Program, and the second argument is Files\\My, which is not the intended behavior. The arguments are interpreted correctly, however, regardless of whether they contain spaces, if the expanding strings are wrapped in quotation marks as follows:

`"%SYSTEMROOT%\MyProgram" "%1" "%2"`

## Do Not Confuse Autoplay/Autorun with File Associations

File Associations are similar to Autoplay/Autorun in some ways. However, Autoplay/Autorun offers separate and distinct facilities from those provided by file associations. For more information see [Creating an AutoRun-enabled CD-ROM Application](autoplay.md).

## Do Not Confuse the Internet Explorer MIME Database with File Associations

File Associations are similar to the Windows Internet Explorer MIME database, in that file types can (and should) include a MIME type definition. However, the Internet Explorer MIME database is separate and distinct from file associations.

## Use Properly Formed and Versioned ProgIDs

Always use [versioned ProgIDs](fa-progids.md), even if there is only one version of the ProgID. Versioned ProgIDs help to avoid ProgID conflicts and overwrites. They also enable different versions of an application to co-exist.

## Do Not Use Short File Name Extensions

Long file name extensions offer the following advantages:

- The limited length of short extensions make them prone to *extension collisions.* An extension collision occurs when the same extension is used to classify multiple file types. Using long extensions significantly decreases the chances of a collision.
- Short file names tend to be somewhat cryptic. Long extensions tend to be more meaningful because additional information can be embedded in the extension.

For more information, see [file name extensions](fa-file-extensions.md).

## Register New File Types in the IANA MIME Database

The Internet Assigned Numbers Authority (IANA) keeps a public database of registered MIME types. When defining a new public file type, we recommended that you also define a MIME type for the file type and register this type with the IANA. There is no cost for registration.

## Sign Up with the Windows Web Service for File Associations

Application developers can sign up with the Windows Web Service that users use to find applications that can operate on specific file types. The process for signing up with the web service is detailed in Windows File Association System on-boarding process (KB 929149).

## Related topics

<dl> <dt>

[File Association Sample Scenario](fa-sample-scenarios.md)
</dt> <dt>

[Guidelines for Managing Default Applications in Windows Vista and Later](vista-managing-defaults.md)
</dt> <dt>

[Default Programs](default-programs.md)
</dt> <dt>

[Set Program Access and Computer Defaults (SPAD)](cpl-setprogramaccess.md)
</dt> </dl>

 

 



