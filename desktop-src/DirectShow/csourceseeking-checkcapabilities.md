---
Description: The CheckCapabilities method queries whether the stream has specified seeking capabilities. This method implements the IMediaSeeking::CheckCapabilities method.
ms.assetid: 5d37e179-9e04-44e1-acbc-dfd2682830c0
title: CSourceSeeking.CheckCapabilities method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CSourceSeeking.CheckCapabilities method

The `CheckCapabilities` method queries whether the stream has specified seeking capabilities. This method implements the [**IMediaSeeking::CheckCapabilities**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-checkcapabilities) method.

## Syntax


```C++
HRESULT CheckCapabilities(
   DWORD *pCapabilities
);
```



## Parameters

<dl> <dt>

*pCapabilities* 
</dt> <dd>

Pointer to a bitwise combination of one or more [**AM\_SEEKING\_SEEKING\_CAPABILITIES**](/windows/desktop/api/strmif/ne-strmif-am_seeking_seekingcapabilities) attributes.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values listed in the following table.



| Return code                                                                               | Description                                                            |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>   | Not all of the capabilities in *pCapabilities* are present.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | All capabilities in *pCapabilities* are present.<br/>            |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/>                                  |



 

## Remarks

As implemented, this method checks the value of *\*pCapabilities* against the [**CSourceSeeking::m\_dwSeekingCaps**](csourceseeking-m-dwseekingcaps.md) member variable. However, it does not set *\*pCapabilities* equal to **m\_dwSeekingCaps**, as described for the [**IMediaSeeking::CheckCapabilities**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-checkcapabilities) method. Also, in the case where none of the specified capabilities are available, the method does not return E\_FAIL. A more complete implementation would be as follows:


```C++
STDMETHODIMP CheckCapabilities(DWORD *pCapabilities)
{
    CheckPointer(pCapabilities, E_POINTER)
;
    DWORD dwCaps;
    HRESULT hr = GetCapabilities(&amp;dwCaps);
    if (SUCCEEDED(hr))
    {
        dwCaps &amp;= *pCapabilities;
        if (dwCaps)
        {
            hr =  (dwCaps == *pCapabilities ? S_OK : S_FALSE );
        }
        else 
        {
            hr = E_FAIL;
        }
        *pCapabilities = dwCaps;
    }
    else 
    {
        *pCapabilities = 0;
    }
    return hr;
}
```



## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




