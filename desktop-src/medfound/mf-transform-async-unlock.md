---
description: Enables the use of an asynchronous Media Foundation transform (MFT).
ms.assetid: e12ab57e-ebc2-46af-afdf-d78d4db16fcf
title: MF_TRANSFORM_ASYNC_UNLOCK attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TRANSFORM\_ASYNC\_UNLOCK attribute

Enables the use of an asynchronous Media Foundation transform (MFT).

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

Asynchronous MFTs are not compatible with earlier versions of Microsoft Media Foundation. To prevent existing applications from accidentally using an asynchronous MFT, this attribute must be set to a nonzero value before an asynchronous MFT can be used. The Media Foundation pipeline automatically sets the attribute, so that most applications do not need to use this attribute. However, if an application uses an asynchronous MFT outside of the Media Foundation pipeline, the application must set this attribute.

Synchronous MFTs do not require this attribute.

To test whether an MFT is asynchronous, get the value of the [MF\_TRANSFORM\_ASYNC](mf-transform-async.md) attribute on the MFT.

## Examples

The following code unlocks an asynchronous MFT.


```C++
HRESULT UnlockAsyncMFT(IMFTransform *pMFT)
{
    IMFAttributes *pAttributes = NULL;

    HRESULT hr = hr = pMFT->GetAttributes(&pAttributes);

    if (SUCCEEDED(hr))
    {
        hr = pAttributes->SetUINT32(MF_TRANSFORM_ASYNC_UNLOCK, TRUE);
        pAttributes->Release();
    }
    
    return hr;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Asynchronous MFTs](asynchronous-mfts.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




