---
title: BcdDeviceFileData class
description: Represents a file device element.
ms.assetid: c406ffec-0054-405e-8885-da314b8129f3
keywords:
- BcdDeviceFileData class Boot Config
- BcdDeviceFileData class Boot Config , described
topic_type:
- apiref
api_name:
- BcdDeviceFileData
- BcdDeviceFileData.Parent
- BcdDeviceFileData.Path
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

# BcdDeviceFileData class

Represents a file device element.

## Syntax

``` syntax
class BcdDeviceFileData : BcdDeviceData
{
  BcdDeviceData Parent;
  string        Path;
};
```

## Members

The **BcdDeviceFileData** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdDeviceFileData** class has these properties.

<dl> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**BcdDeviceData**](bcddevicedata.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The parent device.

</dd> <dt>

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

[**SetFileDeviceElement**](setfiledeviceelement-bcdobject.md)
</dt> </dl>

 

 





