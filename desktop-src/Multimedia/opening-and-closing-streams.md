---
title: Opening and Closing Streams
description: Opening and Closing Streams
ms.assetid: 7dcaccbe-63d8-410a-ae00-16ce9e252ad0
keywords:
- AVIFileGetStream function
- AVIStreamRelease function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Opening and Closing Streams

\[The feature associated with this page, [AVIFile Functions and Macros](/windows/win32/multimedia/avifile-functions-and-macros), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **AVIFile Functions and Macros**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Opening data streams is similar to opening files. You can open a stream by using the [**AVIFileGetStream**](/windows/desktop/api/Vfw/nf-vfw-avifilegetstream) function. This function creates a stream interface, places a handle of the stream in the interface, and returns a pointer to the interface. **AVIFileGetStream** also maintains a reference count of the applications that have opened a stream, but not of those that have closed it.

If you want to access a single stream in a file, you can open the file and the stream by using the [**AVIStreamOpenFromFile**](/windows/desktop/api/Vfw/nf-vfw-avistreamopenfromfilea) function. This function combines the operations and function arguments of the [**AVIFileOpen**](/windows/desktop/api/Vfw/nf-vfw-avifileopen) and **AVIFileGetStream** functions.

To access more than one stream in a file, use **AVIFileOpen** once followed by multiple calls to **AVIFileGetStream**.

You can increment the reference count of a stream by using the [**AVIStreamAddRef**](/windows/desktop/api/Vfw/nf-vfw-avistreamaddref) function to keep a stream open when using a function that would normally close the stream.

You can close a stream by using the [**AVIStreamRelease**](/windows/desktop/api/Vfw/nf-vfw-avistreamrelease) function. This function decrements the reference count of the stream and closes it when the reference count reaches zero. Your applications should balance the reference count by including a call to **AVIStreamRelease** for each use of the [**AVIFileGetStream**](/windows/desktop/api/Vfw/nf-vfw-avifilegetstream), [**AVIFileCreateStream**](/windows/desktop/api/Vfw/nf-vfw-avifilecreatestream), **AVIStreamAddRef**, or **AVIStreamOpenFromFile** function. When you release a stream that has been opened by using **AVIStreamOpenFromFile**, AVIFile closes the file containing the stream. If your application releases a file that has open data streams, AVIFile will not close the streams until all of the streams are released.

 

 




