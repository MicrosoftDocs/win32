---
description: Loading a GraphEdit File Programmatically
ms.assetid: 0e1cff4e-43f8-4d0a-b7a7-b6d0278e9e4a
title: Loading a GraphEdit File Programmatically
ms.topic: article
ms.date: 05/31/2018
---

# Loading a GraphEdit File Programmatically

An application can use the **IPersistStream** interface to load a GraphEdit (.grf) file. Use the following code:


```C++
HRESULT LoadGraphFile(IGraphBuilder *pGraph, const WCHAR* wszName)
{
    IStorage *pStorage = 0;
    if (S_OK != StgIsStorageFile(wszName))
    {
        return E_FAIL;
    }
    HRESULT hr = StgOpenStorage(wszName, 0, 
        STGM_TRANSACTED | STGM_READ | STGM_SHARE_DENY_WRITE, 
        0, 0, &pStorage);
    if (FAILED(hr))
    {
        return hr;
    }
    IPersistStream *pPersistStream = 0;
    hr = pGraph->QueryInterface(IID_IPersistStream,
             reinterpret_cast<void**>(&pPersistStream));
    if (SUCCEEDED(hr))
    {
        IStream *pStream = 0;
        hr = pStorage->OpenStream(L"ActiveMovieGraph", 0, 
            STGM_READ | STGM_SHARE_EXCLUSIVE, 0, &pStream);
        if(SUCCEEDED(hr))
        {
            hr = pPersistStream->Load(pStream);
            pStream->Release();
        }
        pPersistStream->Release();
    }
    pStorage->Release();
    return hr;
}

```



> [!Note]  
> The call to **IPersistStream::Load** in the previous code example can return a DirectShow error or success code. For a list of possible return values, see [Error and Success Codes](error-and-success-codes.md).

 

GraphEdit files are intended only for testing and debugging. They are not meant for use by end-user applications.

## Related topics

<dl> <dt>

[Simulating Graph Building with GraphEdit](simulating-graph-building-with-graphedit.md)
</dt> <dt>

[**StgIsStorageFile**](/windows/win32/api/coml2api/nf-coml2api-stgisstoragefile)
</dt> <dt>

[**StgOpenStorage**](/windows/win32/api/coml2api/nf-coml2api-stgopenstorage)
</dt> </dl>

 

 
