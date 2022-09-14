---
title: Error and Exception Handling ACF Attributes
description: Use the following attributes for error handling.
ms.assetid: fb00df67-4645-4ef0-9216-618d0af1d9d4
keywords:
- ACF MIDL , attributes, error and exception-handling
ms.topic: article
ms.date: 05/31/2018
---

# Error and Exception Handling ACF Attributes

Use the following attributes for error handling.



| Attribute                                                                | Usage                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**comm\_status**](comm-status.md)[**fault\_status**](fault-status.md) | Let your client application handle exceptions gracefully by causing communication and server errors to be returned to the client as parameter values. The client application can then call the RPC run-time function [**DceErrorInqText**](/windows/desktop/api/rpcdce/nf-rpcdce-dceerrorinqtext) to relay an error message to the user. |



 

## Related topics

<dl> <dt>

[Importing Files and Type Libraries](importing-files-and-type-libraries.md)
</dt> </dl>

 

 