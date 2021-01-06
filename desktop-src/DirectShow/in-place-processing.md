---
description: In-Place Processing
ms.assetid: 61e5c12c-e42a-42d8-ac5b-e60afaceda82
title: In-Place Processing
ms.topic: article
ms.date: 05/31/2018
---

# In-Place Processing

Certain data transformations can be accomplished by directly modifying the data. This is called *in-place* processing. Many audio and video effects can be done in this manner. If a DMO supports in-place processing, it exposes the [**IMediaObjectInPlace**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-imediaobjectinplace) interface. In-place processing is generally more efficient than using separate buffers for the output. (One major exception is when the buffer resides in video memory. In that situation, read operations are much slower than write operations, so in-place processing is not recommended.)

To process data in place, the client makes a single call to the [**IMediaObjectInPlace::Process**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobjectinplace-process) method, rather than separate calls to **ProcessInput** and **ProcessOutput**. The **Process** method is synchronous; all processing occurs inside the call. Also, in-place processing does not use **IMediaBuffer** objects. The **Process** method takes a pointer directly to the memory buffer.

A DMO that supports in-place processing still must implement the **IMediaObject** interface, including the **ProcessInput** and **ProcessOutput** methods. The client can choose whether to use in-place processing or use separate buffers. However, do not mix the two types of processing. If you call **Process**, do not call **ProcessInput** or **ProcessOutput**, and vice-versa.

**Effect Tails**

An in-place DMO might create some additional output after the input stops. This is called an *effect tail*. For example, a reverb effect continues after the input reaches silence. If there is an effect tail, the **Process** method returns S\_FALSE. Once the application has processed all of its data, it can generate the effect tail by sending empty buffers to the **Process** method.

## Related topics

<dl> <dt>

[Directly Hosting a DMO](directly-hosting-a-dmo.md)
</dt> </dl>

 

 



