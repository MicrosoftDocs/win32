---
description: You can opt a computer in to the Microsoft Update service and then register that service with Automatic Updates.
ms.assetid: d6f3d8ca-3b7e-409c-87b6-db247b7b68e4
title: Opt-In to Microsoft Update
ms.topic: article
ms.date: 05/31/2018
---

# Opt-In to Microsoft Update

You can opt a computer in to the Microsoft Update service and then register that service with Automatic Updates.

The scripting sample in this topic shows you how to use Windows Update Agent (WUA) to register the Microsoft Update service with Automatic Updates. Alternatively, to register the service, the user can visit Microsoft Update.

Before you attempt to run this sample, verify that the version of WUA that is installed on the computer is version 7.0.6000 or a later version. For more information about how to determine the version of WUA that is installed, see [Determining the Current Version of WUA](determining-the-current-version-of-wua.md).

## Example

The following scripting sample shows you how to use the Windows Update Agent (WUA) to register the Microsoft Update service with Automatic Updates. The sample allows deferred or offline processing if needed.

> [!IMPORTANT]
> This script is intended to demonstrate the use of the Windows Update Agent APIs, and provide an example of how developers can use these APIs to solve problems. This script is not intended as production code, and the script itself is not supported by Microsoft (though the underlying Windows Update Agent APIs are supported).

 


```VB
Set ServiceManager = CreateObject("Microsoft.Update.ServiceManager")
ServiceManager.ClientApplicationID = "My App"

'add the Microsoft Update Service, GUID
Set NewUpdateService = ServiceManager.AddService2("7971f918-a847-4430-9279-4a52d1efe18d",7,"")

```



In earlier versions of WUA (a minimum WUA version of 7.0.6000), you can simplify the opt-in process by using a registry setting. After the registry key and values are configured, the Microsoft Update opt-in process occurs the next time WUA performs a search. The opt-in process may be triggered by Automatic Updates or by an API caller.

For example, the full path of the registry key and values to set for the opt-in process are as follows:

**HKLM**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**WindowsUpdate**\\**PendingServiceRegistration**\\**7971f918-a847-4430-9279-4a52d1efe18d**

**ClientApplicationID** = My App

**RegisterWithAU** = 1

> [!Note]
>
> The registry key is respected once only when WUA is updated from a version that is earlier than version 7.0.6000 to version 7.0.6000 or to a later version. We recommend discretion when overwriting existing registry values because overwriting the values may change the result of an earlier service registration request.
>
> Creating this registry key requires administrative credentials. For Windows Vista, the caller must create the registry key in an elevated process.

 

 

 



