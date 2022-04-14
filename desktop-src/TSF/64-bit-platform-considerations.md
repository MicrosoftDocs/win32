---
title: 64-Bit Considerations
description: With the increasing availability of 64-bit Windows, users expect input methods, such as international keyboards in various languages or Input Method Editors (IMEs) in East Asian languages, to work properly with both 32-bit and 64-bit applications.
ms.assetid: 6a99ad45-202c-4fbb-9707-341bc9fde21e
keywords:
- Text Services Framework (TSF),64-bit Windows
- TSF (Text Services Framework),64-bit Windows
- text services,64-bit Windows
- 64-bit Windows
- Text Services Framework (TSF),Input Method Editor (IME)
- TSF (Text Services Framework),Input Method Editor (IME)
- text services,Input Method Editor (IME)
- Input Method Editor (IME)
- IME (Input Method Editor)
- Text Services Framework (TSF),international keyboards
- TSF (Text Services Framework),international keyboards
- text services,international keyboards
- international keyboards
ms.topic: article
ms.date: 05/31/2018
---

# 64-Bit Considerations

With the increasing availability of 64-bit Windows, users expect input methods, such as international keyboards in various languages or Input Method Editors (IMEs) in East Asian languages, to work properly with both 32-bit and 64-bit applications. When developing input method components or text services for Microsoft Windows, it is important to consider 64-bit Windows as a potential target platform for your product.

Because IMEs and text services (based on the Text Services Framework) are typically implemented as dynamic-link libraries (DLLs), it is important to note that DLLs are built specifically for use in either 32-bit environments or 64-bit environments; a DLL built for use in 32-bit environments cannot be used by 64-bit applications, and vice versa.

> [!Note]  
> WOW64 does not mitigate this bit-specific DLL restriction. For information about WOW64, see [Running 32-bit Applications](/windows/desktop/WinProg64/running-32-bit-applications).

 

This topic discusses important design considerations for developing IMEs and text services for use on 64-bit Windows.

## 64-Bit Considerations for IMEs

This section describes the special considerations involved with building IMEs for use with 64-bit Windows. For information about IMEs, see [Input Method Editor](/previous-versions/windows/desktop/dnacc/input-method-editor-and-text-services-framework-accessibility).

## Building 32-Bit and 64-Bit Versions of an IME

Because of the previously mentioned 32-bit/64-bit compatibility issue with DLLs, some precautions must be taken to ensure that IMEs work transparently with any application (32-bit or 64-bit) running on 64-bit Windows. The recommended solution for enabling your IME to work transparently with both 32-bit and 64-bit applications on a 64-bit platform is to build and install parallel 32-bit and 64-bit versions of the IME DLL. Typically, developers build parallel DLLs from a single source by adjusting the target platform settings in their build environment. For more information about single-sourcing 32-bit and 64-bit applications, see [Getting Ready for 64-bit Windows](/windows/desktop/WinProg64/getting-ready-for-64-bit-windows).

## Side-by-Side Installation of 64-Bit and 32-Bit Input Method Editors

Developers of IMEs and text services should be aware of the 64-bit considerations described throughout this topic. Fortunately, end users of these services need not be concerned with these implementation-specific details. A feature of 64-bit Windows is the ability to hide the need for 64-bit and 32-bit-specific versions of the IME DLLs from end users. When both versions of the IME are properly installed in a side-by-side manner, 64-bit Windows recognizes the presence of both 64-bit and 32-bit versions of the IME and presents these bit-specific IMEs to the end user as a single *logical* IME. When an end user needs to use an IME, 64-bit Windows transparently chooses the version of the IME (32-bit or 64-bit) that is appropriate for the given circumstances.

For side-by-side installations of 64-bit and 32-bit IMEs to function properly (that is, to represent the two platform-specific DLLs as a single logical IME to the user), the following conditions must be met:

-   Developers must build platform-specific versions (one for 32-bit Windows and one for 64-bit Windows) of the IME DLL.
-   The 32-bit and 64-bit DLLs must share the same file name.
-   Installation directory requirements must be followed. For more information, see Installation Directory Requirements.

Side-by-side installations of 32-bit and 64-bit IME DLLs share the same registry key for storing configuration data (including the DLL file name):


```C++
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layouts
```



The [**ImmInstallIME**](/windows/desktop/api/imm/nf-imm-imminstallimea) function is used to create this registry key. The setup and installation program for an IME must call this function to register the IME as a supported keyboard layout. The **ImmInstallIME** function should be called only once, either from the 32-bit or 64-bit version of the IME DLL.

## Mismatched IME DLLs

Installing only the 32-bit version of an IME on 64-bit Windows is neither recommended nor supported. If a 64-bit application attempts to load a 32-bit IME, the IME fails silently when the application attempts to load the associated keyboard layout.

> [!IMPORTANT]
>
> No warning dialog or message displays when a 64-bit application/32-bit IME conflict error occurs.

 

64-Bit Considerations for Text Services

This section describes the special considerations involved with building text services for use in 64-bit environments. For more information about text services and the Text Services Framework, see [Text Services Framework](text-services-framework.md).

## Building 32-Bit and 64-Bit Text Services

A text service is implemented as a Component Object Model (COM) object exposed on a DLL. Consequently, 32-bit/64-bit DLL conflicts can occur with text services installed on 64-bit Windows. Just as with IMEs, the recommended solution for enabling your text service to work transparently with both 32-bit and 64-bit applications on a 64-bit platform is to build and install parallel 32-bit and 64-bit versions of the text service DLL.

## Side-by-Side Installation of 64-Bit and 32-Bit Text Services

For a 32-bit version and a 64-bit version of a text service to be installed side-by-side and represented to the user as a single, logical text service, the following conditions must be met:

-   Both versions of the text service specify the same class identifier (CLSID) when they are registered with the COM subsystem.
-   Both versions of the text service are registered independently. For more information, see [Registering COM Applications](/windows/desktop/com/registering-com-applications).

When a 32-bit text service is registered with 64-bit Windows, the registration operation is transparently redirected to the following registry key:


```C++
HKEY_CLASS_ROOT\Wow6432Node\CLSID
```



[Registry Redirector](/windows/desktop/WinProg64/registry-redirector)


```C++
HKEY_LOCAL_MACHINE\Software\Microsoft\CTF\TIP
```



[ITfInputProcessorProfiles](/windows/desktop/api/Msctf/nn-msctf-itfinputprocessorprofiles)[Text Service Registration](text-service-registration.md)

The 64-bit version and the 32-bit version of a text service might be in use simultaneously. In cases where both versions of a text service need to manipulate any shared objects, coordination for access shared objects should be designed into the text service. Each text service is responsible for managing any shared objects that are used or needed.

## Installing Only 32-Bit Text Services on 64-Bit Windows

Installing only the 32-bit version of a text service on a 64-bit Windows platform is neither recommended nor supported. Because of the registration mapping that is done on 64-bit Windows platforms, a 64-bit application can enumerate the services of a 32-bit Text Service through the **ITfInputProcessorProfiles** interface. However, if a 64-bit application attempts to load a 32-bit text service, the load fails silently.

> [!IMPORTANT]
>
> No warning dialog or message displays when a 64-bit application/32-bit text service conflict error occurs.

 

Other Considerations

## Installation Directory Requirements

This section describes requirements for where to install IME and text service binary files. If these requirements are not followed, your text service or IME might not function correctly.

**IME DLLs**

On 64-bit Windows platforms, install the 32-bit and 64-bit IME DLLs in the following directories:

-   Install 32-bit IME DLLs in the SysWOW64 system directory; call [**GetSystemWow64Directory**](/windows/desktop/api/wow64apiset/nf-wow64apiset-getsystemwow64directorya), or [**SHGetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha) with **CSIDL\_SYSTEMX86** to retrieve this directory path. Alternately, if you are using [Windows Installer](/windows/desktop/Msi/about-windows-installer), use the [**SystemFolder**](/windows/desktop/Msi/systemfolder) property.
-   Install 64-bit IME DLLs in the System32 system directory; call [**GetSystemDirectory**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya), or **SHGetFolderPath** with [CSIDL\_SYSTEM](/windows/desktop/shell/csidl) to retrieve this directory path. Or, for Windows Installer, use the [**System64Folder**](/windows/desktop/Msi/system64folder) property.

**Text Service DLLs and Related Binary Files**

On 64-bit Windows platforms, install the 32-bit and 64-bit text service DLLs, as well as any other binary files related to your text service or IME, in the following directories:

-   Install 32-bit text service DLLs and any other 32-bit binary files in a subdirectory in the Program Files (x86) directory; call **SHGetFolderPath** with **CSIDL\_PROGRAM\_FILESX86** to retrieve this directory path. Or, for Windows Installer, use the [**ProgramFilesFolder**](/windows/desktop/Msi/programfilesfolder) property.
-   Install 64-bit text service DLLs and any other 64-bit binary files in a subdirectory under the Program Files directory; call **SHGetFolderPath** with **CSIDL\_PROGRAM\_FILES** to retrieve this directory path. Or, for Windows Installer, use the [**ProgramFiles64Folder**](/windows/desktop/Msi/programfiles64folder) property.

If you are not using a Windows Installer package to install your IME or text service, it is strongly recommnded that you use a 64-bit installation application. The WOW64 file system redirector might cause 32-bit installers to place files in the wrong directories (for example, WOW64 file system redirection might cause files intended for the System32 directory to be installed in the SysWOW64 directory instead). If you must use a 32-bit installer, disable WOW64 file redirection during the installation process to ensure that the file-redirector service does not cause any unintended redirection during the installation process. For information about the WOW64 file system redirector, see [File System Redirector](/windows/desktop/WinProg64/file-system-redirector). For information about how to disable or enable WOW64 file system redirection, see [**Wow64EnableWow64FsRedirection**](/windows/win32/api/wow64apiset/nf-wow64apiset-wow64enablewow64fsredirection).

> [!TIP]
>
> Avoid hard-coded installation paths. For more information, see [Locate Directories Using the Application Programming Interface Not Hard-Coded Paths](/previous-versions//ms675638(v=vs.85))

 

> [!IMPORTANT]
>
> Do not install any IME or text service files in the special directory %WINDIR%\\IME (by default, c:\\Windows\\IME ). This directory contains system files that support text services and IMEs; it is not intended to contain any third-party IME or text service files, and WOW64 file system redirection is not supported for this directory.

 

## Dual Ctfmon.exe Processes Run on 64-Bit Windows Platforms

The ctfmon.exe process manages the Text Services Framework on the desktop and also provides the language bar user interface (UI). On 64-bit Windows, a 32-bit version and a 64-bit version of the ctfmon.exe process run simultaneously. The 64-bit ctfmon.exe process manages 64-bit text services, and, likewise, the 32-bit ctfmon.exe process manages 32-bit text services.

## Display Behavior for Different Versions of the Language Bar UI

On 64-bit Windows, only the language bar UI associated with the 64-bit version of a text service is ever shown. In cases where a 32-bit application is using the 32-bit version of a text service, 64-bit Windows automatically inserts the language bar UI for the equivalent 64-bit text service. This ensures that no special work is required for 32-bit text services to appear in the 64-bit version of the language bar.

## Control Panel Considerations on 64-Bit Windows

64-bit Windows provides access to both 32-bit and 64-bit versions of text services and IMEs through the Control Panel. To access Control Panel settings for specific versions of text services or IMEs, look in the following locations.

-   **Control Panel access for 32-bit Text Services and IMEs:** Start -> Settings -> Control Panel -> View x86 Control Panel Icons
-   **Control Panel access for 64-bit Text Services and IMEs:** Start -> Settings -> Control Panel -> Regional and Language Options

There may be circumstances where some settings might be available only through the 32-bit Control Panel. In these cases, be sure that users of your text service or IME are aware of this, by providing appropriate documentation or offering UI hints in your 64-bit settings interface.

 

 