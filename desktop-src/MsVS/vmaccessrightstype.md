---
title: VMAccessRightsType enumeration
description: The VMAccessRightsType enumeration specifies access rights for the user or group.
ms.assetid: ba23382c-3c19-4d21-b607-c1f5e14d9666
keywords:
- VMAccessRightsType enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMAccessRightsType
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VMAccessRightsType enumeration

The **VMAccessRightsType** enumeration specifies access rights for the user or group.

## Syntax


```C++
typedef enum  { 
  vmAccessRights_Allowed  = 0,
  vmAccessRights_Denied   = 1
} VMAccessRightsType;
```



## Constants

<dl> <dt>

<span id="vmAccessRights_Allowed"></span><span id="vmaccessrights_allowed"></span><span id="VMACCESSRIGHTS_ALLOWED"></span>**vmAccessRights\_Allowed**
</dt> <dd>

Allow access for the user or group.

</dd> <dt>

<span id="vmAccessRights_Denied"></span><span id="vmaccessrights_denied"></span><span id="VMACCESSRIGHTS_DENIED"></span>**vmAccessRights\_Denied**
</dt> <dd>

Deny access for the user or group.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





