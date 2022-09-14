---
title: registrationInfoType Complex Type
description: Defines the child elements and sequencing information for the RegistrationInfo element.
ms.assetid: 855eb0a4-6037-4868-ae09-6c9f01d91545
keywords:
- registrationInfoType complex type Task Scheduler
topic_type:
- apiref
api_name:
- registrationInfoType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# registrationInfoType Complex Type

Defines the child elements and sequencing information for the [**RegistrationInfo**](taskschedulerschema-registrationinfo-tasktype-element.md) element.

``` syntax
<xs:complexType name="registrationInfoType">
    <xs:all>
        <xs:element name="URI"
            type="anyURI"
            minOccurs="0"
         />
        <xs:element name="SecurityDescriptor"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Source"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Date"
            type="dateTime"
            minOccurs="0"
         />
        <xs:element name="Author"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Version"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Description"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Documentation"
            type="string"
            minOccurs="0"
         />
    </xs:all>
</xs:complexType>
```

## Child elements



| Element                                                                                           | Type     | Description                                                                                                        |
|---------------------------------------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------|
| [**Author**](taskschedulerschema-author-registrationinfotype-element.md)                         | string   | Specifies the author of the task.<br/>                                                                       |
| [**Date**](taskschedulerschema-date-registrationinfotype-element.md)                             | dateTime | Specifies the date and time when the task is registered.<br/>                                                |
| [**Description**](taskschedulerschema-description-registrationinfotype-element.md)               | string   | Specifies the description of the task.<br/>                                                                  |
| [**Documentation**](taskschedulerschema-documentation-registrationinfotype-element.md)           | string   | Specifies any additional documentation for the task.<br/>                                                    |
| [**SecurityDescriptor**](taskschedulerschema-securitydescriptor-registrationinfotype-element.md) | string   | Specifies the security descriptor of the task.<br/>                                                          |
| [**Source**](taskschedulerschema-source-registrationinfotype-element.md)                         | string   | Specifies where the task originated from. For example, from a component, service, application, or user.<br/> |
| [**URI**](taskschedulerschema-uri-registrationinfotype-element.md)                               | anyURI   | Specifies the URI of the task.<br/>                                                                          |
| [**Version**](taskschedulerschema-version-registrationinfotype-element.md)                       | string   | Specifies the version number of the task.<br/>                                                               |



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

 

 





