---
description: The following list contains the CMSPStream methods called by the MSPCall object.
ms.assetid: 7a59ca78-b5e8-45e9-8fdb-89402ffef916
title: CMSPStream Methods Called by MSPCall Object
ms.topic: article
ms.date: 05/31/2018
---

# CMSPStream Public Methods Called by MSPCall Object



| CMSPStream public methods                                 | Description                                                                             |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**Init**](/windows/desktop/api/Mspstrm/nf-mspstrm-cmspstream-init)                           | Called by the **MSPCall** when the stream is created.                                   |
| [**ShutDown**](/windows/desktop/api/Mspstrm/nf-mspstrm-cmspstream-shutdown)                   | Called by the **MSPCall** to unselect all terminal objects and release the call object. |
| [**GetState**](/windows/desktop/api/Mspstrm/nf-mspstrm-cmspstream-getstate)                   | Called by the MSPCall object to get the current status of the stream.                   |
| [**HandleTSPData**](/windows/desktop/api/Mspstrm/nf-mspstrm-cmspstream-handletspdata)         | Derived call object may call this method to let the stream handle the TSP commands.     |
| [**ProcessGraphEvent**](/windows/desktop/api/Mspstrm/nf-mspstrm-cmspstream-processgraphevent) | Called by the MSPCall object to let the stream handle graph events.                     |



 

 

 



