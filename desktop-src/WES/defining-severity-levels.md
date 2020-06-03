---
title: Defining Severity Levels
description: Levels are used to group events and typically indicate the severity or verbosity of an event.
ms.assetid: dfa4e0a9-4d89-4f50-aef9-1dae0dc11726
ms.topic: article
ms.date: 05/31/2018
---

# Defining Severity Levels

Levels are used to group events and typically indicate the severity or verbosity of an event. To define a level, use the **level** element. The Winmeta.xml file defines the following commonly used severity levels:

-   win:Critical
-   win:Error
-   win:Warning
-   win:Informational
-   win:Verbose

Consumers use levels to query for events that contain a specific level value. An ETW tracing session can also use levels to limit the events that are written to the event tracing log file; events with a level value equal to or less than the specified level value are written to the log file. For example, if the session specified the level value for win:Warning, the log file would contain warning, error, and critical events.

The following example shows how to define a level. You must specify the level's **name** and **value** attributes. The value of the **value** attribute must be in the range from 16 through 255. The **symbol** and **message** attributes are optional.


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

                <levels>
                    <level name="NotValid"
                           value="16"
                           symbol="LEVEL_SAMPLEPROVIDER_NOTVALID"
                           message="$(string.Level.NotValid)"/>
                    <level name="Valid"
                           value="17"
                           symbol="LEVEL_SAMPLEPROVIDER_VALID"
                           message="$(string.Level.Valid)"/>
                </levels>

                . . .

            </provider>
        </events>
    </instrumentation>

    <localization>
        <resources culture="en-US">
            <stringTable>
                <string id="Provider.Name" value="Sample Provider"/>
                <string id="Level.Valid" value="Valid"/>
                <string id="Level.NotValid" value="Not Valid"/>
            </stringTable>
        </resources>
    </localization>

</instrumentationManifest>
```
