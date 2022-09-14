---
title: LISTBOX Element
description: LISTBOX Element
ms.assetid: b83ba0cb-1838-494d-b4cb-55b4da18a038
keywords:
- Windows Media Player skins,LISTBOX element
- skins,LISTBOX element
- LISTBOX element
- reference for skins,LISTBOX element
- elements,LISTBOX
ms.topic: article
ms.date: 05/31/2018
---

# LISTBOX Element

The **LISTBOX** element provides a way for users to select items from a list. These items can be specified by using **ITEM** elements as children of the **LISTBOX** element. If you need a list box control that is displayed only when needed, use the **POPUP** element, which is identical to the **LISTBOX** element except for the default value of the **popUp** attribute, which dictates its display behavior.

The **LISTBOX** element supports the following attributes.



| Attribute                                        | Description                                                                                                           |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [backgroundColor](listbox-backgroundcolor.md)   | Specifies or retrieves the background color in the list box control.                                                  |
| [border](listbox-border.md)                     | Specifies or retrieves a value indicating whether the list box control has a border. Can only be set at design time.  |
| [firstVisibleItem](listbox-firstvisibleitem.md) | Specifies or retrieves the index of the first visible line in the list box control.                                   |
| [focusItem](listbox-focusitem.md)               | Specifies or retrieves the line that contains focus.                                                                  |
| [fontFace](listbox-fontface.md)                 | Specifies or retrieves the font for the list box control.                                                             |
| [fontSize](listbox-fontsize.md)                 | Specifies or retrieves the font size for the list box control.                                                        |
| [fontStyle](listbox-fontstyle.md)               | Specifies or retrieves the font style for the list box control.                                                       |
| [foregroundColor](listbox-foregroundcolor.md)   | Specifies or retrieves the text color in the list box control.                                                        |
| [itemCount](listbox-itemcount.md)               | Retrieves the number of items in the list box control.                                                                |
| [multiSelect](listbox-multiselect.md)           | Specifies or retrieves a value indicating whether the user can select multiple lines. Can only be set at design time. |
| [popUp](listbox-popup.md)                       | Specifies a value indicating whether the element represents a popup or list box control.                              |
| [readOnly](listbox-readonly.md)                 | Specifies or retrieves a value indicating whether text is read-only or text can be selected by the user.              |
| [selectedItem](listbox-selecteditem.md)         | Specifies or retrieves the index of the item selected in the list box control.                                        |
| [sorted](listbox-sorted.md)                     | Specifies or retrieves a value indicating whether the list box control is sorted alphabetically.                      |



 

The **LISTBOX** element supports the following methods.



| Method                                                 | Description                                                                                                           |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [appendItem](listbox-appenditem.md)                   | Inserts new text at the end of the list box control.                                                                  |
| [deleteAll](listbox-deleteall.md)                     | Deletes all items from the list box control.                                                                          |
| [deleteItem](listbox-deleteitem.md)                   | Deletes the list box control item at the specified index.                                                             |
| [dismiss](listbox-dismiss.md)                         | Hides the control.                                                                                                    |
| [findItem](listbox-finditem.md)                       | Searches for a given string starting with the item following the specified item index.                                |
| [getItem](listbox-getitem.md)                         | Retrieves the text for the item with the specified index.                                                             |
| [getNextSelectedItem](listbox-getnextselecteditem.md) | Retrieves the next selected item in the list box control starting at the item after the one with the specified index. |
| [insertItem](listbox-insertitem.md)                   | Inserts the specified text at the specified index in the list box control.                                            |
| [replaceItem](listbox-replaceitem.md)                 | Replaces the text at the specified index with the specified text.                                                     |
| [setSelectedState](listbox-setselectedstate.md)       | Selects or unselects the item with the specified index.                                                               |
| [show](listbox-show.md)                               | Displays the control.                                                                                                 |



 

> [!Note]  
> This element requires Windows Media Player for Windows XP or later.

 

## Related topics

<dl> <dt>

[**POPUP Element**](popup-element.md)
</dt> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




