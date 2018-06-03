---
title: GetSystemDisk method of the BcdStore class
description: Returns the device path to the Windows system disk.
ms.assetid: c54c68bf-2fda-4f60-8e51-818a3ddb5d73
keywords:
- GetSystemDisk method Boot Config
- GetSystemDisk method Boot Config , BcdStore class
- BcdStore class Boot Config , GetSystemDisk method
topic_type:
- apiref
api_name:
- BcdStore.GetSystemDisk
api_location:
- Root\WMI
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSystemDisk method of the BcdStore class

Returns the device path to the Windows system disk.

## Syntax


```mof
boolean GetSystemDisk(
  [out] string Disk
);
```



## Parameters

<dl> <dt>

*Disk* \[out\]
</dt> <dd>

The device path to the Windows system disk.

</dd> </dl>

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdStore**](bcdstore.md)
</dt> </dl>

 

 





