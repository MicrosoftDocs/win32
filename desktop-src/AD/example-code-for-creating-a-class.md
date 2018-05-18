---
title: Example Code for Creating a Class
description: Shows how to create a classSchema object in the ADSI cache.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '021a0c7b-0e08-4d7a-af9a-9e3e868b90b6'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Example Code for Creating a Class", "Creating a Class, Example Code AD"]
---

# Example Code for Creating a Class

The following C and C++ code example shows how to create a [**classSchema**](https://msdn.microsoft.com/library/ms680982) object in the ADSI cache.

The **CreateClass** example function shows how to create the [**classSchema**](https://msdn.microsoft.com/library/ms680982) object and returns an [**IADs**](https://msdn.microsoft.com/library/aa705950) pointer to the new object. Be aware that **CreateClass** does not call [**IADs::SetInfo**](https://msdn.microsoft.com/library/aa746354) to commit the new **classSchema** object to the directory. The caller must make the call using the returned pointer.

The following **BytesToVariantArray** code example shows a utility function that packs an octet string into a variant array.


```C++
HRESULT BytesToVariantArray(PBYTE pValue, 
                            ULONG cValueElements, 
                            VARIANT *pVariant);

////////////////////////////////////////////////////////// 
// CreateClass routine
// Calls IADsContainer::Create to create a new classSchema object in
// the schema container. Sets key properties of the new class.
// Be aware that the CreateClass routine does not commit the new class
// to the directory. The CreateClass caller must commit 
// the new class by calling IADs::SetInfo on the returned 
// pointer to the new class object.
////////////////////////////////////////////////////////// 
HRESULT CreateClass(
    IADsContainer *pSchema,
    LPOLESTR szClassName,
    LPOLESTR szLDAPDisplayName,
    LPOLESTR szClassOID,
    const GUID * pSchemaIDGUID,
    LPOLESTR szSubClassOf,
    LPOLESTR *arrayAuxiliaryClasses,
    DWORD dwSizearrayAuxiliaryClasses,
    LPOLESTR szDefaultObjectCategory,
    LPOLESTR szDescription,
    BOOL bDefaultHidingValue,
    LPOLESTR szDefaultSecurityDescriptor,
    LPOLESTR szRDNAttribute,
    int iObjectClassCategory,
    LPOLESTR *arrayPossibleSuperiors,
    DWORD dwSizearrayPossibleSuperiors,
    LPOLESTR *arrayMustContain,
    DWORD dwSizearrayMustContain,
    LPOLESTR *arrayMayContain,
    DWORD dwSizearrayMayContain,
    LPOLESTR szAdminDisplayName,
    IADs **ppNewClass // Return an IADs pointer to the new class.
    )
{
    if ((!szClassName)
        ||(!szClassOID)
        ||(!szSubClassOf)
        ||(!iObjectClassCategory)
        ||(!arrayPossibleSuperiors)
    )
    {
        return E_INVALIDARG;
    }

    if (!ppNewClass)
    {
        return E_POINTER;
    }

    HRESULT hr = E_FAIL;
    IDispatch *pDisp = NULL;
    LPOLESTR szStart = L"cn=";
    DWORD dwLength = wcslen(szStart) + wcslen(szClassName) + 1;
    LPOLESTR szBuffer = new OLECHAR[dwLength];
    wcscpy_s(szBuffer,szStart);
    wcscat_s(szBuffer,szClassName);
    *ppNewClass = NULL;
    VARIANT var;

    VariantInit(&amp;var);

    if (!pSchema)
    {
        return E_POINTER;
    }

    hr = pSchema->Create(CComBSTR("classSchema"), 
                         CComBSTR(szBuffer), 
                         &amp;pDisp);
    delete [] szBuffer;

    if (SUCCEEDED(hr))
    {
        hr = pDisp->QueryInterface(IID_IADs, (void**)ppNewClass);

        while (SUCCEEDED(hr))
        {
            // Put this value so that it can be read from the cache.
            var.vt = VT_BSTR;
            var.bstrVal = SysAllocString(szClassName);
            hr = (*ppNewClass)->Put(CComBSTR("cn"), var);
            VariantClear(&amp;var);
         
            // Put lDAPDisplayName.
            // If NULL, let it default; that is do not set it.
            if (szLDAPDisplayName)
            {
                var.vt = VT_BSTR;
                var.bstrVal = SysAllocString(szLDAPDisplayName);
                hr = (*ppNewClass)->Put(CComBSTR("lDAPDisplayName"), 
                                        var);
                VariantClear(&amp;var);
            }
         
            // Put attributeID.
            var.vt = VT_BSTR;
            var.bstrVal = SysAllocString(szClassOID);
            hr = (*ppNewClass)->Put(CComBSTR("governsID"), var);
            VariantClear(&amp;var);
         
            // Put schemaIDGUID.
            // If NULL, let it default; that is do not set it.
            if (pSchemaIDGUID)
            {
                hr = BytesToVariantArray(
                    (LPBYTE)pSchemaIDGUID, // Pointer to bytes to 
                                           // put in a variant array.
                    sizeof(GUID),       // Size, in bytes, of pValue.
                    &amp;var // Return variant containing 
                         // octet string (VT_UI1|VT_ARRAY).
                    );

                if (SUCCEEDED(hr))
                {
                    hr = (*ppNewClass)->Put(CComBSTR("schemaIDGUID"), 
                                            var);
                    VariantClear(&amp;var);
                }
            }
         
            // Put subClassOf.
            var.vt = VT_BSTR;
            // Verify existence of the class.
            var.bstrVal = SysAllocString(szSubClassOf);
            hr = (*ppNewClass)->Put(CComBSTR("subClassOf"), var);
            VariantClear(&amp;var);
         
            // Put defaultObjectCategory.
            // If NULL, do not set it.
            if (szDefaultObjectCategory)
            {
                var.vt = VT_BSTR;
                    // Verify that it is a valid DN.
                var.bstrVal = SysAllocString(szDefaultObjectCategory);
                hr = (*ppNewClass)->Put(CComBSTR("defaultObjectCategory"), 
                                                 var);
                VariantClear(&amp;var);
            }
         
            // Put objectClassCategory.
            var.vt = VT_I4;
            var.lVal = iObjectClassCategory;
            hr = (*ppNewClass)->Put(CComBSTR("objectClassCategory"), 
                                    var);
            VariantClear(&amp;var);
         
            // Put defaultHidingValue.
            var.vt = VT_BOOL;
            if (bDefaultHidingValue)
            {
                var.boolVal = VARIANT_TRUE;
            }
            else
            {
                var.boolVal = VARIANT_FALSE;
            }
            hr = (*ppNewClass)->Put(CComBSTR("defaultHidingValue"), 
                                    var);
            VariantClear(&amp;var);
         
            // Put RDNAttrID.
            // If NULL, do not set it.
            if (szRDNAttribute)
            {
                var.vt = VT_BSTR;

                // Verify that it is a valid attribute.
                var.bstrVal = SysAllocString(szRDNAttribute);
                hr = (*ppNewClass)->Put(CComBSTR("rDNAttID"), var);
                VariantClear(&amp;var);
            }
         
            // Put defaultSecurityDescriptor.
            // If NULL, let it default; that is do not set it.
            if (szDefaultSecurityDescriptor)
            {
                var.vt = VT_BSTR;
                var.bstrVal = 
                  SysAllocString(szDefaultSecurityDescriptor);
                hr = 
                  (*ppNewClass)->Put(CComBSTR("defaultSecurityDescriptor"), 
                                     var);
                VariantClear(&amp;var);
            }
         
            if (arrayPossibleSuperiors &amp;&amp; 
                dwSizearrayPossibleSuperiors)
            {
                // Build a Variant of array type, using the 
                // specified string array.
                hr = ADsBuildVarArrayStr(arrayPossibleSuperiors, 
                                         dwSizearrayPossibleSuperiors, 
                                         &amp;var);
                if (SUCCEEDED(hr))
                {
                    // Verify that all the specified classes
                    // are valid.
                    hr = (*ppNewClass)->Put(CComBSTR("possSuperiors"), 
                                            var);
                    VariantClear(&amp;var);
                }
            }
         
            if (arrayMustContain &amp;&amp; dwSizearrayMustContain)
            {
                // Build a Variant of array type, 
                // using the specified string array.
                hr = ADsBuildVarArrayStr(arrayMustContain, 
                                         dwSizearrayMustContain,
                                         &amp;var);
                if (SUCCEEDED(hr))
                {
                    // Verify that all the specified 
                    // attributes are valid.
                    hr = (*ppNewClass)->Put(CComBSTR("mustContain"), 
                                            var);
                    VariantClear(&amp;var);
                }
            }
         
            if (arrayMayContain &amp;&amp; dwSizearrayMayContain)
            {
                // Build a Variant of array type, 
                // using the specified string array.
                hr = ADsBuildVarArrayStr(arrayMayContain, 
                                         dwSizearrayMayContain, 
                                         &amp;var);
                if (SUCCEEDED(hr))
                {
                    // Verify that all the specified 
                    // attributes are valid.
                    hr = (*ppNewClass)->Put(CComBSTR("mayContain"), 
                                            var);
                    VariantClear(&amp;var);
                }
            }
         
            if (arrayAuxiliaryClasses &amp;&amp; 
                dwSizearrayAuxiliaryClasses)
            {
                // Build a Variant of array type,
                // using the specified string array.
                hr = ADsBuildVarArrayStr(arrayAuxiliaryClasses, 
                                         dwSizearrayAuxiliaryClasses,
                                         &amp;var);
                if (SUCCEEDED(hr))
                {
                    // Verify that all the 
                    // specified classes are valid.
                    hr = (*ppNewClass)->Put(CComBSTR("auxiliaryClass"),
                                            var);
                    VariantClear(&amp;var);
                }
            }
         
            // Put description.
            var.vt = VT_BSTR;
            var.bstrVal = SysAllocString(szDescription);
            hr = (*ppNewClass)->Put(CComBSTR("description"), 
                                    var);
            VariantClear(&amp;var);
         
         
            // Put adminDisplayName.
            // If NULL, set it to the same string as cn.
            var.vt = VT_BSTR;
            if (!szAdminDisplayName)
            {
                var.bstrVal = SysAllocString(szClassName);
            }
            else
            {
                var.bstrVal = SysAllocString(szAdminDisplayName);
            }
            hr = (*ppNewClass)->Put(CComBSTR("adminDisplayName"), 
                                var);
            VariantClear(&amp;var);
         
            // End of properties to set.
            break;
        }
    }

    if (pDisp)
    {
        pDisp->Release();
    }
     
    if (FAILED(hr))
    {
        // Cleanup, if failed.
        if (*ppNewClass)
        {
            (*ppNewClass)->Release();
            (*ppNewClass) = NULL;
        }
    }
     
    return hr;
}

////////////////////////////////////////////////////////// 
// BytesToVariantArray
// Packs an octet string into a variant array.
////////////////////////////////////////////////////////// 
HRESULT BytesToVariantArray(
    PBYTE pValue, // Pointer to bytes to put in a 
                  // variant array.
    ULONG cValueElements,// Size of pValue in bytes.
    VARIANT *pVariant // Return variant that contains 
                      // octet string (VT_UI1|VT_ARRAY).
    )
{
    HRESULT hr = E_FAIL;
    SAFEARRAY *pArrayVal = NULL;
    SAFEARRAYBOUND arrayBound;
    CHAR HUGEP *pArray = NULL;
 
    // Set bound for array.
    arrayBound.lLbound = 0;
    arrayBound.cElements = cValueElements;
 
    // Create the safe array for the octet string. 
    // unsigned char elements;single dimension;aBound size.
    pArrayVal = SafeArrayCreate(VT_UI1, 1, &amp;arrayBound);
 
    if (!(pArrayVal == NULL) )
    {
        hr = SafeArrayAccessData(pArrayVal, 
                                (void HUGEP * FAR *) &amp;pArray );
        if (SUCCEEDED(hr))
        {
            // Copy bytes to the safe array.
            memcpy( pArray, pValue, arrayBound.cElements );
            SafeArrayUnaccessData( pArrayVal );
            // Set type to array of unsigned char.
            V_VT(pVariant) = VT_ARRAY | VT_UI1;
            // Assign the safe array to the array member.
            V_ARRAY(pVariant) = pArrayVal;
            hr = S_OK;
        }
        else
        {
            // Cleanup if the array cannot be accessed.
            if ( pArrayVal )
            {
                SafeArrayDestroy( pArrayVal );
            }
        }
    }
    else
    {
        hr = E_OUTOFMEMORY;
    }
 
    return hr;
}
```



 

 




