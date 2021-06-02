---
title: ShowMessage (actionGroup) Element
description: Represents an action that shows a message box.
ms.assetid: 33c6e437-b993-4b5e-b75a-fb3fda9b24df
keywords:
- ShowMessage element Task Scheduler
topic_type:
- apiref
api_name:
- ShowMessage
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ShowMessage (actionGroup) Element

Represents an action that shows a message box.

``` syntax
<xs:element name="ShowMessage"
    type="showMessageType"
 />
```

The **ShowMessage** element is defined by the [**actionGroup**](taskschedulerschema-actiongroup-group.md) .

## Parent element



| Element                                                                    | Derived from                                                       | Description                                            |
|----------------------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------|
| [**Actions (taskType)**](taskschedulerschema-actions-tasktype-element.md) | [**actionsType**](taskschedulerschema-actionstype-complextype.md) | Contains the actions performed by the task.<br/> |



## Child elements



| Element                                                            | Type           | Description                                                               |
|--------------------------------------------------------------------|----------------|---------------------------------------------------------------------------|
| [**Body**](taskschedulerschema-body-showmessagetype-element.md)   | nonEmptyString | Specifies the text to display in the body of the message box. <br/> |
| [**Title**](taskschedulerschema-title-showmessagetype-element.md) | nonEmptyString | Specifies the title of the message box. <br/>                       |



## Remarks

For scripting development, a message box action is specified using the [**ShowMessageAction**](showmessageaction.md) object.

For C++ development, a message box action is specified using the [**IShowMessageAction**](/windows/desktop/api/taskschd/nn-taskschd-ishowmessageaction) interface.

**Windows 8 and Windows Server 2012:** This element has been removed. You can use IExecAction with the Windows scripting [**MsgBox function**](/previous-versions/sfw6660x(v=vs.80)) to show a message in the user session.

## Examples

For a complete example of the XML for a task that uses a message box action, see [Message Box Example (XML)](/previous-versions//aa381917(v=vs.85)).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows 7<br/>                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                    |



 

