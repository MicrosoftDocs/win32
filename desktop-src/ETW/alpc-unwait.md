---
Description: This class is the event type class for ALPC end wait events. The following syntax is simplified from MOF code.
ms.assetid: 89a357dd-c217-4b55-994a-4252fa3cae1c
title: ALPC\_Unwait class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ALPC\_Unwait class

This class is the event type class for ALPC end wait events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(37), EventTypeName("ALPC-Unwait")]
class ALPC_Unwait : ALPC
{
  uint32 Status;
};
```

## Members

The **ALPC\_Unwait** class has these types of members:

-   [Properties](#properties)

### Properties

The **ALPC\_Unwait** class has these properties.

<dl> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Status from wait operation.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




