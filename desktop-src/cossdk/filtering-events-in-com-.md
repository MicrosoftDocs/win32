---
description: 'COM+ Events provides two ways to control which events reach which subscribers: publisher filtering and parameter filtering.'
ms.assetid: dfc82a57-5587-462d-a43d-516b7d70e25e
title: Filtering Events in COM+
ms.topic: article
ms.date: 05/31/2018
---

# Filtering Events in COM+

COM+ Events provides two ways to control which events reach which subscribers: *publisher filtering* and *parameter filtering*.

## Publisher Filtering

Publisher filtering controls the order and firing of an event method by an [event class](the-com--event-class-object.md) object. Publisher filtering allows the publisher to determine which subscribers receive a particular event.

An example of effective use of publisher filtering is that of a stock exchange. Most subscribers want to know when a new stock is added. However, many of these same subscribers may not want to know whenever each stock price changes. Publisher filtering provides the granularity required to effectively deliver events to only the subscribers who want this information.

When a method is invoked on the instantiated event class object, it collects any publisher filters on that method. The filter forces the event object to fire the event method to a specific subscriber. The filter determines which subscriptions to fire and in which order to fire them. For example, the filter could read the subscription list and create the order based on some application criteria and then call the subscribers in that order.

For detailed instructions on creating a publisher filter, see [Creating a Publisher Filter](creating-a-publisher-filter.md).

## Parameter Filtering

In contrast to publisher filtering, the COM+ Events service provides an optional subscriber parameter filtering for each subscription and each event method invocation. Parameter filtering evaluates the subscription FilterCriteria property against the parameters of the event method. This type of filtering is used on a per-method, per-subscription basis and provides a level of subscriber filtering at the event source. The filter criteria string recognizes relational operators for checking equality (=, ==, !, !=, ~, ~=, <>), nested parentheses, and logical keywords **AND**, **OR**, or **NOT**.

Parameter filtering occurs after any publisher filtering and when the standard event object is fired for a given subscription. If publisher filtering is used, parameter filtering occurs only when the publisher filter invokes [**IFiringControl::FireSubscription**](/windows/desktop/api/EventSys/nf-eventsys-ifiringcontrol-firesubscription). Because of this, publisher filtering and parameter filtering can compose together but publisher filtering takes precedence.

## Related topics

<dl> <dt>

[Publishing and Delivering Events in COM+](publishing-and-delivering-events-in-com-.md)
</dt> <dt>

[Subscriptions](subscriptions.md)
</dt> <dt>

[The COM+ Event Class Object](the-com--event-class-object.md)
</dt> <dt>

[Using COM+ Events with COM+ Queued Components](using-com--events-with-com--queued-components.md)
</dt> </dl>

 

 



