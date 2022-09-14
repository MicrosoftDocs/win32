---
title: Change Notifications
description: The Base Filtering Engine (BFE) change notifications follow the publish/subscribe pattern.
ms.assetid: 443f1767-5694-4584-ba0f-229275900774
ms.topic: article
ms.date: 05/31/2018
---

# Change Notifications

The Base Filtering Engine (BFE) change notifications follow the publish/subscribe pattern: in order to receive one of the published change notifications, an application has to subscribe to it.

The published BFE change notifications are Add and Remove for [**callouts**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_callout_subscription0), [**filters**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_filter_subscription0), [**providers**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_provider_subscription0), [**provider contexts**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_provider_context_subscription0), and [**sub-layers**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_sublayer_subscription0).

To subscribe to one of the above notifications, an application calls the corresponding [**Fwpm\*SubscribeChanges0**](fwp-mgmt-functions.md) management function (for example, [**FwpmCalloutSubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutsubscribechanges0)). The callback function passed as an argument to **Fwpm\*SubscribeChanges0** is invoked by BFE when the change to which it subscribed occurs.

To unsubscribe to one of the above notifications, an application calls the corresponding **Fwpm\*UnsubscribeChanges0** management function (for example, [**FwpmCalloutUnsubscribeChanges0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutunsubscribechanges0)).

To see the current subscriptions for one of the above notifications, an application calls the corresponding [**Fwpm\*SubscriptionsGet0**](fwp-mgmt-functions.md) management function (for example [**FwpmCalloutSubscriptionsGet0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmcalloutsubscriptionsget0)).

The change notifications offered by the BFE are:

-   Asynchronous — The function call that triggered a notification may return before the notification has been dispatched to all subscribers.
-   Unreliable — No guarantee is made that notifications will be successfully delivered.

Subscribers do not receive notifications for changes made with the session handle they used to subscribe. Generally, subscribers only need to be informed of the changes made by others; they already know which changes were made by themselves.

 

 




