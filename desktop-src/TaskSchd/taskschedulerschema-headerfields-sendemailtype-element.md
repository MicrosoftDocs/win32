---
title: HeaderFields (sendEmailType) Element
description: Specifies the header fields and their values used in the header of the email message.
ms.assetid: '6261f32e-3012-4ce7-b407-699374596333'
keywords: ["HeaderFields element Task Scheduler"]
topic_type:
- apiref
api_name:
- HeaderFields
api_type:
- Schema
---

# HeaderFields (sendEmailType) Element

Specifies the header fields and their values used in the header of the email message.

``` syntax
<xs:element name="HeaderFields"
    type="headerFieldsType"
 />
```

The **HeaderFields** element is defined by the [**sendEmailType**](taskschedulerschema-sendemailtype-complextype.md) complex type.

## Parent element



| Element                                                                              | Derived from                                                           | Description                                                  |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------|
| [**SendEmail (actionGroup)**](taskschedulerschema-sendemail-actiongroup-element.md) | [**sendEMailType**](taskschedulerschema-sendemailtype-complextype.md) | Represents an action that sends an email message.<br/> |



## Child elements



| Element                                                                         | Type                                                                       | Description                                                    |
|---------------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------|
| [**HeaderField**](taskschedulerschema-headerfield-headerfieldstype-element.md) | [**headerFieldType**](taskschedulerschema-headerfieldtype-complextype.md) | Contains a field for a header in an email message. <br/> |



## Remarks

For C++ development, see [**HeaderFields Property of IEmailAction**](iemailaction-headerfields.md).

For script development, see [**EmailAction.HeaderFields**](emailaction-headerfields.md).

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





