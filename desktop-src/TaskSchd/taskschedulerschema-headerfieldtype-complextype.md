---
title: headerFieldType Complex Type
description: Defines the elements that are used to create a header field in an email message.
ms.assetid: 66036875-1116-46eb-b2f5-8c8ad8373ab1
keywords:
- headerFieldType complex type Task Scheduler
topic_type:
- apiref
api_name:
- headerFieldType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# headerFieldType Complex Type

Defines the elements that are used to create a header field in an email message.

``` syntax
<xs:complexType name="headerFieldType">
    <xs:all>
        <xs:element name="Name"
            type="nonEmptyString"
         />
        <xs:element name="Value"
            type="string"
         />
    </xs:all>
</xs:complexType>
```

## Child elements



| Element                                                            | Type                                                                    | Description                                                            |
|--------------------------------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**Name**](taskschedulerschema-name-headerfieldtype-element.md)   | [**nonEmptyString**](taskschedulerschema-nonemptystring-simpletype.md) | Specifies the name of the header field in an email message.<br/> |
| [**Value**](taskschedulerschema-value-headerfieldtype-element.md) | **string**                                                              | Specifies the value of a header field in an email message.<br/>  |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





