---
Description: Generating a Table of Contents Automatically
ms.assetid: 3acb9c12-0158-4b89-87c4-4abd35ae8c2f
title: Generating a Table of Contents Automatically
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Generating a Table of Contents Automatically

This topic demonstrates how to use [**Table of Contents Generator**](/windows/desktop/api/wmcodecdsp/) (TOC Generator) component to automatically generate a table of contents for a video file.

TOC Generator is a DirectX Media Object (DMO). To use the TOC Generator DMO, build a DirectX filter graph that has a video file as its source. Insert the TOC Generator DMO into the filter graph, and run the graph. You can then obtain the automatically generated table of contents from the TOC Generator DMO.

The following procedure gives the steps in more detail.

1.  Call [**CoCreateInstance**](https://msdn.microsoft.com/windows/desktop/7295a55b-12c7-4ed0-a7a4-9ecee16afdec) to create a Filter Graph object (**CLSID\_FilterGraph**) and obtain an [**IGraphBuilder**](https://msdn.microsoft.com/windows/desktop/54ed8ac8-4821-4c0c-9fb9-789c70dbca37) interface.
2.  Call [**CoCreateInstance**](https://msdn.microsoft.com/windows/desktop/7295a55b-12c7-4ed0-a7a4-9ecee16afdec) to create a DMO Wrapper Filter object (**CLSID\_DMOWrapperFilter**) and obtain an [**IDMOWrapperFilter**](https://msdn.microsoft.com/windows/desktop/c85b828c-095d-4991-85a8-65b96529f305) interface.
3.  Pass **CLSID\_CTocGeneratorDmo** to the [**Init**](https://msdn.microsoft.com/windows/desktop/45f305b5-82bc-44c1-9af7-93aab371ed33) method of your DMO wrapper filter. This creates a TOC Generator DMO and wraps it in your DMO wrapper filter.
4.  Call the [**AddFilter**](https://msdn.microsoft.com/windows/desktop/8f837917-015f-427f-b234-b0ccbcf943eb) method of your [**IGraphBuilder**](https://msdn.microsoft.com/windows/desktop/54ed8ac8-4821-4c0c-9fb9-789c70dbca37) interface to add the wrapped TOC Generator DMO to the filter graph.
    > [!Note]  
    > [**IGraphBuilder**](https://msdn.microsoft.com/windows/desktop/54ed8ac8-4821-4c0c-9fb9-789c70dbca37) inherits from [**IFilterGraph**](https://msdn.microsoft.com/windows/desktop/73a92f44-03c6-47e3-98d1-a20100ed8fa1).

     

5.  Call the [**AddSourceFilter**](https://msdn.microsoft.com/windows/desktop/ed4d7fc6-558b-474f-ae8d-58aa8479b4d2) method of your [**IGraphBuilder**](https://msdn.microsoft.com/windows/desktop/54ed8ac8-4821-4c0c-9fb9-789c70dbca37) interface to create a souce filter and add it to the graph.
6.  Enumerate pins on the DMO wrapper filter and the source filter. This involves obtaining [**IEnumPins**](https://msdn.microsoft.com/windows/desktop/839190b4-fd29-4a94-8838-d84adfdd9668) interfaces and [**IPin**](https://msdn.microsoft.com/windows/desktop/ad0ead4e-9f8e-4935-b220-306d665e50f4) interfaces.
7.  Connect the source filter and the wrapper filter by calling the [**Connect**](https://msdn.microsoft.com/windows/desktop/8ddcbb73-8220-4d70-9ab3-58d99fa8a958) method of your [**IGraphBuilder**](https://msdn.microsoft.com/windows/desktop/54ed8ac8-4821-4c0c-9fb9-789c70dbca37) interface.
8.  Complete the graph by calling the [**Render**](https://msdn.microsoft.com/windows/desktop/de3adac7-ff99-4415-9afc-e25ad420df59) method of your [**IGraphBuilder**](https://msdn.microsoft.com/windows/desktop/54ed8ac8-4821-4c0c-9fb9-789c70dbca37) interface.
9.  Run the graph ([**IMediaControl::Run**](https://msdn.microsoft.com/windows/desktop/b52a5fa7-96f8-4949-9cf0-2d526f23bee1)), and wait for it to complete ([**IMediaEvent::WaitForCompletion**](https://msdn.microsoft.com/windows/desktop/760a90fe-7cbc-4f09-ba64-afe0ab0b4c74)).
10. Obtain an [**IPropertyStore**](https://www.bing.com/search?q=**IPropertyStore**) interface on your DMO filter wrapper, and get the value of the [**MFPKEY\_TOCGENERATOR\_TOCREADY**](/windows/desktop/api/wmcodecdsp/) property. Repeat if necessary until the table of contents is ready.
11. Use your [**IPropertyStore**](https://www.bing.com/search?q=**IPropertyStore**) interface to get the value of the [**MFPKEY\_TOCGENERATOR\_TOCOBJECT**](/windows/desktop/api/wmcodecdsp/) property. This property is an [**IToc**](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-itoc) interface that represents the automatically generated table of contents.

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
         IID_IGraphBuilder, (VOID**)&amp;pBuilder);

      if(SUCCEEDED(hr))
      {
         IDMOWrapperFilter* pWrap = NULL;
         hr = CoCreateInstance(CLSID_DMOWrapperFilter, NULL, CLSCTX_INPROC, 
            IID_IDMOWrapperFilter, (VOID**)&amp;pWrap);

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
                     hr = GetToc(pWrap, &amp;pToc);

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

 

 



