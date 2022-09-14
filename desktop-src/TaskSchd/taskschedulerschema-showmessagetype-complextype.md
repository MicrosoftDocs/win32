---
title: showMessageType Complex Type
description: Defines the elements that represent an action that shows a message box.
ms.assetid: eb841d9f-0be2-433b-9002-5e41c6ee78f9
keywords:
- showMessageType complex type Task Scheduler
topic_type:
- apiref
api_name:
- showMessageType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# showMessageType Complex Type

Defines the elements that represent an action that shows a message box.

``` syntax
<xs:complexType name="showMessageType">
    <xs:complexContent>
        <xs:extension
            base="actionBaseType"
        >
            <xs:all>
                <xs:element name="Title"
                    type="nonEmptyString"
                 />
                <xs:element name="Body"
                    type="nonEmptyString"
                 />
            </xs:all>
        </xs:extension>
    </xs:complexContent>
</xs:complexType>
```

## Child elements



| Element                                                            | Type           | Description                                                               |
|--------------------------------------------------------------------|----------------|---------------------------------------------------------------------------|
| [**Body**](taskschedulerschema-body-showmessagetype-element.md)   | nonEmptyString | Specifies the text to display in the body of the message box. <br/> |
| [**Title**](taskschedulerschema-title-showmessagetype-element.md) | nonEmptyString | Specifies the title of the message box. <br/>                       |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





