---
title: UI_PKEY_Categories
description: Identifies the UI\_PKEY\_Categories property.
ms.assetid: 15f97307-ea3d-407a-a276-46b82f81bdbc
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_Categories

Identifies the UI\_PKEY\_Categories property.

```
propertyDescription
   name = UI_PKEY_Categories
   shellPKey = UI_PKEY_Categories
   formatID = 00000102-7363-696e-8441798acf5aebb7
   propID = 102
   typeInfo
      type = IUICollection
```

## Remarks

UI\_PKEY\_Categories is used by an application to query the categories that are used to group related items in a gallery control.

The property value is an [**IUICollection**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection) object where each item in the collection represents a category.

Each item in this [**IUICollection**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection) must implement [**IUISimplePropertySet**](/windows/desktop/api/uiribbon/nn-uiribbon-iuisimplepropertyset) to expose the read-only properties associated with the item, such as the label or image.

To add or delete items in a gallery control at run time, use the various methods of [**IUICollection**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection).

The following screen shot illustrates the use of two categories, **Selection shapes** and **Selection options**, in a [**SplitButton**](windowsribbon-element-splitbutton.md) menu.

![screen shot that shows two categories, selection shapes and selection options, in a splitbuttongallery control.](images/properties/ui-pkey-collection-categories2.png)

## Related topics

<dl> <dt>

[Collection Properties](windowsribbon-reference-properties-collection.md)
</dt> <dt>

[UI\_PKEY\_CategoryId](windowsribbon-reference-properties-uipkey-categoryid.md)
</dt> </dl>

 

 