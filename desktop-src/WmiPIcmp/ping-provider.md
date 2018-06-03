---
title: Ping Provider
description: The Ping provider supplies WMI access to the status information provided by the standard ping command.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8be082cc-4c94-46d4-b584-7ffd04a7dffb
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- providers Windows Management Instrumentation , Ping
- Ping provider Windows Management Instrumentation
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ping Provider

The Ping provider supplies WMI access to the status information provided by the standard **ping** command. The name of the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instance name is "WMIPingProvider".

As an instance provider, the Ping provider implements the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) method:

-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)

    Note that the address property cannot be specified as a range, but must be exact.

-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)

The Wmipicmp.mof file contains the Ping provider and registration classes. You can access the Ping provider classes only in the root\\cimv2 namespace.

The Ping provider supports the following class:

-   [**Win32\_PingStatus**](win32-pingstatus.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 




