---
Description: An instance provider uses the asynchronous methods of IWbemServices as the primary interface to WMI.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 80425fa8-2746-4eba-8e7d-4a61e222852a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Implementing the Primary Interface for an Instance Provider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing the Primary Interface for an Instance Provider

An instance provider uses the asynchronous methods of [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) as the primary interface to WMI. By implementing only the methods that fulfill the needs of your instance provider, you can reduce the amount of resources you spend coding. However, by implementing methods reserved for other types of providers, you can reduce the number of providers you write.

Because it is also used by applications and providers to request services of WMI, [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) contains many methods that are irrelevant to an instance provider. The following table lists the **IWbemServices** methods that you can implement for an instance provider.



| Method                                                                   | Feature          |
|--------------------------------------------------------------------------|------------------|
| [**GetObjectAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobjectasync?branch=master)                   | Retrieval        |
| [**PutInstanceAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync?branch=master)               | Modification     |
| [**DeleteInstanceAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-deleteinstanceasync?branch=master)         | Deletion         |
| [**CreateInstanceEnumAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-createinstanceenumasync?branch=master) | Enumeration      |
| [**ExecQueryAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execqueryasync?branch=master)                   | Query processing |



 

For methods that you do not use, your provider can supply a stub implementation that returns **WBEM\_E\_PROVIDER\_NOT\_CAPABLE**. This includes all [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) methods not listed in the above table.

A single provider can act simultaneously as a class, instance, and method provider by proper registration and implementation of all relevant methods. For more information, see [Writing a Class Provider](writing-a-class-provider.md) and [Writing a Method Provider](writing-a-method-provider.md).

 

 



