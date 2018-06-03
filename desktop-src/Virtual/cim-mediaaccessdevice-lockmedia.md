---
title: LockMedia method of the CIM\_MediaAccessDevice class
description: Represents a device that can use media to store and retrieve data.
ms.assetid: 13a113b4-e3df-47d2-88bd-99a40cf1efa5
keywords:
- LockMedia method Hyper-V
- LockMedia method Hyper-V , CIM_MediaAccessDevice class
- CIM_MediaAccessDevice class Hyper-V , LockMedia method
topic_type:
- apiref
api_name:
- CIM_MediaAccessDevice.LockMedia
api_location:
- Root\virtualization
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LockMedia method of the CIM\_MediaAccessDevice class

Represents a device that can use media to store and retrieve data.

## Syntax


```mof
uint32 LockMedia(
  [in] boolean Lock
);
```



## Parameters

<dl> <dt>

*Lock* \[in\]
</dt> <dd>

**true** to lock the media, or **false** to unlock the media.

</dd> </dl>

## Return value

This method returns "0" if successful, "1" if not supported, and any other value if an error occurred.

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_MediaAccessDevice**](cim-mediaaccessdevice.md)
</dt> </dl>

 

 





