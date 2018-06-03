---
title: BcdDeviceUnknownData class
description: Represents unknown device data and exposes the data as a BLOB.
ms.assetid: b890f39d-a39e-47c1-833f-99d55c15dc85
keywords:
- BcdDeviceUnknownData class Boot Config
- BcdDeviceUnknownData class Boot Config , described
topic_type:
- apiref
api_name:
- BcdDeviceUnknownData
- BcdDeviceUnknownData.Data
api_location:
- Root\WMI
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BcdDeviceUnknownData class

Represents unknown device data and exposes the data as a BLOB.

## Syntax

``` syntax
class BcdDeviceUnknownData : BcdDeviceData
{
  uint8 Data[];
};
```

## Members

The **BcdDeviceUnknownData** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdDeviceUnknownData** class has these properties.

<dl> <dt>

**Data**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The binary data of the unknown device element.

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
</dt> </dl>

 

 





