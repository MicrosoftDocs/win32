---
title: SystemPropertiesType Complex Type
description: Defines the information that identifies the provider and how it was enabled, the event, the channel to which the event was written, and system information such as the process and thread IDs.
ms.assetid: f86f7940-86cf-49ba-8f09-bf6f473d60fd
keywords:
- SystemPropertiesType complex type EventLog
topic_type:
- apiref
api_name:
- SystemPropertiesType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# SystemPropertiesType Complex Type

Defines the information that identifies the provider and how it was enabled, the event, the channel to which the event was written, and system information such as the process and thread IDs.

``` syntax
<xs:complexType name="SystemPropertiesType">
    <xs:sequence>
        <xs:element name="Provider">
            <xs:complexType>
                <xs:attribute name="Name"
                    type="anyURI"
                    use="optional"
                 />
                <xs:attribute name="Guid"
                    type="GUIDType"
                    use="optional"
                 />
                <xs:attribute name="EventSourceName"
                    type="string"
                    use="optional"
                 />
            </xs:complexType>
        </xs:element>
        <xs:element name="EventID">
            <xs:complexType>
                <xs:simpleContent>
                    <xs:extension
                        base="unsignedShort"
                    >
                        <xs:attribute name="Qualifiers"
                            type="unsignedShort"
                            use="optional"
                         />
                    </xs:extension>
                </xs:simpleContent>
            </xs:complexType>
        </xs:element>
        <xs:element name="Version"
            type="unsignedByte"
            minOccurs="0"
         />
        <xs:element name="Level"
            type="unsignedByte"
            minOccurs="0"
         />
        <xs:element name="Task"
            type="unsignedShort"
            minOccurs="0"
         />
        <xs:element name="Opcode"
            type="unsignedByte"
            minOccurs="0"
         />
        <xs:element name="Keywords"
            type="HexInt64Type"
            minOccurs="0"
         />
        <xs:element name="TimeCreated"
            minOccurs="0"
        >
            <xs:complexType>
                <xs:attribute name="SystemTime"
                    type="dateTime"
                    use="optional"
                 />
                <xs:attribute name="RawTime"
                    type="unsignedLong"
                    use="optional"
                 />
            </xs:complexType>
            <xs:key name="uniqueAtt">
                <xs:selector
                    xpath="."
                 />
                <xs:field
                    xpath="@SystemTime|@RawTime"
                 />
            </xs:key>
        </xs:element>
        <xs:element name="EventRecordID"
            minOccurs="0"
        >
            <xs:complexType>
                <xs:simpleContent>
                    <xs:extension
                        base="unsignedLong"
                     />
                </xs:simpleContent>
            </xs:complexType>
        </xs:element>
        <xs:element name="Correlation"
            minOccurs="0"
        >
            <xs:complexType>
                <xs:attribute name="ActivityID"
                    type="GUIDType"
                    use="optional"
                 />
                <xs:attribute name="RelatedActivityID"
                    type="GUIDType"
                    use="optional"
                 />
            </xs:complexType>
        </xs:element>
        <xs:element name="Execution"
            minOccurs="0"
        >
            <xs:complexType>
                <xs:attribute name="ProcessID"
                    type="unsignedInt"
                    use="required"
                 />
                <xs:attribute name="ThreadID"
                    type="unsignedInt"
                    use="required"
                 />
                <xs:attribute name="ProcessorID"
                    type="unsignedByte"
                    use="optional"
                 />
                <xs:attribute name="SessionID"
                    type="unsignedInt"
                    use="optional"
                 />
                <xs:attribute name="KernelTime"
                    type="unsignedInt"
                    use="optional"
                 />
                <xs:attribute name="UserTime"
                    type="unsignedInt"
                    use="optional"
                 />
                <xs:attribute name="ProcessorTime"
                    type="unsignedInt"
                    use="optional"
                 />
            </xs:complexType>
        </xs:element>
        <xs:element name="Channel"
            type="anyURI"
            minOccurs="0"
         />
        <xs:element name="Computer"
            type="string"
         />
        <xs:element name="Security"
            minOccurs="0"
        >
            <xs:complexType>
                <xs:attribute name="UserID"
                    type="string"
                    use="optional"
                 />
            </xs:complexType>
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



| Element                                                                         | Type                                                        | Description                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Channel**](eventschema-channel-systempropertiestype-element.md)             | anyURI                                                      | The channel to which the event was logged.<br/>                                                                                                                                                                                                                                                                                        |
| [**Computer**](eventschema-computer-systempropertiestype-element.md)           | string                                                      | The name of the computer on which the event occurred.<br/>                                                                                                                                                                                                                                                                             |
| [**Correlation**](eventschema-correlation-systempropertiestype-element.md)     |                                                             | The activity identifiers that consumers can use to group related events together.<br/>                                                                                                                                                                                                                                                 |
| [**EventID**](eventschema-eventid-systempropertiestype-element.md)             |                                                             | The identifier that the provider used to identify the event.<br/>                                                                                                                                                                                                                                                                      |
| [**EventRecordID**](eventschema-eventrecordid-systempropertiestype-element.md) |                                                             | The record number assigned to the event when it was logged.<br/>                                                                                                                                                                                                                                                                       |
| [**Execution**](eventschema-execution-systempropertiestype-element.md)         |                                                             | Contains information about the process and thread that logged the event.<br/>                                                                                                                                                                                                                                                          |
| [**Keywords**](eventschema-keywords-systempropertiestype-element.md)           | [**HexInt64Type**](eventschema-hexint64type-simpletype.md) | A bitmask of the keywords defined in the event. Keywords are used to classify types of events (for example, events associated with reading data).<br/>                                                                                                                                                                                 |
| [**Level**](eventschema-level-systempropertiestype-element.md)                 | unsignedByte                                                | The severity level defined in the event.<br/>                                                                                                                                                                                                                                                                                          |
| [**Opcode**](eventschema-opcode-systempropertiestype-element.md)               | unsignedByte                                                | The opcode defined in the event. Task and opcode are typcially used to identify the location in the application from where the event was logged.<br/>                                                                                                                                                                                  |
| [**Provider**](eventschema-provider-systempropertiestype-element.md)           |                                                             | Identifies the provider that logged the event. The **Name** and **Guid** attributes are included if the provider used an instrumentation manifest to define its events; otherwise, the **EventSourceName** attribute is included if a legacy event provider (using the [Event Logging](/windows/desktop/EventLog/event-logging) API) logged the event.<br/> |
| [**Security**](eventschema-security-systempropertiestype-element.md)           |                                                             | Identifies the user that logged the event.<br/>                                                                                                                                                                                                                                                                                        |
| [**Task**](eventschema-task-systempropertiestype-element.md)                   | unsignedShort                                               | The task defined in the event. Task and opcode are typically used to identify the location in the application from where the event was logged.<br/>                                                                                                                                                                                    |
| [**TimeCreated**](eventschema-timecreated-systempropertiestype-element.md)     |                                                             | The time stamp that identifies when the event was logged. The time stamp will include either the **SystemTime** attribute or the **RawTime** attribute.<br/>                                                                                                                                                                           |
| [**Version**](schema-version-systempropertiestype-element.md)                  | unsignedByte                                                | The version number of the event's definition.<br/>                                                                                                                                                                                                                                                                                     |



## Attributes



| Name              | Type                                                | Description                                                                                                                                                                                                                                                                                             |
|-------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ActivityID        | [**GUIDType**](eventschema-guidtype-simpletype.md) | A globally unique identifier that identifies the current activity. The events that are published with this identifier are part of the same activity.<br/>                                                                                                                                         |
| EventSourceName   | string                                              | The name of the event source that published the event (if the event source is from the legacy [Event Logging](/windows/desktop/EventLog/event-logging) API).<br/>                                                                                                                                                      |
| Guid              | [**GUIDType**](eventschema-guidtype-simpletype.md) | The globally unique identifier that uniquely identifies the provider.<br/>                                                                                                                                                                                                                        |
| KernelTime        | unsignedInt                                         | Elapsed execution time for kernel-mode instructions, in CPU time units. If you are using an ETW private session, use the value in the ProcessorTime member instead. Only available for events logged to an event tracing log file (.etl file).<br/>                                               |
| Name              | anyURI                                              | The name of the provider.<br/>                                                                                                                                                                                                                                                                    |
| ProcessID         | unsignedInt                                         | Identifies the process that generated the event.<br/>                                                                                                                                                                                                                                             |
| ProcessorID       | unsignedByte                                        | The identification number for the processor that processed the event. Only available for events logged to an event tracing log file (.etl file).<br/>                                                                                                                                             |
| ProcessorTime     | unsignedInt                                         | For ETW private sessions, the elapsed execution time for user-mode instructions, in CPU ticks. Only available for events logged to an event tracing log file (.etl file).<br/>                                                                                                                    |
| Qualifiers        | **unsignedShort**                                   | A legacy provider uses a 32-bit number to identify its events. If the event is logged by a legacy provider, the value of **EventID** element contains the low-order 16 bits of the event identifier and the **Qualifier** attribute contains the high-order 16 bits of the event identifier.<br/> |
| RawTime           | unsignedLong                                        | The raw time stamp value; the format of the time stamp depends on the time source used to collect the trace. The raw time stamp offers higher precision than system time. The rendered event output will only contain raw time if you use TraceRpt.exe with the -rts switch.<br/>                 |
| RelatedActivityID | [**GUIDType**](eventschema-guidtype-simpletype.md) | A globally unique identifier that identifies the activity to which control was transferred to. The related events would then have this identifier as their ActivityID identifier.<br/>                                                                                                            |
| SessionID         | unsignedInt                                         | The identification number for the terminal server session in which the event occurred. Only available for events logged to an event tracing log file (.etl file).<br/>                                                                                                                            |
| SystemTime        | dateTime                                            | The system time of when the event was logged.<br/>                                                                                                                                                                                                                                                |
| ThreadID          | unsignedInt                                         | Identifies the thread that generated the event.<br/>                                                                                                                                                                                                                                              |
| UserID            | string                                              | The security identifier (SID) of the user in string form.<br/>                                                                                                                                                                                                                                    |
| UserTime          | unsignedInt                                         | Elapsed execution time for user-mode instructions, in CPU time units. If you are using an ETW private session, use the value in the ProcessorTime member instead. Only available for events logged to an event tracing log file (.etl file).<br/>                                                 |



## Remarks

By default, the event contains the fully qualified domain name (FQDN) of a computer. To use the NETBIOS name rather than the FQDN, you must create a DWORD registry value named CompatFlags under the following registry key, and set the value of CompatFlags to 0x2.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               WINEVT
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

