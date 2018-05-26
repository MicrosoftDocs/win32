---
title: Error-Handling Interfaces
description: Objects that are invoked through virtual function table (VTBL) binding need to use the Automation error handling interfaces and functions to define and return error information.
ms.assetid: c258677e-d53e-499d-a414-ce889709b23e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Error-Handling Interfaces

Objects that are invoked through virtual function table (VTBL) binding need to use the Automation error handling interfaces and functions to define and return error information.

## In this section



| Topic                                                                       | Description                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Returning Error Information](returning-error-information.md)<br/>   | Describes how to return error information.<br/>                                                                                                                                                             |
| [Retrieving Error Information](retrieving-error-information.md)<br/> | Describes how to retrieve error information.<br/>                                                                                                                                                           |
| [**ICreateErrorInfo**](/windows/previous-versions/oaidl/nn-oaidl-icreateerrorinfo?branch=master)<br/>                     | Returns error information.<br/>                                                                                                                                                                             |
| [**IErrorInfo**](/windows/previous-versions/oaidl/nn-oaidl-ierrorinfo?branch=master)<br/>                                 | Provides detailed contextual error information.<br/>                                                                                                                                                        |
| [**ISupportErrorInfo**](/windows/previous-versions/oaidl/nn-oaidl-isupporterrorinfo?branch=master)<br/>                   | Ensures that error information can be propagated up the call chain correctly. Automation objects that use the error handling interfaces must implement [**ISupportErrorInfo**](/windows/previous-versions/oaidl/nn-oaidl-isupporterrorinfo?branch=master).<br/> |



 

## Related topics

<dl> <dt>

[Error-Handling Functions](error-handling-api-functions.md)
</dt> <dt>

[Returning Error Information](returning-error-information.md)
</dt> <dt>

[Retrieving Error Information](retrieving-error-information.md)
</dt> </dl>

 

 





