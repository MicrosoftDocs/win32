---
title: InstrumentationType Complex Type
description: Defines the contents of the instrumentation section of the manifest.
ms.assetid: dbbb978d-50dd-44c0-8bd1-3e48b41afb88
keywords:
- InstrumentationType complex type EventLog
topic_type:
- apiref
api_name:
- InstrumentationType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# InstrumentationType Complex Type

Defines the contents of the instrumentation section of the manifest.

``` syntax
<xs:complexType name="InstrumentationType">
    <xs:sequence>
        <xs:element name="events"
            type="EventsType"
         />
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



| Element                                                                  | Type                                                             | Description                                                        |
|--------------------------------------------------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------|
| [**events**](eventmanifestschema-events-instrumentationtype-element.md) | [**EventsType**](eventmanifestschema-eventstype-complextype.md) | Contains a list of providers that the manifest defines.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





