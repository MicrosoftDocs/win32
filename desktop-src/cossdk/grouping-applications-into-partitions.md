---
description: Grouping Applications into Partitions
ms.assetid: bdfe2428-9769-4bcb-b74e-a141ba67a67e
title: Grouping Applications into Partitions
ms.topic: article
ms.date: 05/31/2018
---

# Grouping Applications into Partitions

When deciding how to group applications into partitions, administrators need to be aware of certain rules and restrictions, including the following:

-   An application can be installed into one or more partitions.
-   Only one instance of a given component can exist in an application.

## Public and Private Components

Other restrictions exist when deciding how to group COM+ applications. These restrictions pertain to public versus private components within an application. Application components can generally be either public or private. However, when grouping applications into partitions, administrators should be aware of some restrictions around public and private components. The following table lists these restrictions.



| If an application is:              | Then components in a partition can be:                                                                                   |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| A server application<br/>    | Public and private.<br/>                                                                                           |
| A library application<br/>   | Public only. Otherwise, the callers application could have the same components, which would create ambiguity.<br/> |
| In the global partition<br/> | Public only. This ensures backward compatibility.<br/>                                                             |



 

## Application IDs

Every COM+ application installed on a computer has a unique application ID. However, application names need only be unique within a single partition and not on the entire computer.

The following table shows what happens to the application ID when an application is imported into a partition or exported from a partition.



| If an application is:                                              | Then the application ID:                    |
|--------------------------------------------------------------------|---------------------------------------------|
| Imported to the global partition<br/>                        | Remains the same<br/>                 |
| Imported to a partition other than the global partition<br/> | Is changed<br/>                       |
| Exported<br/>                                                | Is included in the exported file<br/> |



 

## Related topics

<dl> <dt>

[Collecting Partition Metrics](collecting-partition-metrics.md)
</dt> <dt>

[Configuring the Partition Cache](configuring-the-partition-cache.md)
</dt> <dt>

[Managing Local Partitions](managing-local-partitions.md)
</dt> <dt>

[Managing Partitions Within Active Directory](managing-partitions-within-active-directory.md)
</dt> <dt>

[Setting Administrative Rights for a Partition](setting-administrative-rights-for-a-partition.md)
</dt> </dl>

 

 




