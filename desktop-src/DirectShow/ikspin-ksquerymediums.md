---
description: The KsQueryMediums method retrieves the mediums supported by a pin.
ms.assetid: 554bf968-6054-4f9d-95db-facf0444641f
title: IKsPin::KsQueryMediums method (Ksproxy.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IKsPin.KsQueryMediums
api_type: 
- COM
api_location: 
- Strmiids.lib
- Strmiids.dll
ms.custom: UpdateFrequency5
---

# IKsPin::KsQueryMediums method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `KsQueryMediums` method retrieves the mediums supported by a pin.

## Syntax


```C++
HRESULT KsQueryMediums(
  [out] KSMULTIPLE_ITEM **ppmi
);
```



## Parameters

<dl> <dt>

*ppmi* \[out\]
</dt> <dd>

Address of a pointer to a [**KSMULTIPLE\_ITEM**](ksmultiple-item.md) structure.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## Remarks

This method returns a task-allocated [**KSMULTIPLE\_ITEM**](ksmultiple-item.md) structure, which is followed by zero or more [**REGPINMEDIUM**](/windows/desktop/api/strmif/ns-strmif-regpinmedium) structures. The **Count** member of the **KSMULTIPLE\_ITEM** structure specifies the number of **REGPINMEDIUM** structures. Each **REGPINMEDIUM** structure defines a medium supported by the pin.

The caller must free the returned structures, using the **CoTaskMemFree** function.

You must include Ks.h before Ksproxy.h.

## Examples

The following helper function attempts to match a pin against a specified medium.


```C++
HRESULT FindMatchingMedium(
    IPin *pPin, 
    REGPINMEDIUM *pMedium, 
    bool *pfMatch)
{
    IKsPin* pKsPin = NULL;
    KSMULTIPLE_ITEM *pmi;

    *pfMatch = false;
    HRESULT hr = pPin->QueryInterface(IID_IKsPin, (void **)&pKsPin);
    if (FAILED(hr)) 
        return hr;  // Pin does not support IKsPin.

    hr = pKsPin->KsQueryMediums(&pmi);
    pKsPin->Release();
    if (FAILED(hr))
        return hr;  // Pin does not support mediums.

    if (pmi->Count) 
    {
        // Use pointer arithmetic to reference the first medium structure.
        REGPINMEDIUM *pTemp = (REGPINMEDIUM*)(pmi + 1);
        for (ULONG i = 0; i < pmi->Count; i++, pTemp++) 
        {
            if (pMedium->clsMedium == pTemp->clsMedium) 
            {
                *pfMatch = true;
                break;
            }
        }
    }        
    CoTaskMemFree(pmi);
    return S_OK;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Ksproxy.h</dt> </dl>    |
| Library<br/>                  | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**IKsPin Interface**](ikspin.md)
</dt> <dt>

[WDM Class Driver Filters](wdm-class-driver-filters.md)
</dt> </dl>

 

 




