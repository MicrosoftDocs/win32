---
title: Defining Keywords Used to Classify Types of Events
description: Providers use keywords to classify different types of events.
ms.assetid: 1cbad719-bc59-4255-8a15-9e45f363d199
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Defining Keywords Used to Classify Types of Events

Providers use keywords to classify different types of events. For example, you can create a keyword for all read events and then apply the read keyword to any event that performs a read operation such as reading from a file or registry. Consumers could then use the keyword bit values to filter for different classification of events. For example, the consumer could request all read events or all read events from task X (if you also group events by task). To define a keyword, use the **keyword** element.

An ETW tracing session can use the keywords (in the same way that it uses level) to limit the events that the ETW service writes to its event tracing log file. A tracing session can enable the provider using two sets of keyword bitmasks: an "Any" bitmask where the event is written if any of the event's keyword bits match any of the bits set in this mask, and an "All" bitmask where for those events that matched the "Any" case, the event is written only if all of the bits in the "All" mask exist in the event's keyword bitmask.

For example, if the provider defines an event that specifies a read keyword (bit 0) and a local access keyword (bit 1), and a second event that specifies a read keyword (bit 0) and a remote access keyword (bit 2), you could set the "Any" bitmask to 1 to receive all read events, or you could set the "Any" bitmask to 1 and "All" bitmask to 3 to receive only local reads.

The following example shows how to define a keyword. You must specify the keyword's **name** and **mask** attributes. The mask must have only one set—the keyword identifies the bit. The event definition's **keyword** attribute contains a space-separated list of keyword names. The **symbol** and **message** attributes are optional.


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

                <keywords>
                    <keyword name="Read" mask="0x1" symbol="READ_KEYWORD"/>
                    <keyword name="Write" mask="0x2" symbol="WRITE_KEYWORD"/>
                    <keyword name="Local" mask="0x4" symbol="LOCAL_KEYWORD"/>
                    <keyword name="Remote" mask="0x8" symbol="REMOTE_KEYWORD"/>
                </keywords>

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



 

 




