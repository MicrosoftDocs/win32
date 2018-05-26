---
title: Server (sendEmailType) Element
description: Contains the email server used to send the email message.
ms.assetid: 4c6084d1-70c5-4d8b-8fcb-ab4cd8aab441
keywords:
- Server element Task Scheduler
topic_type:
- apiref
api_name:
- Server
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Server (sendEmailType) Element

Contains the email server used to send the email message.

``` syntax
<xs:element name="Server"
    type="nonEmptyString"
 />
```

The **Server** element is defined by the [**sendEmailType**](taskschedulerschema-sendemailtype-complextype.md) complex type.

## Parent element



| Element                                                                              | Derived from                                                           | Description                                                  |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------|
| [**SendEmail (actionGroup)**](taskschedulerschema-sendemail-actiongroup-element.md) | [**sendEMailType**](taskschedulerschema-sendemailtype-complextype.md) | Represents an action that sends an email message.<br/> |



## Remarks

For C++ development, see [**Server Property of IEmailAction**](/windows/win32/taskschd/nf-taskschd-iemailaction-get_server?branch=master).

For script development, see [**EmailAction.Server**](emailaction-server.md).

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





