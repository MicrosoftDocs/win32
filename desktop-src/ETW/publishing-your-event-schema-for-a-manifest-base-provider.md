---
description: Manifest-based providers use a manifest to publish the schema for their events.
ms.assetid: 37d1a504-ecc7-4df3-bf31-546debb62123
title: Publishing Your Event Schema for a Manifest-based Provider
ms.topic: article
ms.date: 05/31/2018
---

# Publishing Your Event Schema for a Manifest-based Provider

[Manifest-based](about-event-tracing.md) providers use a manifest to publish the schema for their events. The manifest is embedded in the provider binary, which means that the provider must be available on the computer for the consumer to consume its events. For complete details on writing a manifest, see [Writing an Instrumentation Manifest](../wes/writing-an-instrumentation-manifest.md).

The following manifest defines the events that are used in examples in the [Providing Events](providing-events.md) and [Consuming Events](consuming-events.md) section of the document.

``` syntax
<!-- <?xml version="1.0" encoding="UTF-16"?> -->
<instrumentationManifest
    xmlns="http://schemas.microsoft.com/win/2004/08/events" 
    xmlns:win="https://manifests.microsoft.com/win/2004/08/windows/events"
    xmlns:xs="https://www.w3.org/2001/XMLSchema"    
    >

    <instrumentation>
        <events>

            <provider name="Microsoft-Windows-ETWProvider" 
                guid="{D8909C24-5BE9-4502-98CA-AB7BDC24899D}" 
                symbol="ProviderGuid" 
                resourceFileName="c:\code\etw\v2provider\debug\v2provider.exe" 
                messageFileName="c:\code\etw\v2provider\debug\v2provider.exe"
                message="$(string.Provider.Name)"
                >

                <keywords>
                    <keyword name="Read" symbol="READ_KEYWORD" mask="0x1" />
                    <keyword name="Write" symbol="WRITE_KEYWORD" mask="0x2" />
                    <keyword name="Local" symbol="LOCAL_KEYWORD" mask="0x4" />
                    <keyword name="Remote" symbol="REMOTE_KEYWORD" mask="0x8" />
                </keywords>

                <maps>
                    <valueMap name="TransferType">
                        <map value="1" message="$(string.Map.Download)"/>
                        <map value="2" message="$(string.Map.Upload)"/>
                        <map value="3" message="$(string.Map.UploadReply)"/>
                    </valueMap>

                    <bitMap name="DaysOfTheWeek">
                        <map value="0x1" message="$(string.Map.Sunday)"/>
                        <map value="0x2" message="$(string.Map.Monday)"/>
                        <map value="0x4" message="$(string.Map.Tuesday)"/>
                        <map value="0x8" message="$(string.Map.Wednesday)"/>
                        <map value="0x10" message="$(string.Map.Thursday)"/>
                        <map value="0x20" message="$(string.Map.Friday)"/>
                        <map value="0x40" message="$(string.Map.Saturday)"/>
                    </bitMap>
                </maps>

                <templates>

                   <template tid="TransferTemplate">
                        <data name="Image" inType="win:Pointer"/>
                        <data name="Scores" inType="win:UInt16" count="3"/>
                        <data name="ID" inType="win:GUID"/>
                        <data name="Certificate" inType="win:Binary" length="11" />
                        <data name="IsLocal" inType="win:Boolean" />
                        <data name="Path" inType="win:UnicodeString" />

                        <data name="ValuesCount" inType="win:UInt16" />
                        <struct name="Values" count="ValuesCount" >
                            <data name="Name" inType="win:UnicodeString" />
                            <data name="Value" inType="win:UInt16" />
                        </struct>

                        <data name="Day" inType="win:UInt32" map="DaysOfTheWeek"/>
                        <data name="Transfer" inType="win:UInt32" map="TransferType"/>

                        <UserData>
                            <EventData xmlns="ProviderNamespace">
                                <Transfer> %10 </Transfer>
                                <Day> %9 </Day>
                                <ValuesCount> %7 </ValuesCount>
                                <Values> %8 </Values>
                                <Path> %6 </Path>
                                <IsLocal> %5 </IsLocal>
                                <Scores> %2 </Scores>
                                <Image> %1 </Image>
                                <Certificate> %4 </Certificate>
                                <ID> %3 </ID>
                            </EventData>
                        </UserData>
                    </template>

                </templates>

                <events>
                    <event value="1" 
                        level="win:Informational" 
                        template="TransferTemplate" 
                        symbol="TransferEvent"
                        message ="$(string.Event.WhenToTransfer)"
                        keywords="Read Local" />
                </events>


            </provider>

        </events>

    </instrumentation>

    <localization>
        <resources culture="en-US">
            <stringTable>

                <string id="Provider.Name" value="Microsoft-Windows-ETWProvider"/>

                <string id="Map.Download" value="Download"/>
                <string id="Map.Upload" value="Upload"/>
                <string id="Map.UploadReply" value="Upload-reply"/> 

                <string id="Map.Sunday" value="Sunday"/>
                <string id="Map.Monday" value="Monday"/>
                <string id="Map.Tuesday" value="Tuesday"/>
                <string id="Map.Wednesday" value="Wednesday"/>
                <string id="Map.Thursday" value="Thursday"/>
                <string id="Map.Friday" value="Friday"/>
                <string id="Map.Saturday" value="Saturday"/>

                <string id="Event.WhenToTransfer" value="The %10 transfer will occur %9."/>

            </stringTable>
        </resources>
    </localization>

</instrumentationManifest>
```

 

 
