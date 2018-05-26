---
title: BcdBooleanElement class
description: Represents a boolean element.
ms.assetid: af186918-d3ce-4fde-b1e0-b907e5cf08ce
keywords:
- BcdBooleanElement class Boot Config
- BcdBooleanElement class Boot Config , described
topic_type:
- apiref
api_name:
- BcdBooleanElement
- BcdBooleanElement.Boolean
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

# BcdBooleanElement class

Represents a boolean element.

## Syntax

``` syntax
class BcdBooleanElement : BcdElement
{
  boolean Boolean;
};
```

## Members

The **BcdBooleanElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdBooleanElement** class has these properties.

<dl> <dt>

**Boolean**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The boolean value of the element.

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

[**SetBooleanElement**](setbooleanelement-bcdobject.md)
</dt> </dl>

 

 





