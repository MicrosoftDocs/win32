---
description: Working with DMO Media Buffers
ms.assetid: 6d0c51b8-0d79-4f04-8e90-0cea4f3b1427
title: Working with DMO Media Buffers
ms.topic: article
ms.date: 05/31/2018
---

# Working with DMO Media Buffers

Input data is passed to the codec DMOs using media buffers. A media buffer is an object that implements the [**IMediaBuffer**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediabuffer) interface. You can implement a class for this purpose or, if you are using the Windows Media Format SDK in your application, you can use the buffer objects that are defined in that SDK.

If you implement your own buffer class, be careful about how the buffer memory is handled. When you pass an input sample, the DMO keeps a reference to the buffer until it is finished with the sample. You can immediately release your reference to the [**IMediaBuffer**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediabuffer) interface, but you have no way of knowing when the codec no longer needs its reference. To be certain that the memory is freed when the object deletes itself, you should implement your class so that it allocates and frees the memory for the buffer internally.

Because the DMOs keep references to buffers for an unknown period of time, it is not a trivial matter to use a limited pool of buffers. The simplest solution is to allocate a new buffer for each sample, although doing so is inefficient.

A better solution is to implement an object to manage a pool of buffers. To do this, write code in the **Release** method of your [**IMediaBuffer**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediabuffer) implementation that calls a method of your buffer manager (instead of deleting itself) when the reference count drops to zero. The buffer manager can then maintain a list of pointers to allocated buffer objects. Create a method in your buffer manager to check the list of free buffers and return a pointer so that your application can access buffers when needed. This method should create new buffers as needed and add them to the list.

## Related topics

<dl> <dt>

[Working with Codec DMOs](workingwithcodecdmos.md)
</dt> </dl>

 

 
