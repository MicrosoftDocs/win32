---
description: CMSPCallBase Pure Virtual Methods - These methods must be overridden by derived classes.
ms.assetid: 2ea9d35a-c87e-44f4-8dc6-618251c81fe4
title: CMSPCallBase Pure Virtual Methods
ms.topic: reference
ms.date: 05/31/2018
---

# CMSPCallBase Pure Virtual Methods

These methods must be overridden by derived classes.



| CMSPCallBase pure virtual methods                                 | Description                                                                                                                             |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**MSPCallAddRef**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallbase-mspcalladdref)               | Private AddRef method for the call object.                                                                                              |
| [**MSPCallRelease**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallbase-mspcallrelease)             | Private Release method for the call object.                                                                                             |
| [**Init**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallbase-init)                                 | Called by the MSP address object (in the method [**CreateMSPCall**](/windows/desktop/api/msp/nf-msp-itmspaddress-createmspcall)) to initialize the MSP call object. |
| [**ShutDown**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallbase-shutdown)                         | Called by the MSP address object to shut down the call..                                                                                |
| [**InternalCreateStream**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallbase-internalcreatestream) | Called by [**CreateStream**](/windows/win32/api/tapi3if/nf-tapi3if-itstreamcontrol-createstream) to create a stream object.                                               |
| [**CreateStreamObject**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallbase-createstreamobject)     | Called by [**InternalCreateStream**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallbase-internalcreatestream) to create a stream object.                                  |
| [**RemoveStream**](/windows/desktop/api/Mspcall/nf-mspcall-cmspcallbase-removestream)                 | Called by the application to remove a stream from the call                                                                              |



 

## Related topics

<dl> <dt>

[**CMSPCallBase**](/windows/desktop/api/Mspcall/nl-mspcall-cmspcallbase)
</dt> </dl>

 

 
