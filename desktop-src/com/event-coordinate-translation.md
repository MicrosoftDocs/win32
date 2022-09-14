---
title: Event Coordinate Translation
description: Event Coordinate Translation
ms.assetid: e7de8af1-a409-4140-9e85-e035bd583912
ms.topic: article
ms.date: 05/31/2018
---

# Event Coordinate Translation

The 96 specification for controls requires that coordinates passed for events fired by the control change from being HIMETRIC to being points based. This change brings the event passing of coordinates in line with properties and methods and thus coordinate translation is no longer the responsibility of the container. This raises certain compatibility issues where a control fires events using a coordinate base that it is not expecting, this should only be an issue where a 96 control container is hosting an older pre-96 control as follows:

-   When an older pre-96 container hosts a 96 control the control will present the event coordinates as points, this should not cause the container any problems as the container should recognize the parameter type.
-   When a 96 container hosts a pre-96 control the control will present the container with coordinates and expect the container to any translation necessary. However the 96 container will be expecting a control to conform to the 96 controls specification and present its coordinates as points. The control uses the [**TransformCoords**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrolsite-transformcoords) method on the [**IOleControlSite**](/windows/desktop/api/OCIdl/nn-ocidl-iolecontrolsite) interface provided by the container in the same way as it does for properties and methods to achieve this.

As a result the user of a 96 container hosting pre-96 controls will need to be aware that further translation of coordinates may be necessary when events are fired.

 

 




