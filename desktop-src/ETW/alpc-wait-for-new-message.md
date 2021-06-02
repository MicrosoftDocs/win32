---
description: This class is the event type class for ALPC wait for new message events. The following syntax is simplified from MOF code.
ms.assetid: 7f7fa4b8-ed12-49a0-a84e-37f66af4f5f1
title: ALPC_Wait_For_New_Message class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ALPC_Wait_For_New_Message
- ALPC_Wait_For_New_Message.IsServerPort
- ALPC_Wait_For_New_Message.PortName
api_type: 
- NA
api_location: 
---

# ALPC\_Wait\_For\_New\_Message class

This class is the event type class for ALPC wait for new message events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(36), EventTypeName("ALPC-Wait-For-New-Message")]
class ALPC_Wait_For_New_Message : ALPC
{
  uint32 IsServerPort;
  string PortName;
};
```

## Members

The **ALPC\_Wait\_For\_New\_Message** class has these types of members:

-   [Properties](#properties)

### Properties

The **ALPC\_Wait\_For\_New\_Message** class has these properties.

<dl> <dt>

**IsServerPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the port is a server port.

</dd> <dt>

**PortName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

String that contains the name of the port on which ALPC is waiting.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




