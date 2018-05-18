---
title: BcdDeviceElement class
description: The base device element class.
ms.assetid: '6878dc14-dbdc-45f9-ace7-9b7a00efd0f5'
keywords: ["BcdDeviceElement class Boot Config", "BcdDeviceElement class Boot Config , described"]
topic_type:
- apiref
api_name:
- BcdDeviceElement
- BcdDeviceElement.Device
api_location:
- Root\WMI
api_type:
- Schema
---

# BcdDeviceElement class

The base device element class.

## Syntax

``` syntax
class BcdDeviceElement : BcdElement
{
  BcdDeviceData Device;
};
```

## Members

The **BcdDeviceElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdDeviceElement** class has these properties.

<dl> <dt>

**Device**
</dt> <dd> <dl> <dt>

Data type: **BcdDeviceData**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The information about the device.

</dd> </dl>

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdElement**](bcdelement.md)
</dt> <dt>

[**SetDeviceElement**](setdeviceelement-bcdobject.md)
</dt> </dl>

 

 





