---
title: Using Windows Event Collector
description: This section lists the topics that explain the tasks that can be accomplished using the Windows Event Collector SDK. Code examples and explanations for all the tasks are included in each of the following topics.
ms.assetid: 3396454a-4f43-45d0-951e-3096b9a4a077
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Using Windows Event Collector

This section lists the topics that explain the tasks that can be accomplished using the Windows Event Collector SDK. Code examples and explanations for all the tasks are included in each of the following topics.

## In This Section

-   [Creating a Collector Initiated Subscription](creating-an-event-collector-subscription.md)

    Provides information and a C++ code example for creating a collector-initiated subscription. A collector-initiated subscription enables you to receive events on a local computer (the event collector) that are forwarded from a remote computer (an event source).

-   [Setting up a Source Initiated Subscription](setting-up-a-source-initiated-subscription.md)

    Provides information and a C++ code example for creating a source-initiated subscription. A source-initiated subscription enables you to receive events on a local computer (the event collector) that are forwarded from a remote computer (an event source) without specifying the event sources in the subscription.

-   [Adding an Event Source to a Collector Initiated Subscription](adding-an-event-source-to-an-event-collector-subscription.md)

    Provides information and a C++ code example for adding an event source (local computer or remote computer) to a collector-initiated subscription. A collector initiated subscription cannot start collecting events until an event source is added to the subscription.

-   [Creating Hardware Event Subscriptions](creating-hardware-event-subscriptions.md)

    Provides information about how to create an event subscription in order to receive hardware events from a computer that has a Baseboard Management Controller (BMC) installed.

-   [Deleting an Event Collector Subscription](deleting-an-event-collector-subscription.md)

    Provides information and a C++ code example for deleting an Event Collector subscription from a local computer.

-   [Displaying the Properties of an Event Collector Subscription](displaying-the-properties-of-an-event-collector-subscription.md)

    Provides information and a C++ code example for displaying the property values of an Event Collector subscription. Property values can provide useful information, such as the addresses of event sources, the status of the subscription and event sources, and information about how events are delivered.

-   [Displaying the Status of an Event Collector Subscription](displaying-the-status-of-an-event-collector-subscription.md)

    Provides information and a C++ code example for displaying the run time status of events sources that are associated to an Event Collector subscription. This enables you to view error messages that can help solve problems, which prevent an event source from forwarding events.

-   [Listing Event Collector Subscriptions](listing-event-collector-subscriptions.md)

    Provides information and a C++ code example for listing the subscriptions that exist on a local computer. You can use the subscription names that are obtained with this example to delete a subscription, add an event source to a subscription, retrieve the properties of a subscription, or view the status of a subscription.

-   [Removing an Event Source from a Collector Initiated Subscription](removing-an-event-source-from-an-event-collector-subscription.md)

    Provides information and a C++ code example for removing an event source from a collector-initiated subscription. You can remove an event source from a collector-initiated subscription without disabling the subscription.

-   [Retrying an Event Collector Subscription](retrying-an-event-collector-subscription.md)

    Provides information and a C++ code example for retrying an Event Collector subscription when one or more event sources have failed. You can retry a single event source or you can retry the entire subscription.

 

 




