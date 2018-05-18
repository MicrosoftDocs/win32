---
title: Using Display Attributes
description: Text Services Framework (TSF) enables a text service to provide display attributes for text.
ms.assetid: 'b0f6e8e8-586a-4b51-a498-fb22bd36161f'
keywords: ["Text Services Framework (TSF),display attributes", "TSF (Text Services Framework),display attributes", "TSF-enabled applications,display attributes", "display attributes"]
---

# Using Display Attributes

Text Services Framework (TSF) enables a text service to provide display attributes for text. This enables an application to display additional visual feedback. For example, a spelling checker text service can highlight a misspelled word with a red underline. The display attributes that can be provided are defined by the [TF\_DISPLAYATTRIBUTE](tf-displayattribute.md) structure and include text color, text background color, underline style, underline color, and underline weight.

When rendering text, an application should obtain the display attributes for the text drawn and use the attributes to modify how the text is drawn. Complete the following steps to obtain display attributes.

1.  Obtain a property object for GUID\_PROP\_ATTRIBUTE by calling [ITfContext::GetProperty](itfcontext-getproperty.md).
2.  Obtain the value of the GUID\_PROP\_ATTRIBUTE for the specified range by calling [ITfReadOnlyProperty::GetValue](itfreadonlyproperty-getvalue.md). This supplies a [TfGuidAtom](tfguidatom.md) value.
3.  Convert the [TfGuidAtom](tfguidatom.md) value into a GUID by calling [ITfCategoryMgr::GetGUID](itfcategorymgr-getguid.md).
4.  Create an [ITfDisplayAttributeInfo](itfdisplayattributeinfo.md) object for the display attribute by calling [ITfDisplayAttributeMgr::GetDisplayAttributeInfo](itfdisplayattributemgr-getdisplayattributeinfo.md).
5.  Obtain the display attribute information by calling [ITfDisplayAttributeInfo::GetAttributeInfo](itfdisplayattributemgr-getdisplayattributeinfo.md).

The following code example demonstrates a function that obtains the display attributes from a supplied context, range, and edit cookie.


```C++
HRESULT GetDispAttrFromRange(   ITfContext *pContext, 
                                ITfRange *pRange, 
                                TfEditCookie ec, 
                                TF_DISPLAYATTRIBUTE *pDispAttr)
{
    HRESULT     hr;
    
    //Create the category manager. 
    ITfCategoryMgr  *pCategoryMgr;
    hr = CoCreateInstance(  CLSID_TF_CategoryMgr,
                            NULL, 
                            CLSCTX_INPROC_SERVER, 
                            IID_ITfCategoryMgr, 
                            (LPVOID*)&amp;pCategoryMgr);
    if(FAILED(hr))
    {
        return hr;
    }

    //Create the display attribute manager. 
    ITfDisplayAttributeMgr  *pDispMgr;
    hr = CoCreateInstance(  CLSID_TF_DisplayAttributeMgr,
                            NULL, 
                            CLSCTX_INPROC_SERVER, 
                            IID_ITfDisplayAttributeMgr, 
                            (LPVOID*)&amp;pDispMgr);
    if(FAILED(hr))
    {
        pCategoryMgr->Release();
        return hr;
    }
    
    //Get the display attribute property. 
    ITfProperty *pProp;
    hr = pContext->GetProperty(GUID_PROP_ATTRIBUTE, &amp;pProp);
    if(SUCCEEDED(hr))
    {
        VARIANT var;

        VariantInit(&amp;var);
        hr = pProp->GetValue(ec, pRange, &amp;var);
        if(S_OK == hr)  //Returns S_FALSE if the range is not completely covered by the property.  
        {
            if(VT_I4 == var.vt)
            {
                //The property is a guidatom. 
                GUID    guid;

                //Convert the guidatom into a GUID. 
                hr = pCategoryMgr->GetGUID((TfGuidAtom)var.lVal, &amp;guid);
                if(SUCCEEDED(hr))
                {
                    ITfDisplayAttributeInfo *pDispInfo;

                    //Get the display attribute info object for this attribute. 
                    hr = pDispMgr->GetDisplayAttributeInfo(guid, &amp;pDispInfo, NULL);
                    if(SUCCEEDED(hr))
                    {
                        //Get the display attribute info. 
                        hr = pDispInfo->GetAttributeInfo(pDispAttr);

                        pDispInfo->Release();
                    }
                }
            }
            else
            {
                //An error occurred; GUID_PROP_ATTRIBUTE must always be VT_I4. 
                hr = E_FAIL;
            }
            VariantClear(&amp;var);
        }
    pProp->Release();
    }

    pCategoryMgr->Release();
    pDispMgr->Release();

    return hr;
}

```



## Related topics

<dl> <dt>

[TF\_DISPLAYATTRIBUTE](tf-displayattribute.md)
</dt> <dt>

[ITfContext::GetProperty](itfcontext-getproperty.md)
</dt> <dt>

[ITfReadOnlyProperty::GetValue](itfreadonlyproperty-getvalue.md)
</dt> <dt>

[TfGuidAtom](tfguidatom.md)
</dt> <dt>

[ITfCategoryMgr::GetGUID](itfcategorymgr-getguid.md)
</dt> <dt>

[ITfDisplayAttributeInfo](itfdisplayattributeinfo.md)
</dt> <dt>

[ITfDisplayAttributeMgr::GetDisplayAttributeInfo](itfdisplayattributemgr-getdisplayattributeinfo.md)
</dt> <dt>

 ITfDisplayAttributeInfo::GetAttributeInfo 
</dt> </dl>

 

 




