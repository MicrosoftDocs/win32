---
title: GetSystemPartition method of the BcdStore class
description: Returns the device path to the Windows system partition.
ms.assetid: 1d55c2ac-2cb7-4202-82f8-8f5612ab49b9
keywords:
- GetSystemPartition method Boot Config
- GetSystemPartition method Boot Config , BcdStore class
- BcdStore class Boot Config , GetSystemPartition method
topic_type:
- apiref
api_name:
- BcdStore.GetSystemPartition
api_location:
- Root\WMI
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetSystemPartition method of the BcdStore class

Returns the device path to the Windows system partition.

## Syntax


```mof
boolean GetSystemPartition(
  [out] string Partition
);
```



## Parameters

<dl> <dt>

*Partition* \[out\]
</dt> <dd>

The device path to the Windows system partition.

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

 

 





