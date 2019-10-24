---
title: ErrorItem Object
description: The ErrorItem object provides a way to access error information.
ms.assetid: 14bc9c12-98c6-4b72-9ae5-d6afeb1303f9
keywords:
- ErrorItem Object Windows Media Player
topic_type:
- apiref
api_name:
- ErrorItem Object
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ErrorItem Object

The **ErrorItem** object provides a way to access error information.

The **ErrorItem** object supports the following properties.



| Property                                           | Description                                                                                     |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [condition](erroritem-condition.md)               | Retrieves a value indicating the condition for the error.                                       |
| [customUrl](erroritem-customurl.md)               | Retrieves the URL of a website that displays specific information about codec download failure. |
| [errorCode](erroritem-errorcode.md)               | Retrieves the current error code.                                                               |
| [errorContext](erroritem-errorcontext.md)         | Retrieves a value indicating the context of the error.                                          |
| [errorDescription](erroritem-errordescription.md) | Retrieves a description of the error.                                                           |
| **remedy**                                         | Reserved for future use.                                                                        |



 

The **ErrorItem** object is accessed through the following methods.



| Object                    | Method                   |
|---------------------------|--------------------------|
| [Error](error-object.md) | [item](error-item.md)   |
| [Media](media-object.md) | [error](media-error.md) |



 

For purposes of illustration, *player*.*error*.*item*(*index*) is used in the reference syntax sections.

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




