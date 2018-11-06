---
title: Example Code for Setting Read Property Rights on an Object
description: The following code example contains a function that creates an ACE that assigns read access to all properties of the object to the specified trustee.
ms.assetid: 343538d7-fef4-492d-a385-37433ce1250b
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , setting read property rights on an object
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Setting Read Property Rights on an Object

The following code example contains a function that creates an ACE that assigns read access to all properties of the object to the specified trustee.


```C++
/***************************************************************************

    CreateAceEffectiveReadAllProperties()

    Create an ACE that assigns read property rights to all properties on the 
    object. This ACE is not inherited; that is, it applies only to the 
    current object.

***************************************************************************/

HRESULT CreateAceEffectiveReadAllProperties(LPWSTR pwszTrustee, 
                                            IDispatch **ppDispACE)
{
    if(!pwszTrustee || !ppDispACE)
    {
        return E_INVALIDARG;
    }
    
    HRESULT hr = E_FAIL;
    CComPtr<IADsAccessControlEntry> spACE;
    
    // Create the COM object for the new ACE.
    hr  = CoCreateInstance(CLSID_AccessControlEntry,
        NULL,
        CLSCTX_INPROC_SERVER,
        IID_IADsAccessControlEntry,
        (void **)&spACE);
    if (SUCCEEDED(hr))
    {
        // Set the properties of the new ACE.

        //Set the access mask containing the rights to assign.
        //This function assigns read property rights.
        hr = spACE->put_AccessMask(ADS_RIGHT_DS_READ_PROP);
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
        
        // Set the AceType.
        hr = spACE->put_AceType(ADS_ACETYPE_ACCESS_ALLOWED);
        if(FAILED(hr))
        {
            return hr;
        }
        
        // For this function, set AceFlags so that ACE is not inherited by child objects.
        // You can set AceFlags to 0 or let it default to 0 by not calling put_AceFlags.
        hr = spACE->put_AceFlags(0);
        if(FAILED(hr))
        {
            return hr;
        }
        
        // For this function, set ObjectType to NULL because the right applies to all properties
        // and set Flags to 0. You can also not call these two methods and let them default to NULL. 
        hr = spACE->put_ObjectType(NULL);
        if(FAILED(hr))
        {
            return hr;
        }

        hr = spACE->put_Flags(0);
        if(FAILED(hr))
        {
            return hr;
        }
        
        // Is not inherited; set object type to NULL or let it default to NULL by not calling the method.
        hr = spACE->put_InheritedObjectType(NULL);
        if(FAILED(hr))
        {
            return hr;
        }
        
        // QueryInterface for a IDispatch pointer to pass to the AddAce method.
        hr = spACE->QueryInterface(IID_IDispatch, (void**)ppDispACE);
        if(FAILED(hr))
        {
            return hr;
        }
    }
     
    return hr;
}
```



 

 




