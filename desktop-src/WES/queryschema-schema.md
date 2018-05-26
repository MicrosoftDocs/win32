---
title: Query Schema
ms.assetid: 5710231b-5195-413e-8953-e47a411897a6
description: 
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Query Schema

The Query Schema defines the following elements and types that you can use to write a structured XML query to retrieve events from a channel or log file:

-   [QuerySchema Elements](queryschema-elements.md)
-   [QuerySchema Complex Types](queryschema-complex-types.md)

The elements section contains the names of the elements that you use in your query; however, to get the details for each element, see the complex type that contains the element.

A query can contain one or more XPath expressions that are used to include or exclude event in the query result set. You can query for events from multiple channels or log files but you cannot mix channels and log files. You can use a query in any function that takes an XPath (for example, the [**EvtQuery**](/windows/win32/WinEvt/nf-winevt-evtquery?branch=master) or [**EvtSubscribe**](/windows/win32/WinEvt/nf-winevt-evtsubscribe?branch=master) functions). Each XPath that you specify is limited to 32 expressions. For an example, see [Consuming Events](consuming-events.md).

The Windows SDK includes the schema in the \\Include\\Query.xsd file.

In addition to the Query schema, Windows Event Log also defines the following schemas:

-   [EventManifest Schema](eventmanifestschema-schema.md)—defines the elements and types used to write an instrumentation manifest.
-   [Event Schema](eventschema-schema.md)—defines the elements and types used to render an event.

## Related topics

<dl> <dt>

[Consuming Events](consuming-events.md)
</dt> </dl>

 

 




