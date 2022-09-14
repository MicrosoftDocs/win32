---
description: The following list contains the CMSPCallMultiGraph public methods called by the thread pool.
ms.assetid: f0a5f621-99c4-40f0-8a0e-0e43792e00a1
title: CMSPCallMultiGraph Public Methods, Called by Thread Pool
ms.topic: article
ms.date: 05/31/2018
---

# CMSPCallMultiGraph Public Methods, Called by Thread Pool



| CMSPCallMultiGraph public methods                                   | Description                                                                                                                                                                                              |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DispatchGraphEvent**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallmultigraph-dispatchgraphevent) | Called when the filter graph signals an event.                                                                                                                                                           |
| [**HandleGraphEvent**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallmultigraph-handlegraphevent)     | Called by the [**DispatchGraphEvent**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallmultigraph-dispatchgraphevent) static method. Queues [**ProcessGraphEvent**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallmultigraph-processgraphevent) on the main MSP worker thread. |
| [**ProcessGraphEvent**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallmultigraph-processgraphevent)   | Allows the MSP call object instance to handle the filter graph event.                                                                                                                                    |



 

## Related topics

<dl> <dt>

[**CMSPCallMultiGraph**](/windows/desktop/api/Mspcall/nl-mspcall-cmspcallmultigraph)
</dt> </dl>

 

 



