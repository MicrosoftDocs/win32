---
title: UI_PKEY_ItemsSource
description: Identifies the UI\_PKEY\_ItemsSource property.
ms.assetid: f5e99d2a-f50a-4932-ae77-581037cb9ac8
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_ItemsSource

Identifies the UI\_PKEY\_ItemsSource property.

```
propertyDescription
   name = UI_PKEY_ItemsSource
   shellPKey = UI_PKEY_ItemsSource
   formatID = 00000101-7363-696e-8441798acf5aebb7
   propID = 101
   typeInfo
      type = IUICollection
```

## Remarks

UI\_PKEY\_ItemsSource is used by an application to query the collection of items in a gallery control, such as the Quick Access Toolbar (QAT).

The property value is an [**IUICollection**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection) object.

Each item in this [**IUICollection**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection) must implement [**IUISimplePropertySet**](/windows/desktop/api/uiribbon/nn-uiribbon-iuisimplepropertyset) to expose the read-only properties associated with the item, such as the label or image.

To add or delete items in a gallery control at run time, use the [**IUICollection**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection) methods.

The following screen shot illustrates a collection of items in a [**SplitButtonGallery**](windowsribbon-element-splitbuttongallery.md) menu.

![screen shot showing categories in a ribbon gallery.](images/markup/splitbutton-gallery-control.png)

## Related topics

<dl> <dt>

[Collection Properties](windowsribbon-reference-properties-collection.md)
</dt> </dl>

 

 