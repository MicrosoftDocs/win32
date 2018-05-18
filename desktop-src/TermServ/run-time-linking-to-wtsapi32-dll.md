---
title: Run-Time linking to Wtsapi32.dll
description: Your application can use the Remote Desktop Services API to dynamically link to the Wtsapi32.dll at run time. To do this, your application should call the LoadLibrary function to load Wtsapi32.dll.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b8227e65-be08-4045-a74e-dd3f398a7b9f'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# Run-Time linking to Wtsapi32.dll

If your application runs in an environment that is not a Remote Desktop Services environment, but you want your application to provide additional functionality when it does run in a Remote Desktop Services environment, the application can use the Remote Desktop Services API to implement the additional functionality, and dynamically link to the Wtsapi32.dll at run time. To do this, your application should call the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) function to load Wtsapi32.dll. If the **LoadLibrary** call fails, your application can run using its basic functionality. If **LoadLibrary** succeeds, your application can call the [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) function to retrieve pointers to the Remote Desktop Services functions that you want to call.

If your application is intended only for a Remote Desktop Services environment, dynamic linking is not necessary. In this case, you can include Wtsapi32.h and link with Wtsapi32.lib. Then, if your application starts up in an environment other than Remote Desktop Services, it will exit because Wtsapi32.dll is not present.

For information about determining whether your application is running in a Remote Desktop Services environment, see [Detecting the Remote Desktop Services Environment](detecting-the-terminal-services-environment.md).

## Related topics

<dl> <dt>

[General programming guidelines](general-programming-guidelines.md)
</dt> </dl>

 

 




