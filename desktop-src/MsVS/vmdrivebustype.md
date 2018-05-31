---
title: VMDriveBusType enumeration
description: The VMDriveBusType enumeration specifies the type of bus.
ms.assetid: 5c2a07f3-a9f4-43d1-8c1d-e0a3bc1d8259
keywords:
- VMDriveBusType enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMDriveBusType
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# VMDriveBusType enumeration

The **VMDriveBusType** enumeration specifies the type of bus.

## Syntax


```C++
typedef enum  { 
  vmDriveBusType_Invalid  = -1,
  vmDriveBusType_IDE      = 0,
  vmDriveBusType_SCSI     = 1
} VMDriveBusType;
```



## Constants

<dl> <dt>

<span id="vmDriveBusType_Invalid"></span><span id="vmdrivebustype_invalid"></span><span id="VMDRIVEBUSTYPE_INVALID"></span>**vmDriveBusType\_Invalid**
</dt> <dd>

No bus type.

</dd> <dt>

<span id="vmDriveBusType_IDE"></span><span id="vmdrivebustype_ide"></span><span id="VMDRIVEBUSTYPE_IDE"></span>**vmDriveBusType\_IDE**
</dt> <dd>

IDE bus type.

</dd> <dt>

<span id="vmDriveBusType_SCSI"></span><span id="vmdrivebustype_scsi"></span><span id="VMDRIVEBUSTYPE_SCSI"></span>**vmDriveBusType\_SCSI**
</dt> <dd>

SCSI bus type.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





