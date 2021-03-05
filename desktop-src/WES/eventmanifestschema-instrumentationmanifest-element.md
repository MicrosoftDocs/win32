---
title: instrumentationManifest Element
description: The root node of the manifest.
ms.assetid: cb7b5201-be11-48f9-bcca-4606904f0c1d
keywords:
- instrumentationManifest element EventLog
topic_type:
- apiref
api_name:
- instrumentationManifest
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# instrumentationManifest Element

The root node of the manifest.

``` syntax
<xs:element name="instrumentationManifest">
    <xs:complexType>
        <xs:complexContent>
            <xs:extension
                base="InstrumentationManifestType"
            >
                <xs:choice
                    maxOccurs="3"
                >
                    <xs:choice>
                        <xs:element name="metadata"
                            type="MetadataType"
                         />
                        <xs:element name="instrumentation"
                            type="InstrumentationType"
                         />
                    </xs:choice>
                    <xs:element name="localization"
                        type="LocalizationType"
                     />
                    <xs:any
                        processContents="lax"
                        minOccurs="0"
                        maxOccurs="unbounded"
                        namespace="##other"
                     />
                </xs:choice>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
</xs:element>
```

## Child elements



| Element                                                                                        | Type                                                                               | Description                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**instrumentation**](eventmanifestschema-instrumentation-instrumentationmanifest-element.md) | [**InstrumentationType**](eventmanifestschema-instrumentationtype-complextype.md) | This section defines one or more event providers and the events that they log.<br/>                                                                                                                                                                                                                     |
| [**localization**](eventmanifestschema-localization-instrumentationmanifest-element.md)       | [**LocalizationType**](eventmanifestschema-localizationtype-complextype.md)       | This section defines the localized message strings that consumers use for display. For example, this section would contain the localized message string for the name of your provider, the events that you define, and any event attributes that you define, such as channels, tasks, and opcodes.<br/> |
| [**metadata**](eventmanifestschema-metadata-instrumentationmanifest-element.md)               | [**MetadataType**](eventmanifestschema-metadatatype-complextype.md)               | This section defines metadata types that other manifests can use. For an example, see the Winmeta.xml file included in the \\Include folder of the Windows SDK.<br/>                                                                                                                                    |



## Remarks

The **instrumentationManifest** element must contain the following namespaces:

<dl> xmlns="https://schemas.microsoft.com/win/2004/08/events"  
xmlns:win="https://manifests.microsoft.com/win/2004/08/windows/events"  
xmlns:xs="https://www.w3.org/2001/XMLSchema"  
</dl>

A manifest must contain an instrumentation section and a localization section. The instrumentation section and metadata section are mutually exclusive (you cannot define both in the same manifest). Although you can create a manifest that contains a metadata section, the service will not use it; the only metadata that the service recognizes is the metadata found in the Winmeta.xml file.

## Examples

The following example shows the skeleton of a fully defined instrumentation manifest.


```XML
<instrumentationManifest
    xmlns="http://schemas.microsoft.com/win/2004/08/events" 
    xmlns:win="https://manifests.microsoft.com/win/2004/08/windows/events"
    xmlns:xs="https://www.w3.org/2001/XMLSchema"    
    >

    <instrumentation>
        <events>
            <provider ...>
                <channels>
                    <importChanel .../>
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
                <namedQueries>
                    <patternMap ...>
                        <map .../>
                    </patternMap>  
                </namedQueries>
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



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





