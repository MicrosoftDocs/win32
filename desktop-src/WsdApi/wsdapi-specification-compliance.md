---
description: Web Services on Devices API (WSDAPI) provides support for the Devices Profile for Web Services (DPWS) on Windows Vista, which enables Web Services (WS) communication between Windows-based PCs and network connected devices.
ms.assetid: 61fceca3-a33e-40f7-9370-97605a81eb06
title: WSDAPI Specification Compliance
ms.topic: article
ms.date: 05/31/2018
---

# WSDAPI Specification Compliance

Web Services on Devices API (WSDAPI) provides support for the [Devices Profile for Web Services](https://specs.xmlsoap.org/ws/2006/02/devprof/) (DPWS) on Windows Vista, which enables Web Services (WS) communication between Windows-based PCs and network connected devices. DPWS assembles basic WS specifications, such as [WS-Eventing](https://schemas.xmlsoap.org/ws/2004/08/eventing/), [WS-Discovery](https://specs.xmlsoap.org/ws/2005/04/discovery/ws-discovery.pdf), and [WS-MetadataExchange](https://schemas.xmlsoap.org/ws/2004/09/mex/), and enhances or constrains them to provide a baseline set of capabilities for resource-constrained devices. This baseline specification contains required functionality, such as the ability to describe properties of the device through metadata, and optional functionality, such as the ability to reject specific messages for security reasons.

The WSDAPI implementation in Windows Vista is the first release of explicit support for the DPWS, and is an unmanaged implementation of DPWS that is separate and distinct from other Web Services implementations (such as the [Windows Communication Foundation](/previous-versions/dotnet/netframework-3.0/ms735119(v=vs.85)) or [WS-Management](https://schemas.xmlsoap.org/ws/2005/06/management/)).

The following topics are of interest to device manufacturers and other device implementers that create devices that interoperate with Windows-based WSDAPI clients and hosts without using WSDAPI. These topics describe the implementation of WSDAPI relative to the underlying specifications. They cover the implementation of required functionality, optional functionality, and additional functionality not defined in the specification.

-   [DPWS Specification Compliance](dpws-specification-compliance.md)
-   [WS-Discovery Specification Compliance](ws-discovery-specification-compliance.md)
-   [WS-MetadataExchange and WS-Transfer Specification Compliance](ws-metadataexchange-and-ws-transfer-specification-compliance.md)
-   [Additional WS-Discovery Functionality](additional-ws-discovery-functionality.md)

## Related topics

<dl> <dt>

[WSD Device Development](wsd-device-development.md)
</dt> <dt>

[WSD Device Implementation Recommendations](wsd-device-implementation-recommendations.md)
</dt> </dl>

 

 
