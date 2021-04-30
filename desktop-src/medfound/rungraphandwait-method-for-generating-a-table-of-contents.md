---
description: RunGraphAndWait Function for Generating a Table of Contents
ms.assetid: f6eac1cf-05c3-48b6-b9b4-02966facdc95
title: RunGraphAndWait Function for Generating a Table of Contents
ms.topic: article
ms.date: 05/31/2018
---

# RunGraphAndWait Function for Generating a Table of Contents

The following function is a helper function in an example program that is discussed in [Generating a Table of Contents Automatically](generating-a-table-of-contents-automatically.md).


```C++
HRESULT RunGraphAndWait(IGraphBuilder* pGraph)
{
   IMediaControl* pControl = NULL;
   HRESULT hr = pGraph->QueryInterface(IID_IMediaControl, (VOID**)&pControl);

   if(SUCCEEDED(hr))
   {
      hr = pControl->Run();

      if(SUCCEEDED(hr))
      {
         IMediaEvent* pEvent = NULL;
         hr = pControl->QueryInterface(IID_IMediaEvent, (VOID**)&pEvent);

         if(SUCCEEDED(hr))
         {
           long eventCode = 0;
           hr = pEvent->WaitForCompletion(INFINITE, &eventCode);
           pEvent->Release();
           pEvent = NULL;
         }
      }

      pControl->Release();
      pControl = NULL;
   }

   return hr;
}
```



## Related topics

<dl> <dt>

[Generating a Table of Contents Automatically](generating-a-table-of-contents-automatically.md)
</dt> </dl>

 

 



