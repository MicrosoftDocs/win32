---
title: BcdObjectListElement class
description: Represents a list of objects.
ms.assetid: 2ec1df00-16a4-48d8-8fd0-ffa4ad2d9b90
keywords:
- BcdObjectListElement class Boot Config
- BcdObjectListElement class Boot Config , described
topic_type:
- apiref
api_name:
- BcdObjectListElement
- BcdObjectListElement.Ids
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

# BcdObjectListElement class

Represents a list of objects. Each element in the Ids array specifies the **GUID** of an object in the same store.

## Syntax

``` syntax
class BcdObjectListElement : BcdElement
{
  string Ids[];
};
```

## Members

The **BcdObjectListElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **BcdObjectListElement** class has these properties.

<dl> <dt>

**Ids**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The array of object identifiers.

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

[**SetObjectListElement**](setobjectlistelement-bcdobject.md)
</dt> </dl>

 

 





