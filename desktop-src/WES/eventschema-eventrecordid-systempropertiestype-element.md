---
title: EventRecordID (SystemPropertiesType) Element
description: The record number assigned to the event when it was logged.
ms.assetid: d042de4d-e532-432e-bba2-1876a26860a4
keywords:
- EventRecordID element EventLog
topic_type:
- apiref
api_name:
- EventRecordID
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EventRecordID (SystemPropertiesType) Element

The record number assigned to the event when it was logged.

``` syntax
<xs:element name="EventRecordID">
    <xs:complexType>
        <xs:simpleContent>
            <xs:extension
                base="unsignedLong"
             />
        </xs:simpleContent>
    </xs:complexType>
</xs:element>
```

The **EventRecordID** element is defined by the [**SystemPropertiesType**](eventschema-systempropertiestype-complextype.md) complex type.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





