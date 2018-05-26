---
title: Enumeration Helper Functions
description: There are three enumerator helper functions that can be used from C/C++ to aid in the navigation of Active Directory objects. They are ADsBuildEnumerator, ADsEnumerateNext, and ADsFreeEnumerator.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 019958c8-5bf5-45eb-871c-796ff3750cdc
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- ADsBuildEnumerator ADSI ,using
- ADsEnumerateNext ADSI ,using
- ADsFreeEnumerator ADSI ,using
- ADSI ADSI ,example code C/C++ ,using ADsBuildEnumerator ADsEnumerateNext and ADsFreeEnumerator
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enumeration Helper Functions

There are three enumerator helper functions that can be used from C/C++ to aid in the navigation of Active Directory objects. They are [**ADsBuildEnumerator**](/windows/win32/Adshlp/nf-adshlp-adsbuildenumerator?branch=master), [**ADsEnumerateNext**](/windows/win32/Adshlp/nf-adshlp-adsenumeratenext?branch=master), and [**ADsFreeEnumerator**](/windows/win32/Adshlp/nf-adshlp-adsfreeenumerator?branch=master).

## ADsBuildEnumerator

The [**ADsBuildEnumerator**](/windows/win32/Adshlp/nf-adshlp-adsbuildenumerator?branch=master) helper function encapsulates the code required to create an enumerator object. It calls the [**IADsContainer::get\_\_NewEnum**](/windows/win32/Iads/nf-iads-iadscontainer-get__newenum?branch=master) method to create an enumerator object and then calls the [**QueryInterface**](_com_iunknown_queryinterface) method of [**IUnknown**](_com_iunknown) to get a pointer to the [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface for that object. The enumeration object is the Automation mechanism to enumerate over containers. Use the [**ADsFreeEnumerator**](/windows/win32/Adshlp/nf-adshlp-adsfreeenumerator?branch=master) function to release this enumerator object.

## ADsEnumerateNext

The [**ADsEnumerateNext**](/windows/win32/Adshlp/nf-adshlp-adsenumeratenext?branch=master) helper function populates a VARIANT array with elements fetched from an enumerator object. The number of elements retrieved can be smaller than the number requested.

## ADsFreeEnumerator

Frees an enumerator object previously created through the [**ADsBuildEnumerator**](/windows/win32/Adshlp/nf-adshlp-adsbuildenumerator?branch=master) function.

The following code example shows a function that uses enumerator helper functions in C++.


```C++
/*****************************************************************************
  Function:    TestEnumObject
  Arguments:   pszADsPath - ADsPath of the container to be enumerated (WCHAR*).
  Return:      S_OK if successful, an error code otherwise.
  Purpose:     Example using ADsBuildEnumerator, ADsEnumerateNext and
               ADsFreeEnumerator.
******************************************************************************/
#define MAX_ENUM      100  
 
HRESULT
TestEnumObject( LPWSTR pszADsPath )
{
    ULONG cElementFetched = 0L;
    IEnumVARIANT * pEnumVariant = NULL;
    VARIANT VariantArray[MAX_ENUM];
    HRESULT hr = S_OK;
    IADsContainer * pADsContainer =  NULL;
    DWORD dwObjects = 0, dwEnumCount = 0, i = 0;
    BOOL  fContinue = TRUE;
 
 
    hr = ADsGetObject(
                pszADsPath,
                IID_IADsContainer,
                (void **)&amp;pADsContainer
                );
 
 
    if (FAILED(hr)) {
 
        printf("\"%S\" is not a valid container object.\n", pszADsPath) ;
        goto exitpoint ;
    }
 
    hr = ADsBuildEnumerator(
            pADsContainer,
            &amp;pEnumVariant
            );
 
    if( FAILED( hr ) )
    {
      printf("ADsBuildEnumerator failed with %lx\n", hr ) ;
      goto exitpoint ;
    }
 
    fContinue  = TRUE;
    while (fContinue) {
 
        IADs *pObject ;
 
        hr = ADsEnumerateNext(
                    pEnumVariant,
                    MAX_ENUM,
                    VariantArray,
                    &amp;cElementFetched
                    );

        if ( FAILED( hr ) )
        {
            printf("ADsEnumerateNext failed with %lx\n",hr);
            goto exitpoint;
        }
 
        if (hr == S_FALSE) {
            fContinue = FALSE;
        }
 
        dwEnumCount++;
 
        for (i = 0; i < cElementFetched; i++ ) {
 
            IDispatch *pDispatch    = NULL;
            BSTR        bstrADsPath = NULL;
 
            pDispatch = VariantArray[i].pdispVal;
 
            hr = V_DISPATCH( VariantArray + i )->QueryInterface(IID_IADs, (void **) &amp;pObject) ;
 
            if( SUCCEEDED( hr ) )
            {
               pObject->get_ADsPath( &amp;bstrADsPath );
               printf( "%S\n", bstrADsPath );
            }
            pObject->Release();
            VariantClear( VariantArray + i );
            SysFreeString( bstrADsPath );
        }
 
        dwObjects += cElementFetched;
    }
 
    printf("Total Number of Objects enumerated is %d\n", dwObjects);
 
exitpoint:
    if (pEnumVariant) {
        ADsFreeEnumerator( pEnumVariant );
    }
 
    if (pADsContainer) {
        pADsContainer->Release();
    }
 
    return(hr);
}
```



 

 




