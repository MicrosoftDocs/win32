---
title: Referencing Skins in URLs
description: Referencing Skins in URLs
ms.assetid: 9ae30c12-2dee-46b2-90e2-c101a83856fb
keywords:
- Windows Media Player skins,URL references
- skins,URL references
- URL references in skins
ms.topic: article
ms.date: 05/31/2018
---

# Referencing Skins in URLs

If you use a URL to load a media file that will be played by Windows Media Player, you can request that a particular skin be used with that file. If the skin is already installed on the user's machine, it will be used; otherwise the previous skin will be used.

To request a skin, add the following to the end of the URL:


```C++
?WMPSkin=skinname
```



*skinname* is the name of the skin you want to request. Do not use quotes around the name of the skin.

For example, to request the headspace skin be used, type the following http URL:


```C++
https://www.proseware.com/mymedia.wma?WMPSkin=headspace

```



## Related topics

<dl> <dt>

[**About Skins**](about-skins.md)
</dt> </dl>

 

 




