---
title: Defining Channels
description: Events can be written to event log channels, event tracing log files, or both. A channel is basically a sink that collects events.
ms.assetid: 3c2f39ee-fbc0-40ae-8279-566905250f47
ms.topic: article
ms.date: 05/31/2018
---

# Defining Channels

Events can be written to event log channels, event tracing log files, or both. A channel is basically a sink that collects events. If the target audience for your events uses event consumers such as the Windows Event Viewer, you must define new channels to collect your events or import an existing channel that another provider defined.

To define your own channels, use the **channel** element. To define an imported channel, use the **importChannel** element. You can specify up to eight channels in any combination of imported channels or channels that you define.

The channel must be of one of four types: Admin, Operational, Analytic, and Debug. Each channel type has an intended audience, which determines the type of events that you write to the channel. For a description of each type, see the [**ChannelType**](eventmanifestschema-channeltype-complextype.md) complex type.

To specify the channel to which an event is written, set the event definition's **channel** attribute to the same value as the channel definition's **chid** attribute. Events can only be written to one channel at a time, but can also be collected by up to 7 other ETW sessions at the same time.

The following example shows how to import a channel. You must set the **chid** and **name** attributes. The **chid** attribute uniquely identifies the channel—each channel identifier in your list of channels must be unique. Set the **name** attribute to the same name that the provider used when it defined the channel.


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

                <channels>
                    <channel chid="c1"
                             name="Microsoft-Windows-BaseProvider/Admin"
                             symbol="CHANNEL_BASEPROVIDER_ADMIN"
                             type="Admin"/>
                </channels>

                . . .

            </provider>
        </events>
    </instrumentation>

    <localization>
        <resources culture="en-US">
            <stringTable>
                <string id="Provider.Name" value="Microsoft-Windows-SampleProvider"/>
            </stringTable>
        </resources>
    </localization>

</instrumentationManifest>
```

Although Winmeta.xml defines legacy channels that you can import, you should not use them unless you are supporting legacy consumers that consume events out of the legacy channels (for example, Application or System). The Winmeta.xml file is included in the Windows SDK.

The following example shows how to define a channel. You must set the **chid**, **name**, and **type** attributes. The **chid** attribute uniquely identifies the channel—each channel identifier in your list of channels must be unique. Set the **chid** attribute to a value that is unique for the channels that your provider lists; the channel identifier is referenced in one or more of your event definitions. The convention for naming the channel is to use the provider name and channel type in the form, *providername*/*channeltype*.

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

                <channels>
                    <importChannel chid="c1"
                                   name="Microsoft-Windows-BaseProvider/Admin"
                                   symbol="CHANNEL_BASEPROVIDER_ADMIN"
                                   />

                    <channel chid="c2"
                             name="Microsoft-Windows-SampleProvider/Operational"
                             type="Operational"
                             enabled="true"
                             />
                </channels>

                . . .

            </provider>
        </events>
    </instrumentation>

    <localization>
        <resources culture="en-US">
            <stringTable>
                <string id="Provider.Name" value="Microsoft-Windows-SampleProvider"/>
            </stringTable>
        </resources>
    </localization>

</instrumentationManifest>
```
