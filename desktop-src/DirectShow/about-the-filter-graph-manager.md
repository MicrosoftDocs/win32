---
description: About the Filter Graph Manager
ms.assetid: a227539a-7f9a-4f8d-99fe-f9ab67df9ef4
title: About the Filter Graph Manager
ms.topic: article
ms.date: 05/31/2018
---

# About the Filter Graph Manager

The [Filter Graph Manager](filter-graph-manager.md) is a COM object that controls the filters in a filter graph. It performs many functions, including the following:

-   Coordinating state changes among the filters.
-   Establishing a reference clock.
-   Communicating events back to the application.
-   Providing methods for applications to build the filter graph.

Each of these functions is described briefly here. Details can be found elsewhere in the documentation.

**State changes**. State changes within filters must occur in a particular order. Therefore, the application does not issue state-change commands directly to the filters. Instead, it gives a single command to the Filter Graph Manager, which distributes the command to each of the filters. Seeking works in a similar fashion: The application gives a seek command to the Filter Graph Manager, which distributes it to the filters.

**Reference clock**. All of the filters in the graph use the same clock, called a *reference clock*. The reference clock ensures that all the streams are synchronized. The time at which a video frame or audio sample should be rendered is called the *presentation time*. The presentation time is measured relative to the reference clock. The Filter Graph Manager chooses a reference clock, usually either the clock on the sound card, or the system clock.

**Graph events**. The Filter Graph Manager uses an event queue to inform the application of events that occur in the filter graph. This mechanism is similar to a Windows message loop.

**Graph-building methods**. The Filter Graph Manager provides methods for the application to add filters to the graph, connect filters to other filters, and disconnect filters.

One function the Filter Graph Manager does not handle is moving data from one filter to the next. This is done by the filters themselves, through their pin connections. Processing always happens on a separate thread.

> [!Note]  
> Filters are always free-threaded, reside in the same process as the Filter Graph Manager, and are loaded from in-process servers. Therefore, method calls are not marshaled between filters, or between filters and the Filter Graph Manager.

 

## Related topics

<dl> <dt>

[Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> <dt>

[Setting the Graph Clock](setting-the-graph-clock.md)
</dt> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> </dl>

 

 



