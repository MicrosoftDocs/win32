---
title: From (sendEmailType) Element
description: Contains the email address of the email sender.
ms.assetid: b80733de-e050-4026-a2fe-f63833ec2660
keywords:
- From element Task Scheduler
topic_type:
- apiref
api_name:
- From
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# From (sendEmailType) Element

Contains the email address of the email sender.

``` syntax
<xs:element name="From"
    type="string"
 />
```

The **From** element is defined by the [**sendEmailType**](taskschedulerschema-sendemailtype-complextype.md) complex type.

## Parent element



| Element                                                                              | Derived from                                                           | Description                                                  |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------|
| [**SendEmail (actionGroup)**](taskschedulerschema-sendemail-actiongroup-element.md) | [**sendEMailType**](taskschedulerschema-sendemailtype-complextype.md) | Represents an action that sends an email message.<br/> |



## Remarks

For C++ development, see [**From Property of IEmailAction**](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_from).

For script development, see [**EmailAction.From**](emailaction-from.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





