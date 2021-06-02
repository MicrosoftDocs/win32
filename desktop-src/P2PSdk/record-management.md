---
description: To manage records, you can work with information that is stored in PEER\_RECORD structures.
ms.assetid: d38ea2d3-5cfb-4c4a-a63f-b274aa0dfe71
title: Record Management
ms.topic: article
ms.date: 05/31/2018
---

# Record Management

To manage records, you can work with information that is stored in [**PEER\_RECORD**](/windows/desktop/api/P2P/ns-p2p-peer_record) structures. When records are created, updated, or deleted, the changes made to a graph are replicated to all nodes. The following table identifies the rules for updating and automatically refreshing records.



| Management Task     | Rule                                                                                                                                                                                                            |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Updating a record   | Keep the expiration time the same or increase it. You cannot decrease the expiration time.                                                                                                                      |
| Refreshing a record | Use the [**PEER\_RECORD\_FLAG\_AUTOREFRESH**](/windows/desktop/api/P2P/ns-p2p-peer_record) flag to automatically refresh a record. Only use this flag when the node that is publishing a record is online. Otherwise, do not use this flag. |



 

 

 



