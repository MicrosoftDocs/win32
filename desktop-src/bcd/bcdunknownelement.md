---
title: BcdUnknownElement class
description: Represents an unknown element.
ms.assetid: b6fd34ec-f65e-448a-93a0-ba36431ff827
keywords:
- BcdUnknownElement class Boot Config
- BcdUnknownElement class Boot Config , described
topic_type:
- apiref
api_name:
- BcdUnknownElement
- BcdUnknownElement.ActualType
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

# BcdUnknownElement class

Represents an unknown element.

## Syntax

``` syntax
class BcdUnknownElement : BcdElement
{
  uint64 ActualType;
};
```

## Members

The **BcdUnknownElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdUnknownElement** class has these properties.

<dl> <dt>

**ActualType**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The actual value of the element inside the BCD store. The value is passed as a string because Automation does not natively support 64-bit integers.

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

[**BcdElement**](bcdelement.md)
</dt> <dt>

[**SetIntegerElement**](setintegerelement-bcdobject.md)
</dt> </dl>

 

 





