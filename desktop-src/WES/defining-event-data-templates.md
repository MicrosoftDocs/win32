---
title: Defining Event Data Templates
description: Providers use data templates to define the event-specific data that they include with an event and to define the filter data that an ETW tracing session can pass to the provider when it enables the provider.
ms.assetid: 064227a2-7ce8-461a-9dc0-7519652e6628
ms.topic: article
ms.date: 05/31/2018
---

# Defining Event Data Templates

Providers use data templates to define the event-specific data that they include with an event and to define the filter data that an ETW tracing session can pass to the provider when it enables the provider. If the event does not include event-specific data, you will not define a template. To define a template, use the **template** element. A template includes a data item for each piece of data that the provider includes with the event. You can specify integral types, strings, arrays, and structures. You must write the event data in the order that the data items were defined in the template.

You can also include in the template, an XML fragment that consumers should use to determine how to render the event data. If you do not include the fragment, consumers should render the event data in the order that the data items were defined in the template.

When you define a template, you must give it a template identifier that you use to reference the template in an event definition. Each data item in the template must specify a name and input data type (for a list of input types, see the Remarks section of the [**InputType**](eventmanifestschema-inputtype-complextype.md) complex type). If the input data type can be rendered in multiple formats, you should specify the output data type that tells consumers how to render the data item. For example, an UInt32 input data type can be rendered as an unsigned integer, thread identifier, IPv4 address, and Win32 error code among others. If you do not specify the output data type, consumers should use the input type's default output type to render the data item.

To specify an array, include the **count** attribute on the data item and set it to the number of elements in the array. The array can be a variable size array or fixed size array. If the array is a fixed size array, set **count** to the size of the array. For example, if an array of integers has a fixed size of 10, set **count** to 10. When you write the array, you must write 40 bytes of data.

If the array is a variable size array, set **count** to the name of the data item that contains the size of the array. If the array contains pointers, the address of the pointers are written as the event data, not the data to which the pointers point.

You must specify the **length** attribute if the data item is a binary blob. You can also specify the **length** attribute for fixed length strings.

Specify the **map** attribute if the data item represents an enumeration value and you want the consumer to print a string for the value instead of the value itself.

If you include structures in the template, you should write the members of the structure individually instead of writing the structure unless you can guarantee 8-byte boundary alignment.

You should carefully consider the information that you include in the events, especially when the events are written into the global channels. As a general rule, you should not include private information in the events. This includes plaintext passwords and personal user information. Additionally, programs run by the user, URLs that the user visited, and other information related to the user activities on the computer should be considered private.

If you must record URLs and user names in the events, do not write them to the Windows channels (System and Application) because these channels are readable by all authenticated users. Instead, write them to your own Operational or Analytic channels. Set the access permissions on these channels to allow only administrators to read the events. You may need to provide an appropriate disclosure to notify users of the fact that private information is made available to the administrators.

The following example shows how to define a template. You must specify the template's **tid** attribute that you reference in the event definition or filter definition.


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

                <maps>
                    <valueMap name="TransferType">
                        <map value="1" message="$(string.TransferType.Download)"/>
                        <map value="2" message="$(string.TransferType.Upload)"/>
                        <map value="3" message="$(string.TransferType.UploadReply)"/>
                    </valueMap>
                    <bitMap name="DaysOfTheWeek">
                        <map value="0x1" message="$(string.DaysOfTheWeek.Sunday)"/>
                        <map value="0x2" message="$(string.DaysOfTheWeek.Monday)"/>
                        <map value="0x4" message="$(string.DaysOfTheWeek.Tuesday)"/>
                        <map value="0x8" message="$(string.DaysOfTheWeek.Wednesday)"/>
                        <map value="0x10" message="$(string.DaysOfTheWeek.Thursday)"/>
                        <map value="0x20" message="$(string.DaysOfTheWeek.Friday)"/>
                        <map value="0x40" message="$(string.DaysOfTheWeek.Saturday)"/>
                    </bitMap>
                </maps>

                <templates>
                    <template tid="t2">
                        <data name="TransferName" inType="win:UnicodeString"/>
                        <data name="Day" inType="win:UInt32" map="DaysOfTheWeek"/>
                        <data name="Transfer" inType="win:UInt32" map="TransferType"/>
                    </template>

                    <template tid="t3">
                        <data name="TransferName" inType="win:UnicodeString"/>
                        <data name="ErrorCode" inType="win:Int32" outType="win:HResult"/>
                        <data name="FilesCount" inType="win:UInt16" />
                        <data name="Files" inType="win:UnicodeString" count="FilesCount"/>
                        <data name="BufferSize" inType="win:UInt32" />
                        <data name="Buffer" inType="win:Binary" length="BufferSize"/>
                        <data name="Certificate" inType="win:Binary" length="11" />
                        <data name="IsLocal" inType="win:Boolean" />
                        <data name="Path" inType="win:UnicodeString" />
                        <data name="ValuesCount" inType="win:UInt16" />
                        <struct name="Values" count="ValuesCount" >
                            <data name="Value" inType="win:UInt16" />
                            <data name="Name" inType="win:UnicodeString" />
                        </struct>
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
                <string id="TransferType.Download" value="Download"/>
                <string id="TransferType.Upload" value="Upload"/>
                <string id="TransferType.UploadReply" value="Upload-reply"/>
                <string id="DaysOfTheWeek.Sunday" value="Sunday"/>
                <string id="DaysOfTheWeek.Monday" value="Monday"/>
                <string id="DaysOfTheWeek.Tuesday" value="Tuesday"/>
                <string id="DaysOfTheWeek.Wednesday" value="Wednesday"/>
                <string id="DaysOfTheWeek.Thursday" value="Thursday"/>
                <string id="DaysOfTheWeek.Friday" value="Friday"/>
                <string id="DaysOfTheWeek.Saturday" value="Saturday"/>
            </stringTable>
        </resources>
    </localization>

</instrumentationManifest>
```
