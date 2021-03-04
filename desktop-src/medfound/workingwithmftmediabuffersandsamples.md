---
description: Working with MFT Media Buffers and Samples
ms.assetid: dda4048e-bc4c-40ac-a6bd-34984f3717e0
title: Working with MFT Media Buffers and Samples
ms.topic: article
ms.date: 05/31/2018
---

# Working with MFT Media Buffers and Samples

Codec MFTs pass media data back and forth by using media buffers and samples.

A media buffer is a COM object that manages a block of memory, typically to hold media data. When data is passed to or from an MFT, it is always passed in the form of a media buffer.

All media buffers expose the **IMFMediaBuffer** interface. This interface is designed for any type of data. Buffers containing video data often also expose **IMF2DBuffer**.

A media buffer has a maximum size, which is the amount of memory allocated for the buffer. To find the maximum size, call **IMFMediaBuffer::GetMaxLength**. At any point in time, a media buffer also has a current length, which is the amount of valid data in the buffer, ranging from zero bytes up to the maximum size. To get the current length, call **IMFMediaBuffer::GetCurrentLength**. When the buffer is created, the current length is zero. If you write data to the buffer, call **IMFMediaBuffer::SetCurrentLength** to update the current length.

To access the memory in the buffer, call **IMFMediaBuffer::Lock**. This method returns a pointer to the start of the memory block. When you are done using the pointer, call **IMFMediaBuffer::Unlock**. The **Lock** method is not a thread synchronization mechanism; it does not guarantee that other threads cannot access the buffer. The **Lock** method is used to assure that the memory accessed will remain valid until you call the **Unlock** method.

A media sample object (in the context of the Media Foundation SDK) is an object that contains an ordered list of zero or more buffers. Media samples expose the **IMFSample** interface.

To create a new sample, call the **MFCreateSample** function. Initially, the sample's buffer list is empty. To add a buffer to the end of the list, call **IMFSample::AddBuffer**.

## Related topics

<dl> <dt>

[Working with Codec DMOs](workingwithcodecdmos.md)
</dt> <dt>

[Working with Codec MFTs](workingwithcodecmfts.md)
</dt> </dl>

 

 



