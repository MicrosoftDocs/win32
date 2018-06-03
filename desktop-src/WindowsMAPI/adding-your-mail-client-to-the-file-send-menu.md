---
Description: This topic explains how to add your mail client to Send on the File menu in applications that use Simple MAPI or MAPI.
ms.assetid: 0C4C935C-F223-4881-A699-138735B5E652
title: Adding Your Mail Client to the File.Send Menu
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Your Mail Client to the File.Send Menu

This topic explains how to add your mail client to **Send** on the **File** menu in applications that use Simple MAPI or MAPI.

**Adding Your Mail Client to the File.Send Menu**

1.  Create the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Clients**\\**Mail**\\***MyMailClient*** registry key.

2.  If your mail client supports the Windows Installer, formerly the Microsoft Software Installer (MSI), follow the instructions in [Setting Up the MSI Keys for Your MAPI DLL](https://msdn.microsoft.com/windows/desktop/d869c201-f126-4c8c-b842-258f8806b6bf). Otherwise, proceed with the following steps.

3.  Set the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Clients**\\**Mail::(default)** value to identify your client's subkey; for example, (REG\_SZ) ***MyMailClient***.

4.  Create the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Clients**\\**Mail**\\***MyMailClient*::DLLPath** and set the value to (REG\_SZ) C:\\*path*\\*to*\\*MyMAPI.dll*, or (REG\_EXPAND\_SZ) %ENVVAR%\\*MyMAPI.dll*, where the path identifies the DLL that exports Simple MAPI functions.

    Note that use of environmental variables in the path is supported; the stub library performs the substitution when resolving the path.

5.  If your mail client supports MAPI functions, create the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Clients**\\**Mail**\\***MyMailClient*::DLLPathEx** value and set the value to (REG\_SZ) C:\\*myinstall*\\*MyMAPIex.dll*, or (REG\_EXPAND\_SZ) %ENVVAR%\\*MyMapi32.dll*, where the path identifies the DLL that exports extended MAPI functions.

    Note that use of environmental variables in the path is supported; the stub library performs the substitution when resolving the path.

## Related topics

<dl> <dt>

[Mapi32 Stub Library](mapi32-stub-library.md)
</dt> </dl>

 

 



