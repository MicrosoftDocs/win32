---
title: Example Code for Creating an Attribute
description: The following code example creates an attributeSchema object in the schema container.
ms.assetid: 5f679a88-29d1-44ec-918b-091522188ae9
ms.tgt_platform: multiple
keywords:
- Example Code for Creating an Attribute AD
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Creating an Attribute

The following code example creates an [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) object in the schema container.

The **CreateAttribute** function creates an [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) object in the schema container, but does not commit it to the directory. Call the [**IADs.SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) method to commit the new **attributeSchema** object to the directory.

The **BytesToVariantArray** function is a utility function that packs an octet string into a variant array.


```C++
/********************************************************************

    BytesToVariantArray()

    Converts an arrya of BYTEs into a VARIANT array.

    Parameters:

    pValue = Contains an array of BYTES to convert. cValueElements 
    contains the number of elements in this array.

    cValueElements - Contains the number of elements in the pValue
    array.

    pVariant - Receives the VARIANT that contains an octet string
    (VT_UI1 | VT_ARRAY)

*********************************************************************/

HRESULT BytesToVariantArray(
    PBYTE pValue,
    ULONG cValueElements,
    VARIANT *pVariant
    )
{
    HRESULT hr = E_FAIL;
    SAFEARRAY *pArrayVal = NULL;
    SAFEARRAYBOUND arrayBound;
    CHAR HUGEP *pArray = NULL;

    // Check parameters.
    if((NULL == pValue) || !(cValueElements > 0))
    {
        return E_INVALIDARG;
    }
 
    // Set bound for array.
    arrayBound.lLbound = 0;
    arrayBound.cElements = cValueElements;
 
    // Create the safe array for the octet string. unsigned char
    // elements;single dimension;aBound size.
    pArrayVal = SafeArrayCreate(VT_UI1, 1, &arrayBound);
 
    if (!(NULL == pArrayVal))
    {
        hr = SafeArrayAccessData(pArrayVal,
                                 (void HUGEP * FAR *) &pArray);
        if (SUCCEEDED(hr))
        {
            // Copy the bytes to the safe array.
            memcpy(pArray, pValue, arrayBound.cElements);
            SafeArrayUnaccessData(pArrayVal);
            
            // Set type to array of unsigned char.
            V_VT(pVariant) = VT_ARRAY | VT_UI1;
            
            // Assign the safe array to the array member.
            V_ARRAY(pVariant) = pArrayVal;
            
            hr = S_OK;
        }
        else
        {
            // Cleanup if the array cannot be accessed.
            if (pArrayVal)
            {
                SafeArrayDestroy(pArrayVal);
            }
        }
    }
    else
    {
      hr = E_OUTOFMEMORY;
    }
 
    return hr;
}

/*******************************************************************

    CreateAttribute()

    Creates a new attribute in the schema container 
    IADsContainer.Create. 
    This function creates the attributeSchema object, but does not 
    commit it to the directory. The caller must call IADs.SetInfo
    on the new attribute object to commit it to the directory.

    Parameters:

    pwszAttributeName - Contains a null-terminated string that
    contains the name of the attribute.

    pwszLDAPDisplayName - Contains a null-terminated string that 
    contains the lDAPDisplayName of the attribute.

    pwszAttributeOID - Contains a null-terminated string that 
    contains the OID of the attribute.

    pSchemaIDGUID - 
    pwszAttributeSyntax - Contains a null-terminated string that 
    contains the syntax of the attribute.

    iOmSyntax - Contains the value for the oMSyntax attribute.

    pbomObjectClass - Pointer to a BYTE array that contains the 
    value for the oMObjectClass attribute. dwSizeomObjectClass 
    contains the number of elements in this array.

    dwSizeomObjectClass - Contains the number of elements in the 
    pbomObjectClass array.

    pwszDescription - Contains a null-terminated string that 
    contains the description of the attribute.

    fIsSingleValued - Contains TRUE if the attribute is 
    single-valued or FALSE if the attribute is multi-valued.

    fIsInGC - Contains TRUE if the attribute is contained in the
    global catalog or FALSE if the attribute should not be 
    contained in the global catalog.
    
    fIsIndexed - Contains TRUE if the attribute is indexed or 
    FALSE if the attribute is not indexed.
    
    iLowerRange - Contains the lower range of the attribute value.
    Contains zero if the range should not be set.
    
    iUpperRange - Contains the upper range of the attribute value. 
    Contains zero if the range should not be set.
    
    iLinkID - Contains the value for the linkID attribute. If this
    cotnains zero, the linkID attribute is not set.
    
    pwszAdminDisplayName - Contains a null-terminated string that 
    contains the admin display name of the attribute.
    
    ppadsNewAttribute - Receives a pointer to the IADs interface of 
    the attribute object created.

********************************************************************/

HRESULT CreateAttribute(
    LPCWSTR pwszAttributeName,
    LPCWSTR pwszLDAPDisplayName,
    LPCWSTR pwszAttributeOID,
    const GUID * pSchemaIDGUID,
    LPCWSTR pwszAttributeSyntax,
    int iOmSyntax,
    PBYTE pbomObjectClass, 
    DWORD dwSizeomObjectClass,
    LPCWSTR pwszDescription,
    BOOL fIsSingleValued,
    BOOL fIsInGC,
    BOOL fIsIndexed,
    int iLowerRange,
    int iUpperRange,
    int iLinkID,
    LPCWSTR pwszAdminDisplayName,
    IADs **ppadsNewAttribute
    )
{
    if(!ppadsNewAttribute)
    {
        return E_POINTER;
    }

    *ppadsNewAttribute = NULL;

    if( (!pwszAttributeName) ||
        (!pwszAttributeOID) ||
        (!pwszAttributeSyntax) ||
        (!iOmSyntax)
    )
    {
        return E_INVALIDARG;
    }

    if(iLowerRange < iUpperRange)
    {
        return E_INVALIDARG;
    }

    HRESULT hr;
    CComPtr<IADs> spRoot;

    hr = ADsGetObject(L"LDAP://RootDSE",
                    IID_IADs,
                    (void**)&spRoot);
    if(FAILED(hr))
    {
        return hr;
    }

    CComVariant svarSchema;
     
    // Get the disintguished name of the schema container.
    hr = spRoot->Get(CComBSTR("schemaNamingContext"), &svarSchema);
    if(FAILED(hr))
    {
        return hr;
    }

    // Bind to the IADsContainer interface of the schema container.
    CComPtr<IADsContainer> spSchemaCont;
    hr = ADsOpenObject( L"LDAP://RootDSE",
                        NULL,
                        NULL,
                        ADS_SECURE_AUTHENTICATION,
                        IID_IADs,
                        (void**)&spSchemaCont);
    if(FAILED(hr))
    {
        return hr;
    }

    CComPtr<IDispatch> spDisp;

    CComBSTR sbstrAttribute = "CN=";
    sbstrAttribute += pwszAttributeName;
    
    // Create the object in the schema container.
    hr = spSchemaCont->Create(CComBSTR("attributeSchema"), 
                              sbstrAttribute, 
                              &spDisp);
    CComPtr<IADs> spNewAttribute;
    hr = spDisp->QueryInterface(IID_IADs, (void**)&spNewAttribute);
    if(FAILED(hr))
    {
        return hr;
    }

    CComBSTR sbstrAttributeToSet;
    CComVariant svar;

    // Put this value so that it can be read from the cache.
    sbstrAttributeToSet = "cn";
    svar = pwszAttributeName;
    hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
    if(FAILED(hr))
    {
        return hr;
    }
    
    // Put lDAPDisplayName.
    // If NULL, let it default; that is, do not set it.
    if (pwszLDAPDisplayName)
    {
        sbstrAttributeToSet = "lDAPDisplayName";
        svar = pwszLDAPDisplayName;
        hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
        if(FAILED(hr))
        {
            return hr;
        }
    }
    
    // Put attributeID.
    sbstrAttributeToSet = "attributeID";
    svar = pwszAttributeOID;
    hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
    if(FAILED(hr))
    {
        return hr;
    }
    
    
    // Put schemaIDGUID.
    // If NULL, let it default; that is, do not set it.
    if (pSchemaIDGUID)
    {
        hr = BytesToVariantArray(
            (LPBYTE)pSchemaIDGUID,
            sizeof(GUID),
            &svar
            );
        if(FAILED(hr))
        {
            return hr;
        }

        sbstrAttributeToSet = "schemaIDGUID";
        hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
        if(FAILED(hr))
        {
            return hr;
        }
    }
    
    // Put attributeSyntax.
    sbstrAttributeToSet = "attributeSyntax";
    svar = pwszAttributeSyntax;
    hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
    if(FAILED(hr))
    {
        return hr;
    }
    
    // Put oMSyntax.
    sbstrAttributeToSet = "oMSyntax";
    svar = iOmSyntax;
    hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
    if(FAILED(hr))
    {
        return hr;
    }
    
    // Put searchFlags.
    sbstrAttributeToSet = "searchFlags";
    if (fIsIndexed)
    {
        svar = 1;
    }
    else
    {
        svar = 0;
    }
    hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
    if(FAILED(hr))
    {
        return hr;
    }

    // Put isSingleValued.
    sbstrAttributeToSet = "isSingleValued";
    if (fIsSingleValued)
    {
        svar = VARIANT_TRUE;
    }
    else
    {
        svar = VARIANT_FALSE;
    }
    hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
    if(FAILED(hr))
    {
        return hr;
    }
    
    
    // Put isMemberOfPartialAttributeSet.
    sbstrAttributeToSet = "isMemberOfPartialAttributeSet";
    if (fIsInGC)
    {
        svar = VARIANT_TRUE;
    }
    else
    {
        svar = VARIANT_FALSE;
    }
    svar.vt = VT_BOOL;
    hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
    if(FAILED(hr))
    {
        return hr;
    }
    
    
    // Put description.
    sbstrAttributeToSet = "description";
    svar = pwszDescription;
    hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
    if(FAILED(hr))
    {
        return hr;
    }
    
    // Put rangeLower and rangeUpper.
    // If both are 0, let them default; that is do not set them.
    if ((iLowerRange >= 0) && (iUpperRange > 0))
    {
        // Set rangeUpper.
        sbstrAttributeToSet = "rangeUpper";
        svar = iUpperRange;
        hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
        if(FAILED(hr))
        {
            return hr;
        }

        // Set rangeLower.
        sbstrAttributeToSet = "rangeLower";
        svar = iLowerRange;
        hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
        if(FAILED(hr))
        {
            return hr;
        }
    }
    
    // Put linkID. If linkID is 0, let it default; that 
    // is, do not set it.
    if (iLinkID>0)
    {
        sbstrAttributeToSet = "linkID";
        svar = iLinkID;
        hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
        if(FAILED(hr))
        {
            return hr;
        }
    }
    
    // Put adminDisplayName.
    // If NULL, set it to the same string as cn.
    sbstrAttributeToSet = "adminDisplayName";
    if (!pwszAdminDisplayName)
    {
        svar = pwszAttributeName;
    }
    else
    {
        svar = pwszAdminDisplayName;
    }
    hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
    if(FAILED(hr))
    {
        return hr;
    }
        
    // Put omObjectClass.
    // Only set this if used to delineate omSyntax 127 attributes.
    if (pbomObjectClass && dwSizeomObjectClass) 
    {
        hr = BytesToVariantArray(
            pbomObjectClass,
            dwSizeomObjectClass,
            &svar
            );
        if(FAILED(hr))
        {
            return hr;
        }

        sbstrAttributeToSet = "omObjectClass";
        hr = spNewAttribute->Put(sbstrAttributeToSet, svar);
        if(FAILED(hr))
        {
            return hr;
        }
    }

    // Get a copy of the interface to return.
    hr = spNewAttribute->QueryInterface(IID_IADs, 
                                        (LPVOID*)ppadsNewAttribute);
     
    return hr;
}
```



 

 