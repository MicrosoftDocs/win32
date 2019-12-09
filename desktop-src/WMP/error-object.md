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
ms.date: 05/31/2018
api_location: 
---

# Error Object

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

 

 




