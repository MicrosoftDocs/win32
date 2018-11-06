---
title: IPaper Load
description: The following C++ sample code shows how to open the existing stream in the storage, read new paper properties in and then set them as the current values for COPaper.
ms.assetid: a1559d97-387f-4d1a-8a9d-fa5c27abd545
keywords:
- IPaper Load
ms.topic: article
ms.date: 05/31/2018
---

# IPaper::Load

The following C++ sample code shows how to open the existing stream in the storage, read new paper properties in and then set them as the current values for COPaper.

The following is the **IPaper::Load** method from Paper.cpp.


```
STDMETHODIMP COPaper::CImpIPaper::Load(
                 SHORT nLockKey,
                 IStorage* pIStorage)
  {
    HRESULT hr = E_FAIL;
    IStream* pIStream;
    INKDATA* paInkData;
    ULONG ulToRead, ulReadIn;
    LONG lNewArraySize;
    PAPER_PROPERTIES NewProps;

    if (OwnThis())
    {
      if (m_bLocked && m_cLockKey == nLockKey && NULL != pIStorage)
      {
       // Open the "PAPERDATA" stream where the paper data is stored.
        hr = pIStorage->OpenStream(
               STREAM_PAPERDATA_USTR,
               0,
               STGM_READ | STGM_DIRECT | STGM_SHARE_EXCLUSIVE,
               0,
               &pIStream);
        if (SUCCEEDED(hr))
        {
          // Obtained paper data stream. Read the Paper Properties.
          ulToRead = sizeof(PAPER_PROPERTIES);
          hr = pIStream->Read(
                           &NewProps,
                           ulToRead,
                           &ulReadIn);
          if (SUCCEEDED(hr) && ulToRead != ulReadIn)
            hr = E_FAIL;
          if (SUCCEEDED(hr))
          {
            // Handle the different versions of ink data format.
            switch (NewProps.lInkDataVersion)
            {
              case INKDATA_VERSION10:
                // Allocate an ample-sized ink data array.
                lNewArraySize = NewProps.lInkArraySize + 
                                               INKDATA_ALLOC;
                paInkData = new INKDATA[(LONG) lNewArraySize];
                if (NULL != paInkData)
                {
                  // Delete the old ink data array.
                  delete [] m_paInkData;

                  // Assign the new array.
                  m_paInkData = paInkData;
                  m_lInkDataMax = lNewArraySize;

                  // Read the complete array of Ink Data.
                  ulToRead = NewProps.lInkArraySize * sizeof(INKDATA);
                  hr = pIStream->Read(m_paInkData, 
                                      ulToRead, &ulReadIn);
                  if (SUCCEEDED(hr) && ulToRead != ulReadIn)
                    hr = E_FAIL;
                  if (SUCCEEDED(hr))
                  {
                    // Set COPaper to use the new PAPER_PROPERTIES
                    // data.
                    m_lInkDataEnd = NewProps.lInkArraySize-1;
                    m_crWinColor = NewProps.crWinColor;
                    m_WinRect.right = NewProps.WinRect.right;
                    m_WinRect.bottom = NewProps.WinRect.bottom;

                    // Copy the new properties into current 
                    // properties.
                    memcpy(
                      &m_PaperProperties,
                      &NewProps,
                      sizeof(PAPER_PROPERTIES));
                  }
                }
                else
                  hr = E_OUTOFMEMORY;
                break;
              default:
                hr = E_FAIL;  // Bad version.
                break;
            }
          }

          // Release the stream.
          pIStream->Release();
        }
      }

      UnOwnThis();
    }

    // Notify other connected clients that Paper is now loaded.
    // If Paper not loaded, then erase to a safe, empty ink data 
    // array.
    if (SUCCEEDED(hr))
      m_pBackObj->NotifySinks(PAPER_EVENT_LOADED, 0, 0, 0, 0);
    else
      Erase(nLockKey);

    return hr;
  }
```



Now, the [**IStorage::OpenStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstream) method is called to open the existing stream in the storage called "PAPERDATA". Access mode flags are for read-only, direct, and non-shared exclusive access. When the stream is open, the [**IStream::Read**](/windows/desktop/api/Objidl/nn-objidl-istream) method is called to read the PAPER\_PROPERTIES structure. If the amount actually read does not equal the amount requested, the load operation is aborted, and E\_FAIL is returned. If the format version in the newly read PAPER\_PROPERTIES is not recognized, then the load operation is aborted and **Load** returns E\_FAIL.

With a valid ink data format version, the size of the new ink data array from the PAPER\_PROPERTIES that was read in is used to allocate a new ink data array of the required size. The existing ink data is deleted, and its data is lost. If this data was valuable, it should have been saved before **Load** was called. After the new array is allocated, [**IStream::Read**](/windows/desktop/api/Objidl/nn-objidl-istream) is called again to read the data into the array from the stream. If this call succeeds, the values in the newly read paper properties are adopted as the current values for COPaper.

During this load operation, a temporary PAPER\_PROPERTIES structure, NewProps, was used to hold the new properties read in. If all succeeds with the load, NewProps is copied into the PAPER\_PROPERTIES structure, m\_PaperProperties. As before, after Load is done and the [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) is no longer required, the **IStream** pointer is released.

If there is an error at the end of **Load**, the ink data array is erased, because it may contain damaged data.

If there is no error at the end of **Load**, the client [**IPaperSink::Loaded**](ipapersink-methods.md) method is called, in the COPaper internal NotifySinks method, to notify the client that the load operation is completed. This is an important notification for the client, because it must display this new loaded ink data. This notification makes significant use of connectable object features in COPaper.

 

 




