---
Description: Mapi32 Stub Library
ms.assetid: 7D45E60B-0B38-4837-91A8-D66D3357C167
title: Mapi32 Stub Library
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Mapi32 Stub Library

\[Simple MAPI is no longer supported as of Microsoft Outlook 2007. \]

Many applications support the addition of their product name to **Send** on the **File** menu through the installation of a custom version of Mapi32.dll in the system directory.

This situation creates versioning problems because many applications, such as the Microsoft Exchange client and earlier versions of Microsoft Outlook, require use of the system-supplied Mapi32.dll library and fail to operate properly when the new Mapi32.dll is installed. In addition, supported Microsoft Windows operating systems provide administrators with the ability to lock down the system directory, thereby preventing applications from overwriting system dynamic-link libraries during an installation.

To avoid such dynamic-link library (DLL) conflict, supported Microsoft Windows operating systems, Microsoft Outlook 2000, 2002, and 2003, and Microsoft Internet Explorer versions 5, 6, and 7 install a stub library called Mapi32.dll that acts as a central dispatcher for simple and extended Messaging Application Programming Interface (MAPI) calls.

The supported versions of Windows that install the MAPI stub library Mapi32.dll in the &lt;drive&gt;\\Windows\\System32 folder are as follows.

-   Windows 7
-   Windows Vista
-   Windows Server 2008
-   Windows Server 2003
-   Windows XP

Simple MAPI provides a set of functions that enable you to add a basic level of messaging functionality to Microsoft Windows-based applications. Extended MAPI is the same as [Microsoft Outlook 2007 MAPI](3d980b86-7001-4869-9780-121c6bfc7275), and is simply referred to as MAPI in the MAPI documentation.

## The Mapi32.dll Stub Installation

During installation, the original Mapi32.dll is renamed to Eumapi32.dll if the DLL was provided by Eudora, Nsmapi32.dll if the DLL was provided by Netscape, or otherwise Mapi32x.dll. The stub library, which is contained in the file Mapi32stub.dll, is then copied to Mapi32.dll. When the Mapi32.dll is loaded and Simple MAPI or MAPI calls are made, the stub library dispatches the call to an appropriate DLL. The stub library uses settings in the registry under the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Clients**\\**Mail** key to locate appropriate DLLs at runtime. These registry settings are described in [Mapi32.dll Stub Registry Settings](mapi32-dll-stub-registry-settings.md).

The stub DLL version number is set to 1.0 so that subsequent applications can install over the stub without the user being prompted that a newer version of the DLL is currently on the system. If you need to restore the stub, follow the instructions in [Installing or Restoring the Mapi32.dll Stub](installing-or-restoring-the-mapi32-dll-stub.md).

## In this section



| Topic                                                                                                         | Description |
|---------------------------------------------------------------------------------------------------------------|-------------|
| [Mapi32.dll Stub Registry Settings](mapi32-dll-stub-registry-settings.md)<br/>                         |             |
| [Explicitly Mapping MAPI Calls to MAPI DLLs](explicitly-mapping-mapi-calls-to-mapi-dlls.md)<br/>       |             |
| [Adding Your Mail Client to the File.Send Menu](adding-your-mail-client-to-the-file-send-menu.md)<br/> |             |
| [Setting Up the MSI Keys for Your MAPI DLL](setting-up-the-msi-keys-for-your-mapi-dll.md)<br/>         |             |
| [Installing or Restoring the Mapi32.dll Stub](installing-or-restoring-the-mapi32-dll-stub.md)<br/>     |             |



 

## Related topics

<dl> <dt>

[Adding Your Mail Client to the File.Send Menu](adding-your-mail-client-to-the-file-send-menu.md)
</dt> <dt>

[Explicitly Mapping MAPI Calls to MAPI DLLs](explicitly-mapping-mapi-calls-to-mapi-dlls.md)
</dt> <dt>

[Setting Up the MSI Keys for Your MAPI DLL](setting-up-the-msi-keys-for-your-mapi-dll.md)
</dt> </dl>

 

 




