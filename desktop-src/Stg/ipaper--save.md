---
title: IPaper Save
description: The principal focus in this sample code is how COPaper can load and save its paper data in compound files. The IPaper, Load, and Save method implementations are discussed in detail.
ms.assetid: 62154658-ff47-425f-94da-ee2806de5318
ms.topic: article
ms.date: 05/31/2018
---

# IPaper::Save

The principal focus in this sample code is how COPaper can load and save its paper data in compound files. The [**IPaper**](ipaper-methods.md), [**Load**](ipaper--load.md), and **Save** method implementations are discussed in detail.

The following is the **IPaper::Save** method from Paper.cpp.


```C++
STDMETHODIMP COPaper::CImpIPaper::Save(
                 SHORT nLockKey,
                 IStorage* pIStorage)
  {
    HRESULT hr = E_FAIL;
    IStream* pIStream;
    ULONG ulToWrite, ulWritten;

    if (OwnThis())
    {
      if (m_bLocked && m_cLockKey == nLockKey && NULL != pIStorage)
      {
        // Use the COM service to mark this compound file as one 
        // that is handled by our server component, DllPaper.
        WriteClassStg(pIStorage, CLSID_DllPaper);

        // Use the COM Service to write user-readable clipboard 
        // format into the compound file.
        WriteFmtUserTypeStg(pIStorage, m_ClipBdFmt, 
                            TEXT(CLIPBDFMT_STR));

        // Create the stream to be used for the actual paper data.
        // Call it "PAPERDATA".
        hr = pIStorage->CreateStream(
               STREAM_PAPERDATA_USTR,
        STGM_CREATE | STGM_WRITE | STGM_DIRECT | STGM_SHARE_EXCLUSIVE,
               0,
               0,
               &pIStream);
        if (SUCCEEDED(hr))
        {
          // Obtained a stream. Write data to it.
          // First, write PAPER_PROPERTIES structure.
          m_PaperProperties.lInkArraySize = m_lInkDataEnd+1;
          m_PaperProperties.crWinColor = m_crWinColor;
          m_PaperProperties.WinRect.right = m_WinRect.right;
          m_PaperProperties.WinRect.bottom = m_WinRect.bottom;
          ulToWrite = sizeof(PAPER_PROPERTIES);
          hr = pIStream->Write(&m_Paper_Properties, ulToWrite, 
                               &ulWritten);
          if (SUCCEEDED(hr) && ulToWrite != ulWritten)
            hr = STG_E_CANTSAVE;
          if (SUCCEEDED(hr))
          {
            // Now, write the complete array of Ink Data.
            ulToWrite = m_PaperProperties.lInkArraySize * 
                                                     sizeof(INKDATA);
            hr = pIStream->Write(m_paInkData, ulToWrite, &ulWritten);
            if (SUCCEEDED(hr) && ulToWrite != ulWritten)
              hr = STG_E_CANTSAVE;
          }

          // Release the stream.
          pIStream->Release();
        }
      }

      UnOwnThis();
    }

    // Notify all other connected clients that Paper is now saved.
    if (SUCCEEDED(hr))
      m_pBackObj->NotifySinks(PAPER_EVENT_SAVED, 0, 0, 0, 0);

    return hr;
  }
```



In this client and server relationship, COPaper does not create the compound file used to store paper data. For both the **Save** and [**Load**](ipaper--load.md) methods, the client passes an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface pointer for an existing compound file. It then uses the **IStorage** to write and read data in that compound file. In **IPaper::Save** above, several types of data are stored.

The CLSID for DllPaper, CLSID\_DllPaper, is serialized and stored in a special COM-controlled stream within the storage object called "\\001CompObj". The [**WriteClassStg**](/windows/desktop/api/coml2api/nf-coml2api-writeclassstg) service function performs this storage. This stored CLSID data can be used to associate the storage content with the DllPaper component that created and can interpret it. In this sample, the root storage is passed by **StoClien**, and thus the entire compound file is associated with the DllPaper component. This CLSID data can be retrieved later with a call to the [**ReadClassStg**](/windows/desktop/api/coml2api/nf-coml2api-readclassstg) service function.

Because DllPaper deals with editable data, it is also appropriate to record a clipboard format in the storage. The [**WriteFmtUserTypeStg**](/windows/desktop/api/Ole2/nf-ole2-writefmtusertypestg) service function is called to store both a clipboard format designation and a user-readable name for the format. The user-readable name is meant for GUI display in selection lists. The name passed above uses a macro, CLIPBDFMT\_STR, which is defined as "DllPaper 1.0" in Paper.h. This stored clipboard data can be retrieved later with a call to the service function [**ReadFmtUserTypeStg**](/windows/desktop/api/Ole2/nf-ole2-readfmtusertypestg). This function returns a string value that is allocated using the task memory allocator. The caller is responsible for freeing the string.

**Save** next creates a stream in the storage for the COPaper paper data. The stream is called "PAPERDATA" and is passed using the STREAM\_PAPERDATA\_USTR macro. The [**IStorage::CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream) method requires that this string be in Unicode. Because the string is fixed at compile time, the macro is defined as Unicode in Paper.h.

``` syntax
#define STREAM_PAPERDATA_USTR L"PAPERDATA"
```

The 'L' before the string, indicating LONG, achieves this.

The [**CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream) method creates and opens a stream within the specified storage. An [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) interface pointer for the new stream is passed in a caller interface pointer variable. AddRef is called on this interface pointer within **CreateStream**, and the caller must release this pointer after using it. The **CreateStream** method is passed numerous access mode flags, as follows.

STGM\_CREATE \| STGM\_WRITE \| STGM\_DIRECT \| STGM\_SHARE\_EXCLUSIVE

[**STGM\_CREATE**](stgm-constants.md) creates a new stream or overwrites an existing one of the same name. [**STGM\_WRITE**](stgm-constants.md) opens the stream with write permission. [**STGM\_DIRECT**](stgm-constants.md) opens the stream for direct access, as opposed to transacted access. [**STGM\_SHARE\_EXCLUSIVE**](stgm-constants.md) opens the file for exclusive, non-shared use by the caller.

After the PAPERDATA stream is successfully created, the [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) interface is used to write into the stream. The **IStream::Write** method is used to first store the content of the PAPER\_PROPERTIES structure. This is essentially a properties header at the front of the stream. Because the version number is the first thing in the file, it can be read independently to determine how to deal with the data that follows. If the amount of data actually written does not equal the amount requested, the Save method is aborted, and it returns STG\_E\_CANTSAVE.

Saving the entire array of ink data into the stream is simple.


```C++
// Now write the complete array of Ink Data.
  ulToWrite = m_PaperProperties.lInkArraySize * sizeof(INKDATA);
  hr = pIStream->Write(m_paInkData, ulToWrite, &ulWritten);
  if (SUCCEEDED(hr) && ulToWrite != ulWritten)
    hr = STG_E_CANTSAVE;
```



Because the [**IStream::Write**](/windows/desktop/api/Objidl/nn-objidl-istream) method operates on a byte array, the number of bytes of stored ink data in the array is calculated and the write operation begins at the start of the array. If the amount of data actually written does not equal the amount requested, the **Save** method returns STG\_E\_CANTSAVE.

After the stream is written, the **IPaper::Save** method releases the [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) pointer it was using.

The **Save** method also calls the client [**IPaperSink**](ipapersink-methods.md) (in the COPaper internal NotifySinks method) to notify the client that the save operation is complete. At this point the **Save** method returns to the calling client, which will typically release the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) pointer.

 

 




