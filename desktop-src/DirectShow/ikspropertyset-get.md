---
description: The Get method retrieves a property identified by a property set GUID and a property ID.
ms.assetid: f39862db-0659-4533-8cee-aee2f778e085
title: IKsPropertySet::Get method (Ksproxy.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IKsPropertySet.Get
api_type: 
- COM
api_location: 
- Strmiids.lib
- Strmiids.dll
ms.custom: UpdateFrequency5
---

# IKsPropertySet::Get method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Get** method retrieves a property identified by a property set GUID and a property ID.

## Syntax


```C++
HRESULT Get(
  [in]  REFGUID guidPropSet,
  [in]  DWORD   dwPropID,
  [in]  LPVOID  pInstanceData,
  [in]  DWORD   cbInstanceData,
  [out] LPVOID  pPropData,
  [in]  DWORD   cbPropData,
  [out] DWORD   *pcbReturned
);
```



## Parameters

<dl> <dt>

*guidPropSet* \[in\]
</dt> <dd>

The GUID of the property set .

</dd> <dt>

*dwPropID* \[in\]
</dt> <dd>

The identifier of the property within the property set.

</dd> <dt>

*pInstanceData* \[in\]
</dt> <dd>

A pointer to an array of bytes that contains instance data for the property.

</dd> <dt>

*cbInstanceData* \[in\]
</dt> <dd>

The size of the array given in *pInstanceData*, in bytes.

</dd> <dt>

*pPropData* \[out\]
</dt> <dd>

A pointer to an array of bytes that receives the property data.

</dd> <dt>

*cbPropData* \[in\]
</dt> <dd>

The size of the array given in *pPropData*, in bytes.

</dd> <dt>

*pcbReturned* \[out\]
</dt> <dd>

Receives the number of bytes the method copies to the *pPropData* array.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                              | Description                                                                 |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                     | Success.<br/>                                                         |
| <dl> <dt>**E\_PROP\_SET\_UNSUPPORTED**</dt> </dl> | The property set is not supported.<br/>                               |
| <dl> <dt>**E\_PROP\_ID\_UNSUPPORTED**</dt> </dl>  | The property ID is not supported for the specified property set.<br/> |



 

## Remarks

> [!Note]  
> Another interface by this name exists in the dsound.h header file. The two interfaces are not compatible. The [IKsControl](/windows-hardware/drivers/ddi/ksproxy/nn-ksproxy-ikscontrol) interface, documented in the DirectShow DDK, is now the recommended interface for passing property sets between WDM drivers and user mode components.

 

To retrieve a property, allocate a buffer which this method will then fill in. To determine the necessary buffer size, specify **NULL** for *pPropData* and zero (0) for *cbPropData*. This method returns the necessary buffer size in *pcbReturned*.

You must include Ks.h before Ksproxy.h.

## Examples

The following example queries a pin for its pin category, by retrieving the **AMPROPERTY\_PIN\_CATEGORY** property. (See [Pin Property Set](pin-property-set.md).)


```C++
HRESULT GetPinCategory(IPin *pPin, GUID *pPinCategory)
{
    IKsPropertySet *pKs = NULL;

    HRESULT hr = pPin->QueryInterface(IID_PPV_ARGS(&pKs));
    if (FAILED(hr))
    {
        return hr;
    }

    // Try to retrieve the pin category.
    DWORD cbReturned = 0;
    hr = pKs->Get(AMPROPSETID_Pin, AMPROPERTY_PIN_CATEGORY, NULL, 0, 
        pPinCategory, sizeof(GUID), &cbReturned);
    
    // If this succeeded, pPinCategory now contains the category GUID.

    SafeRelease(&pKs);
    return hr;
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

[**IKsPropertySet Interface**](ikspropertyset.md)
</dt> <dt>

[Property Sets](property-sets.md)
</dt> </dl>

 

 
