---
title: External.NavigateTaskPaneURL method
description: Note This topic describes functionality designed for use by online stores. | External.NavigateTaskPaneURL method
ms.assetid: c3a888c0-6589-4d21-9d47-37372d9069f4
keywords:
- NavigateTaskPaneURL method Windows Media Player
- NavigateTaskPaneURL method Windows Media Player , External class
- External class Windows Media Player , NavigateTaskPaneURL method
topic_type:
- apiref
api_name:
- External.NavigateTaskPaneURL
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# External.NavigateTaskPaneURL method

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **NavigateTaskPaneURL** method opens a webpage in the specified task pane, and changes focus to the specified pane.

## Syntax


```JScript
External.NavigateTaskPaneURL(
  bstrKeyName,
  bstrTaskPane,
  bstrParams
)
```



## Parameters

<dl> <dt>

*bstrKeyName* \[in\]
</dt> <dd>

**String** containing the key name for the online store. (required)

</dd> <dt>

*bstrTaskPane* \[in\]
</dt> <dd>

**String** containing the name of the task pane in which the webpage opens. (required)

</dd> <dt>

*bstrParams* \[in\]
</dt> <dd>

**String** containing the query string parameters to append to the URL specified by the **Navigate** element of the ServiceInfo document. (optional)

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Navigating to a pane that your online store does not support may cause the current online store to change.

The value specified for *bstrParams* is valid only when **NavigateTaskPaneURL** is called from webpages provided by the online store.

The following table lists of valid values for *bstrTaskPane* and the associated task pane for each.



| Value            | Task Pane                      |
|------------------|--------------------------------|
| **ServiceTask1** | First online store task pane.  |
| **ServiceTask2** | Second online store task pane. |
| **ServiceTask3** | Third online store task pane.  |



 

Your webpage code should specify a value for [External.SelectedTaskPane](external-selectedtaskpane.md) when loading to ensure that the correct task pane button is highlighted after navigation is completed.

## Examples

The following example code shows how **NavigateTaskPaneURL** creates the URL of the webpage to display for **ServiceTask1**.

Example of the **Navigate** element:


```XML
<Navigate
    BaseURL = "https://www.proseware.com/online store/html/navigate.asp">
</Navigate>
```



Example call to the **NavigateTaskPaneURL** method:


```XML
external.NavigateTaskPaneURL("Proseware", "ServiceTask1", "Pane=Store");
```



Example of resulting URL used for the webpage displayed in **ServiceTask1**:


```XML
https://www.proseware.com/online store/html/navigate.asp?Pane=Store
```



## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 10 or later<br/>                                        |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 2 Online Stores**](external-object-for-type-2-online-stores.md)
</dt> <dt>

[**External.SelectedTaskPane**](external-selectedtaskpane.md)
</dt> </dl>

 

 





