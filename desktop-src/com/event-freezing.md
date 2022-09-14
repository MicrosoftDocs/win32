---
title: Event Freezing
description: Event Freezing
ms.assetid: 1e537503-f7e7-42f4-aa3c-3c71715b84fe
ms.topic: article
ms.date: 05/31/2018
---

# Event Freezing

A container can notify a control that it is not ready to respond to events by calling [**IOleControl::FreezeEvents**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-freezeevents) with **TRUE**. It can unfreeze the events by calling **FreezeEvents** with **FALSE**. When a container freezes events, it is freezing event processing, not event receiving; that is, a container can still receive events while events are frozen. If a container receives an event notification while its events are frozen, the container should ignore the event. No other action is appropriate.

A control should take note of a container's call to [**FreezeEvents**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-freezeevents) with **TRUE** if it is important to the control that an event is not missed. While a container's event processing is frozen, a control should implement one of the following techniques:

-   Fire the events in the full knowledge that the container will take no action.
-   Discard all events that the control would have fired.
-   Queue up all pending events and fire them after the container has called [**FreezeEvents**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-freezeevents) with **FALSE**.
-   Queue up only relevant or important events and fire them after the container has called [**FreezeEvents**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-freezeevents) with **FALSE**.

Each technique is acceptable and appropriate in different circumstances. The control developer is responsible for determining and implementing the appropriate technique for the control's functionality.

 

 




