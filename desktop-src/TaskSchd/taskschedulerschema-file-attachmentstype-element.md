---
title: File (attachmentsType) Element
description: Contains the path to a file sent as an attachment in an email message.
ms.assetid: a53f591b-ac59-43b4-8cc2-661e76d307cc
keywords:
- File element Task Scheduler
topic_type:
- apiref
api_name:
- File
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# File (attachmentsType) Element

Contains the path to a file sent as an attachment in an email message.

``` syntax
<xs:element name="File"
    type="nonEmptyString"
 />
```

The **File** element is defined by the [**attachmentsType**](taskschedulerschema-attachmentstype-complextype.md) complex type.

## Parent element



| Element                                                                                      | Derived from                                                               | Description                                                     |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|-----------------------------------------------------------------|
| [**Attachments (sendEmailType)**](taskschedulerschema-attachments-sendemailtype-element.md) | [**attachmentsType**](taskschedulerschema-attachmentstype-complextype.md) | Contains a list of attachments in the email message.<br/> |



## Remarks

For C++ development, see [**Attachments Property of IEmailAction**](/windows/desktop/api/taskschd/nf-taskschd-iemailaction-get_attachments).

For script development, see [**EmailAction.Attachments**](emailaction-attachments.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





