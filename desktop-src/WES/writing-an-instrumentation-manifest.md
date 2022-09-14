---
title: Writing an Instrumentation Manifest
description: Applications and DLLs use an instrumentation manifest to identify their instrumentation providers and the events that the providers write.
ms.assetid: eec9d129-acde-4302-9121-634b3fad8455
ms.topic: article
ms.date: 05/31/2018
---

# Writing an Instrumentation Manifest

Applications and DLLs use an instrumentation manifest to identify their instrumentation providers and the events that the providers write. A manifest is an XML file that contains the elements that identify your provider. The convention is to use .man as the extension for your manifest. The manifest must conform to the event manifest XSD. For details on the schema, see [EventManifest Schema](eventmanifestschema-schema.md).

An instrumentation provider is any application or DLL that calls the [**EventWriteEx**](/windows/desktop/api/evntprov/nf-evntprov-eventwriteex), [**EventWriteString**](/windows/desktop/api/evntprov/nf-evntprov-eventwritestring), or [**EventWriteTransfer**](/windows/desktop/api/evntprov/nf-evntprov-eventwritetransfer) functions to write events to an [Event Tracing](/windows/desktop/ETW/event-tracing-portal) (ETW) tracing session or an Event Log channel. An application can define a single instrumentation provider that covers all events that it writes or it can define a provider for the application and a provider for each of its DLLs. The number of providers that the application defines in the manifest depends solely on how the application wants to organize the events that it writes.

The advantage of specifying a provider for each DLL is that you can then enable and disable the individual providers and thus the events that they generate. This advantage applies only if the provider is enabled by an ETW tracing session. Any events that specify an event log channel are always written to that channel.

The manifest must identify the provider and the events that it writes but the other metadata such as channels, levels, and keywords are optional; whether you define the optional metadata depends on who will be consuming the events. For example, if administrators or support personnel consume the events using a tool like the Windows Event Viewer that reads events from event log channels, then you must define the channels to which the events are written. However, if the provider will only be enabled by an ETW tracing session, then you do not need to define channels.

Although the levels, tasks, opcodes, and keywords metadata are optional, you should use them to logically group or bucket the events. Grouping the events helps the consumers consume only those events that are of interest. For example, the consumer could query for all events where level is "critical" and keyword is "write", or query for all events written by a specific task.

In addition to consumers using level and keywords to consume specific types of events, an ETW tracing session can use the level and keyword metadata to tell ETW to limit the events that are written to the event tracing log. For example, the session could limit the events to only events where level is "error" or "critical" and keyword is "read".

A provider can define filters that a session uses to filter the events based on event data. With level and keywords, ETW determines whether the event is written to the log but with filters, the provider uses the filter data criteria to determine whether it writes the event to that session. The filters are applicable only when an ETW tracing session enables your provider.

The following sections show how to define the components of the manifest:

-   [Identifying the provider](identifying-the-provider.md)
-   [Defining the channels to where the events are written](defining-channels.md)
-   [Defining the severity levels of events that the provider writes](defining-severity-levels.md)
-   [Defining the tasks and operations that your provider performs](defining-tasks-and-opcodes.md)
-   [Defining the keywords that classify the events that the provider writes](defining-keywords-used-to-classify-types-of-events.md)
-   [Defining the filters that the provider uses to filter the events that it writes](defining-filters.md)
-   [Defining the name/value maps that your template data references](defining-name-value-mappings.md)
-   [Defining the templates that define the event-specific data](defining-event-data-templates.md)
-   [Defining the events that the provider writes](defining-events.md)

Although you can author an instrumentation manifest manually, you should consider using the ECManGen.exe tool that is included in the \\Bin folder of the Windows SDK. The ECManGen.exe tool uses a GUI that guides you through creating a manifest from scratch without ever having to use XML tags. Having knowledge of the information in this section and in the [EventManifest Schema](eventmanifestschema-schema.md) section will help when using the tool.

If you use Visual Studio as your XML editor, you can add the [EventManifest](eventmanifestschema-schema.md) schema to the project (see the XML menu) to take advantage of Intellisense, inline schema validation, and other features to make writing the manifest easy and accurate.

After writing your manifest, use the message compiler to validate the manifest and generate the resource and header files that you include in your provider. For more information, see [Compiling an Instrumentation Manifest](compiling-an-instrumentation-manifest.md).

The following example shows the skeleton of a fully defined event manifest.


```XML
<instrumentationManifest
    xmlns="http://schemas.microsoft.com/win/2004/08/events" 
    xmlns:win="http://manifests.microsoft.com/win/2004/08/windows/events"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    >

    <instrumentation>
        <events>
            <provider ...>
                <channels>
                    <importChannel .../>
                    <channel .../>
                </channels>
                <levels>
                    <level .../>
                </levels>
                <tasks>
                    <task .../>
                </tasks>
                <opcodes>
                    <opcode .../>
                </opcodes>
                <keywords>
                    <keyword .../>
                </keywords>
                <filters>
                    <filter .../>
                </filters>
                <maps>
                    <valueMap ...>
                        <map .../>
                    </valueMap>
                    <bitMap ...>
                        <map .../>
                    </bitMap>
                </maps>
                <templates>
                    <template ...>
                        <data .../>
                        <UserData>
                            <!-- valid XML fragment -->
                        </UserData>
                    </template>
                </templates>
                <events>
                    <event .../>
                </events>
            </provider>
        </events>
    </instrumentation>

    <localization>
        <resources ...>
            <stringTable>
                <string .../>
            </stringTable>
        </resources>
    </localization>

</instrumentationManifest>
```



 

 
