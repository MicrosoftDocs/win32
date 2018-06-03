---
title: BcdDeviceLocateElementData class
description: Represents a locate device element. This class is not used.
ms.assetid: 980ee450-020a-473a-a75e-65f75d476e27
keywords:
- BcdDeviceLocateElementData class Boot Config
- BcdDeviceLocateElementData class Boot Config , described
topic_type:
- apiref
api_name:
- BcdDeviceLocateElementData
- BcdDeviceLocateElementData.Element
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

# BcdDeviceLocateElementData class

Represents a locate device element. This class is not used.

## Syntax

``` syntax
class BcdDeviceLocateElementData : BcdDeviceLocateData
{
  uint32 Element;
};
```

## Members

The **BcdDeviceLocateElementData** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdDeviceLocateElementData** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The device element for the virtual hard disk.

</dd> </dl>

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdDeviceLocateStringData**](bcddevicelocatestringdata.md)
</dt> </dl>

 

 





