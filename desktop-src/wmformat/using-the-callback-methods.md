---
title: Using the Callback Methods
description: Using the Callback Methods
ms.assetid: 098cb90b-8c21-4692-a4f9-bacce042520a
keywords:
- Windows Media Format SDK,callback methods
- Windows Media Format SDK,methods called asynchronously
- callback methods
ms.topic: reference
ms.date: 05/31/2018
---

# Using the Callback Methods

Several interfaces in the Windows Media Format SDK contain methods that are called asynchronously. Most of these methods use callback functions to pass information to the controlling application.

The following sections describe some of the general issues regarding the use of callback methods with the Windows Media Format SDK.



| Section                                                                          | Description                                                                                                                                                                                          |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Using the OnStatus Callback](using-the-onstatus-callback.md)                   | Describes how to implement the [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) callback method, which is used by several objects to advise applications of SDK operation progress. |
| [Using Events with Asynchronous Calls](using-events-with-asynchronous-calls.md) | Describes a common technique to handle asynchronous method calls in an application.                                                                                                                  |
| [Using the Context Parameter](using-the-context-parameter.md)                   | Introduces the *pvContext* parameter, shared by several callbacks and their calling methods, and explains how to use it.                                                                             |



 

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 




