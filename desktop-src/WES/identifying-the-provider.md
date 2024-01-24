---
title: Identifying the Provider
description: A manifest can identify one or more providers. To identify a provider, use the provider element.
ms.assetid: 3bd40405-2b7a-4709-aef7-8615de8c5b6a
ms.topic: article
ms.date: 05/31/2018
---

# Identifying the Provider

A manifest can identify one or more providers. To identify a provider, use the **provider** element. You must specify the **name**, **guid**, **resourceFileName**, **messageFileName**, and **symbol** attributes. If you localize your manifest, you should also specify the **message** attribute, which consumers use as the display the name of the provider. If you do not specify the **message** attribute, consumers use the value of the **name** attribute.

You can identify up to 16 providers in the manifest. If you want to identify more than 16 providers, you must include the **messageTable** section of the manifest that the seventeenth and on providers must use to assign resource values for the message strings that they define—the message table must not include any message strings that providers 1 through 16 defined.

The following example shows how to use the **provider** element to identify a provider.


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
