---
title: StructDefinitionType Complex Type
description: Defines a structure that includes one or more data items that you want to include with the event. | StructDefinitionType Complex Type
ms.assetid: eb6b3682-1035-472b-8027-583d43c31748
keywords:
- StructDefinitionType complex type EventLog
topic_type:
- apiref
api_name:
- StructDefinitionType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StructDefinitionType Complex Type

Defines a structure that includes one or more data items that you want to include with the event.

``` syntax
<xs:complexType name="StructDefinitionType"
    mixed="true"
>
    <xs:sequence>
        <xs:element name="data"
            type="DataDefinitionType"
            maxOccurs="unbounded"
         />
    </xs:sequence>
    <xs:attribute name="name"
        type="string"
        use="required"
     />
    <xs:attribute name="length"
        type="LengthType"
        use="optional"
     />
    <xs:attribute name="count"
        type="CountType"
        use="optional"
     />
    <xs:anyAttribute
        processContents="lax"
        namespace="##other"
     />
</xs:complexType>
```

## Child elements



| Element                                                               | Type                                                                             | Description                                                               |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [**data**](eventmanifestschema-data-structdefinitiontype-element.md) | [**DataDefinitionType**](eventmanifestschema-datadefinitiontype-complextype.md) | Defines a data item that you want to include in the structure.<br/> |



## Attributes



| Name   | Type                                                            | Description                                                                                                                                                                                                                                                                               |
|--------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| count  | [**CountType**](eventmanifestschema-counttype-simpletype.md)   | The number of elements in an array of structures. This attribute indicates that the structure is defining an array of structures. You can specify the actual count or the name of a data item outside of the structure that contains the count. <br/>                               |
| length | [**LengthType**](eventmanifestschema-lengthtype-simpletype.md) | Not available.<br/> **Windows Server 2008 and Windows Vista:** The length of this structure, in bytes. Not available starting with Windows 7.<br/>                                                                                                                            |
| name   | string                                                          | The name to the structure. You can use the name to reference the data item in your XML fragment if you specify a [**UserData**](eventmanifestschema-userdata-templateitemtype-element.md) section in your template.<br/> **Windows Vista:** This attribute is optional.<br/> |



## Remarks

Providers write the structure as a blob and not as individual members of the structure. If the C structure that you are writing contains pointers (for example, a pointer of type LPWSTR), the event data will contain the pointer value, not the dereferenced data.

You should not use structures but instead should define data items for each member and write them separately. If you decide to use structure, the structure should contain only integral types and you must ensure that the members of the structure align to an 8-byte boundary. If you do not, you will likely receive alignment errors when you try to access the data. Consider using the \#pragma pack() directive to force alignment on an 8-byte boundary.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





