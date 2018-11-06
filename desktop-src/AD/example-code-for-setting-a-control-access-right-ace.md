---
title: Example Code for Setting a Control Access Right ACE
description: The following C/C++ code example adds an ACE for a control access right to the ACL of an object.
ms.assetid: 8fb5eb47-27ca-4e60-ad39-ca4392da4e7d
ms.tgt_platform: multiple
keywords:
- Example Code for Setting a Control Access Right ACE AD
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Setting a Control Access Right ACE

The following C/C++ code example adds an ACE for a control access right to the ACL of an object.


```C++
/***************************************************************************

    SetExtendedRight()

    This function uses the rightsGUID in StringFromGUID2 format and assumes 
    it is the GUID for the correct control access right. For control access 
    rights in a DACL, lAccessType must be ADS_ACETYPE_ACCESS_ALLOWED_OBJECT 
    or ADS_ACETYPE_ACCESS_DENIED_OBJECT.

***************************************************************************/

HRESULT SetExtendedRight(IADs *pObject,
                         LPWSTR pwszRightsGUID,
                         LONG lAccessType,
                         LONG fInheritanceFlags,
                         LONG fAppliesToObjectType,
                         LPWSTR pwszTrustee)
 
{
    if(!pObject || !pwszRightsGUID || !pwszTrustee)
    {
        return E_INVALIDARG;
    }
    
    if((lAccessType != ADS_ACETYPE_ACCESS_ALLOWED_OBJECT) && 
        (lAccessType != ADS_ACETYPE_ACCESS_DENIED_OBJECT))
    {
        return E_INVALIDARG;
    }

    HRESULT hr;

    // Get the nTSecurityDescriptor attribute.
    CComBSTR sbstrNTSecDesc = L"nTSecurityDescriptor";
    CComVariant svarSecDesc;
    hr = pObject->Get(sbstrNTSecDesc, &svarSecDesc);
    if(FAILED(hr))
    {
        return hr;
    }

    /*
    The type should be VT_DISPATCH which is an IDispatch pointer to the 
    security descriptor object.
    */
    if(VT_DISPATCH != svarSecDesc.vt)
    {
        return E_FAIL;
    }

    // Get the IADsSecurityDescriptor interface from the IDispatch pointer.
    CComPtr<IADsSecurityDescriptor> spSecDesc;
    hr = svarSecDesc.pdispVal->QueryInterface(IID_IADsSecurityDescriptor, (void**)&spSecDesc);
    if(FAILED(hr))
    {
        return hr;
    }

    // Get the DACL object.
    CComPtr<IDispatch> spDispDACL;
    hr = spSecDesc->get_DiscretionaryAcl(&spDispDACL);
    if(FAILED(hr))
    {
        return hr;
    }

    // Get the IADsAccessControlList interface from the DACL object.
    CComPtr<IADsAccessControlList> spACL;
    hr = spDispDACL->QueryInterface(IID_IADsAccessControlList, (void**)&spACL);
    if(FAILED(hr))
    {
        return hr;
    }

    // Create the COM object for the new ACE.
    CComPtr<IADsAccessControlEntry> spACE;
    hr  = CoCreateInstance(CLSID_AccessControlEntry,
        NULL,
        CLSCTX_INPROC_SERVER,
        IID_IADsAccessControlEntry,
        (void **)&spACE);
    if(FAILED(hr))
    {
        return hr;
    }

    // Set the properties of the new ACE.

    /*
    For an extended control access right, set the mask to 
    ADS_RIGHT_DS_CONTROL_ACCESS.
    */
    hr = spACE->put_AccessMask(ADS_RIGHT_DS_CONTROL_ACCESS);
    if(FAILED(hr))
    {
        return hr;
    }

    // Set the trustee.
    hr = spACE->put_Trustee(pwszTrustee);
    if(FAILED(hr))
    {
        return hr;
    }

    /*
    For extended control access rights, set AceType to 
    ADS_ACETYPE_ACCESS_ALLOWED_OBJECT or ADS_ACETYPE_ACCESS_DENIED_OBJECT.
    */
    hr = spACE->put_AceType(lAccessType);
    if(FAILED(hr))
    {
        return hr;
    }

    /*
    For this example, set the AceFlags so that ACE is not inherited by child 
    objects.
    */
    hr = spACE->put_AceFlags(fInheritanceFlags);
    if(FAILED(hr))
    {
        return hr;
    }

    /*
    Flags specifies whether the ACE applies to the current object, child objects, 
    or both. For this example, fAppliesToInheritedObject is set to 
    ADS_FLAG_OBJECT_TYPE_PRESENT so that the right applies only to the current 
    object.
    */
    hr = spACE->put_Flags(fAppliesToObjectType);
    if(FAILED(hr))
    {
        return hr;
    }

    /*
    For extended control access rights, set ObjectType to the rightsGUID of the 
    extended right.
    */
    if(fAppliesToObjectType & ADS_FLAG_OBJECT_TYPE_PRESENT)
    {
        hr = spACE->put_ObjectType(pwszRightsGUID);
        if(FAILED(hr))
        {
            return hr;
        }
    }

    // Set the inherited object type if right applies to child objects.
    if(fAppliesToObjectType & ADS_FLAG_INHERITED_OBJECT_TYPE_PRESENT)
    {
        hr = spACE->put_InheritedObjectType(pwszRightsGUID);
        if(FAILED(hr))
        {
            return hr;
        }
    }

    // Get the IDispatch pointer for the ACE.
    CComPtr<IDispatch> spDispACE;
    hr = spACE->QueryInterface(IID_IDispatch, (void**)&spDispACE);
    if(FAILED(hr))
    {
        return hr;
    }

    // Add the ACE to the ACL.
    hr = spACL->AddAce(spDispACE);
    if(FAILED(hr))
    {
        return hr;
    }

    // Update the DACL property.
    hr = spSecDesc->put_DiscretionaryAcl(spDispDACL);
    if(FAILED(hr))
    {
        return hr;
    }

    /*
    Write the updated value for the ntSecurityDescriptor attribute to the 
    property cache.
    */
    hr = pObject->Put(sbstrNTSecDesc, svarSecDesc);
    if(FAILED(hr))
    {
        return hr;
    }

    // Call SetInfo to update the property on the object in the directory.
    hr = pObject->SetInfo();

    return hr;
}
```



 

 




