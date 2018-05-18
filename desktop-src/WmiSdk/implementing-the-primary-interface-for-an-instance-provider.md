---
Description: 'An instance provider uses the asynchronous methods of IWbemServices as the primary interface to WMI.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '80425fa8-2746-4eba-8e7d-4a61e222852a'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Implementing the Primary Interface for an Instance Provider
---

# Implementing the Primary Interface for an Instance Provider

An instance provider uses the asynchronous methods of [**IWbemServices**](iwbemservices.md) as the primary interface to WMI. By implementing only the methods that fulfill the needs of your instance provider, you can reduce the amount of resources you spend coding. However, by implementing methods reserved for other types of providers, you can reduce the number of providers you write.

Because it is also used by applications and providers to request services of WMI, [**IWbemServices**](iwbemservices.md) contains many methods that are irrelevant to an instance provider. The following table lists the **IWbemServices** methods that you can implement for an instance provider.



| Method                                                                   | Feature          |
|--------------------------------------------------------------------------|------------------|
| [**GetObjectAsync**](iwbemservices-getobjectasync.md)                   | Retrieval        |
| [**PutInstanceAsync**](iwbemservices-putinstanceasync.md)               | Modification     |
| [**DeleteInstanceAsync**](iwbemservices-deleteinstanceasync.md)         | Deletion         |
| [**CreateInstanceEnumAsync**](iwbemservices-createinstanceenumasync.md) | Enumeration      |
| [**ExecQueryAsync**](iwbemservices-execqueryasync.md)                   | Query processing |



 

For methods that you do not use, your provider can supply a stub implementation that returns **WBEM\_E\_PROVIDER\_NOT\_CAPABLE**. This includes all [**IWbemServices**](iwbemservices.md) methods not listed in the above table.

A single provider can act simultaneously as a class, instance, and method provider by proper registration and implementation of all relevant methods. For more information, see [Writing a Class Provider](writing-a-class-provider.md) and [Writing a Method Provider](writing-a-method-provider.md).

 

 



