---
title: Execution (SystemPropertiesType) Element
description: Contains information about the process and thread that logged the event.
ms.assetid: 4d2feb0d-a3e6-479c-aa34-cd95a708add5
keywords:
- Execution element EventLog
topic_type:
- apiref
api_name:
- Execution
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Execution (SystemPropertiesType) Element

Contains information about the process and thread that logged the event.

``` syntax
<xs:element name="Execution">
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
```

The **Execution** element is defined by the [**SystemPropertiesType**](eventschema-systempropertiestype-complextype.md) complex type.

## Attributes



| Name          | Type         | Description                                                                                               |
|---------------|--------------|-----------------------------------------------------------------------------------------------------------|
| KernelTime    | unsignedInt  | Elapsed execution time for kernel-mode instructions, in CPU time units.<br/>                        |
| ProcessID     | unsignedInt  | Identifies the process that generated the event.<br/>                                               |
| ProcessorID   | unsignedByte | The identification number for the processor that processed the event.<br/>                          |
| ProcessorTime | unsignedInt  | For ETW private sessions, the elapsed execution time for user-mode instructions, in CPU ticks.<br/> |
| SessionID     | unsignedInt  | The identification number for the terminal server session in which the event occurred.<br/>         |
| ThreadID      | unsignedInt  | Identifies the thread that generated the event.<br/>                                                |
| UserTime      | unsignedInt  | Elapsed execution time for user-mode instructions, in CPU time units.<br/>                          |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**SystemPropertiesType**](eventschema-systempropertiestype-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**System (EventType)**](eventschema-system-eventtype-element.md)
</dt> </dl>

 

 





