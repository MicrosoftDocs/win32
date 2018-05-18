---
title: Data Complex Type
description: Defines a report property.
ms.assetid: '2da0c353-7b5a-403c-9a4d-5bd59eecd78a'
keywords: ["Data complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Data
api_type:
- Schema
---

# Data Complex Type

Defines a report property.

``` syntax
<xs:complexType name="Data">
    <xs:simpleContent>
        <xs:extension
            base="xsd:string"
        >
            <xs:attribute name="id"
                type="xsd:string"
                use="required"
             />
            <xs:attribute name="name"
                type="xsd:string"
                use="required"
             />
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>
```

## Attributes



| Name | Type           | Description                                                               |
|------|----------------|---------------------------------------------------------------------------|
| id   | **xsd:string** | An identifier that identifies the property.<br/>                    |
| name | **xsd:string** | The localized name of the property that is used in the report.<br/> |



## Remarks

The text body of the **Data** element contains the property's value. The parent element determines the list of properties.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





