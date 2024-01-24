---
title: EventManifest Schema
ms.assetid: 89acbc43-739b-4e89-a96a-cc3438ec8ecc
description: "Learn more about: EventManifest Schema"
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# EventManifest Schema

The EventManifest schema defines the following elements and types that you use to write an instrumentation manifest:

-   [EventManifestSchema Elements](eventmanifestschema-elements.md)
-   [EventManifestSchema Simple Types](eventmanifestschema-simple-types.md)
-   [EventManifestSchema Complex Types](eventmanifestschema-complex-types.md)

The elements section contains the names of the elements that you use in your manifest; however, to get the details for each element, see the complex type that contains the element.

An instrumentation manifest is an XML file that defines an event provider, the channels to which the events are written, the events themselves, the event filtering criteria such as levels, tasks, and opcodes, and the localized strings used when rendering the events. The convention is to use .man as the extension for manifest files. For details on writing a manifest, see [Writing an Instrumentation Manifest](writing-an-instrumentation-manifest.md).

The Windows SDK includes the schema in the \\Include\\Eventman.xsd file. You can use the XSD to validate your manifest.

In addition to the EventManifest schema, Windows Event Log also defines the following schemas:

-   [Event Schema](eventschema-schema.md)—defines the elements and types used to render an event.
-   [Query Schema](queryschema-schema.md)—defines the elements and types used to write a query to retrieve events from one or more channels.

 

 




