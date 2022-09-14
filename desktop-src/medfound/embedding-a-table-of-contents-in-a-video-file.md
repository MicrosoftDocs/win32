---
description: Embedding a Table of Contents in a Video File
ms.assetid: 1546388a-7868-4411-be20-34d28becbe76
title: Embedding a Table of Contents in a Video File
ms.topic: article
ms.date: 05/31/2018
---

# Embedding a Table of Contents in a Video File

This topic demonstrates how to create a table of contents (TOC) and embed it in a video file. To keep the example code short, the table of contents is very simple; it contains only one entry, and the entry is populated with a minimum of information.

To create a table of contents and embed it in a file, you must create the following four objects by calling **CoCreateInstance**.

-   TOC Entry
-   TOC Entry List
-   TOC
-   TOC Parser

Class identifiers for the objects are given in [Class Identifiers for Table of Contents Parser](class-identifiers-for-toc-parser.md).

First populate the TOC entry with information that describes one portion of the video file. Add the TOC entry to the TOC entry list, and then add the TOC entry list to the TOC. Finally, add the TOC to the TOC parser, which provides the functionality for embedding the TOC in the video file. The following list gives the steps in more detail.

1.  Create a TOC Entry object and obtain an [**ITocEntry**](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-itocentry) interface on it.
2.  Populate a [**TOC\_ENTRY\_DESCRIPTOR**](/windows/desktop/api/wmcodecdsp/ns-wmcodecdsp-toc_entry_descriptor) structure and pass it to [**ITocEntry::SetDescriptor**](/windows/desktop/api/wmcodecdsp/nf-wmcodecdsp-itocentry-setdescriptor).
3.  Create a TOC Entry List object and obtain an [**ITocEntryList**](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-itocentrylist) interface on it.
4.  Add the TOC Entry object you created in step 1 to the TOC Entry List object by calling [**ITocEntryList::AddEntryByIndex**](/windows/desktop/api/wmcodecdsp/nf-wmcodecdsp-itocentrylist-addentrybyindex).
5.  Create a TOC object and obtain an [**IToc**](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-itoc) interface on it.
6.  Add the TOC Entry List object you created in step 3 to the TOC object by calling [**IToc::AddEntryListByIndex**](/windows/desktop/api/wmcodecdsp/nf-wmcodecdsp-itoc-addentrylistbyindex).
7.  Create a TOC Parser object and obtain an [**ITocParser**](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-itocparser) interface on it.
8.  Call [**ITocParser::Init**](/windows/desktop/api/wmcodecdsp/nf-wmcodecdsp-itocparser-init) to initialize the TOC Parser object and associate it with a video file.
9.  Add the TOC object you created in step 5 to the TOC Parser object by calling [**ITocParser::AddToc**](/windows/desktop/api/wmcodecdsp/nf-wmcodecdsp-itocparser-addtoc).
10. Embed the table of contents in the video file by calling [**ITocParser::Commit**](/windows/desktop/api/wmcodecdsp/nf-wmcodecdsp-itocparser-commit).

The following code demonstrates the steps given in the preceding list.


```C++
#include <wmcodecdsp.h>
HRESULT InitTocParserAndCommit(IToc* pToc);

void main()
{
   HRESULT hr = CoInitialize(NULL);
   
   if(SUCCEEDED(hr))
   {    
      ITocEntry* pEntry = NULL;
      hr = CoCreateInstance(CLSID_CTocEntry, NULL, 
         CLSCTX_INPROC_SERVER, IID_ITocEntry, (VOID**)&pEntry); 

      if(SUCCEEDED(hr))
      {
         TOC_ENTRY_DESCRIPTOR tocDesc = {0};
         tocDesc.qwStartTime = 4; 
         tocDesc.qwEndTime = 8;
         pEntry->SetDescriptor(&tocDesc); // HRESULT ignored for simplicity.    
    
         ITocEntryList* pEntryList = NULL;
         hr = CoCreateInstance(CLSID_CTocEntryList, NULL, 
            CLSCTX_INPROC_SERVER, IID_ITocEntryList, (VOID**)&pEntryList);

         if(SUCCEEDED(hr))
         {
            pEntryList->AddEntryByIndex(0, pEntry); // HRESULT ignored.
      
            IToc* pToc = NULL;
            hr = CoCreateInstance(CLSID_CToc, NULL, 
               CLSCTX_INPROC_SERVER, IID_IToc, (VOID**)&pToc);

            if(SUCCEEDED(hr))
            {
               pToc->AddEntryListByIndex(0, pEntryList); // HRESULT ignored.
               hr = InitTocParserAndCommit(pToc);
            }
         }
      }
     
      CoUninitialize();
   }
}

HRESULT InitTocParserAndCommit(IToc* pToc)
{
   ITocParser* pTocParser = NULL;
   HRESULT hr = CoCreateInstance(CLSID_CTocParser, NULL, 
      CLSCTX_INPROC_SERVER, IID_ITocParser, (VOID**)&pTocParser);

   if(SUCCEEDED(hr))
   {
      hr = pTocParser->Init(L"\\\\?\\c:\\experiment\\seattle.wmv");

      if(SUCCEEDED(hr))
      {
         DWORD tocIndex = 0;
         hr = pTocParser->AddToc(TOC_POS_TOPLEVELOBJECT, pToc, &tocIndex);

         if(SUCCEEDED(hr))
         {
            hr = pTocParser->Commit();
         }
      }

      pTocParser->Release();
      pTocParser = NULL;
   }

   return hr;
}
```



## Related topics

<dl> <dt>

[Reading a Table of Contents From a Video File](reading-a-table-of-contents-from-a-video-file.md)
</dt> <dt>

[Table of Contents Parser Objects](toc-parser-objects.md)
</dt> <dt>

[Table of Contents Parser Programming Guide](toc-parser-programming-guide.md)
</dt> </dl>

 

 



