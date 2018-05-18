---
title: Providing Display Attributes
description: Text Services Framework (TSF) enables a text service to provide display attributes for text.
ms.assetid: '5809f5b8-0396-4abd-b5fe-61ecc8cd0914'
keywords: ["Text Services Framework (TSF),display attributes", "TSF (Text Services Framework),display attributes", "text services,display attributes", "display attributes"]
---

# Providing Display Attributes

Text Services Framework (TSF) enables a text service to provide display attributes for text. This enables additional visual feedback to be supplied to the user. For example, a spelling checker text service can highlight a misspelled word with a red underline. The display attributes provided are defined by the [TF\_DISPLAYATTRIBUTE](tf-displayattribute.md) structure and include text color, text background color, underline style, underline color, and underline weight.

Clients that use this display attribute information will most often be applications, but can also include text services. The TSF manager mediates between the display attribute provider and the client and tracks the display attribute provider of the specific display attributes.

To provide display attributes, a text service must do the following.

1.  Register the text service as a display attribute provider by calling [ITfCategoryMgr::RegisterCategory](itfcategorymgr-registercategory.md) with the class identifier of the text service for the first parameter, GUID\_TFCAT\_DISPLAYATTRIBUTEPROVIDER for the second parameter and the class identifier of the text service again for the third parameter.
2.  Implement [ITfDisplayAttributeProvider](itfdisplayattributeprovider.md) and make it available from the class factory.
3.  Implement [IEnumTfDisplayAttributeInfo](ienumtfdisplayattributeinfo.md) and make it available from [ITfDisplayAttributeProvider::EnumDisplayAttributeInfo](itfdisplayattributeprovider-enumdisplayattributeinfo.md).
4.  Implement an [ITfDisplayAttributeInfo](itfdisplayattributeinfo.md) object for each type of display attribute that the text service provides.

## Applying the Display Attributes

The text service must apply the display attribute to a range of text. A text service can only modify the property value during a read/write edit session.

Assuming this is within a read/write edit session, a display attribute is applied in the following manner.

1.  Obtain an [ITfRange](itfrange.md) object that covers the text that the display attribute will be applied to.
2.  Obtain an [ITfProperty](itfproperty.md) object for the text attributes by calling [ITfContext::GetProperty](itfcontext-getproperty.md) with GUID\_PROP\_ATTRIBUTE.
3.  Create a [TfGuidAtom](tfguidatom.md) from the text service-defined display attribute identifier **GUID** by calling [ITfCategoryMgr::RegisterGUID](itfcategorymgr-registerguid.md).
4.  Initialize a VARIANT variable to VT\_I4 and set the **lVal** member to the **TfGuidAtom** created in the previous step.
5.  Apply the display attribute to the range by calling [ITfProperty::SetValue](itfproperty-setvalue.md) with the read/write edit cookie, the range and the VARIANT initialized in the previous step.


```C++
STDAPI CEditSession::DoEditSession(TfEditCookie ec)
{
    HRESULT hr;
    ITfCategoryMgr *pCategoryMgr;
    TfGuidAtom  gaDisplayAttribute = TF_INVALID_GUIDATOM;

    //Create a TfGuidAtom for the display attribute identifier. 
    hr = CoCreateInstance(CLSID_TF_CategoryMgr,
                         NULL, 
                         CLSCTX_INPROC_SERVER, 
                         IID_ITfCategoryMgr, 
                         (void**)&amp;pCategoryMgr);
    
    if(SUCCEEDED(hr))
    {
        hr = pCategoryMgr->RegisterGUID(guidDisplayAttribute, &amp;gaDisplayAttribute);

        pCategoryMgr->Release();
    }
    
    //Apply the display attribute to the selected text. 
    if(TF_INVALID_GUIDATOM != gaDisplayAttribute)
    {
        TF_SELECTION tfSel;
        ULONG cFetched;

        //Get the selection. 
        hr = m_pContext->GetSelection(ec, TF_DEFAULT_SELECTION, 1, &amp;tfSel, &amp;cFetched);
        if(SUCCEEDED(hr) &amp;&amp; cFetched)
        {
            ITfProperty *pDisplayAttributeProperty;

            //Get the display attribute property. 
            hr = m_pContext->GetProperty(GUID_PROP_ATTRIBUTE, &amp;pDisplayAttributeProperty);
            if(SUCCEEDED(hr))
            {
                VARIANT var;

                VariantInit(&amp;var);

                //All display attributes are TfGuidAtoms and TfGuidAtoms are VT_I4. 
                var.vt = VT_I4; 
                var.lVal = gaDisplayAttribute;

                //Set the display attribute value over the range. 
                hr = pDisplayAttributeProperty->SetValue(ec, tfSel.range, &amp;var);

                pDisplayAttributeProperty->Release();
            }

            tfSel.range->Release();
        }
    }

    return S_OK;
}
```



## Supplying the Display Attribute Information Object

A client obtains an **ITfDisplayAttributeInfo** object in one of two ways.

1.  The client calls [ITfDisplayAttributeMgr::GetDisplayAttributeInfo](itfdisplayattributemgr-getdisplayattributeinfo.md) with the **GUID** identifier of the display attribute. The first time the client calls **ITfDisplayAttributeMgr::GetDisplayAttributeInfo**, the TSF manager will create an instance of the display attribute provider by calling CoCreateInstance with the class identifier passed as the first parameter to **ITfCategoryMgr::RegisterCategory**. Subsequent calls to **ITfDisplayAttributeMgr::GetDisplayAttributeInfo** will reuse the display attribute provider object.

    The TSF manager then calls [ITfDisplayAttributeProvider::GetDisplayAttributeInfo](itfdisplayattributeprovider-getdisplayattributeinfo.md) with the display attribute **GUID** to obtain the **ITfDisplayAttributeInfo** object.

    The TSF manager then passes the **ITfDisplayAttributeInfo** object back to the client.

2.  The client calls [ITfDisplayAttributeMgr::EnumDisplayAttributeInfo](itfdisplayattributemgr-enumdisplayattributeinfo.md) to obtain an **IEnumTfDisplayAttributeInfo** object that contains all of the display attributes provided by all of the display attribute providers. The TSF manager enumerates each display attribute provider and creates an instance of each provider by calling CoCreateInstance with the class identifier passed as the third parameter to **ITfCategoryMgr::RegisterCategory**.

    The TSF manager then calls each provider's **ITfDisplayAttributeProvider::EnumDisplayAttributeInfo** to obtain an **IEnumTfDisplayAttributeInfo** object that contains all of the display attributes provided by the provider.

    The TSF manager then calls the provider's [IEnumTfDisplayAttributeInfo::Next](ienumtfdisplayattributeinfo-next.md) method, adding each **ITfDisplayAttributeInfo** object obtained to the manager's own enumerator, until the end of the provider's enumeration is reached.

    When all of the **ITfDisplayAttributeInfo** objects for all of the display attribute providers are added to the TSF manager's enumerator, the manager returns its enumerator to the client. The client then calls **IEnumTfDisplayAttributeInfo::Next** one or more times to obtain the **ITfDisplayAttributeInfo** objects.

## Related topics

<dl> <dt>

[TF\_DISPLAYATTRIBUTE](tf-displayattribute.md)
</dt> <dt>

[ITfCategoryMgr::RegisterCategory](itfcategorymgr-registercategory.md)
</dt> <dt>

[ITfDisplayAttributeProvider](itfdisplayattributeprovider.md)
</dt> <dt>

[IEnumTfDisplayAttributeInfo](ienumtfdisplayattributeinfo.md)
</dt> <dt>

[ITfDisplayAttributeProvider::EnumDisplayAttributeInfo](itfdisplayattributeprovider-enumdisplayattributeinfo.md)
</dt> <dt>

[ITfDisplayAttributeInfo](itfdisplayattributeinfo.md)
</dt> <dt>

[ITfRange](itfrange.md)
</dt> <dt>

[ITfProperty](itfproperty.md)
</dt> <dt>

[ITfContext::GetProperty](itfcontext-getproperty.md)
</dt> <dt>

[TfGuidAtom](tfguidatom.md)
</dt> <dt>

[ITfCategoryMgr::RegisterGUID](itfcategorymgr-registerguid.md)
</dt> <dt>

[ITfProperty::SetValue](itfproperty-setvalue.md)
</dt> <dt>

[ITfDisplayAttributeMgr::GetDisplayAttributeInfo](itfdisplayattributemgr-getdisplayattributeinfo.md)
</dt> <dt>

[ITfDisplayAttributeProvider::GetDisplayAttributeInfo](itfdisplayattributeprovider-getdisplayattributeinfo.md)
</dt> <dt>

[ITfDisplayAttributeMgr::EnumDisplayAttributeInfo](itfdisplayattributemgr-enumdisplayattributeinfo.md)
</dt> <dt>

 IEnumTfDisplayAttributeInfo 
</dt> <dt>

 ITfDisplayAttributeProvider::EnumDisplayAttributeInfo 
</dt> <dt>

[IEnumTfDisplayAttributeInfo::Next](ienumtfdisplayattributeinfo-next.md)
</dt> </dl>

 

 




