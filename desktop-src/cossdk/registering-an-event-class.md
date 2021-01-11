---
description: So that subscribers can find an event class and subscribe to it, event classes must be registered in the COM+ catalog.
ms.assetid: b9d59b9d-52ba-4c71-9226-9cb5b93ec3d4
title: Registering an Event Class
ms.topic: article
ms.date: 05/31/2018
---

# Registering an Event Class

So that subscribers can find an event class and subscribe to it, event classes must be registered in the COM+ catalog. COM+ requires a type library that describes the event interfaces and methods so that it can properly match and connect subscribers and publishers. The type library must reside in or be accompanied by a self-registering DLL.

You can use the Component Services administrative tool or the COM+ Administrative functions to register an event class in the COM+ catalog.

**To register an event class with the Component Services administrative tool**

1.  Create a new COM+ application.

2.  Open the application folder and select **Components**.

3.  On the **Action** menu, click **New**. (You can also select the **Components** folder, right-click, point to **New**, and then click **Component**.)

4.  Click **Install new event class(es)**.

5.  Enter the path to the event class component DLL.

6.  Click **OK**.

The event class is registered in the COM+ catalog and can be located by subscribers interested in obtaining the information provided by the event class. For information about how to register the event class by using the COM+ administrative interfaces, see [**ICOMAdminCatalog::InstallEventClass**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-installeventclass).

## Related topics

<dl> <dt>

[Registering a Subscription](registering-a-subscription.md)
</dt> </dl>

 

 



