---
title: Event Schema
ms.assetid: 36037697-b777-4e5c-99af-77964200a3e4
description: "Learn more about: Event Schema"
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Event Schema

The Event schema defines the following elements and types that identify the elements and attributes of a logged event:

-   [EventSchema Elements](eventschema-elements.md)
-   [EventSchema Simple Types](eventschema-simple-types.md)
-   [EventSchema Complex Types](eventschema-complex-types.md)

The elements section contains the names of the elements that you would find in a logged events; however, to get the details for each element, see the complex type that contains the element.

The Windows SDK includes the schema in the \\Include\\Event.xsd file.

You can use this schema to identify the elements and attributes when calling the [**EvtRender**](/windows/desktop/api/WinEvt/nf-winevt-evtrender) function to render specific sections or properties of the event. For an example that shows how to use this schema when rendering events, see [Rendering Events](rendering-events.md).

In addition to the Event schema, Windows Event Log also defines the following schemas:

-   [EventManifest Schema](eventmanifestschema-schema.md)—defines the elements and types used to write an instrumentation manifest.
-   [Query Schema](queryschema-schema.md)—defines the elements and types used to write a query to retrieve events from one or more channels.

 

 




