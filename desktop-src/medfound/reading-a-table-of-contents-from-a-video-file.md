---
Description: Reading a Table of Contents from a Video File
ms.assetid: 10c4f4ca-cb30-453c-b18d-0470bfecc14e
title: Reading a Table of Contents from a Video File
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reading a Table of Contents from a Video File

This topic demonstrates how to read a table of contents that has already been embedded in a video file.

Start by calling [**CoCreateInstance**](com.cocreateinstance) to create a TOC Parser object and obtain an [**ITocParser**](/windows/win32/wmcodecdsp/nn-wmcodecdsp-itocparser?branch=master) interface. Then obtain the following interfaces by calling methods.

-   [**IToc**](/windows/win32/wmcodecdsp/nn-wmcodecdsp-itoc?branch=master)
-   [**ITocEntryList**](/windows/win32/wmcodecdsp/nn-wmcodecdsp-itocentrylist?branch=master)
-   [**ITocEntry**](/windows/win32/wmcodecdsp/nn-wmcodecdsp-itocentry?branch=master)

Use the methods of [**ITocEntry**](/windows/win32/wmcodecdsp/nn-wmcodecdsp-itocentry?branch=master) to inspect an individual entry in the table of contents. For example, you can inspect the title, the start time, and the end time of the entry.

The following list gives the steps in more detail.

1.  Call [**CoCreateInstance**](com.cocreateinstance) to create a TOC Parser object and obtain an [**ITocParser**](/windows/win32/wmcodecdsp/nn-wmcodecdsp-itocparser?branch=master) interface on it.
2.  Call [**ITocParser::Init**](/windows/win32/wmcodecdsp/nf-wmcodecdsp-itocparser-init?branch=master) to initialize the TOC parser and associate it with a video file.
3.  Obtain an [**IToc**](/windows/win32/wmcodecdsp/nn-wmcodecdsp-itoc?branch=master) interface by calling [**ITocParser::GetTocByIndex**](/windows/win32/wmcodecdsp/nf-wmcodecdsp-itocparser-gettocbyindex?branch=master).
4.  Obtain an [**ITocEntryList**](/windows/win32/wmcodecdsp/nn-wmcodecdsp-itocentrylist?branch=master) interface by calling [**IToc::GetEntryListByIndex**](/windows/win32/wmcodecdsp/nf-wmcodecdsp-itoc-getentrylistbyindex?branch=master).
5.  Obtain an [**ITocEntry**](/windows/win32/wmcodecdsp/nn-wmcodecdsp-itocentry?branch=master) interface by calling [**ITocEntryList::GetEntryByIndex**](/windows/win32/wmcodecdsp/nf-wmcodecdsp-itocentrylist-getentrybyindex?branch=master).
6.  Allocate a [**TOC\_ENTRY\_DESCRIPTOR**](/windows/win32/wmcodecdsp/ns-wmcodecdsp-_toc_entry_descriptor?branch=master) structure.
7.  Populate the [**TOC\_ENTRY\_DESCRIPTOR**](/windows/win32/wmcodecdsp/ns-wmcodecdsp-_toc_entry_descriptor?branch=master) structure by calling [**ITocEntry::GetDescriptor**](/windows/win32/wmcodecdsp/nf-wmcodecdsp-itocentry-getdescriptor?branch=master).

The following code demonstrates the steps in the preceding list.


```C++
#include <stdio.h>
#include <wmcodecdsp.h>

HRESULT ShowEntryInfo(ITocEntry* pEntry);

void main()
{
   HRESULT hr = CoInitialize(NULL);
   
   if(SUCCEEDED(hr))
   {    
      ITocParser* pTocParser = NULL;

      hr = CoCreateInstance(CLSID_CTocParser, NULL, CLSCTX_INPROC_SERVER, 
         IID_ITocParser, (VOID**)&amp;pTocParser);  
      
      if(SUCCEEDED(hr))
      {  
         hr = pTocParser->Init(L"\\\\?\\c:\\experiment\\seattle.wmv");

         if(SUCCEEDED(hr))
         {
            IToc* pToc = NULL;
            hr = pTocParser->GetTocByIndex(TOC_POS_TOPLEVELOBJECT, 0, &amp;pToc);

            if(SUCCEEDED(hr))
            {
               ITocEntryList* pEntryList = NULL;
               hr = pToc->GetEntryListByIndex(0, &amp;pEntryList);

               if(SUCCEEDED(hr))
               {
                  ITocEntry* pEntry = NULL;
                  hr = pEntryList->GetEntryByIndex(0, &amp;pEntry);

                  if(SUCCEEDED(hr))
                  {
                     hr = ShowEntryInfo(pEntry);
                     pEntry->Release();
                     pEntry = NULL;
                  }

                  pEntryList->Release();
                  pEntryList = NULL;
               }

               pToc->Release();
               pToc = NULL;
            }
         }

         pTocParser->Release();
         pTocParser = NULL;  
      }
                   
      CoUninitialize();
   }
}

HRESULT ShowEntryInfo(ITocEntry* pEntry)
{
   HRESULT hr = E_FAIL;

   TOC_ENTRY_DESCRIPTOR entryDesc = {0};
   hr = pEntry->GetDescriptor(&amp;entryDesc);

   if(SUCCEEDED(hr))
   {
      printf_s("qwStartTime: %x\n", entryDesc.qwStartTime);
      printf_s("qwEndTime: %x\n", entryDesc.qwEndTime);
      printf_s("qwStartStartPacketOffset: %x\n", entryDesc.qwStartPacketOffset);
      printf_s("qwEndPacketOffset: %x\n", entryDesc.qwEndPacketOffset);
      printf_s("qwRepresentativeFrameTime: %x\n", entryDesc.qwRepresentativeFrameTime);
   }

   return hr;
}
```



## Related topics

<dl> <dt>

[Embedding a Table of Contents in a Video File](embedding-a-table-of-contents-in-a-video-file.md)
</dt> <dt>

[Table of Contents Parser Objects](toc-parser-objects.md)
</dt> <dt>

[Table of Contents Parser Programming Guide](toc-parser-programming-guide.md)
</dt> </dl>

 

 



