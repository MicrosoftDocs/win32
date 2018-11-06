---
title: Example Code for Converting an objectSid into a Bindable String
description: This topic contains a code example that converts an objectSid to a bindable string to add a member that belongs to a down-level domain to a group in an up-level domain.
ms.assetid: 8308c2e1-1a6f-4bbe-84fd-03b5fe13f0ec
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Converting an objectSid into a Bindable String

This topic contains a code example that converts an **objectSid** to a bindable string to add a member that belongs to a down-level domain to a group in an up-level domain.

The following C++ code example shows how to convert an **objectSid** into a bindable string.


```C++

HRESULT VariantArrayToBytes(VARIANT Variant, 
                            LPBYTE *ppBytes, 
                            DWORD *pdwBytes);

/********************************************************************

    GetLDAPSidBindStringFromVariantSID()

    Converts a SID in VARIANT form, such as an objectSid value,  
    and converts it into a bindale string in the form:

    LDAP://<SID=xxxxxxx...>

    The returned string is allocated with AllocADsMem and must  
    be freed by the caller with FreADsMem.

*******************************************************************/

LPWSTR GetLDAPSidBindStringFromVariantSID(VARIANT vSID)
{
    LPWSTR pwszReturn = NULL;

    if(vSID.vt != VT_EMPTY) 
    {
        HRESULT hr;
        LPBYTE pByte;
        DWORD dwBytes = 0;

        hr = VariantArrayToBytes(vSID, &pByte, &dwBytes);
        if(S_OK == hr)
        {
            // Convert the BYTE array into a string of 
            // hex characters.
            CComBSTR sbstrTemp = "LDAP://<SID=";

            for(DWORD i = 0; i < dwBytes; i++)
            {
                WCHAR wszByte[3];

                swprintf_s(wszByte, L"%02x", pByte[i]);
                sbstrTemp += wszByte;
            }

            sbstrTemp += ">";
            pwszReturn = 
              (LPWSTR)AllocADsMem((sbstrTemp.Length() + 1) * 
                                   sizeof(WCHAR));
            if(pwszReturn)
            {
                wcscpy_s(pwszReturn, sbstrTemp.m_str);
            }

            FreeADsMem(pByte);
        }
    }

    return pwszReturn;
}

/******************************************************************

    VariantArrayToBytes()

    This function converts a VARIANT array into an array of BYTES.  
    This function allocates the buffer using AllocADsMem. The caller 
    must free this memory with FreeADsMem when it is no longer 
    required.

******************************************************************/

HRESULT VariantArrayToBytes(VARIANT Variant, 
                            LPBYTE *ppBytes,  
                            DWORD *pdwBytes)
{
    if(!(Variant.vt & VT_ARRAY) ||
        !Variant.parray ||
        !ppBytes ||
        !pdwBytes)
    {
        return E_INVALIDARG;
    }

    *ppBytes = NULL;
    *pdwBytes = 0;

    HRESULT hr = E_FAIL;
    SAFEARRAY *pArrayVal = NULL;
    CHAR HUGEP *pArray = NULL;
    
    // Retrieve the safe array.
    pArrayVal = Variant.parray;
    DWORD dwBytes = pArrayVal->rgsabound[0].cElements;
    *ppBytes = (LPBYTE)AllocADsMem(dwBytes);
    if(NULL == *ppBytes) 
    {
        return E_OUTOFMEMORY;
    }

    hr = SafeArrayAccessData(pArrayVal, (void HUGEP * FAR *) &pArray);
    if(SUCCEEDED(hr))
    {
        // Copy the bytes to the safe array.
        CopyMemory(*ppBytes, pArray, dwBytes);
        SafeArrayUnaccessData( pArrayVal );
        *pdwBytes = dwBytes;
    }
    
    return hr;
}
```



 

 




