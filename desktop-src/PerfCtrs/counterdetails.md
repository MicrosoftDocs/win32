---
description: The CounterDetails table describes a specific counter on a particular computer.
ms.assetid: e2a16a6e-8cd4-4fd3-adeb-461faed948e4
title: CounterDetails
ms.topic: article
ms.date: 05/31/2018
---

# CounterDetails

The **CounterDetails** table describes a specific counter on a particular computer.

The **CounterDetails** table defines the following fields:

-   **CounterID:** A unique identifier in the database that maps to a specific counter name text string. This field is the primary key of this table.
-   **MachineName:** The name of the computer that logged this data set.
-   **ObjectName:** The name of the performance object.
-   **CounterName:** The name of the counter.
-   **CounterType:** The counter type. For a list of counter types and their formulas, see the Counter Types section of the [Windows Server 2003 Deployment Kit](/previous-versions/windows/it-pro/windows-server-2003/cc776490(v=ws.10)).
-   **DefaultScale:** The default scaling to be applied to the raw performance counter data.
-   **InstanceName:** The name of the counter instance.
-   **InstanceIndex:** The index number of the counter instance.
-   **ParentName:** Some counters are logically associated with others, and are referred to as parents. For example, the parent of a thread is a process and the parent of a logical disk driver is a physical drive. This field contains the name of the parent. Either the value in this field or the **ParentObjectID** field identifies a specific parent instance. If the value in this field is **NULL**, the value in the **ParentObjectID** field must be checked to identify the parent. If the values in both fields are **NULL**, the counter does not have a parent.
-   **ParentObjectID:** The unique identifier of the parent. The value in either this field or the **ParentName** field identifies a specific parent instance. If the value in this field is **NULL**, the value in the **ParentName** field must be checked to identify the parent.

 

 
