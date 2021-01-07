---
description: This class is the event type class for ALPC send message events. The following syntax is simplified from MOF code.
ms.assetid: 7f12259b-f737-4bef-9dea-2ffe3517e0da
title: ALPC_Send_Message class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ALPC_Send_Message
- ALPC_Send_Message.MessageID
api_type: 
- NA
api_location: 
---

# ALPC\_Send\_Message class

This class is the event type class for ALPC send message events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(33), EventTypeName("ALPC-Send-Message")]
class ALPC_Send_Message : ALPC
{
  uint32 MessageID;
};
```

## Members

The **ALPC\_Send\_Message** class has these types of members:

-   [Properties](#properties)

### Properties

The **ALPC\_Send\_Message** class has these properties.

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



 

 




