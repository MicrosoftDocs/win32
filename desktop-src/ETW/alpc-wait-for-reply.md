---
description: This class is the event type class for ALPC wait for reply events. The following syntax is simplified from MOF code.
ms.assetid: 9aaa2c93-41cc-4025-80f9-b7740a37c4d8
title: ALPC_Wait_For_Reply class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ALPC_Wait_For_Reply
- ALPC_Wait_For_Reply.MessageID
api_type: 
- NA
api_location: 
---

# ALPC\_Wait\_For\_Reply class

This class is the event type class for ALPC wait for reply events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(35), EventTypeName("ALPC-Wait-For-Reply")]
class ALPC_Wait_For_Reply : ALPC
{
  uint32 MessageID;
};
```

## Members

The **ALPC\_Wait\_For\_Reply** class has these types of members:

-   [Properties](#properties)

### Properties

The **ALPC\_Wait\_For\_Reply** class has these properties.

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



 

 




