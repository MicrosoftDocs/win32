---
title: Defining Keywords Used to Classify Types of Events
description: Providers use keywords to classify different types of events.
ms.assetid: 1cbad719-bc59-4255-8a15-9e45f363d199
ms.topic: article
ms.date: 05/31/2018
---

# Defining Keywords Used to Classify Types of Events

An ETW keyword is a 64-bit bitmask used to indicate an event's membership in a set of event categories. Each bit in the keyword corresponds to a category. If an event's keyword has a bit set then the event belongs to the event category corresponding to that bit.

The low 48 bits of the keyword (bitmask 0x0000FFFFFFFFFFFF) are defined by the event provider(the author of the manifest). The top 16 bits of the keyword (bitmask 0xFFFF000000000000) are defined by Microsoft. See `winmeta.h` or `winmeta.xml` in the Windows Kits include folder for the definitions of the Microsoft-defined keywords.

Providers use keywords to classify different types of events. For example, you could define keyword bit 0 (keyword value `0x1`) as the **read** category and then apply the **read** keyword to any event that performs a read operation such as reading from a file or registry. Consumers could then use the keyword bit values to filter for different classifications of events. For example, the consumer could set the event collection session's MatchAnyKeyword property to `0x1` to make the session collect only the events in the **read** category.

An ETW event collection session can use the keywords (in the same way that it uses level) to limit the events that the ETW service writes to its event tracing log file. A tracing session can enable the provider using two sets of keyword bitmasks: a "MatchAnyKeyword" bitmask where the event is written if any of the event's keyword bits match any of the bits set in this mask, and a "MatchAllKeyword" bitmask where for those events that matched the "MatchAnyKeyword" case, the event is written only if all of the bits in the "MatchAllKeyword" mask exist in the event's keyword bitmask.

For example, if the provider defines an event that specifies a read keyword (bit 0 = `0x1`) and a local access keyword (bit 1 = `0x2`), and a second event that specifies a read keyword (bit 0 = `0x1`) and a remote access keyword (bit 2 = `0x4`), you could set the event collection session's "MatchAnyKeyword" bitmask to `0x1` (read) and the "MatchAllKeyword" bitmask to `0x0` (none) to receive all read events, or you could set the "MatchAnyKeyword" bitmask to `0x1` and "MatchAllKeyword" bitmask to `0x3` (read + local) to receive only local reads.

To define a keyword for your provider, use the **keyword** element. Once a keyword has been
defined for the provider, you can assign the keyword to any of the provider's events using the **keywords** attribute of the **event** element.

You must specify the keyword's **name** and **mask** attributes. The mask must be an integer with one bit set, between bit 0 and bit 47, such as `mask="256"` or `mask="0x100"` to set keyword bit 8. Bits 48 through 63 are defined by Microsoft (see `winmeta.h` or `winmeta.xml`) and cannot be used in the **keyword** element.

The **symbol** and **message** attributes are optional.

The following example shows how to define a keyword.

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
