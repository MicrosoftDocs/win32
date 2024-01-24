---
title: HeaderField (headerFieldsType) Element
description: Contains a field for a header in an email message.
ms.assetid: ec6fc593-8798-4dd0-b589-48657b7cdeb1
keywords:
- HeaderField element Task Scheduler
topic_type:
- apiref
api_name:
- HeaderField
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# HeaderField (headerFieldsType) Element

Contains a field for a header in an email message.

``` syntax
<xs:element name="HeaderField"
    type="headerFieldType"
 />
```

The **HeaderField** element is defined by the [**headerFieldsType**](taskschedulerschema-headerfieldstype-complextype.md) complex type.

## Parent element



| Element                                                                        | Derived from                                                                 | Description                                                                                      |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**HeaderFields**](taskschedulerschema-headerfields-sendemailtype-element.md) | [**headerFieldsType**](taskschedulerschema-headerfieldstype-complextype.md) | Specifies the header fields and their values used in the header of the email message.<br/> |



## Child elements



| Element                                                            | Type                                                                    | Description                                                            |
|--------------------------------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**Name**](taskschedulerschema-name-headerfieldtype-element.md)   | [**nonEmptyString**](taskschedulerschema-nonemptystring-simpletype.md) | Specifies the name of the header field in an email message.<br/> |
| [**Value**](taskschedulerschema-value-headerfieldtype-element.md) | **string**                                                              | Specifies the value of a header field in an email message.<br/>  |



## Remarks

For C++ development, see [**HeaderFields Property of IEmailAction**](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_headerfields).

For script development, see [**EmailAction.HeaderFields**](emailaction-headerfields.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





