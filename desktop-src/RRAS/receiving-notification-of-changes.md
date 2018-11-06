---
title: Receiving Notification of Changes
description: Many clients can simultaneously update the routing table, and clients must be notified when changes to routing information occur.
ms.assetid: d42e16e2-32b2-4178-967b-e937730b3cca
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Notification of Changes

Many clients can simultaneously update the routing table, and clients must be notified when changes to routing information occur. For example, a client that is not notified of another client's changes to the routing table could advertise outdated route information. This can be prevented by programming clients to register with the routing table manager to be notified of changes in the routing table. The routing table manager sends notifications of changes to all clients that register to receive them.

Change notification applies only to destinations. There is no way to query the routing table manager for changes to a particular route.

When a change is made to one of the routes to a destination, the routing table manager sends out a notification that a change has occurred. This notification goes only to those clients that have registered with the routing table manager for the type of change that has occurred. All changes to routing information in the routing table manager occur in one or more views, and change notification messages can be requested in any subset of supported views.

There are currently three types of change notifications for which a client can register:

-   Notification of any change to the routes for the destination. This request is made using the RTM\_CHANGE\_TYPE\_ALL flag.
-   Notification if the best route to the destination changes, or any of the following information for the current best route changes:

    -   Preference
    -   Next hops
    -   Route flags

    This request is made using the RTM\_CHANGE\_TYPE\_BEST flag.

-   Notification of all changes of the type RTM\_CHANGE\_TYPE\_BEST, except changes in non-forwarding flags in the best route. For example, the router manager waits for changes of this type in the unicast view, and updates information in the unicast forwarder. This request is made using the RTM\_CHANGE\_TYPE\_FORWARDING flag.

Requests for notifications of changes can also be restricted to a subset of destinations by registering for notifications of changes only to "marked" destinations. The client can mark a destination for change notification by calling [**RtmMarkDestForChangeNotification**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmmarkdestforchangenotification).

When a change occurs, the routing table manager checks to see if there are any clients that must be notified of this change. A client must be notified of a change if all of the following conditions are met:

-   The type of change that occurred is a type for which the client has registered for notification
-   Changes to a destination that the client has marked have occurred or any destination, if the client has requested changes for all destinations
-   The client requested change notification for the view in which this change occurred

If the change meets all of the above criteria, the change is cached and the client is notified.

The notification does not specify what the actual changes are, only that they have occurred. The client must retrieve the changes by calling [**RtmGetChangedDests**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetchangeddests) using the notification handle that was obtained from a previous call to [**RtmRegisterForChangeNotification**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmregisterforchangenotification).

 

 




