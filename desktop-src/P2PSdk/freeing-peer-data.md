---
Description: All pointers that the Peer Infrastructure functions return must be freed by using PeerGraphFreeData or PeerFreeData.
ms.assetid: c7669404-2550-4f0d-908e-540d9a34008f
title: Freeing Peer Data
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Freeing Peer Data

All pointers that the Peer Infrastructure functions return must be freed by using [**PeerGraphFreeData**](/windows/win32/P2P/nf-p2p-peergraphfreedata?branch=master) or [**PeerFreeData**](/windows/win32/P2P/nf-p2p-peerfreedata?branch=master). These functions must only be called for structures that are directly returned by a Peer Infrastructure function. Do not call a different FreeData function to free nested pointers, for example, do not call a FreeData function on the pointers in a [**PEER\_RECORD**](/windows/win32/P2P/ns-p2p-peer_record_tag?branch=master) structure.

## Example of Freeing Data

The following code snippet shows you how to retrieve the properties associated with a graph, and then free the data that is returned.


```C++
PEER_GRAPH_PROPERTIES  * pGraphProperties = NULL;
HRESULT hr = PeerGraphGetProperties(hGraph, &amp;pGraphProperties);
if (SUCCEEDED(hr) &amp;&amp; (NULL != pGraphProperties))
{
  // use pGraphProperties
  wprintf(L"%d\n", pGraphProperties->pwzGraphId);

  // release the data
  PeerGraphFreeData(pGraphProperties);
}
```



 

 



