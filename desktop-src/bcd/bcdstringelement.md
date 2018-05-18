---
title: BcdStringElement class
description: Represents a string element.
ms.assetid: 'c400a2ea-9508-4583-9ff0-d305751c7494'
keywords: ["BcdStringElement class Boot Config", "BcdStringElement class Boot Config , described"]
topic_type:
- apiref
api_name:
- BcdStringElement
- BcdStringElement.String
api_location:
- Root\WMI
api_type:
- Schema
---

# BcdStringElement class

Represents a string element.

## Syntax

``` syntax
class BcdStringElement : BcdElement
{
  string String;
};
```

## Members

The **BcdStringElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdStringElement** class has these properties.

<dl> <dt>

**String**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The string value.

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

[**SetStringElement**](setstringelement-bcdobject.md)
</dt> </dl>

 

 





