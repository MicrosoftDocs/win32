---
description: This class is the event type class for ALPC receive message events. The following syntax is simplified from MOF code.
ms.assetid: 6aa98240-e559-47b6-ae55-5a6379e08077
title: ALPC_Receive_Message class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ALPC_Receive_Message
- ALPC_Receive_Message.MessageID
api_type: 
- NA
api_location: 
---

# ALPC\_Receive\_Message class

This class is the event type class for ALPC receive message events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(34), EventTypeName("ALPC-Receive-Message")]
class ALPC_Receive_Message : ALPC
{
  uint32 MessageID;
};
```

## Members

The **ALPC\_Receive\_Message** class has these types of members:

-   [Properties](#properties)

### Properties

The **ALPC\_Receive\_Message** class has these properties.

<dl> <dt>

**MessageID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Message identifier.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




