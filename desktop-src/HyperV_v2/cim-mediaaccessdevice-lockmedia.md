---
Description: Locks and unlocks the media in a removeable access device.
ms.assetid: 357ee552-82d0-4201-bcc2-0acf208e16a0
title: LockMedia method of the CIM_MediaAccessDevice class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_MediaAccessDevice.LockMedia
api_type: 
- COM
api_location: 
- vmms.exe
---

# LockMedia method of the CIM\_MediaAccessDevice class

Locks and unlocks the media in a removeable access device.

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

If **TRUE**, locks the media. If **FALSE**, releases the media.

</dd> </dl>

## Return value

Returns a 0 on success; otherwise, returns an error.

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_MediaAccessDevice**](cim-mediaaccessdevice.md)
</dt> </dl>

 

 




