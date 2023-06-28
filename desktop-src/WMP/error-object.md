---
title: Error Object (WMP SDK)
description: The Error object provides access to a collection of ErrorItem objects.
ms.assetid: 1f026ad4-0240-48fe-90ad-739a24e8a7ca
keywords:
- Error Object Windows Media Player
topic_type:
- apiref
api_name:
- Error Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# Error Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Error** object provides access to a collection of [ErrorItem](erroritem-object.md) objects.

The **Error** object supports the following property.



| Property                           | Description                                        |
|------------------------------------|----------------------------------------------------|
| [errorCount](error-errorcount.md) | Retrieves the number of errors in the error queue. |



 

The **Error** object supports the following methods.



| Method                                       | Description                                                                                     |
|----------------------------------------------|-------------------------------------------------------------------------------------------------|
| [clearErrorQueue](error-clearerrorqueue.md) | Clears the errors from the error queue.                                                         |
| [item](error-item.md)                       | Retrieves an [ErrorItem](erroritem-object.md) object from the error queue.                     |
| [webHelp](error-webhelp.md)                 | Launches the Windows Media Player Web Help page to display further information about the error. |



 

The **Error** object is accessed through the following property.



| Object                      | Property                  |
|-----------------------------|---------------------------|
| [Player](player-object.md) | [error](player-error.md) |



 

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




