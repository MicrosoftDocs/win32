---
title: BcdObjectElement class
description: Represents an object element.
ms.assetid: '94249c20-f500-4b20-821d-e4d083ffc58e'
keywords: ["BcdObjectElement class Boot Config", "BcdObjectElement class Boot Config , described"]
topic_type:
- apiref
api_name:
- BcdObjectElement
- BcdObjectElement.Id
api_location:
- Root\WMI
api_type:
- Schema
---

# BcdObjectElement class

Represents an object element. The Id property specifies a [**BcdObject**](bcdobject.md) in the same store.

## Syntax

``` syntax
class BcdObjectElement : BcdElement
{
  string Id;
};
```

## Members

The **BcdObjectElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdObjectElement** class has these properties.

<dl> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **GUID** of the object.

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

[**SetObjectElement**](setobjectelement-bcdobject.md)
</dt> </dl>

 

 





