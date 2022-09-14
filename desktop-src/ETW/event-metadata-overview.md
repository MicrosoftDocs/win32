---
description: 'This is an overview of what to expect for the end-to-end journey of an event for each of the four tracing technologies furnished by Microsoft: TraceLogging, Manifest-based, WPP, and MOF.'
ms.assetid: 6102593C-C6D5-4BDB-A0EF-067AF91DE00B
title: Event Metadata Overview
ms.topic: article
ms.date: 05/31/2018
---

# Event Metadata Overview

This is an overview of what to expect for the end-to-end journey of an event for each of the four tracing technologies furnished by Microsoft: [TraceLogging](../tracelogging/trace-logging-about.md), [Manifest-based](writing-manifest-based-events.md), [WPP](windows-software-trace-preprocessor.md), and [MOF](tracing-events.md). It approaches the problem with respect to both an individual event's payload and the accompanying metadata that describes its structure, making it possible to later decode the event into sensible pieces of data. Understanding the journey of each piece of an event is important when choosing which tracing technology is appropriate for a project. There is no one-size-fits-all solution to tracing.

## Event Payloads

For any of the Microsoft-provided tracing technologies, when calling the Write command (for instance [**EventWrite**](/windows/desktop/api/Evntprov/nf-evntprov-eventwrite) for manifest-based or [**TraceLoggingWrite**](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingwrite) for TraceLogging), the data provided for the event at runtime is folded into a contiguous binary blob called the event payload. This is separate from the event schema or event metadata (discussed below), which describes the layout of this binary blob for decoding tools. How exactly the generation of the event payload happens varies depending on the tracing technology used and ultimately whether the event is classic ([**TraceEvent**](/windows/win32/api/evntrace/nf-evntrace-traceevent) style) or modern (**EventWrite** style).

For classic events, the flag in [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) is passed into [**TraceEvent**](/windows/win32/api/evntrace/nf-evntrace-traceevent) which determines how this occurs:

\- If **WNODE\_FLAG\_USE\_MOF\_PTR** is specified, an array of [**MOF\_FIELDS**](/windows/win32/api/evntrace/ns-evntrace-mof_field) follows the [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) in memory. The ETW runtime will concatenate the event data as specified in these fields to form the event payload.

\- If **WNODE\_FLAG\_USE\_MOF\_PTR** is not specified, the event payload is constructed by the user directly in memory following the [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header).

Both MOF and WPP are classic providers. However, the WPP implementation takes care of all of this for you.

For non-classic events, a number of [**EVENT\_DATA\_DESCRIPTORS**](/windows/desktop/api/Evntprov/ns-evntprov-event_data_descriptor) are passed into [**EventWrite**](/windows/desktop/api/Evntprov/nf-evntprov-eventwrite). The ETW runtime will concatenate the event data as specified in these descriptors to form the event payload.

Both Manifest-based and TraceLogging technologies are generally modern providers. With manifest-based, if you let mc.exe generate logging code for you (um or km switch), payload generation is taken care of for you. Payload generation is always taken care of by TraceLogging.

The end result is that a payload for an event is generated at runtime. All payloads are fundamentally similar in that they are binary blobs of data containing only the field data for that particular event, regardless of the tracing technology used and which field types are supported by that tracing technology. Without the event metadata, the event payload is meaningless and unintelligable.

The ETW runtime's duty is then to carry this event blob from the provider to the consumer, where it is re-associated with its metadata and becomes decodable. The ETW runtime will add a bit of extra metadata indicating the circumstances of the payload -- for instance things like the timestamp, thread ID, and keywords of the event. This information is relevant to how the event was routed through the runtime, and it is also useful for understanding the identity and context of the event at decoding time. It is eventually surfaced as part of the [**EVENT\_TRACE**](/windows/win32/api/evntrace/ns-evntrace-event_trace) or [**EVENT\_RECORD**](/windows/win32/api/evntcons/ns-evntcons-event_record) for the consumer

## Event Metadata

The journey for event metadata is different depending on which tracing technology is used, and it is one of the largest considerations when comparing each technology.

### MOF

Event metadata is authored by hand by the creator of the event in the form of a special MOF schema in a .mof file. The schema authored must match the payload that is logged in order for the event to be correctly decoded by consumers. Event decoders require that the .mof file is registered on the system using [mofcomp.exe](../wmisdk/mofcomp.md). For more information on publishing MOF schemas, see [Publishing Your Event Schema for a Classic Provider](publishing-your-event-schema-for-a-classic-provider.md).

### WPP

Event metadata is automatically generated and stored in your binary's .pdb by tracewpp.exe during the build process. This metadata can later be extracted in the form of a standalone .tmf file by way of tracepdb.exe. Event decoders typically require either the .pdb or the .tmf file. For more information on tracepdb.exe, see [Tracepdb Overview](/windows-hardware/drivers/devtest/tracepdb-overview), and for more information on tracewpp.exe, see [TraceWPP task](/windows-hardware/drivers/devtest/tracewpp-task).

### Manifest-based

Event definitions are authored in a .man file. Event manifests are run through the manifest compiler ([mc.exe](../wes/message-compiler--mc-exe-.md)), generating the headers needed for source compilation as well as several .bin binary resource files. These resource files must then be compiled as resources into a binary and the resulting binary placed on the system that intends to decode events from that manifest-based provider. Additionally, the manifest must be installed on the system using [wevtutil.exe](../wes/windows-event-log-tools.md) Most importantly, the **resourceFileName** and **messageFileName** attributes on the provider XML element in the installed event manifest must correctly identify the full absolute path to the binary in which the resource files were placed. Note that these paths may be overwritten at manifest install time by using the wevtutil.exe switches /rf and /mf. A system that has not correctly and fully performed these steps will be unable to decode events from this provider. Event decoders thus require an installed manifest, and the binary with the associated resources installed in the location specified by resource and message file paths. For more information on publishing manifest-based schemas, see [Publishing Your Event Schema for a Manifest-based Provider](publishing-your-event-schema-for-a-manifest-base-provider.md).

### TraceLogging

All TraceLogging events are self-describing. The event metadata necessary to decode the event is automatically generated and transmitted along with the payload in a compact binary format. Event decoders need only the TraceLogging event and an understanding of the TraceLogging metadata format.

## Configuring TDH for Decoding

There are many decoding tools out there. However, it is recommended that you use TDH where possible, as it decodes all tracing technologies with a unified API. Depending on the type of tracing you are interested in decoding, TDH may require explicit configuration.

### MOF

TDH utilizes MOF decoding data registered on the system using mofcomp.exe. For more information, see [Publishing Your Event Schema for a Classic Provider](publishing-your-event-schema-for-a-classic-provider.md).

### WPP

TDH must be pointed towards either the .pdb file or the associated .tmf for the WPP provider you are trying to decode. This can be performed by calling [**TdhSetDecodingParameter**](/windows/desktop/api/Tdh/nf-tdh-tdhsetdecodingparameter). Otherwise, the decoding engine will fall back on the environment variable TRACE\_FORMAT\_SEARCH\_PATH.

### Manifest-based

TDH utilizes all manifest-based providers registered on the system using wevtutil.exe.

### TraceLogging

The newest versions of TDH automatically detect and decode TraceLogging events with no additional steps.

 

 
