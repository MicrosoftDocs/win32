---
Description: Installing or Restoring the Mapi32.dll Stub
ms.assetid: BADC5CF9-380F-4625-8442-30ACDCB14BFF
title: Installing or Restoring the Mapi32.dll Stub
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Installing or Restoring the Mapi32.dll Stub

\[No longer available for use as of Windows Vista.\]

Installations and upgrades of supported Microsoft Windows operating systems, and Microsoft Outlook and Microsoft Internet Explorer versions install Mapi32.dll. Each of these installations runs an executable file called Fixmapi.exe to do so.

In the event that an application overwrites Mapi32.dll, you can restore it using Fixmapi.exe. Fixmapi.exe can be found in the same location as the stub library itself, usually the system directory. This utility copies the current Mapi32.dll (the new DLL that overwrote the stub library) to Mapi32x.DLL, and then copies the stub image, contained in the Mapistub.dll file, to Mapi32.dll. There are no arguments for Fixmapi.exe.

If the MAPI DLL was provided by Netscape or Eudora email clients, the DLL is renamed to Nsmapi.dll or Eumapi.dll respectively, and the appropriate **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Clients**\\**Mail** subkey and **DLLPath** value are created. The **DLLPath** value points to the renamed DLL because both DLLs support Simple MAPI calls, so the **DLLPathEx** value is not needed.

Fixmapi.exe never copies the stub to Mapi32x.dll by checking the DLL for the **GetOutlookVersion** exported symbol. To determine whether a particular DLL is the stub library, you can check for the **GetOutlookVersion** exported symbol using the Dumpbin.exe utility provided with Microsoft Visual Studio using the following syntax.

**dumpbin /exports mapistub.dll \| grep "GetOutlookVersion"**

**dumpbin /exports mapi32.dll \| grep "GetOutlookVersion"**

## Installing and Uninstalling Mail Clients

Many applications, when uninstalled, explicitly remove the Mapi32.dll from the system directory. If you have the stub library installed and you uninstall one of these applications, you need to run Fixmapi.exe to restore the stub. You also need to manually remove the DLL for that application. New applications that are aware of the stub library should not remove the stub on uninstall, and should instead remove only their MAPI DLLs and keys from the registry.

## Related topics

<dl> <dt>

[Mapi32 Stub Library](mapi32-stub-library.md)
</dt> </dl>

 

 



