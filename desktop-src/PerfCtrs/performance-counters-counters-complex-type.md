---
description: Defines the section of the instrumentation manifest that identifies the provider and the counters that they provide.
ms.assetid: c661f1af-ebe8-4f8a-b77e-a2229f45facd
title: counters Complex Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# counters Complex Type

Defines the section of the instrumentation manifest that identifies the provider and the counters that they provide.

``` syntax
<xs:complexType name="counters">
    <xs:choice
        minOccurs="1"
        maxOccurs="1"
    >
        <xs:element name="provider"
            type="man:provider"
         />
    </xs:choice>
    <xs:attribute name="schemaVersion"
        use="required"
    >
        <xs:simpleType>
            <xs:restriction
                base="xs:string"
            >
                <xs:enumeration
                    value="1.1"
                 />
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
</xs:complexType>
```

## Child elements



| Element      | Type                                                               | Description                                              |
|--------------|--------------------------------------------------------------------|----------------------------------------------------------|
| **provider** | [**man:provider**](performance-counters-provider-complex-type.md) | Identifies a provider that provides counters.<br/> |



## Attributes



| Name          | Type | Description                                                      |
|---------------|------|------------------------------------------------------------------|
| schemaVersion |      | The version of the schema used to write the manifest.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**instrumentation**](/windows/desktop/WES/eventmanifestschema-instrumentationtype-complextype)
</dt> </dl>

 

