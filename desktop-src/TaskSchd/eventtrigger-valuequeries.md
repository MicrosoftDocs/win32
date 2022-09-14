---
title: EventTrigger.ValueQueries property
description: For scripting, gets or sets a collection of named XPath queries. Each query in the collection is applied to the last matching event XML that is returned from the subscription query specified in the Subscription property.
ms.assetid: 9ff92b66-f63c-4736-b086-df7dd8cd2b10
keywords:
- ValueQueries property Task Scheduler
- ValueQueries property Task Scheduler , EventTrigger object
- EventTrigger object Task Scheduler , ValueQueries property
topic_type:
- apiref
api_name:
- EventTrigger.ValueQueries
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EventTrigger.ValueQueries property

For scripting, gets or sets a collection of named XPath queries. Each query in the collection is applied to the last matching event XML that is returned from the subscription query specified in the [**Subscription**](eventtrigger-subscription.md) property.

## Syntax


```VB
EventTrigger.ValueQueries As String
```



## Property value

A collection of of name-value pairs. Each name-value pair in the collection defines a unique name for a property value of the event that triggers the event trigger. The property value of the event is defined as an XPath event query. For more information about XPath event queries, see [Event Selection](/previous-versions//aa385231(v=vs.85)).

## Remarks

The name of the query can be used as a variable in the following action properties:

-   [**ShowMessageAction.MessageBody**](showmessageaction-messagebody.md)
-   [**ShowMessageAction.Title**](showmessageaction-title.md)
-   [**ExecAction.Arguments**](execaction-arguments.md)
-   [**ExecAction.WorkingDirectory**](execaction-workingdirectory.md)
-   [**EmailAction.Server**](emailaction-server.md)
-   [**EmailAction.Subject**](emailaction-subject.md)
-   [**EmailAction.To**](emailaction-to.md)
-   [**EmailAction.Cc**](emailaction-cc.md)
-   [**EmailAction.Bcc**](emailaction-bcc.md)
-   [**EmailAction.ReplyTo**](emailaction-replyto.md)
-   [**EmailAction.From**](emailaction-from.md)
-   [**EmailAction.Body**](emailaction-body.md)
-   [**ComHandlerAction.Data**](comhandleraction-data.md)

The following code example strings show two name value pairs that can be used in a name-value collection. The values returned by the XPath queries can replace variables in an action's property. The values are referenced by name, with `$(user)` and `$(machine)`, in the action property. For example, if the `$(user)` and `$(machine)` variables are used in the [**ShowMessageAction.MessageBody**](showmessageaction-messagebody.md) string, then the value of the XPath queries will replace the variables in the string.

``` syntax
name: user
value: Event/UserData/SubjectUserName

name: machine
value: Event/UserData/MachineName
```

For more information about writing a query string for certain events, see [Event Selection](/previous-versions//aa385231(v=vs.85)) and [Subscribing to Events](../wes/subscribing-to-events.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> <dt>

[**EventTrigger**](eventtrigger.md)
</dt> </dl>

 

