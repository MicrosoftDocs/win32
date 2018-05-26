---
title: OCUR Devices
description: OCUR Devices
ms.assetid: 7b641b94-9854-4ca8-8362-a9e1e49bbdd2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OCUR Devices

In December 2005, Cable Television Laboratories published the Digital Receiver Interface Protocol Specification as a new method to discover and make use of OpenCable Unidirectional Cable Receivers (OCUR). Microsoft TV technologies supports OCUR devices by mapping certain Microsoft Broadcast Driver Architecture (BDA) interfaces to the Digital Receiver Interface (DRI) protocol.

The following BDA interfaces are mapped to the DRI protocol:

-   [**IBDA\_AutoDemodulateEx**](/windows/win32/Bdaiface/nn-bdaiface-ibda_autodemodulateex?branch=master)
-   [**IBDA\_ConditionalAccess**](/windows/win32/Bdaiface/nn-bdaiface-ibda_conditionalaccess?branch=master)
-   [**IBDA\_DeviceControl**](/windows/win32/bdaiface/nn-bdaiface-ibda_devicecontrol?branch=master)
-   [**IBDA\_DiagnosticProperties**](/windows/win32/bdaiface/?branch=master)
-   [**IBDA\_DigitalDemodulator**](/windows/win32/bdaiface/nn-bdaiface-ibda_digitaldemodulator?branch=master)
-   [**IBDA\_Topology**](/windows/win32/bdaiface/nn-bdaiface-ibda_topology?branch=master)
-   [**IDigitalCableLocator**](/windows/previous-versions/tuner/?branch=master)
-   [**IDigitalCableTuneRequest**](/windows/previous-versions/tuner/nn-tuner-idigitalcabletunerequest?branch=master)
-   [**IEncoderAPI**](/windows/win32/Strmif/nn-strmif-iencoderapi?branch=master)
-   [**IScanningTuner**](/windows/previous-versions/tuner/nn-tuner-iscanningtuner?branch=master)
-   [**IMPEG2PIDMap**](https://msdn.microsoft.com/library/windows/desktop/dd407132)

Documentation on how to use these interfaces to support OCUR devices can be found in the DRI specification, which can be downloaded at <http://www.opencable.com>.

## Related topics

<dl> <dt>

[Overview of Microsoft TV Technologies](overview-of-microsoft-tv-technologies.md)
</dt> </dl>

 

 




