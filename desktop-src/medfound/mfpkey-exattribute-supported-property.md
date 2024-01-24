---
description: Specifies whether a Media Foundation transform (MFT) copies attributes from input samples to output samples.
ms.assetid: 039ecb35-9aa9-4e8a-bbbc-042b9c4c874c
title: MFPKEY_EXATTRIBUTE_SUPPORTED property (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_EXATTRIBUTE\_SUPPORTED property

Specifies whether a Media Foundation transform (MFT) copies attributes from input samples to output samples.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**VARIANT\_BOOL**

VT\_BOOL

**boolVal**



## Remarks

This attribute can have the following values.



| Value              | Description                                                                                                                                             |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **VARIANT\_TRUE**  | The MFT copies attributes from the input samples to the output samples.                                                                                 |
| **VARIANT\_FALSE** | The Media Session copies attributes from input samples to output samples. It does not overwrite any attributes that the MFT sets on the output samples. |



 

To get this attribute, call **QueryInterface** on the MFT for the **IPropertyStore** interface.

The default value is **VARIANT\_FALSE**. If the MFT does not expose the **IPropertyStore** interface, or if this property is not set, treat the value as **VARIANT\_FALSE**.

This property is read-only.

> [!NOTE] 
> This attribute does not apply to asynchronous MFTs. Attributes will not be copied from the input samples to the output samples for asynchronous MFTs, regardless of the value of this attribute.

## Examples

The following example returns VARIANT\_TRUE if an MFT copies sample attributes.


```C++
BOOL TransformCopiesSampleAttributes(IMFTransform *pMFT)
{
    BOOL bCopiesAttributes = FALSE;

    IPropertyStore *pProps = NULL;

    HRESULT hr = pMFT->QueryInterface(IID_PPV_ARGS(&pProps));
    
    if (SUCCEEDED(hr))
    {
        PROPVARIANT var;
        hr = pProps->GetValue(MFPKEY_EXATTRIBUTE_SUPPORTED, &var);

        if (SUCCEEDED(hr))
        {
            bCopiesAttributes = 
                (var.vt == VT_BOOL && var.boolVal == VARIANT_TRUE);

            PropVariantClear(&var);
        }
        pProps->Release();
    }
    return bCopiesAttributes;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> <dt>

[**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput)
</dt> </dl>

 

 




