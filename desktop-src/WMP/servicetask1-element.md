---
title: ServiceTask1 Element
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The ServiceTask1 element represents the first online store task pane.
ms.assetid: 39b149ae-ea67-4fba-812b-15a97044fcd8
keywords:
- ServiceTask1 Element Windows Media Player
topic_type:
- apiref
api_name:
- ServiceTask1 Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ServiceTask1 Element

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **ServiceTask1** element represents the first online store task pane.

``` syntax
<ServiceTask1
    URL = "URL"
/>
```

## Attributes



| Term                                                                                                                             | Description                                                        |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <span id="URL__required_"></span><span id="url__required_"></span><span id="URL__REQUIRED_"></span>**URL** (required)<br/> | URL for the webpage that Windows Media Player displays.<br/> |



 

## Parent/Child Elements



| Hierarchy       | Element                       |
|-----------------|-------------------------------|
| Parent elements | **ServiceInfo**               |
| Child elements  | **ButtonText**, **ButtonTip** |



 

## Remarks

**ServiceTask1** is considered the primary task pane for engaging in commercial activity. It is the task pane that displays when the user chooses to purchase music.

> [!Note]  
> Windows Media Player 10 has three task panes where an online store can display its webpages. The online store can choose to use one, two, or all three of the task panes. Windows Media Player 11 has only one task pane, represented by **ServiceTask1**, which the user can view by clicking on the **Online Stores** tab.

 

Online store task panes share a single browser instance. This means that you should not write script code in your webpage that you expect to continue to run when the user switches away from the current service task.

When the user switches task panes, Windows Media Player stores the URL and session cookies. When the user switches back to the task pane, the Player restores the URL and cookies. If the user chooses to use a different online store, the URL and session data are cleared.

The following table details the parameters sent with the URL request. Others may be present for legacy compatibility purposes.



| Name         | Value                                                                                                                                                               |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *geoid*      | Windows geographical location ID. The location ID is specified by the user in the **Location** area of the Regional and Language Options settings in Control Panel. |
| *locale*     | Windows Media Player locale ID.                                                                                                                                     |
| *userlocale* | Windows locale ID. The locale is specified by the user in the **Standards and Formats** area of the Regional and Language Options settings in Control Panel.        |
| *version*    | Windows Media Player version number using the following format: 10.0.x.xxxx or 11.0.x.xxxx.                                                                         |



 

## Requirements



| Requirement | Value |
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

 

 





