---
Description: Reading a Table of Contents from a Video File
ms.assetid: '10c4f4ca-cb30-453c-b18d-0470bfecc14e'
title: Reading a Table of Contents from a Video File
---

# Reading a Table of Contents from a Video File

This topic demonstrates how to read a table of contents that has already been embedded in a video file.

Start by calling [**CoCreateInstance**](com.cocreateinstance) to create a TOC Parser object and obtain an [**ITocParser**](itocparser.md) interface. Then obtain the following interfaces by calling methods.

-   [**IToc**](itoc.md)
-   [**ITocEntryList**](itocentrylist.md)
-   [**ITocEntry**](itocentry.md)

Use the methods of [**ITocEntry**](itocentry.md) to inspect an individual entry in the table of contents. For example, you can inspect the title, the start time, and the end time of the entry.

The following list gives the steps in more detail.

1.  Call [**CoCreateInstance**](com.cocreateinstance) to create a TOC Parser object and obtain an [**ITocParser**](itocparser.md) interface on it.
2.  Call [**ITocParser::Init**](itocparser-init.md) to initialize the TOC parser and associate it with a video file.
3.  Obtain an [**IToc**](itoc.md) interface by calling [**ITocParser::GetTocByIndex**](itocparser-gettocbyindex.md).
4.  Obtain an [**ITocEntryList**](itocentrylist.md) interface by calling [**IToc::GetEntryListByIndex**](itoc-getentrylistbyindex.md).
5.  Obtain an [**ITocEntry**](itocentry.md) interface by calling [**ITocEntryList::GetEntryByIndex**](itocentrylist-getentrybyindex.md).
6.  Allocate a [**TOC\_ENTRY\_DESCRIPTOR**](toc-entry-descriptor.md) structure.
7.  Populate the [**TOC\_ENTRY\_DESCRIPTOR**](toc-entry-descriptor.md) structure by calling [**ITocEntry::GetDescriptor**](itocentry-getdescriptor.md).

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

 

 



