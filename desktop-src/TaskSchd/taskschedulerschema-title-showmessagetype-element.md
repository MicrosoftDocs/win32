---
title: Title (showMessageType) Element
description: Contains the title of the message box.
ms.assetid: 089d2043-41ed-4050-b794-af24ab7ac8b9
keywords:
- Title element Task Scheduler
topic_type:
- apiref
api_name:
- Title
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Title (showMessageType) Element

Contains the title of the message box.

``` syntax
<xs:element name="Title"
    type="nonEmptyString"
 />
```

The **Title** element is defined by the [**showMessageType**](taskschedulerschema-showmessagetype-complextype.md) complex type.

## Parent element



| Element                                                                                  | Derived from                                                               | Description                                               |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|-----------------------------------------------------------|
| [**ShowMessage (actionGroup)**](taskschedulerschema-showmessage-actiongroup-element.md) | [**showMessageType**](taskschedulerschema-showmessagetype-complextype.md) | Represents an action that shows a message box.<br/> |



## Remarks

For C++ development, see [**Title Property of IShowMessageAction**](/windows/desktop/api/taskschd/nf-taskschd-ishowmessageaction-get_title).

For script development, see [**ShowMessageAction.Title**](showmessageaction-title.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





