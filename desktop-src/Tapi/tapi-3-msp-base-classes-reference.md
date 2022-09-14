---
description: The following material provides details on the Media Service Provider base classes.
ms.assetid: ef845c44-1ff5-42a1-8e91-38d66e6fe363
title: TAPI 3 MSP Base Classes Reference
ms.topic: article
ms.date: 05/31/2018
---

# TAPI 3 MSP Base Classes Reference

The following material provides details on the Media Service Provider base classes.



| Media service provider base classes (alphabetical order) | Description                                                                                                                                                                                             |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CAudioCaptureTerminal](caudiocaptureterminal.md)       | Derived from [CSingleFilterTerminal](csinglefilterterminal.md) and implements a static audio capture terminal for wave devices using the DirectShow wavein filter. Defined in MSPtmac.h.               |
| [CAudioRenderTerminal](caudiorenderterminal.md)         | Derived from [CSingleFilterTerminal](csinglefilterterminal.md) and implements a static audio render terminal for wave devices using the DirectShow waveout filter. Defined in MSPtrmar.h.              |
| [CBaseTerminal](cbaseterminal.md)                       | A terminal base class applicable to both static and dynamic terminals. It is completely generic, so any terminal implementation can derive from this class directly or indirectly. Defined in MSPterm.h |
| [**CMSPAddress**](/windows/desktop/api/Mspaddr/nl-mspaddr-cmspaddress)                       | Implements the MSP address object and supports the [**ITMSPAddress**](/windows/desktop/api/msp/nn-msp-itmspaddress) interface. Defined in MSPaddr.h.                                                                                |
| [CMSPArray](cmsparray.md)                               | A template that implements a smart array that will grow on demand. Defined in MSPutils.h.                                                                                                               |
| [**CMSPCallBase**](/windows/desktop/api/Mspcall/nl-mspcall-cmspcallbase)                     | Provides a generic implementation of the call object and supports the [**ITStreamControl**](/windows/win32/api/tapi3if/nn-tapi3if-itstreamcontrol) interface. Defined in MSPcall.h.                                                       |
| [**CMSPCallMultiGraph**](/windows/desktop/api/Mspcall/nl-mspcall-cmspcallmultigraph)         | Defines a call that uses a filter graph for each stream. Defined in MSPcall.h.                                                                                                                          |
| [**CMSPStream**](/windows/desktop/api/Mspstrm/nl-mspstrm-cmspstream)                         | Exposes methods that allow an application to start, pause, or stop a substream, and to select or unselect terminals. Defined in MSPstrm.h.                                                              |
| [CMSPThread](cmspthread.md)                             | Implements the MSP's worker thread. Defined in MSPthrd.h.                                                                                                                                               |
| [CSingleFilterTerminal](csinglefilterterminal.md)       | An additional terminal base class applicable to both static and dynamic terminals. Makes implementation more specific by assuming the terminal has a single DirectShow filter. Defined in MSPterm.h.    |
| [CVideoCaptureTerminal](cvideocaptureterminal.md)       | Derived from [CSingleFilterTerminal](csinglefilterterminal.md) and implements a static video capture terminal using a single DirectShow filter. Defined in MSPtmvc.h.                                  |



 

 

 
