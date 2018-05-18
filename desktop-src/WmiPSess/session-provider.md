---
title: Session Provider
description: The Session provider enables developers to manage network sessions and connections with command-line commands, WMI scripts, webpages, or standard programming languages.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e54463f0-3bd8-4eef-9dc0-6a1dd2767c7e'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["providers Windows Management Instrumentation ,Session", "Session provider Windows Management Instrumentation"]
---

# Session Provider

The Session provider enables developers to manage network sessions and connections with command-line commands, WMI scripts, webpages, or standard programming languages. The [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instance name is "SessionProvider".

As an instance and property provider, the Session provider supports the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface, as well as the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)

The Session provider also implements the following provider framework method:

-   [**Provider::EnumerateInstances**](https://msdn.microsoft.com/library/aa392767)

The Session provider supports the following classes located in the \\root\\cimv2 namespace:

-   [**Win32\_ServerSession**](win32-serversession.md)
-   [**Win32\_ServerConnection**](win32-serverconnection.md)

The Session provider also supports the following association classes, also in the \\root\\cimv2 namespace:

-   [**Win32\_ConnectionShare**](win32-connectionshare.md)
-   [**Win32\_SessionConnection**](win32-sessionconnection.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 




