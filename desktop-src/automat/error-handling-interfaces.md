---
title: Error-Handling Interfaces
description: Objects that are invoked through virtual function table (VTBL) binding need to use the Automation error handling interfaces and functions to define and return error information.
ms.assetid: c258677e-d53e-499d-a414-ce889709b23e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Error-Handling Interfaces

Objects that are invoked through virtual function table (VTBL) binding need to use the Automation error handling interfaces and functions to define and return error information.

## In this section



| Topic                                                                       | Description                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Returning Error Information](returning-error-information.md)<br/>   | Describes how to return error information.<br/>                                                                                                                                                             |
| [Retrieving Error Information](retrieving-error-information.md)<br/> | Describes how to retrieve error information.<br/>                                                                                                                                                           |
| [**ICreateErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-icreateerrorinfo)<br/>                     | Returns error information.<br/>                                                                                                                                                                             |
| [**IErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ierrorinfo)<br/>                                 | Provides detailed contextual error information.<br/>                                                                                                                                                        |
| [**ISupportErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-isupporterrorinfo)<br/>                   | Ensures that error information can be propagated up the call chain correctly. Automation objects that use the error handling interfaces must implement [**ISupportErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-isupporterrorinfo).<br/> |



 

## Related topics

<dl> <dt>

[Error-Handling Functions](error-handling-api-functions.md)
</dt> <dt>

[Returning Error Information](returning-error-information.md)
</dt> <dt>

[Retrieving Error Information](retrieving-error-information.md)
</dt> </dl>

 

 





