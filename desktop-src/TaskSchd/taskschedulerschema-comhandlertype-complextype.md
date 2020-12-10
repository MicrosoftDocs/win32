---
title: comHandlerType Complex Type
description: Defines the child elements and sequencing information for the ComHandler element.
ms.assetid: 688e79f3-8b7e-4892-8119-b0a457ce9c7f
keywords:
- comHandlerType complex type Task Scheduler
topic_type:
- apiref
api_name:
- comHandlerType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# comHandlerType Complex Type

Defines the child elements and sequencing information for the [**ComHandler**](taskschedulerschema-comhandler-actiongroup-element.md) element.

``` syntax
<xs:complexType name="comHandlerType">
    <xs:complexContent>
        <xs:extension
            base="actionBaseType"
        >
            <xs:all>
                <xs:element name="ClassId"
                    type="guidType"
                 />
                <xs:element name="Data"
                    type="dataType"
                    minOccurs="0"
                 />
            </xs:all>
        </xs:extension>
    </xs:complexContent>
</xs:complexType>
```

## Child elements



| Element                                                               | Type                                                         | Description                                                        |
|-----------------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------------|
| [**ClassId**](taskschedulerschema-classid-comhandlertype-element.md) | [**guidType**](taskschedulerschema-guidtype-simpletype.md)  | Specifies the identifier of the handler class.<br/>          |
| [**Data**](taskschedulerschema-data-comhandlertype-element.md)       | [**dataType**](taskschedulerschema-datatype-complextype.md) | Specifies additional data associated with the handler. <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Task Scheduler Schema Complex Types](task-scheduler-schema-complex-types.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 





