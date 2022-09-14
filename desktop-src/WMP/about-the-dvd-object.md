---
title: About the DVD Object
description: About the DVD Object
ms.assetid: 6c255e9e-d537-4f4f-865c-b7fb26c8e413
keywords:
- Windows Media Player,DVD object
- Windows Media Player object model,DVD object
- object model,DVD object
- Windows Media Player ActiveX control,DVD object
- ActiveX control,DVD object
- Windows Media Player Mobile ActiveX control,DVD object
- Windows Media Player Mobile,DVD object
- DVD object
ms.topic: article
ms.date: 05/31/2018
---

# About the DVD Object

The **DVD** object adds functionality specific to DVD media. In a general sense, DVD media is treated just like other digital media in Windows Media Player. For instance, DVD drives are enumerated using the **CdromCollection** object and DVD titles and chapters are manipulated using **Playlist** objects and **Media** objects. Some functionality is DVD-specific, however, and the **DVD** object provides this. For example, DVD has a concept called domain. To retrieve the current domain for DVD media, type the following:


```C++
mydomain = player.dvd.domain;

```



## Related topics

<dl> <dt>

[**DVD Object**](dvd-object.md)
</dt> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> </dl>

 

 




