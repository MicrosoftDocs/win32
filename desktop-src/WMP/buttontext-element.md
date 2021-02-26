---
title: ButtonText Element
description: Note This section describes functionality designed for use by online stores. | ButtonText Element
ms.assetid: 1afe1626-769a-40c8-883a-968ebd995a93
keywords:
- ButtonText Element Windows Media Player
topic_type:
- apiref
api_name:
- ButtonText Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ButtonText Element

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **ButtonText** element specifies the text string that Windows Media Player displays for a task pane button.

``` syntax
<ButtonText>
   text string
</ButtonText>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy       | Element                                              |
|-----------------|------------------------------------------------------|
| Parent elements | **ServiceTask1**, **ServiceTask2**, **ServiceTask3** |
| Child elements  | None                                                 |



 

## Remarks

This element is required for each instance of **ServiceTask1**, **ServiceTask2**, or **ServiceTask3**.

> [!Note]  
> Windows Media Player 10 has three task panes where an online store can display its webpages. The online store can choose to use one, two, or all three of the task panes. Windows Media Player 11 has only one task pane, which the user can view by clicking on the **Online Stores** tab. Windows Media Player 11 ignores the **ServiceTask2** and **ServiceTask3** elements.

 

Windows Media Player may crop button text to fit the available space. The Player always uses the Tahoma bold 8-point font for this text. There are two lines available to display button text, but the Player does not automatically wrap text from the first line to the second. To specify a line break in the button text, insert the new line escape sequence "\\n" in your text string.

The text string is also displayed in the **GoTo** menu in the Windows Media Player user interface.

You should test your online store using a variety of display settings to ensure that text displays as you expect.

## Requirements



|                    |                                              |
|--------------------|----------------------------------------------|
| Version<br/> | Windows Media Player 10 or later.<br/> |



## See also

<dl> <dt>

[**Example ServiceInfo Document for a Type 1 Online Store**](example-serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 2 Online Store**](example-serviceinfo-document-for-a-type-2-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 





