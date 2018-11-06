---
title: About the Error and ErrorItem Objects
description: About the Error and ErrorItem Objects
ms.assetid: 187f6835-3101-45db-87bd-930d222165ce
keywords:
- Windows Media Player,Error object
- Windows Media Player object model,Error object
- object model,Error object
- Windows Media Player ActiveX control,Error object
- ActiveX control,Error object
- Windows Media Player Mobile ActiveX control,Error object
- Windows Media Player Mobile,Error object
- Error object
- Windows Media Player,ErrorItem object
- Windows Media Player object model,ErrorItem object
- object model,ErrorItem object
- Windows Media Player ActiveX control,ErrorItem object
- ActiveX control,ErrorItem object
- Windows Media Player Mobile ActiveX control,ErrorItem object
- Windows Media Player Mobile,ErrorItem object
- ErrorItem object
ms.topic: article
ms.date: 05/31/2018
---

# About the Error and ErrorItem Objects

The **Error** and **ErrorItem** objects govern the error-handling capabilities of Windows Media Player. The **Error** object is obtained from the **Player** object through the **error** property. You can get a specific code from the **Error** object by using the **item** property of the **Error** object to create the **ErrorItem** object. For example, to get the error code of the first error item, type:


```C++
myerrorcode = player.error.item(0).errorCode;

```



You can also invoke Web Help with the **Error** object by using the following code:


```C++
player.error.webHelp();

```



## Related topics

<dl> <dt>

[**Error Object**](error-object.md)
</dt> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> </dl>

 

 




