---
title: Implementing the DLL Entry Points
description: Implementing the DLL Entry Points
ms.assetid: 0cdadf3c-989a-4c90-a450-dbede601a150
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the DLL Entry Points

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Each language resource DLL must implement and export the following entry points. The DLL file can be registered to be in any folder.

**DllMain.** Standard entry point to DLL.

**DllRegisterServer.** Registers the DLL in the registry. You register the DLL by running the Regsvr32.exe program with the DLL file name for the language resource as an argument.

regsvr32.exe %SystemRoot%\\MyFolder\\wordbreaker.dll

**DllCanUnloadNow.** Clients call this entry point through Component Object Model (COM) to determine whether it is possible to unload the language resource DLL.

**DllUnRegisterServer.** Removes the DLL in the registry.

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> <dt>

[Troubleshooting Language Resources](troubleshooting-language-resources.md)
</dt> </dl>

 

 




