---
description: Windows Installer accepts a Uniform Resource Locator (URL) as a valid source for an installation.
ms.assetid: f1bb2dc0-4236-4bd7-89a2-f4416b5b9dda
title: Downloading an Installation from the Internet
ms.topic: article
ms.date: 05/31/2018
---

# Downloading an Installation from the Internet

Windows Installer accepts a Uniform Resource Locator (URL) as a valid source for an installation. Windows Installer can install packages, patches, and transforms from a URL location.

If the installation database is at a URL, the installer downloads the database to a cache location before starting the installation. The installer also downloads the files and cabinet files from the Internet source that are appropriate for the user's selections. See [A URL-based Windows Installer Installation Example](a-url-based-windows-installer-installation-example.md) for more information.

For example, to install a package with a source located on a web server at https://server/share/package.msi, you can use the [command line](command-line-options.md) options to install the package and set [public](public-properties.md) properties.

msiexec /i https://server/share/package.msi *PROPERTY=VALUE*

A command line like the one previously shown should be passed to the installer to start an installation from a web browser. In general, you should not download and install the package simply by double-clicking the .msi file from within the browser. This downloads the .msi file to the temporary Internet files folder and passes the following command to the installer:

**msiexec /i c:\\windows\\temporary internet files\\package.msi**

The installation fails if the package requires any external source files or cabinets because these are not located in the same location as the .msi file.

Note that because the [**Installer**](installer-object.md) object is not marked as [SafeForScripting](safeforscripting.md) on the user's computer, users need to adjust their browser security settings for the example to work correctly.

The [**InstallProduct**](installer-installproduct.md) method could be used to run the previous command from a browser as an on-click event.


```VB
'Downloading an Installation from the Internet
'The InstallProduct method could be used to run 
'the previous command from a browser as an on-click event.

<SCRIPT LANGUAGE="VBScript"> 
<!-- 
Dim Installer
On Error Resume Next
set Installer=CreateObject("WindowsInstaller.Installer")
Installer.InstallProduct "https://server/share/package.msi", "PROPERTY=VALUE "
set Installer=Nothing
-->
</SCRIPT>
```



Note that because some web servers are case sensitive, the FileName field in the [File](file-table.md) table must match the case of the source files exactly to ensure support of Internet downloads.

See [Downloading and Installing a Patch from the Internet](downloading-and-installing-a-patch-from-the-internet.md). For more information about securing installations and using digital certificates, see [Guidelines for Authoring Secure Installations](guidelines-for-authoring-secure-installations.md) and [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md). For more information about how to create a web installation of a Windows Installer package, see [Internet Download Bootstrapping](internet-download-bootstrapping.md).

## Available Internet Protocols

Beginning with Windows Server 2003 and Windows XP, the installer can use the HTTP, HTTPS and FILE protocols. The installer does not support the FTP and GOPHER protocols.

Windows Installer version 2.0 can use the HTTP, FILE, and FTP protocols and cannot use the HTTPS and GOPHER protocols.

 

 



