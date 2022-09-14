---
description: Default Partitions
ms.assetid: ce6ad7c1-d4a1-4573-860e-f7859c588773
title: Default Partitions
ms.topic: article
ms.date: 05/31/2018
---

# Default Partitions

When a default partition is assigned to a user, COM+ attempts to activate components in that partition first. If the activation fails, COM+ searches the global partition for the component to activate. The exception to this process occurs when the COM+ component includes a partition moniker, which explicitly specifies the partition in which the component is located. In this case, the partition moniker takes precedence over any default partition configuration.

When using local partitions, the default partition is assigned to users using the **COM+ Partition Users** folder in the Component Services administrative tool on the application server. When using partition sets in the Active Directory, the user's default partition is determined by the user's partition set.

## Related topics

<dl> <dt>

[Local Partitions](local-partitions.md)
</dt> <dt>

[Partition Properties](partition-properties.md)
</dt> <dt>

[Partitions and Active Directory](partitions-and-active-directory.md)
</dt> <dt>

[The Global Partition](the-global-partition.md)
</dt> </dl>

 

 



