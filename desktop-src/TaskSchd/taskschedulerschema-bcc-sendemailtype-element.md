---
title: Bcc (sendEmailType) Element
description: Contains the email addresses used on the Bcc line of an email message.
ms.assetid: 'c80407d0-3b3f-4efe-91de-7a3a7abc996f'
keywords: ["Bcc element Task Scheduler"]
topic_type:
- apiref
api_name:
- Bcc
api_type:
- Schema
---

# Bcc (sendEmailType) Element

Contains the email addresses used on the Bcc line of an email message.

``` syntax
<xs:element name="Bcc"
    type="string"
 />
```

The **Bcc** element is defined by the [**sendEmailType**](taskschedulerschema-sendemailtype-complextype.md) complex type.

## Parent element



| Element                                                                              | Derived from                                                           | Description                                                  |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------|
| [**SendEmail (actionGroup)**](taskschedulerschema-sendemail-actiongroup-element.md) | [**sendEMailType**](taskschedulerschema-sendemailtype-complextype.md) | Represents an action that sends an email message.<br/> |



## Remarks

For C++ development, see [**Bcc Property of IEmailAction**](iemailaction-bcc.md).

For script development, see [**EmailAction.Bcc**](emailaction-bcc.md).

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





