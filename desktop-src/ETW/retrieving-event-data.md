---
description: Understand how to retrieve event data when you consume events. To consume event-specific data, the consumer must know the format of the event data.
ms.assetid: d783ff64-73c5-4ace-a866-38a42db7c8b6
title: Retrieving Event Data
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Event Data

To consume event specific data, the consumer must know the format of the event data. This is not an issue if you are consuming events from your own provider because you know the format of the data. However, to consume an event from any provider, the provider must publish the layout of the event data. For an overview of how event metadata operates as well as how to publish your event metadata so others can use it, see [Event Metadata Overview](event-metadata-overview.md).

To consume events on Windows Vista that were published using a manifest, MOF, or TMF files, as well as TraceLogging events, see [Retrieving Event Data Using TDH](retrieving-event-data-using-tdh.md).

To consume events prior to Windows Vista that were published using MOF, see [Retrieving Event Data Using MOF](retrieving-event-data-using-mof.md).

 

 



