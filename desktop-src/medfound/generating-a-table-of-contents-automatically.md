---
Description: Generating a Table of Contents Automatically
ms.assetid: 3acb9c12-0158-4b89-87c4-4abd35ae8c2f
title: Generating a Table of Contents Automatically
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Generating a Table of Contents Automatically

This topic demonstrates how to use [**Table of Contents Generator**](https://msdn.microsoft.com/en-us/library/Ff819466(v=VS.85).aspx) (TOC Generator) component to automatically generate a table of contents for a video file.

TOC Generator is a DirectX Media Object (DMO). To use the TOC Generator DMO, build a DirectX filter graph that has a video file as its source. Insert the TOC Generator DMO into the filter graph, and run the graph. You can then obtain the automatically generated table of contents from the TOC Generator DMO.

The following procedure gives the steps in more detail.

1.  Call [**CoCreateInstance**](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx) to create a Filter Graph object (**CLSID\_FilterGraph**) and obtain an [**IGraphBuilder**](https://msdn.microsoft.com/en-us/library/Dd390085(v=VS.85).aspx) interface.
2.  Call [**CoCreateInstance**](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx) to create a DMO Wrapper Filter object (**CLSID\_DMOWrapperFilter**) and obtain an [**IDMOWrapperFilter**](https://msdn.microsoft.com/en-us/library/Dd406848(v=VS.85).aspx) interface.
3.  Pass **CLSID\_CTocGeneratorDmo** to the [**Init**](https://msdn.microsoft.com/en-us/library/Dd406849(v=VS.85).aspx) method of your DMO wrapper filter. This creates a TOC Generator DMO and wraps it in your DMO wrapper filter.
4.  Call the [**AddFilter**](https://msdn.microsoft.com/en-us/library/Dd390016(v=VS.85).aspx) method of your [**IGraphBuilder**](https://msdn.microsoft.com/en-us/library/Dd390085(v=VS.85).aspx) interface to add the wrapped TOC Generator DMO to the filter graph.
    > [!Note]  
    > [**IGraphBuilder**](https://msdn.microsoft.com/en-us/library/Dd390085(v=VS.85).aspx) inherits from [**IFilterGraph**](https://msdn.microsoft.com/en-us/library/Dd389989(v=VS.85).aspx).

     

5.  Call the [**AddSourceFilter**](https://msdn.microsoft.com/en-us/library/Dd390087(v=VS.85).aspx) method of your [**IGraphBuilder**](https://msdn.microsoft.com/en-us/library/Dd390085(v=VS.85).aspx) interface to create a souce filter and add it to the graph.
6.  Enumerate pins on the DMO wrapper filter and the source filter. This involves obtaining [**IEnumPins**](https://msdn.microsoft.com/en-us/library/Dd376610(v=VS.85).aspx) interfaces and [**IPin**](https://msdn.microsoft.com/en-us/library/Dd390397(v=VS.85).aspx) interfaces.
7.  Connect the source filter and the wrapper filter by calling the [**Connect**](https://msdn.microsoft.com/en-us/library/Dd390088(v=VS.85).aspx) method of your [**IGraphBuilder**](https://msdn.microsoft.com/en-us/library/Dd390085(v=VS.85).aspx) interface.
8.  Complete the graph by calling the [**Render**](https://msdn.microsoft.com/en-us/library/Dd390089(v=VS.85).aspx) method of your [**IGraphBuilder**](https://msdn.microsoft.com/en-us/library/Dd390085(v=VS.85).aspx) interface.
9.  Run the graph ([**IMediaControl::Run**](https://msdn.microsoft.com/en-us/library/Dd390177(v=VS.85).aspx)), and wait for it to complete ([**IMediaEvent::WaitForCompletion**](https://msdn.microsoft.com/en-us/library/Dd406914(v=VS.85).aspx)).
10. Obtain an [**IPropertyStore**](https://msdn.microsoft.com/en-us/library/Bb761474(v=VS.85).aspx) interface on your DMO filter wrapper, and get the value of the [**MFPKEY\_TOCGENERATOR\_TOCREADY**](https://msdn.microsoft.com/en-us/library/Ff819466(v=VS.85).aspx) property. Repeat if necessary until the table of contents is ready.
11. Use your [**IPropertyStore**](https://msdn.microsoft.com/en-us/library/Bb761474(v=VS.85).aspx) interface to get the value of the [**MFPKEY\_TOCGENERATOR\_TOCOBJECT**](https://msdn.microsoft.com/en-us/library/Ff819466(v=VS.85).aspx) property. This property is an [**IToc**](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-itoc) interface that represents the automatically generated table of contents.

The following code demonstrates the procedure for generating a table of contents automatically. The code uses three helper functions ([**BuildGraph**](buildgraph-method-for-generating-a-table-of-contents.md), [**RunGraphAndWait**](rungraphandwait-method-for-generating-a-table-of-contents.md), and [**GetToc**](gettoc-method-for-generating-a-table-of-contents.md)) that are shown on other pages of this documentation.


```C++
#include <dshow.h>
#include <dmodshow.h>
#include <wmcodecdsp.h>
#include <dmoreg.h>
#include <propsys.h>
#include <propidl.h>
#include <initguid.h>

HRESULT GetToc(IDMOWrapperFilter* pWrap, IToc** ppToc);
HRESULT RunGraphAndWait(IGraphBuilder* pGraph);
HRESULT BuildGraph(IGraphBuilder* pGraph, IDMOWrapperFilter* pWrap);

WCHAR g_sourceFile[] = L"c:\\experiment\\Seattle.wmv";

void main()
{
   HRESULT hr = E_FAIL;
   hr = CoInitialize(NULL);

   if(SUCCEEDED(hr))
   {
      IGraphBuilder* pBuilder = NULL;
      hr = CoCreateInstance(CLSID_FilterGraph, NULL, CLSCTX_INPROC_SERVER, 
         IID_IGraphBuilder, (VOID**)&pBuilder);

      if(SUCCEEDED(hr))
      {
         IDMOWrapperFilter* pWrap = NULL;
         hr = CoCreateInstance(CLSID_DMOWrapperFilter, NULL, CLSCTX_INPROC, 
            IID_IDMOWrapperFilter, (VOID**)&pWrap);

         if(SUCCEEDED(hr))
         {
            hr = pWrap->Init(CLSID_CTocGeneratorDmo, DMOCATEGORY_VIDEO_EFFECT); 

            if(SUCCEEDED(hr))
            {
               hr = BuildGraph(pBuilder, pWrap);

               if(SUCCEEDED(hr))
               {
                  hr = RunGraphAndWait(pBuilder);

                  if(SUCCEEDED(hr))
                  {
                     IToc* pToc = NULL;
                     hr = GetToc(pWrap, &pToc);

                     if(SUCCEEDED(hr))
                     {
                        // Inspect the table of contents by calling IToc methods.

                        pToc->Release();
                        pToc = NULL;
                     }
                  }
               }
            }

            pWrap->Release();
            pWrap = NULL;
         }

         pBuilder->Release();
         pBuilder = NULL;
      }

      CoUninitialize();
   }
}
```



## Related topics

<dl> <dt>

[BuildGraph Function for Generating a Table of Contents](buildgraph-method-for-generating-a-table-of-contents.md)
</dt> <dt>

[GetToc Function for Generating a Table of Contents](gettoc-method-for-generating-a-table-of-contents.md)
</dt> <dt>

[RunGraphAndWait Function for Generating a Table of Contents](rungraphandwait-method-for-generating-a-table-of-contents.md)
</dt> <dt>

[Table of Contents Parser Programming Guide](toc-parser-programming-guide.md)
</dt> </dl>

 

 



