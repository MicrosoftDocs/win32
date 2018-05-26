---
Description: Getting Buffers
ms.assetid: be61aee9-41d5-42bc-b905-d0216d301faf
title: Getting Buffers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting Buffers

If your filter has a custom allocator that uses filter resources, the allocator's [**IMemAllocator::GetBuffer**](/windows/win32/Strmif/nf-strmif-imemallocator-getbuffer?branch=master) method should hold the streaming lock, as with other streaming methods:


```C++
HRESULT CMyInputAllocator::GetBuffer(
    IMediaSample **ppBuffer,
    REFERENCE_TIME *pStartTime, 
    REFERENCE_TIME *pEndTime,
    DWORD dwFlags)
{
    CAutoLock cObjectLock(&amp;m_csReceive);

    /* Use resources. */

    return CMemAllocator::GetBuffer(ppBuffer, pStartTime, pEndTime, dwFlags);    
}
```



## Related topics

<dl> <dt>

[Threads and Critical Sections](threads-and-critical-sections.md)
</dt> </dl>

 

 



