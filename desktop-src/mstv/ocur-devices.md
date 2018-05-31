---
title: OCUR Devices
description: OCUR Devices
ms.assetid: 7b641b94-9854-4ca8-8362-a9e1e49bbdd2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OCUR Devices

In December 2005, Cable Television Laboratories published the Digital Receiver Interface Protocol Specification as a new method to discover and make use of OpenCable Unidirectional Cable Receivers (OCUR). Microsoft TV technologies supports OCUR devices by mapping certain Microsoft Broadcast Driver Architecture (BDA) interfaces to the Digital Receiver Interface (DRI) protocol.

The following BDA interfaces are mapped to the DRI protocol:

-   [**IBDA\_AutoDemodulateEx**](/windows/desktop/api/Bdaiface/nn-bdaiface-ibda_autodemodulateex)
-   [**IBDA\_ConditionalAccess**](/windows/desktop/api/Bdaiface/nn-bdaiface-ibda_conditionalaccess)
-   [**IBDA\_DeviceControl**](/windows/desktop/api/bdaiface/nn-bdaiface-ibda_devicecontrol)
-   [**IBDA\_DiagnosticProperties**](/windows/desktop/api/bdaiface/)
-   [**IBDA\_DigitalDemodulator**](/windows/desktop/api/bdaiface/nn-bdaiface-ibda_digitaldemodulator)
-   [**IBDA\_Topology**](/windows/desktop/api/bdaiface/nn-bdaiface-ibda_topology)
-   [**IDigitalCableLocator**](idigitalcablelocator.md)
-   [**IDigitalCableTuneRequest**](idigitalcabletunerequest.md)
-   [**IEncoderAPI**](/windows/desktop/api/Strmif/nn-strmif-iencoderapi)
-   [**IScanningTuner**](iscanningtuner.md)
-   [**IMPEG2PIDMap**](https://msdn.microsoft.com/library/windows/desktop/dd407132)

Documentation on how to use these interfaces to support OCUR devices can be found in the DRI specification, which can be downloaded at <http://www.opencable.com>.

## Related topics

<dl> <dt>

[Overview of Microsoft TV Technologies](overview-of-microsoft-tv-technologies.md)
</dt> </dl>

 

 




