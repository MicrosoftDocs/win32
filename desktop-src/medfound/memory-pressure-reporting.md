---
description: Memory pressure reporting enables a Direct3D application to determine when its video-memory working set has grown too large.
ms.assetid: 3aa2f81e-81a1-40a3-ad24-72781d36f713
title: Memory Pressure Reporting
ms.topic: article
ms.date: 05/31/2018
---

# Memory Pressure Reporting

Memory pressure reporting enables a Direct3D application to determine when its video-memory working set has grown too large.

*Memory pressure* is the demand placed on the memory subsystem by an application. While any Direct3D application can use memory pressure reporting, this feature is especially useful for applications that render video by using Direct3D. Video playback typically benefits from large amounts of buffering, so that frames can be decoded in advance. While buffering generally results in smoother playback, it can actually degrade performance if the working set grows too large, due to the following factors:

-   Memory might be evicted from the cache. In the worst case, this can occur on every video frame.
-   Memory allocations might be placed in nonoptimal memory segments.

Starting in Windows 7, Direct3D can report some statistics about the video memory pressure:

-   The number of bytes evicted by the process over an interval of time.
-   The amount of memory placed in nonoptimal memory segments.
-   A rough indication of the overall efficiency of the memory allocations placed in nonoptimal memory.

This information can help an application to maintain a reasonable working set.

## Using Memory Pressure Reporting

Memory pressure reporting uses the existing **IDirect3DQuery9** interface to query the device. A new query type has been added to the **D3DQUERYTYPE** enumeration.


```C++
D3DQUERYTYPE_MEMORYPRESSURE        = 19,
```



To use this query, perform the following steps:

1.  Call **IDirect3DDevice9Ex::CreateQuery** with the **D3DQUERYTYPE\_MEMORYPRESSURE** flag. This method returns a pointer to the **IDirect3DQuery9** interface.
2.  Call **IDirect3DQuery9::Issue** with the **D3DISSUE\_BEGIN** flag to begin the measurement interval.
3.  Call **IDirect3DQuery9::Issue** with the **D3DISSUE\_END** flag.
4.  Call **IDirect3DQuery9::GetData** to get the query result. The query returns a [**D3DMEMORYPRESSURE**](d3dmemorypressure.md) structure.

## Example Code

The following example shows two functions that measure memory pressure. The first begins the measurement interval, and the second retrieves the results of the measurement.


```C++
HRESULT BeginMemoryPressureQuery(
    IDirect3DDevice9Ex *pDevice, 
    IDirect3DQuery9 **ppQuery
    )
{
    HRESULT hr = pDevice->CreateQuery(D3DQUERYTYPE_MEMORYPRESSURE, ppQuery);

    if (SUCCEEDED(hr))
    {
        hr = (*ppQuery)->Issue(D3DISSUE_BEGIN);
        if (FAILED(hr))
        {
            (*ppQuery)->Release();
            *ppQuery = NULL;
        }
    }
    return hr;
}

HRESULT EndMemoryPressureQuery(
    IDirect3DQuery9 *pQuery, 
    D3DMEMORYPRESSURE *pResult
    )
{
    HRESULT hr = pQuery->Issue(D3DISSUE_END);
    if (SUCCEEDED(hr))
    {
        hr = pQuery->GetData(pResult, sizeof(*pResult), D3DGETDATA_FLUSH);
    }
    return hr;
}
```



## Related topics

<dl> <dt>

[Direct3D Video APIs](direct3d-video-apis.md)
</dt> </dl>

 

 



