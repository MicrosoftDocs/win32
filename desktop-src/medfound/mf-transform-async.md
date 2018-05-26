---
Description: Specifies whether a Media Foundation transform (MFT) performs asynchronous processing.
ms.assetid: fcc70282-cfac-487c-b9ff-39e62c836f8b
title: MF\_TRANSFORM\_ASYNC attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TRANSFORM\_ASYNC attribute

Specifies whether a Media Foundation transform (MFT) performs asynchronous processing.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Remarks

The attribute is a Boolean value:

-   If the attribute is nonzero, the MFT performs asynchronous processing.
-   If the attribute is 0 or not set, the MFT is synchronous.

To get this attribute, first call [**IMFTransform::GetAttributes**](/windows/win32/mftransform/nf-mftransform-imftransform-getattributes?branch=master) to get the MFT's attribute store. If that method succeeds, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master) to get the attribute value. If either of the two methods fails, the MFT is synchronous.

For asynchronous MFTs, this attribute must be set to a nonzero value. For synchronous MFTs, this attribute is optional, but must be set to 0 if present.

Asynchronous MFTs are not compatible with earlier versions of Media Foundation. To use an asynchronous MFT, the client must set the [**MF\_TRANSFORM\_ASYNC\_UNLOCK**](mf-transform-async-unlock.md) attribute on the MFT. (The Microsoft Media Foundation pipeline performs this step automatically.)

## Examples

The following code tests whether an MFT performs asynchronous processing.


```C++
BOOL IsTransformAsync(IMFTransform *pMFT)
{
    BOOL bAsync = FALSE;
    IMFAttributes *pAttributes = NULL;

    HRESULT hr = pMFT->GetAttributes(&amp;pAttributes);
    if (SUCCEEDED(hr))
    {
        bAsync = MFGetAttributeUINT32(pAttributes, MF_TRANSFORM_ASYNC, FALSE);
        pAttributes->Release();
    }

    return (bAsync != FALSE);
}
```



## Requirements



|                                     |                                                                                          |
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
</dt> <dt>

[**MF\_TRANSFORM\_ASYNC\_UNLOCK**](mf-transform-async-unlock.md)
</dt> </dl>

 

 




