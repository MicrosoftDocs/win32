---
title: Cc (sendEmailType) Element
description: Contains the email addresses used on the Cc line of an email message.
ms.assetid: cb8bc5b3-c352-43e3-bf28-d2090a519c7f
keywords:
- Cc element Task Scheduler
topic_type:
- apiref
api_name:
- Cc
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Cc (sendEmailType) Element

Contains the email addresses used on the Cc line of an email message.

``` syntax
<xs:element name="Cc"
    type="string"
 />
```

The **Cc** element is defined by the [**sendEmailType**](taskschedulerschema-sendemailtype-complextype.md) complex type.

## Parent element



| Element                                                                              | Derived from                                                           | Description                                                  |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------|
| [**SendEmail (actionGroup)**](taskschedulerschema-sendemail-actiongroup-element.md) | [**sendEMailType**](taskschedulerschema-sendemailtype-complextype.md) | Represents an action that sends an email message.<br/> |



## Remarks

For C++ development, see [**Cc Property of IEmailAction**](/windows/win32/taskschd/nf-taskschd-iemailaction-get_cc?branch=master).

For script development, see [**EmailAction.Cc**](emailaction-cc.md).

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





