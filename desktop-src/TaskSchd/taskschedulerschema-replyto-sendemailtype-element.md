---
title: ReplyTo (sendEmailType) Element
description: Contains the email addresses that are replied to in the email message.
ms.assetid: c09b72f6-de2c-41dc-942c-d6184863e33c
keywords:
- ReplyTo element Task Scheduler
topic_type:
- apiref
api_name:
- ReplyTo
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ReplyTo (sendEmailType) Element

Contains the email addresses that are replied to in the email message.

``` syntax
<xs:element name="ReplyTo"
    type="string"
 />
```

The **ReplyTo** element is defined by the [**sendEmailType**](taskschedulerschema-sendemailtype-complextype.md) complex type.

## Parent element



| Element                                                                              | Derived from                                                           | Description                                                  |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------|
| [**SendEmail (actionGroup)**](taskschedulerschema-sendemail-actiongroup-element.md) | [**sendEMailType**](taskschedulerschema-sendemailtype-complextype.md) | Represents an action that sends an email message.<br/> |



## Remarks

For C++ development, see [**ReplyTo Property of IEmailAction**](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_replyto).

For script development, see [**EmailAction.ReplyTo**](emailaction-replyto.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





