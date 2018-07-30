---
Description: 'Two types of track terminals are defined: Recording Track Terminal and Playback Track Terminal, which, respectively, belong to and are managed by File Recording Terminal and File Playback Terminal.'
ms.assetid: bf23bc26-5763-45a3-a63d-e43ce2480956
title: Track Terminals
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Track Terminals

Two types of track terminals are defined: Recording Track Terminal and Playback Track Terminal, which, respectively, belong to and are managed by File Recording Terminal and File Playback Terminal.

All track terminals expose the [**ITFileTrack**](/windows/desktop/api/tapi3if/nn-tapi3if-itfiletrack) and [**ITTerminal**](https://msdn.microsoft.com/en-us/library/ms732646(v=VS.85).aspx) interfaces. The **ITTerminal** interface allows the selection of track terminals onto streams or calls.

> [!Note]  
> Track terminals also expose a private interface, [**ITMediaControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itmediacontrol), which the MSP uses. Applications should not attempt to access this interface.

 

 

 



