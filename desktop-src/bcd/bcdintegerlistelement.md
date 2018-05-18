---
title: BcdIntegerListElement class
description: Represents an integer list element.
ms.assetid: '9fbd28a8-6c10-40ee-86a7-5ac9b2310bd4'
keywords: ["BcdIntegerListElement class Boot Config", "BcdIntegerListElement class Boot Config , described"]
topic_type:
- apiref
api_name:
- BcdIntegerListElement
- BcdIntegerListElement.Integers
api_location:
- Root\WMI
api_type:
- Schema
---

# BcdIntegerListElement class

Represents an integer list element.

## Syntax

``` syntax
class BcdIntegerListElement : BcdElement
{
  string Integers[];
};
```

## Members

The **BcdIntegerListElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdIntegerListElement** class has these properties.

<dl> <dt>

**Integers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The array of 64-bit integers. The values are passed as strings because Automation does not natively support 64-bit integers.

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

[**SetObjectListElement**](setobjectlistelement-bcdobject.md)
</dt> </dl>

 

 





