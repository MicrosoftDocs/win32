---
Description: Asynchronous Callback Methods
ms.assetid: ea778eaa-6460-4a93-bd6a-1857ea8b6230
title: Asynchronous Callback Methods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Asynchronous Callback Methods

Media Foundation provides a consistent way to implement asynchronous methods, using a callback interface.

This section describes how to implement the callback interface and how to write asynchronous methods that use this interface. It contains the following topics.



| Topic                                                                                | Description                                                                                         |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [Calling Asynchronous Methods](calling-asynchronous-methods.md)                     | How to call asynchronous methods in Media Foundation.                                               |
| [Implementing the Asynchronous Callback](implementing-the-asynchronous-callback.md) | How to implement the callback method in the [**IMFAsyncCallback**](/windows/win32/mfobjects/nn-mfobjects-imfasynccallback?branch=master) interface. |
| [Supporting Multiple Callbacks](supporting-multiple-callbacks.md)                   | How to support multiple callbacks within the same C++ class.                                        |
| [Work Queues](work-queues.md)                                                       | Work queues provide an efficient way to perform asynchronous operations on another thread.          |
| [Writing an Asynchronous Method](writing-an-asynchronous-method.md)                 | How to implement asynchronous methods in Media Foundation.                                          |
| [Custom Asynchronous Result Objects](custom-asynchronous-result-objects.md)         | How to provide a custom implementation of the [**IMFAsyncResult**](/windows/win32/mfobjects/nn-mfobjects-imfasyncresult?branch=master) interface.   |



 

## Related topics

<dl> <dt>

[**IMFAsyncCallback Interface**](/windows/win32/mfobjects/nn-mfobjects-imfasynccallback?branch=master)
</dt> <dt>

[**IMFAsyncResult Interface**](/windows/win32/mfobjects/nn-mfobjects-imfasyncresult?branch=master)
</dt> <dt>

[Media Foundation Platform APIs](media-foundation-platform-apis.md)
</dt> </dl>

 

 



