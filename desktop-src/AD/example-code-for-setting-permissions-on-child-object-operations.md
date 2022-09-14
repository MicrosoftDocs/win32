---
title: Example Code for Setting Permissions on Child Object Operations
description: The following C and C++ code example creates an ACE that assigns creation rights for user objects to the specified trustee.
ms.assetid: 51010092-fa85-4f9c-8869-97fed30acc7f
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , setting permissions on child object operations
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Setting Permissions on Child Object Operations

The following C and C++ code example creates an ACE that assigns creation rights for user objects to the specified trustee.


```C++
/***************************************************************************

    CreateAceCreateUsers()

    Create an ACE that assigns the right to create User objects under the 
    current object. For this function, the ACE is inherited by all subobjects 
    and is an effective right on the current object.    

***************************************************************************/

HRESULT CreateAceCreateUsers(LPWSTR pwszTrustee, BOOL fAllowed, IDispatch **ppDispACE)
{
    if(!pwszTrustee || !ppDispACE)
    {
        return E_INVALIDARG;
    }
    
    HRESULT hr;
    CComPtr<IADsAccessControlEntry> spACE;

    // Create the COM object for the new ACE.
    hr = spACE.CoCreateInstance(CLSID_AccessControlEntry);
    if(FAILED(hr))
    {
        return hr;
    }

    // Set the properties of the new ACE.

    /*
    Set the access mask that contains the rights to assign. This function 
    assigns rights to create objects.
    */
    hr = spACE->put_AccessMask(ADS_RIGHT_DS_CREATE_CHILD);
    if(FAILED(hr))
    {
        return hr;
    }
    
    // Set the trustee.
    hr = spACE->put_Trustee(CComBSTR(pwszTrustee));
    if(FAILED(hr))
    {
        return hr;
    }
    
    /*
    The AceType property must be ADS_ACETYPE_ACCESS_ALLOWED_OBJECT or 
    ADS_ACETYPE_ACCESS_DENIED_OBJECT.
    */
    if(fAllowed)
    {
        hr = spACE->put_AceType(ADS_ACETYPE_ACCESS_ALLOWED_OBJECT);
    }
    else
    {
        hr = spACE->put_AceType(ADS_ACETYPE_ACCESS_DENIED_OBJECT);
    }
    if(FAILED(hr))
    {
        return hr;
    }

    /*
    Set Flags to ADS_FLAG_OBJECT_TYPE_PRESENT so that the right applies to 
    the creation of a specific object class within the current object and 
    all its subobjects.
    */
    hr = spACE->put_Flags(ADS_FLAG_OBJECT_TYPE_PRESENT);
    if(FAILED(hr))
    {
        return hr;
    }

    // Set ObjectType to the schemaIDGUID of the user class so that the right
    // controls creation of user objects. 
    hr = spACE->put_ObjectType(CComBSTR("BF967ABA-0DE6-11D0-A285-00AA003049E2"));
    if(FAILED(hr))
    {
        return hr;
    }

    // For this function, set AceFlags so that ACE is inherited by child objects 
    hr = spACE->put_AceFlags(ADS_ACEFLAG_INHERIT_ACE);
    if(FAILED(hr))
    {
        return hr;
    }

    // Set InheritedObjectType to NULL so that it is inherited by all subobjects.
    hr = spACE->put_InheritedObjectType(NULL);
    if(FAILED(hr))
    {
        return hr;
    }

    // QueryInterface for the IDispatch pointer to pass to the AddAce method.
    hr = spACE->QueryInterface(IID_IDispatch, (void**)ppDispACE);
    if(FAILED(hr))
    {
        return hr;
    }
     
    return hr;
}
```



 

 




