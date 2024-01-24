---
title: attachmentsType Complex Type
description: Defines the elements used to specify an attachment sent with an email message.
ms.assetid: b13d9346-a28d-4362-bcfc-dc11869fb8eb
keywords:
- attachmentsType complex type Task Scheduler
topic_type:
- apiref
api_name:
- attachmentsType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# attachmentsType Complex Type

Defines the elements used to specify an attachment sent with an email message.

``` syntax
<xs:complexType name="attachmentsType">
    <xs:sequence>
        <xs:element name="File"
            type="nonEmptyString"
            minOccurs="0"
            maxOccurs="8"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                          | Type                                                                    | Description                                                                                |
|------------------------------------------------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**File**](taskschedulerschema-file-attachmentstype-element.md) | [**nonEmptyString**](taskschedulerschema-nonemptystring-simpletype.md) | Specifies the path to a file that is sent as an attachment in an email message.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





