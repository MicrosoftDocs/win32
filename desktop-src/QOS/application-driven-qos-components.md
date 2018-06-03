---
title: Application-Driven QOS Components
description: Application-driven QOS components include RSVP service provider, traffic control modules, Resource ReSerVation Protocol, QOS API, and Traffic Control (TC) API.
ms.assetid: a8522461-1995-4ac1-8d02-4d173defbea4
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Application-Driven QOS Components

<dl> <dt>

<span id="RSVP_Service_Provider"></span><span id="rsvp_service_provider"></span><span id="RSVP_SERVICE_PROVIDER"></span>[RSVP Service Provider](rsvp-service-provider.md)
</dt> <dd>

The RSVP service provider facilitates Windows 2000 QOS and invokes other QOS components.

</dd> <dt>

<span id="Traffic_Control_Modules"></span><span id="traffic_control_modules"></span><span id="TRAFFIC_CONTROL_MODULES"></span>[Traffic Control Modules](traffic-control-modules.md)
</dt> <dd>

Traffic control modules facilitate traffic control. Traffic control modules include the packet classifier, the packet scheduler, and the packet shaper.

</dd> <dt>

<span id="Resource_Reservation_Protocol_________RSVP__Service"></span><span id="resource_reservation_protocol_________rsvp__service"></span><span id="RESOURCE_RESERVATION_PROTOCOL_________RSVP__SERVICE"></span>Resource Reservation Protocol ( [RSVP](rsvp.md)) Service
</dt> <dd>

Resource ReSerVation Protocol is invoked by the RSVP service provider (SP), and the carrier of RSVP messages across the entire network, with a functional interface for each QOS-enabled network device, hop across the network. Though important to overall Windows 2000 QOS technology, and to QOS in general, certain QOS faculties do not require RSVP to operate, which means that quality of service can be achieved without RSVP signaling.

</dd> <dt>

<span id="QOS_API"></span><span id="qos_api"></span>[QOS API](qos-api.md)
</dt> <dd>

The QOS API is the programmatic interface to the RSVP SP.

</dd> <dt>

<span id="Traffic_Control_API________TC_API_"></span><span id="traffic_control_api________tc_api_"></span><span id="TRAFFIC_CONTROL_API________TC_API_"></span>[Traffic Control API](traffic-control-api.md) (TC API)
</dt> <dd>

The traffic control API is a programmatic interface to the traffic control components that regulate network traffic on local hosts.

</dd> </dl>

 

 




