---
title: Navigating to Other Online Stores
description: Navigating to Other Online Stores
ms.assetid: e88164ef-0f8e-4c54-be34-422662796c63
keywords:
- Windows Media Player online stores,navigating
- online stores,navigating
- type 2 online stores,navigating
- navigating type 2 online stores
ms.topic: article
ms.date: 05/31/2018
---

# Navigating to Other Online Stores

You can create links to other online stores you own or cross-link to online stores provided by others. To do this, you need to know the key name for the online store to which you want to navigate.

The following example code shows HTML that creates a link to switch from the Proseware online store to the "ServiceTask2" feature of the Southridge Video online store:


```C++
<A HREF = 
"javascript:window.external.NavigateTaskPaneURL('SouthridgeVideo', 'ServiceTask2', 'From=Proseware&To=2')"
>Switch to Southridge Video</A>

```



When the user clicks the link, Windows Media Player prompts the user to switch to the Southridge Video store. If the user permits it, the Player then switches stores and navigates to the specified task pane, appending the query string parameters. The query string parameters shown in the preceding example are custom parameters. This means that the online store you switch to must expect these values and handle them. Your online store (and any store you switch to) can use query string parameters any way you choose.

## Related topics

<dl> <dt>

[**Navigating between Service Task Panes**](navigating-between-service-task-panes.md)
</dt> <dt>

[**Navigation for Type 2 Online Stores**](navigation-for-type-2-online-stores.md)
</dt> </dl>

 

 




