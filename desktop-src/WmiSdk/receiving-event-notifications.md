---
description: Event queries are used by temporary event consumers, permanent event consumers, and event providers. Event consumers use event queries to specify events of interest, and event providers use the queries to specify the events that they provide.
ms.assetid: 851ad9bd-2604-4988-8de0-8d29b5300b21
ms.tgt_platform: multiple
title: Receiving Event Notifications
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Event Notifications

Event queries are used by temporary event consumers, permanent event consumers, and event providers. Event consumers use event queries to specify events of interest, and event providers use the queries to specify the events that they provide.

[Temporary consumers](receiving-events-for-the-duration-of-your-application.md) place queries in calls to the [**IWbemServices::ExecNotificationQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationquery) or [**IWbemServices::ExecNotificationQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationqueryasync) method. [Permanent event consumers](receiving-events-at-all-times.md) place queries in the **Query** property of an instance of the [**\_\_EventFilter**](--eventfilter.md) system class.

[Event providers](writing-an-event-provider.md) use event queries to register to support one or more types of events. They place queries in the **EventQueryList** property of an instance of the [**\_\_EventProviderRegistration**](--eventproviderregistration.md) system class. All event providers create an **\_\_EventProviderRegistration** instance to register with Windows Management Instrumentation (WMI). For more information, see [Registering an Event Provider](registering-an-event-provider.md).

Event consumers and providers use the [SELECT statement](select-statement-for-event-queries.md) and a related WHERE clause for event queries, plus a variety of extensions specific to the WMI Query Language (WQL). The extensions are used to protect consumers from being flooded with notifications that occur too frequently to be useful.

Consumers that do not require notification each time an event occurs can specify the following clauses in their queries:

-   [WITHIN](within-clause.md) clause
-   [GROUP](group-clause.md) clause
-   [HAVING](having-clause.md) clause

The WITHIN and HAVING clauses affect the timing of events, and the GROUP clause causes a representative event to be sent in place of a frequently occurring event.

 

 



