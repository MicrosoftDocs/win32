---
title: Next Hop Flags
description: Next Hop Flags
ms.assetid: e4c7e9ea-21f5-491a-b005-1ef1a457cb80
keywords:
- Next
- Next Hop Flags
ms.topic: article
ms.date: 05/31/2018
---

# Next Hop Flags

## Next Hop State Flags



| Constant                     | Value | Description                              |
|------------------------------|-------|------------------------------------------|
| RTM\_NEXTHOP\_STATE\_CREATED | 0     | Indicates that the next hop was created. |
| RTM\_NEXTHOP\_STATE\_DELETED | 1     | Indicates that the next hop was deleted. |



 

## Next Hop Flags



| Constant                    | Value  | Description                                                                                                                                           |
|-----------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| RTM\_NEXTHOP\_FLAGS\_REMOTE | 0x0001 | This next hop points to a remote destination that is not directly reachable. To obtain the complete path, the client must perform a recursive lookup. |
| RTM\_NEXTHOP\_FLAGS\_DOWN   | 0x0002 | This flag is reserved for future use.                                                                                                                 |



 

## Next Hop Added



| Constant                  | Value | Description                 |
|---------------------------|-------|-----------------------------|
| RTM\_NEXTHOP\_CHANGE\_NEW | 0x01  | A new next hop was created. |



 

 

 




