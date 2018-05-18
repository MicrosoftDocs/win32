---
title: BcdIntegerElement class
description: Represents an integer element.
ms.assetid: 'aa81a706-9d9d-4b8b-ab3f-7bdf256601d1'
keywords: ["BcdIntegerElement class Boot Config", "BcdIntegerElement class Boot Config , described"]
topic_type:
- apiref
api_name:
- BcdIntegerElement
- BcdIntegerElement.Integer
api_location:
- Root\WMI
api_type:
- Schema
---

# BcdIntegerElement class

Represents an integer element.

## Syntax

``` syntax
class BcdIntegerElement : BcdElement
{
  uint64 Integer;
};
```

## Members

The **BcdIntegerElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdIntegerElement** class has these properties.

<dl> <dt>

**Integer**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The integer value of the element. The value is passed as a string because Automation does not natively support 64-bit integers.

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

[**SetIntegerElement**](setintegerelement-bcdobject.md)
</dt> </dl>

 

 





