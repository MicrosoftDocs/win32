---
title: ChannelPublishingType Complex Type
description: Defines the logging properties for the session that the channel uses. | ChannelPublishingType Complex Type
ms.assetid: 4b3980f4-8652-4070-97c0-99cd1a9fc85a
keywords:
- ChannelPublishingType complex type EventLog
topic_type:
- apiref
api_name:
- ChannelPublishingType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ChannelPublishingType Complex Type

Defines the logging properties for the session that the channel uses.

``` syntax
<xs:complexType name="ChannelPublishingType">
    <xs:sequence
        minOccurs="0"
    >
        <xs:element name="level"
            type="UInt8Type"
            default="0"
            minOccurs="0"
         />
        <xs:element name="keywords"
            type="UInt64Type"
            default="0"
            minOccurs="0"
         />
        <xs:element name="controlGuid"
            type="GUIDType"
            minOccurs="0"
         />
        <xs:element name="bufferSize"
            type="UInt32Type"
            minOccurs="0"
         />
        <xs:element name="minBuffers"
            type="UInt32Type"
            minOccurs="0"
         />
        <xs:element name="fileMax"
            type="UInt32Type"
            minOccurs="0"
         />
        <xs:element name="maxBuffers"
            type="UInt32Type"
            minOccurs="0"
         />
        <xs:element name="latency"
            type="UInt32Type"
            minOccurs="0"
         />
        <xs:element name="clockType"
            default="SystemTime"
            minOccurs="0"
        >
            <xs:simpleType>
                <xs:restriction
                    base="xs:string"
                >
                    <xs:enumeration
                        value="SystemTime"
                     />
                    <xs:enumeration
                        value="QPC"
                     />
                </xs:restriction>
            </xs:simpleType>
        </xs:element>
        <xs:element name="sidType"
            minOccurs="0"
        >
            <xs:simpleType>
                <xs:restriction
                    base="xs:string"
                >
                    <xs:enumeration
                        value="None"
                     />
                    <xs:enumeration
                        value="Publishing"
                     />
                </xs:restriction>
            </xs:simpleType>
        </xs:element>
        <xs:any
            processContents="lax"
            minOccurs="0"
            maxOccurs="unbounded"
            namespace="##other"
         />
    </xs:sequence>
    <xs:anyAttribute
        processContents="lax"
        namespace="##other"
     />
</xs:complexType>
```

## Child elements



| Element                                                                              | Type                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**bufferSize**](eventmanifestschema-buffersize-channelpublishingtype-element.md)   | [**UInt32Type**](eventmanifestschema-hexint32type-simpletype.md) | The amount of memory, in kilobytes, to allocate for each buffer. If you expect a relatively low event rate, the buffer size should be set to the memory page size. If the event rate is expected to be relatively high, you should specify a larger buffer size and increase the maximum number of buffers.<br/> The buffer size affects the rate at which buffers fill and must be flushed. Although a small buffer size requires less memory, it increases the rate at which buffers must be flushed.<br/> The default buffer size for Analytic and Debug channels is 4 KB and for Admin and Operational it is 64 KB.<br/>                                                                                                                |
| [**clockType**](eventmanifestschema-clocktype-channelpublishingtype-element.md)     |                                                                   | The clock resolution to use when logging the time stamp for each event. You can specify SystemTime or QPC. SystemTime provides a low-resolution (10 milliseconds) time stamp but is comparatively less expensive to retrieve. The default is SystemTime. <br/> Query performance counter (QPC) provides a high-resolution (100 nanoseconds) time stamp but is comparatively more expensive to retrieve. You should QPC if you have high event rates or if the consumer merges events from different buffers.<br/>                                                                                                                                                                                                                                 |
| [**controlGuid**](eventmanifestschema-controlguid-channelpublishingtype-element.md) | [**GUIDType**](eventmanifestschema-guidtype-simpletype.md)       | Identifies the session GUID for an ETW session that contains WPP events. This setting is only allowed for channels of type Debug. These channels cannot be fully enabled with keywords set to zero (0x0000000000000000). They must be enabled with keywords set to 0xffffffffffffffff.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **fileMax**                                                                          | [**UInt32Type**](eventmanifestschema-hexint32type-simpletype.md) | The maximum number of times that you want the service to create a new log file when the channel is enabled (includes when the computer is restarted). If the value is 0 or 1, the service will overwrite the log file each time the channel is enabled and the previous events will be lost. If the value is greater than 1, the service will create a new log file each time the channel is enabled in order to preserve the events. The default is 1 and the maximum that you can specify is 16.<br/> The service appends a three digit decimal number between 0 and fileMax 1 to each file name. For example, *filename*.etl.xxx, where xxx is the three digit decimal number. The files are located in %windir%\\System32\\winevt\\Logs.<br/> |
| [**keywords**](eventmanifestschema-keywords-channelpublishingtype-element.md)       | [**UInt64Type**](eventmanifestschema-hexint64type-simpletype.md) | A bitmask that determines the category of events that are written to the channel. If the value of **keywords** attribute is 0, all events that the provider writes are written to the channel; otherwise only events that have defined a keyword that is included in the **keywords** bitmask are written to the channel. The default is 0.<br/> Debug channels that have the controlGuid attribute set must set the **keywords** attribute to 0xFFFFFFFFFFFFFFFF.<br/> The session passes the keywords value to the provider when it enables the provider.<br/>                                                                                                                                                                            |
| [**latency**](eventmanifestschema-latency-channelpublishingtype-element.md)         | [**UInt32Type**](eventmanifestschema-hexint32type-simpletype.md) | The time to wait before flushing the buffers, in milliseconds. If zero, ETW flushes the buffers as soon as they become full. If nonzero, ETW flushes all buffers that contain events based on the value even if the buffer is not full. Typically, you want to flush buffers only when they become full. Forcing the buffers to flush can increase the file size of the log file with unfilled buffer space. The default value is 1 second for Admin and Operational logs and 5 seconds for Analytic and Debug logs.<br/>                                                                                                                                                                                                                               |
| [**level**](eventmanifestschema-level-channelpublishingtype-element.md)             | [**UInt8Type**](eventmanifestschema-hexint8type-simpletype.md)   | The severity level of the events to write to the channel. The service writes events to the channel that have a level value that is less than or equal to the specified value. The default is 0, which means to log events with any level value.<br/> The session passes the level value to the provider when it enables the provider.<br/>                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**maxBuffers**](eventmanifestschema-maxbuffers-channelpublishingtype-element.md)   | [**UInt32Type**](eventmanifestschema-hexint32type-simpletype.md) | The maximum number of buffers to allocate for the session. Typically, this value is the minimum number of buffers plus twenty. This value must be greater than or equal to the value specified for minBuffers.<br/> The default maximum number of buffers for Analytic and Debug channels is 10 KB and for Admin and Operational it is 64 KB.<br/>                                                                                                                                                                                                                                                                                                                                                                                                |
| [**minBuffers**](eventmanifestschema-minbuffers-channelpublishingtype-element.md)   | [**UInt32Type**](eventmanifestschema-hexint32type-simpletype.md) | The minimum number of buffers to allocate for the session. The default is zero.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [**sidType**](eventmanifestschema-sidtype-channelpublishingtype-element.md)         |                                                                   | Determines whether to include a security identifier (SID) of the principal with each event written to the channel. To include the SID with the event, set this attribute to "Publishing". The SID is set based on the thread identity at the time the event is written. If you do not want to include the SID with the event, set this attribute to "None". The default is "Publishing".<br/>                                                                                                                                                                                                                                                                                                                                                           |



## Remarks

You can specify this publishing information for Analytic and Debug channel types or for any channel that specifies Custom isolation.

Although you can specify level and keywords, you should consider that these will be the only events that you will receive from the provider for that channel.

When a buffer is full, ETW flushes the buffer to the log file. If the buffers are filled faster than they can be flushed, new buffers are allocated and added to the session's buffer pool, up to the maximum number specified. Beyond this limit, the session discards incoming events until a buffer becomes available.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





