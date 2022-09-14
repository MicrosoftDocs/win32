---
title: Using Script in a Web Page Displayed by Firefox
description: Using Script in a Web Page Displayed by Firefox
ms.assetid: 0f1d21b1-1824-4ba9-9c0e-bd23ba847d9d
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player ActiveX control,Web pages
- Windows Media Player Mobile ActiveX control,Web pages
- ActiveX control,Web pages
- Windows Media Player ActiveX control,scripting example
- Windows Media Player Mobile ActiveX control,scripting example
- ActiveX control,scripting example
- embedding,Web pages
- Web page embedding,scripting example
- Windows Media Player,Firefox
- Windows Media Player object model,Firefox
- object model,Firefox
- Windows Media Player Mobile,Firefox
- Windows Media Player ActiveX control,Firefox
- Windows Media Player Mobile ActiveX control,Firefox
- ActiveX control,Firefox
- Firefox,scripting example
- Web page embedding,Firefox
- scripting example for webpage embedding
ms.topic: article
ms.date: 05/31/2018
---

# Using Script in a Web Page Displayed by Firefox

Script on a webpage can use the Player object model to control the Player as the user interacts with the page. For example, the following INPUT element has script that sets the Player volume.


```HTML
<INPUT type="button" value="Vol" OnClick="ChangeVolume()"/>
 
<SCRIPT>
  function ChangeVolume()
  {
    Player.settings.volume = 90;
  }
</SCRIPT>

```



Many of the objects in the Windows Media Player object model are supported by Internet Explorer and by the Firefox plug-in. However, there are some objects that are not supported by the Firefox plug-in. The following table lists all of the objects in the Player object model and shows which objects are supported by the Firefox plug-in.



| Object                                              | Firefox support |
|-----------------------------------------------------|-----------------|
| [Cdrom](cdrom-object.md)                           | no              |
| [CdromCollection](cdromcollection-object.md)       | no              |
| [ClosedCaption](closedcaption-object.md)           | yes             |
| [Controls](controls-object.md)                     | no              |
| [DVD](dvd-object.md)                               | no              |
| [Error](error-object.md)                           | yes             |
| [ErrorItem](erroritem-object.md)                   | yes             |
| [Media](media-object.md)                           | yes             |
| [MediaCollection](mediacollection-object.md)       | no              |
| [MetadataPicture](metadatapicture-object.md)       | no              |
| [MetadataText](metadatatext-object.md)             | no              |
| [Network](network-object.md)                       | yes             |
| [Player](player-object.md)                         | yes             |
| [PlayerApplication](playerapplication-object.md)   | no              |
| [Playlist](playlist-object.md)                     | yes             |
| [PlaylistArray](playlistarray-object.md)           | no              |
| [PlaylistCollection](playlistcollection-object.md) | no              |
| [Query](query-object.md)                           | no              |
| [Settings](settings-object.md)                     | yes             |
| [StringCollection](stringcollection-object.md)     | no              |



 

The Firefox plug-in supports the **Player** object, but certain properties of the **Player** object return **NULL** in a Firefox browser. For example, the [cdromCollection](player-cdromcollection.md) property of the **Player** object returns **NULL** because the Firefox plug-in does not support the **Cdrom** object. Similarly, the [dvd](player-dvd.md), [mediaCollection](player-mediacollection.md), [playerApplication](player-playerapplication.md), and [playlistCollection](player-playlistcollection.md) properties of the **Player** object return **NULL** in a Firefox browser.

The **Player.pluginVersionInfo** property is supported by the Firefox plug-in but not by Internet Explorer. This property returns the version of the Firefox plug-in.

The Firefox plug-in supports the **Media** object, including the [getItemInfoByType](media-getiteminfobytype.md) property. However, in a Firefox browser, the **getItemInfoByType** property does not support the **MetadataText** and **MetadataPicture** return types.

The Firefox plug-in supports the [Settings](settings-object.md) object except for the [setMode](settings-setmode.md) method and the [requestMediaAccessRights](settings-requestmediaaccessrights.md) property. In a Firefox browser, the **requestMediaAccessRight** property always returns false.

## Related topics

<dl> <dt>

[**Using the Windows Media Player Control with Firefox**](using-the-windows-media-player-control-with-firefox.md)
</dt> </dl>

 

 




