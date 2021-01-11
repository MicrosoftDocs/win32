---
description: All pointers that the Peer Infrastructure functions return must be freed by using PeerGraphFreeData or PeerFreeData.
ms.assetid: c7669404-2550-4f0d-908e-540d9a34008f
title: Freeing Peer Data
ms.topic: article
ms.date: 05/31/2018
---

# Freeing Peer Data

All pointers that the Peer Infrastructure functions return must be freed by using [**PeerGraphFreeData**](/windows/desktop/api/P2P/nf-p2p-peergraphfreedata) or [**PeerFreeData**](/windows/desktop/api/P2P/nf-p2p-peerfreedata). These functions must only be called for structures that are directly returned by a Peer Infrastructure function. Do not call a different FreeData function to free nested pointers, for example, do not call a FreeData function on the pointers in a [**PEER\_RECORD**](/windows/desktop/api/P2P/ns-p2p-peer_record) structure.

## Example of Freeing Data

The following code snippet shows you how to retrieve the properties associated with a graph, and then free the data that is returned.


```C++
PEER_GRAPH_PROPERTIES  * pGraphProperties = NULL;
HRESULT hr = PeerGraphGetProperties(hGraph, &pGraphProperties);
if (SUCCEEDED(hr) && (NULL != pGraphProperties))
{
  // use pGraphProperties
  wprintf(L"%d\n", pGraphProperties->pwzGraphId);

  // release the data
  PeerGraphFreeData(pGraphProperties);
}
```



 

 



