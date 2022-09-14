---
title: Example Code for Enumerating the ACL of an Object in Active Directory Domain Services
description: The following code examples can be used to enumerate the access control list (ACL) of an object in Active Directory Domain Services.
ms.assetid: 3629ffde-c516-4566-8b40-a913b8355656
ms.tgt_platform: multiple
keywords:
- Example Code for Enumerating the ACL of an Active Directory Object AD
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Enumerating the ACL of an Object in Active Directory Domain Services

The following code examples can be used to enumerate the access control list (ACL) of an object in Active Directory Domain Services.

The following code example shows a function that enumerates the trustees of an object .


```C++
//*******************************************************************
//
//  EnumTrustees()
//
//*******************************************************************

HRESULT EnumTrustees(IADsAccessControlList *pACL)
{
    if(NULL == pACL)
    {
        return E_INVALIDARG;
    }

    HRESULT hr;
    IUnknown *pUnk;

    /*
    Get the enumerator from the access control list.
    */
    hr = pACL->get__NewEnum(&pUnk);
    if(SUCCEEDED(hr))
    {
        IEnumVARIANT *pEnum;
        
        hr = pUnk->QueryInterface(IID_IEnumVARIANT, (LPVOID*)&pEnum);
        if(SUCCEEDED(hr))
        {
            VARIANT var;
            ULONG ulFetched;
            
            wprintf(L"Trustees:\n");
            
            VariantInit(&var);

            /*
            Enumerate the access control entries 
            in the access control list.
            */
            while( SUCCEEDED(hr = pEnum->Next(1, &var, &ulFetched)) 
                   && (ulFetched > 0) )
            {
                IADsAccessControlEntry *pACE;
                
                /*
                Get the access control entry.
                */
                hr = V_DISPATCH(&var)->QueryInterface(IID_IADsAccessControlEntry, 
                                                      (LPVOID*)&pACE);
                if(SUCCEEDED(hr))
                {
                    CComBSTR sbstrTrustee;

                    /*
                    Get the Trustee for this ACE and print
                    it to the console window.
                    */
                    hr = pACE->get_Trustee(&sbstrTrustee);
                    if(SUCCEEDED(hr))
                    {
                        wprintf(L"\t");
                        wprintf(sbstrTrustee);
                        wprintf(L"\n");
                    }
                    
                    pACE->Release();
                }
                
                VariantClear(&var);
            }
            
            pEnum->Release();
        }

        pUnk->Release();
    }

    return hr;
}

//*******************************************************************
//
//  EnumAccessInfo()
//
//*******************************************************************

HRESULT EnumAccessInfo(IADs *pads)
{
    if(NULL == pads)
    {
        return E_INVALIDARG;
    }
    
    HRESULT hr;
    VARIANT var;

    // Get the ntSecurityDescriptor attribute
    VariantInit(&var);
    hr = pads->Get(CComBSTR("ntSecurityDescriptor"), &var);
    if(SUCCEEDED(hr))
    {
        if(VT_DISPATCH == var.vt)
        {
            /*
            Get the security descriptor from the
            ntSecurityDescriptor attribute.
            */
            IADsSecurityDescriptor *pSD;
            hr = V_DISPATCH(&var)->QueryInterface(IID_IADsSecurityDescriptor,
                                                  (LPVOID*)&pSD);
            if(SUCCEEDED(hr))
            {
                IDispatch *pDisp;

                /*
                Get the DACL from the security descriptor.
                */
                hr = pSD->get_DiscretionaryAcl(&pDisp);
                if(SUCCEEDED(hr))
                {
                    IADsAccessControlList *pACL;

                    hr = pDisp->QueryInterface(IID_IADsAccessControlList, 
                                               (LPVOID*)&pACL);
                    if(SUCCEEDED(hr))
                    {
                        /*
                        Enumerate the trustees of this ACL.
                        */
                        hr = EnumTrustees(pACL);
                        
                        pACL->Release();
                    }
                    
                    pDisp->Release();
                }
                
                pSD->Release();
            }
        }

        VariantClear(&var);
    }

    return hr;
}
```



The following code example shows a function that enumerates the trustees of an object.


```VB
Private Sub EnumAccessInfo(ByVal oObject As IADs)
    Dim SecDesc As SecurityDescriptor
    Dim Dacl As AccessControlList
    
    On Error GoTo CleanUp
    
    ' Get the security descriptor for the object.
    Set SecDesc = oObject.Get("ntSecurityDescriptor")
    
    ' Get the DACL for the object.
    Set Dacl = SecDesc.DiscretionaryAcl
    
    Debug.Print "Trustees:"

    ' Enumerate the ACEs in the DACL, printing the Trustee for each.
    For Each oACE In Dacl
        Debug.Print vbTab + oACE.Trustee
    Next
    
CleanUp:
    Set SecDesc = Nothing
    Set Dacl = Nothing
End Sub
```



 

 




