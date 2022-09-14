---
title: To (sendEmailType) Element
description: Contains the email addresses to which the email will be sent.
ms.assetid: bf3aa878-967b-4ebd-9397-a2a499686a9f
keywords:
- To element Task Scheduler
topic_type:
- apiref
api_name:
- To
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# To (sendEmailType) Element

Contains the email addresses to which the email will be sent.

``` syntax
<xs:element name="To"
    type="string"
 />
```

The **To** element is defined by the [**sendEmailType**](taskschedulerschema-sendemailtype-complextype.md) complex type.

## Parent element



| Element                                                                              | Derived from                                                           | Description                                                  |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------|
| [**SendEmail (actionGroup)**](taskschedulerschema-sendemail-actiongroup-element.md) | [**sendEMailType**](taskschedulerschema-sendemailtype-complextype.md) | Represents an action that sends an email message.<br/> |



## Remarks

For C++ development, see [**To Property of IEmailAction**](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_to).

For script development, see [**EmailAction.To**](emailaction-to.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





