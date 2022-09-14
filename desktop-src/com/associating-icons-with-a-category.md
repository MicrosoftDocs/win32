---
title: Associating Icons with a Category
description: Associating Icons with a Category
ms.assetid: 5e5c3c10-07cf-4a34-9822-97ec940b3117
ms.topic: article
ms.date: 05/31/2018
---

# Associating Icons with a Category

Building a user interface that allows the user to select component categories within a category requires the ability to display a meaningful image for a particular category. To associate an icon with a component category, create a key for the category's CATID and populate that key with a [DefaultIcon](defaulticon.md) subkey. The registry entry is as follows:

``` syntax
HKEY_CLASSES_ROOT\CLSID\{...catid...}\DefaultIcon = "c:\hello\icons.dll,1"
 
```

The filename referenced by the DefaultIcon key can be either an EXE or a DLL file (resource-only DLL).

To associate a small 16x16 "toolbox bitmap" with a component category, create a key in **HKEY\_CLASSES\_ROOT\\CLSID** for the category's CATID and populate that key with a [ToolBoxBitmap32](toolboxbitmap32.md) subkey, as shown in the following example:

``` syntax
HKEY_CLASSES_ROOT\CLSID\{...catid...}\ToolBoxBitmap32 = "c:\goodbye\mycomponent.dll,42"
 
```

The filename referenced by the [ToolBoxBitmap32](toolboxbitmap32.md) key can also be an EXE or DLL file (resource-only DLL).

## Related topics

<dl> <dt>

[Categorizing by Component Capabilities](categorizing-by-component-capabilities.md)
</dt> <dt>

[Categorizing by Container Capabilities](categorizing-by-container-capabilities.md)
</dt> <dt>

[Default Classes and Associations](default-classes-and-associations.md)
</dt> <dt>

[Defining Component Categories](defining-component-categories.md)
</dt> <dt>

[**ICatInformation**](/windows/desktop/api/ComCat/nn-comcat-icatinformation)
</dt> <dt>

[**ICatRegister**](/windows/desktop/api/ComCat/nn-comcat-icatregister)
</dt> <dt>

[The Component Categories Manager](the-component-categories-manager.md)
</dt> </dl>

 

 




