---
title: The AnimationNames Collection
description: The AnimationNames Collection
ms.assetid: 3b06e497-1d03-43be-8d33-e69ef2972237
ms.topic: article
ms.date: 05/31/2018
---

# The AnimationNames Collection

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The [**AnimationNames**](https://www.bing.com/search?q=**AnimationNames**) collection is a special collection that contains the list of animation names compiled for a character. You can use the collection to enumerate the names of the animations for a character. For example, in Visual Basic or VBScript (2.0 or later) you can access these names using the **For Each...Next** statements:


```
   For Each Animation in Genie.AnimationNames
      Genie.Play Animation
   Next
```



Items in the collection have no properties, so individual items cannot be accessed directly.

For .ACF characters, the collection returns all the animations that have been defined for the character, not just the ones that have been retrieved with the [**Get**](get-method.md) method.

 

 




