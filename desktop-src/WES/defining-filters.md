---
title: Defining Filters
description: A provider can define filters that a session uses to filter events based on event data.
ms.assetid: b43912af-0e9c-414b-b3fa-03e7e35e493c
ms.topic: article
ms.date: 05/31/2018
---

# Defining Filters

A provider can define filters that a session uses to filter events based on event data. With level and keywords, ETW determines whether the event is written to the log. However, with filters, the provider uses the filter data criteria that the controlling session passes to it (see the [*EnableCallback*](/windows/desktop/api/evntprov/nc-evntprov-penablecallback) function) to determine whether it writes the event to that session. The filters are applicable only when an ETW tracing session enables your provider.

Typically, providers just write events, and the session identifies the types of events that it wants using level and keywords. If the provider defined a data filter for an event type, the session could use it to filter out events for that event type based on the event data (the semantics of the filter is defined by the provider). For example, if your provider generates process events, you could define a data filter that filtered process events based on a process identifier. The session could then pass a process identifier as filter data to the provider and receive only process events for that process identifier.

The following example shows how to use the **filter** element to define a filter. You must specify the filter's **name** and **value** attributes; the other attributes are optional. The **tid** attribute is required if the filter requires that the session pass filter data.


```XML
<instrumentationManifest
    xmlns="http://schemas.microsoft.com/win/2004/08/events" 
    xmlns:win="http://manifests.microsoft.com/win/2004/08/windows/events"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    >

    <instrumentation>
        <events>
            <provider name="Microsoft-Windows-SampleProvider"
                guid="{1db28f2e-8f80-4027-8c5a-a11f7f10f62d}"
                symbol="PROVIDER_GUID"
                resourceFileName="<path to the exe or dll that contains the metadata resources>"
                messageFileName="<path to the exe or dll that contains the string resources>"
                message="$(string.Provider.Name)">

                . . .

                <filters>
                    <filter name="Pid"
                            value="1"
                            tid="t1"
                            symbol="FILTER_PID"/>
                </filters>

                <templates>
                    <template tid="t1">
                        <data name="Pid" inType="win:UInt32"/>
                    </template>
                </templates>

                . . .

            </provider>
        </events>
    </instrumentation>

    <localization>
        <resources culture="en-US">
            <stringTable>
                <string id="Provider.Name" value="Sample Provider"/>
            </stringTable>
        </resources>
    </localization>

</instrumentationManifest>
```