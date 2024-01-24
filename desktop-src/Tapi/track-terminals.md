---
description: Two types of track terminals are defined Recording Track Terminal and Playback Track Terminal which respectively belong to and are managed by File Recording Terminal and File Playback Terminal.
ms.assetid: 2c5c485e-d46f-4bfe-8651-5ed021b23b66
title: Track Terminals
ms.topic: article
ms.date: 05/31/2018
---

# Track Terminals

Two types of track terminals are defined: Recording Track Terminal and Playback Track Terminal, which, respectively, belong to and are managed by File Recording Terminal and File Playback Terminal.

All track terminals expose the [**ITFileTrack**](/windows/desktop/api/tapi3if/nn-tapi3if-itfiletrack) and [**ITTerminal**](/windows/win32/api/tapi3if/nn-tapi3if-itterminal) interfaces. The **ITTerminal** interface allows the selection of track terminals onto streams or calls.

> [!Note]  
> Track terminals also expose a private interface, [**ITMediaControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itmediacontrol), which the MSP uses. Applications should not attempt to access this interface.

 

 

 
