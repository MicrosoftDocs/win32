---
description: This modal dialog box enables users to select particular items.
ms.assetid: 76e0f369-839e-4dc0-bb42-c48dbf1511f3
title: Selection Dialog
ms.topic: article
ms.date: 05/31/2018
---

# Selection Dialog

This modal dialog box enables users to select particular items.

A Selection Dialog box contains a [SelectionTree control](selectiontree-control.md) that publishes several ControlEvents. Commonly these ControlEvents are subscribed to by [Text](text-control.md), [Icon](icon-control.md), or [Bitmap](bitmap-control.md) controls that display a description, the size, the path, and the icon of the highlighted item.

There is a [PushButton control](pushbutton-control.md) on the dialog box that publishes the [SelectionBrowse ControlEvent](selectionbrowse-controlevent.md) and spawns a [Browse Dialog](browse-dialog.md). The Browse control enables the user to select a directory.

The selection tree is populated only after the [CostInitialize action](costinitialize-action.md) and [CostFinalize action](costfinalize-action.md) are called.

A Selection dialog box is commonly used to select features. The features are listed as items in a SelectionTree control and labeled with the short string of text appearing in the Title column of the [Feature table](feature-table.md). The text string in the Description column of the Feature table is published as a [SelectionDescription ControlEvent](selectiondescription-controlevent.md) and displayed by a [Text control](text-control.md) in the Selection Dialog box. The Selection tree control also publishes the handle to the icon of the highlighted item.

 

 



