---
title: External.SelectedTaskPane
description: Note This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The SelectedTaskPane property specifies or retrieves the currently selected task pane.
ms.assetid: af7b4627-1336-444c-9b4e-5f2e07d9eea7
keywords:
- External.SelectedTaskPane Windows Media Player
topic_type:
- apiref
api_name:
- External.SelectedTaskPane
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.SelectedTaskPane

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **SelectedTaskPane** property specifies or retrieves the currently selected task pane.

## Syntax

window.external.SelectedTaskPane = *servicetask*

## Possible Values

This property is a read/write **String**. Possible values are "ServiceTask1", "ServiceTask2", and "ServiceTask3".

## Remarks

Specifying a value for this property highlights the button for that pane. It does not make the specified task pane active. You should specify a value for this property to set the current task pane button for your webpage when the page loads to ensure that the correct task pane button is active.

To make a particular task pane the active one, use the **NavigateTaskPaneURL** method.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 10 or later<br/>                                        |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 2 Online Stores**](external-object-for-type-2-online-stores.md)
</dt> <dt>

[**External.NavigateTaskPaneURL**](external-navigatetaskpaneurl.md)
</dt> </dl>

 

 





