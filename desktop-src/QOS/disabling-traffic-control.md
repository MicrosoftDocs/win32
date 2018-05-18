---
title: Disabling Traffic Control
description: Traffic control is invoked by default, and is done so immediately upon the receipt of a sending FLOWSPEC.
ms.assetid: 'ca85ab95-2292-44ed-af5b-69a570b47545'
---

# Disabling Traffic Control

Traffic control is invoked by default, and is done so immediately upon the receipt of a sending [**FLOWSPEC**](flowspec.md). Application programmers, however, can disable traffic control by using the [SERVICE\_NO\_TRAFFIC\_CONTROL](service-no-traffic-control.md) service type. When the SERVICE\_NO\_TRAFFIC\_CONTROL service type is used, traffic control is not invoked on the specified flow regardless of RSVP signaling. If quality of service is reset (modified) without the SERVICE\_NO\_TRAFFIC\_CONTROL flag, traffic control is invoked.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

 

 




