---
Description: Because WMI loads a high-performance provider in-process to either WMI or a client application, you must design your high-performance provider as an in-process server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c37e3652-8c76-4125-ba62-ae860858797e
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Implementing the High-Performance Interface
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing the High-Performance Interface

Because WMI loads a high-performance provider in-process to either WMI or a client application, you must design your high-performance provider as an in-process server. In addition, you must implement the high-performance provider methods in the [**IWbemHiPerfProvider**](/windows/win32/Wbemprov/nn-wbemprov-iwbemhiperfprovider?branch=master) and [**IWbemRefresher**](/windows/win32/Wbemcli/nn-wbemcli-iwbemrefresher?branch=master) interfaces.

You should implement a high-performance provider as an in-process server. One feature you should be aware of when implementing the security of an in-process server is how the provider identifies its own location. When loaded in-process to WMI, WMI instantiates the provider using a CLSID. When loaded in process to a client application, the client application instantiates the provider with the **ClientLoadableCLSID** property. By giving different values to a CLSID and **ClientLoadableCLSID**, you allow the provider to determine if it is loaded in-process to WMI or to a client application. If located in a WMI process, the provider should do any necessary client impersonation by using **ClientLoadableCLSID**. If located in a client process, the provider inherits the access token of the thread it is called on. For more information about implementing an in-process server, see the [COM section](http://go.microsoft.com/fwlink/p/?linkid=96666) of MSDN.

As an in-process server, a high-performance provider uses a refresher object to keep data current for the remote client. The following table lists methods that you must implement for a high-performance provider.



| Method                                                                                              | Feature                                           |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| [**IWbemHiPerfProvider::QueryInstances**](/windows/win32/Wbemprov/nf-wbemprov-iwbemhiperfprovider-queryinstances?branch=master)                   | Queries                                           |
| [**IWbemHiPerfProvider::GetObjects**](/windows/win32/Wbemprov/nf-wbemprov-iwbemhiperfprovider-getobjects?branch=master)                           | Object retrieval                                  |
| [**IWbemHiPerfProvider::CreateRefresher**](/windows/win32/Wbemprov/nf-wbemprov-iwbemhiperfprovider-createrefresher?branch=master)                 | Creates a refresher                               |
| [**IWbemHiPerfProvider::CreateRefreshableObject**](/windows/win32/Wbemprov/nf-wbemprov-iwbemhiperfprovider-createrefreshableobject?branch=master) | Creates a refreshable instance object             |
| [**IWbemHiPerfProvider::CreateRefreshableEnum**](/windows/win32/Wbemprov/nf-wbemprov-iwbemhiperfprovider-createrefreshableenum?branch=master)     | Creates a refreshable enumerator                  |
| [**IWbemHiPerfProvider::StopRefreshing**](/windows/win32/Wbemprov/nf-wbemprov-iwbemhiperfprovider-stoprefreshing?branch=master)                   | Stops refreshing an enumerator or instance object |
| [**IWbemRefresher::Refresh**](/windows/win32/Wbemcli/nf-wbemcli-iwbemrefresher-refresh?branch=master)                                           | Creates a refresher                               |



 

## Related topics

<dl> <dt>

[Making an Instance Provider into a High-Performance Provider](making-an-instance-provider-into-a-high-performance-provider.md)
</dt> </dl>

 

 



