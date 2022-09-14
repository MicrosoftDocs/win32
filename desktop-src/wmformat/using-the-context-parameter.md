---
title: Using the Context Parameter
description: Using the Context Parameter
ms.assetid: 50e37c36-0ce1-4abd-bb25-f18bb164fdeb
keywords:
- Windows Media Format SDK,context parameter
- Windows Media Format SDK,pvContext parameter
- pvContext parameter
ms.topic: article
ms.date: 05/31/2018
---

# Using the Context Parameter

Some of the callbacks used by the Windows Media Format SDK take a parameter called *pvContext*. The calling objects pass along the value you specify in the method that began the asynchronous action. For example, when you call [**IWMReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-open), you can pass a value for *pvContext*. When the [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) method is called by the reader object to notify your application that the file has been opened, it will pass whatever value you used in your call to **Open** as the *pvContext* parameter of **OnStatus**. This context parameter is provided for your use and you can use it in any way you like.

The *pvContext* parameter is most often used when multiple objects need to share the same callback. For example, several objects use the [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) method. You can use *pvContext* to enable the different objects to share one implementation of **OnStatus** by passing a different value for *pvContext* on your original call. In your implementation of **OnStatus**, you can branch the message handling logic based on the value of *pvContext*.

## Related topics

<dl> <dt>

[**Using the Callback Methods**](using-the-callback-methods.md)
</dt> </dl>

 

 




