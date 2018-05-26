---
title: BcdDevicePartitionData class
description: Represents a partition device element.
ms.assetid: 90a9fdc0-88ed-442d-a524-a14357d71b26
keywords:
- BcdDevicePartitionData class Boot Config
- BcdDevicePartitionData class Boot Config , described
topic_type:
- apiref
api_name:
- BcdDevicePartitionData
- BcdDevicePartitionData.Path
api_location:
- Root\WMI
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BcdDevicePartitionData class

Represents a partition device element.

## Syntax

``` syntax
class BcdDevicePartitionData : BcdDeviceData
{
  string Path;
};
```

## Members

The **BcdDevicePartitionData** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdDevicePartitionData** class has these properties.

<dl> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The device path.

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

[**BcdDeviceData**](bcddevicedata.md)
</dt> <dt>

[**SetPartitionDeviceElement**](setpartitiondeviceelement-bcdobject.md)
</dt> </dl>

 

 





