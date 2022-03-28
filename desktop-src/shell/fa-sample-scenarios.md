---
description: In the following example, a hypothetical software development company called Litware, Inc.
ms.assetid: e4392907-a84f-40ea-aa88-2ad0510bca3c
title: File Association Example
ms.topic: article
ms.date: 05/31/2018
---

# File Association Example

In the following example, a hypothetical software development company called Litware, Inc. creates a new audio player called LitwarePlayer. Litware wants to design a file association between LitwarePlayer and its primary file type, which uses a newly developed audio format that enables an entire audio CD to be stored in less than 10 kilobytes of memory with no loss of quality.

> [!IMPORTANT]
> This topic does not apply for Windows 10. The way that default file associations work changed in Windows 10. For more information, see the section on **Changes to how Windows 10 handles default apps** in [this post](https://blogs.windows.com/windows-insider/2015/05/20/announcing-windows-10-insider-preview-build-10122-for-pcs/).

 

## Designing a New File Association

The company should take the following steps.

1.  **Decide if the new file type should be treated as public or private.** This new file type is a media type. Because users exchange media files across various platforms and there might be other applications that need to read the LitwarePlayer format, a [public](fa-file-types.md) file type is the most appropriate.
2.  **Determine whether this file type is already defined.** Check the Internet Assigned Numbers Authority (IANA) MIME database, and other public file type databases on the Internet to determine that no comparable file type has been defined. Because this is a new file format, you need to define a new file type.
3.  **Define a file name extension for the new file type.** The developers choose the `.opa-ltw-audio`, which incorporates their vendor abbreviation and a hint about the what the file contains. Research determines that the extension is not being used by anyone else. Following current recommendations, no short extension is defined.
4.  **Define a MIME type for the file type and register it with the IANA.** Litware defines the new MIME type as *audio/LitwarePlayer.1* and prepares a MIME type application, following the guidelines laid out in Request for Comments (RFC) numbers 2045, 2046, 2047, and 2048. They then submit the application to the IANA, which adds the new file type to the database of registered MIME types.
5.  **Determine whether a ProgID exists for the file type.** Because this is a new file type, no [ProgID](fa-progids.md) exists for it. Litware sets about designing a new ProgID for LitwarePlayer. They decide on the friendly name "LitwarePlayer Audio Player" (which is stored as a resource in the LitwarePlayer.exe file), and they design a default icon to use for files associated with LitwarePlayer (also stored in LitwarePlayer.exe). Because LitwarePlayer is a new application, this is a version 1 ProgID.
6.  **Register the ProgID.** When LitwarePlayer is installed, the installation program creates the following [ProgID](fa-progids.md) entry in the registry.

    ```
    HKEY_CLASSES_ROOT
       Litware.LitwarePlayer.1
          (Default) = LitwarePlayer Audio Player
          FriendlyTypeName = @LitwarePlayer, -120
          CurVer
             (Default) = Litware.LitwarePlayer.1
          DefaultIcon
             (Default) = LitwarePlayer, -142
          shell
             play
                command
                   (Default) = "%ProgramFiles%\LitwarePlayer\LitwarePlayer.exe" "%1"
    ```

    In the command key, %1 is passed as the path to the file to play.

7.  **Register the file name extension for the file type.** When LitwarePlayer is installed, the installation program creates the following entries in the registry for its custom file type extension.

    ```
    HKEY_CLASSES_ROOT
       .opa-vwi-audio
          (Default) = Litware.LitwarePlayer.1
          PerceivedType = Audio
          Content Type = audio/LitwarePlayer
    ```

> [!Note]  
> Whenever a file association is created or changed, notify the system that a change has been made by calling [**SHChangeNotify**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotify), specifying the SHCNE\_ASSOCCHANGED event. If this is not done, the Shell might not recognize any changes made until the system restarts.

 

## Additional Resources

- [Introduction to File Associations](fa-intro.md)
- [How to Register an Internet Browser or Email Client With the Windows Start Menu](start-menu-reg.md)
- [Registering an Application to a URI Scheme](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767914(v=vs.85))

## Related topics

<dl> <dt>

[Best Practices for File Associations](fa-best-practices.md)
</dt> <dt>

[Guidelines for Managing Default Applications in Windows Vista and Later](vista-managing-defaults.md)
</dt> <dt>

[Default Programs](default-programs.md)
</dt> <dt>

[Set Program Access and Computer Defaults (SPAD)](cpl-setprogramaccess.md)
</dt> </dl>

 

 
