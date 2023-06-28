---
title: About the Cdrom and CdromCollection Objects
description: About the Cdrom and CdromCollection Objects
ms.assetid: b764806b-d9e1-4c36-b86b-24613501c926
keywords:
- Windows Media Player,Cdrom object
- Windows Media Player object model,Cdrom object
- object model,Cdrom object
- Windows Media Player ActiveX control,Cdrom object
- ActiveX control,Cdrom object
- Windows Media Player Mobile ActiveX control,Cdrom object
- Windows Media Player Mobile,Cdrom object
- Cdrom object
- Windows Media Player,CdromCollection object
- Windows Media Player object model,CdromCollection object
- object model,CdromCollection object
- Windows Media Player ActiveX control,CdromCollection object
- ActiveX control,CdromCollection object
- Windows Media Player Mobile ActiveX control,CdromCollection object
- Windows Media Player Mobile,CdromCollection object
- CdromCollection object
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Cdrom and CdromCollection Objects

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Cdrom** and **CdromCollection** objects govern the interface to the CD drives in your computer for purposes of reading and playing CDs.

The **CdromCollection** object is accessed only through the **cdromCollection** property of the **Player** object. The **cdromCollection** property returns the **CdromCollection** object. You can only access the properties of the **CdromCollection** object after you have created it. For example, to use the **count** property, you must use the following code:


```C++
mycount = player.cdromcollection.count;
```



You can only access the **Cdrom** object through the **CdromCollection** object. For example, to eject the CD by using the **Eject** method, you must first create the collection object and then an item in the object. To eject the CD, use the following code:


```C++
player.cdromcollection.item(0).eject();
```



In both cases, you are first creating the collection object (**CdromCollection**) and then getting a specific object of that collection. The object is the first item in the collection, **Item**(0), which corresponds to the first CD drive. You then call a method, **Eject**, on that item.

## Related topics

<dl> <dt>

[**Cdrom Object**](cdrom-object.md)
</dt> <dt>

[**CdromCollection Object**](cdromcollection-object.md)
</dt> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> </dl>

 

 




