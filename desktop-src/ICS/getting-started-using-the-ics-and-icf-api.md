---
title: Getting Started Using the ICS and ICF API
description: To use ICS, the software application must first obtain an INetSharingManager interface.
ms.assetid: 36cb04d7-2dae-4eca-a200-02bfb89fe837
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting Started Using the ICS and ICF API

\[Internet Connection Firewall may be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

To use ICS, the software application must first obtain an [**INetSharingManager**](/windows/previous-versions/NetCon/nn-netcon-inetsharingmanager?branch=master) interface. Use the [**CoCreateInstance**](_com_cocreateinstance) function to obtain this interface. The **CoCreateInstance** function requires a class identifier (CLSID). One way to obtain the CLSID is to call the [**CLSIDFromProgID**](_com_clsidfromprogid) function with the programmatic ID for the home networking object: HNetCfg.HNetShare.1.

The [**INetSharingManager**](/windows/previous-versions/NetCon/nn-netcon-inetsharingmanager?branch=master) interface provides access directly or indirectly to all the other COM interfaces in the ICS API.

## Enumerating RAS Connections Requires CoInitializeSecurity

To enumerate Remote Access Service (RAS) connections, each process calling the ICS API should call the [**CoInitializeSecurity**](_com_coinitializesecurity) function. The following line of code shows the appropriate parameter values to use when making this call.


```C++
  CoInitializeSecurity (NULL, -1, NULL, NULL,
                        RPC_C_AUTHN_LEVEL_PKT,
                        RPC_C_IMP_LEVEL_IMPERSONATE,
                        NULL, EOAC_NONE, NULL);
```



The call to [**CoInitializeSecurity**](_com_coinitializesecurity) should be made right after calling [**CoInitialize**](_com_coinitialize)( **NULL** ).

 

 




