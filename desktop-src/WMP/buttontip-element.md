---
title: ButtonTip Element
description: Note This section describes functionality designed for use by online stores. | ButtonTip Element
ms.assetid: 93e5d0c8-8d2d-45c1-9d47-bbd0b6eb8b88
keywords:
- ButtonTip Element Windows Media Player
topic_type:
- apiref
api_name:
- ButtonTip Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ButtonTip Element

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **ButtonTip** element specifies the text string that is displayed when the user points to a task pane button.

``` syntax
<ButtonTip>
   text string
</ButtonTip>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy       | Element                                              |
|-----------------|------------------------------------------------------|
| Parent elements | **ServiceTask1**, **ServiceTask2**, **ServiceTask3** |
| Child elements  | None                                                 |



 

## Remarks

This element is optional for each instance of **ServiceTask1**, **ServiceTask2**, or **ServiceTask3**. If this element is not supplied, Windows Media Player uses the button text as the default value.

> [!Note]  
> Windows Media Player 10 has three task panes where an online store can display its webpages. The online store can choose to use one, two, or all three of the task panes. Windows Media Player 11 has only one task pane, which the user can view by clicking on the **Online Stores** tab. Windows Media Player 11 ignores the **ServiceTask2** and **ServiceTask3** elements.

 

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

 

 





