---
description: One of the main tools of Windows Management Instrumentation (WMI) is the ability to query the WMI repository for class and instance information.
ms.assetid: 0cceda42-fba0-4a08-90dd-43f022d0be41
ms.tgt_platform: multiple
title: Querying WMI
ms.topic: article
ms.date: 05/31/2018
---

# Querying WMI

One of the main tools of Windows Management Instrumentation (WMI) is the ability to query the WMI repository for class and instance information. For example, you can request that WMI return all the objects representing shut-down events from your desktop system. You can also retrieve class, instance, or schema data. The following table lists the different types of queries you can make.



| Topic                                                                | Description                                                                                                                                                                                      |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Invoking a Synchronous Query](invoking-a-synchronous-query.md)     | Describes how to maintain a link with WMI throughout the query process. Synchronous queries are good for small queries or queries to a local system.<br/>                                  |
| [Invoking an Asynchronous Query](invoking-an-asynchronous-query.md) | Describes how to set up a separate process to receive queries. Asynchronous queries are more complex and provide a lower level of security, but generally improve system performance.<br/> |



 

In addition to querying the WMI repository, you can also use the [*WMI Query Language (WQL)*](gloss-w.md) to route notification events to your application. For more information, see [Receiving a WMI Event](receiving-a-wmi-event.md).

> [!Note]
>
> To properly query WMI, you must have a good understanding of WQL. A query that is incorrect, too complex, or inappropriate can cause the query processor to return an error or unexpected results. For a comprehensive guide to WQL, see [Querying with WQL](querying-with-wql.md).
>
> There are limits to the number of **AND** and **OR** keywords that can be used in WQL queries. Large numbers of WQL keywords used in a complex query can cause WMI to return the **WBEM\_E\_QUOTA\_VIOLATION** error code as an **HRESULT** value. The limit of WQL keywords depends on how complex the query is.
>
> When querying for property values with a **uint64** or **sint64** data type in a scripting language like VBScript, WMI returns string values. Unexpected results can occur when comparing these values, because comparing strings returns different results than comparing numbers. For example, "10000000000" is less than "9" when comparing strings, and 9 is less than 10000000000 when comparing numbers. To avoid confusion you should use the [CDbl](/previous-versions//ftekwwt0(v=vs.85)) method in VBScript when properties of type **uint64** or **sint64** are retrieved from WMI.

 

> [!Note]  

 

For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

 

