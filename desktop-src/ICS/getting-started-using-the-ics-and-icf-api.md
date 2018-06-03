---
title: Getting Started Using the ICS and ICF API
description: To use ICS, the software application must first obtain an INetSharingManager interface.
ms.assetid: 36cb04d7-2dae-4eca-a200-02bfb89fe837
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started Using the ICS and ICF API

\[Internet Connection Firewall may be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

To use ICS, the software application must first obtain an [**INetSharingManager**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetsharingmanager) interface. Use the [**CoCreateInstance**](https://www.bing.com/search?q=**CoCreateInstance**) function to obtain this interface. The **CoCreateInstance** function requires a class identifier (CLSID). One way to obtain the CLSID is to call the [**CLSIDFromProgID**](https://www.bing.com/search?q=**CLSIDFromProgID**) function with the programmatic ID for the home networking object: HNetCfg.HNetShare.1.

The [**INetSharingManager**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetsharingmanager) interface provides access directly or indirectly to all the other COM interfaces in the ICS API.

## Enumerating RAS Connections Requires CoInitializeSecurity

To enumerate Remote Access Service (RAS) connections, each process calling the ICS API should call the [**CoInitializeSecurity**](https://www.bing.com/search?q=**CoInitializeSecurity**) function. The following line of code shows the appropriate parameter values to use when making this call.


```C++
  CoInitializeSecurity (NULL, -1, NULL, NULL,
                        RPC_C_AUTHN_LEVEL_PKT,
                        RPC_C_IMP_LEVEL_IMPERSONATE,
                        NULL, EOAC_NONE, NULL);
```



The call to [**CoInitializeSecurity**](https://www.bing.com/search?q=**CoInitializeSecurity**) should be made right after calling [**CoInitialize**](https://www.bing.com/search?q=**CoInitialize**)( **NULL** ).

 

 




