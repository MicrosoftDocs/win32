---
title: StgCreatePropSetStg Sample
description: Shows how the StgCreatePropSetStg function can be used to create an IPropertySetStorage interface on top of any given IStorage interface.
ms.assetid: f0d0664a-2cfd-4eb0-b1d5-47d1545394fd
keywords:
- Structured Storage Strctd Stg , samples, StgCreatePropSetStg
ms.topic: article
ms.date: 05/31/2018
---

# StgCreatePropSetStg Sample

The StgCreatePropSetStg.cpp sample shows how the [**StgCreatePropSetStg**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatepropsetstg) function can be used to create an [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface on top of any given [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface.


```C++
//+===================================================================
//
// To Build:   cl /GX StgCreatePropSetStg.cpp
//
//+===================================================================

#define UNICODE
#define _UNICODE
#define WIN32_LEAN_AND_MEAN

#include <stdio.h>
#include <windows.h>
#include <ole2.h>

#pragma comment( lib, "ole32.lib" )

IPropertyStorage*
CreatePropertySetInStorage( IStorage *pStg, const FMTID &fmtid )
{
    HRESULT hr = S_OK;
    IPropertySetStorage *pPropSetStg = NULL;
    IPropertyStorage *pPropStg = NULL;

    try
    {
        hr = StgCreatePropSetStg( pStg, 0 /*reserved*/, 
                                  &pPropSetStg );
        if( FAILED(hr) ) 
            throw L"Failed StgCreatePropSetStg (%08x)";

        hr = pPropSetStg->Create( fmtid, NULL,
            PROPSETFLAG_DEFAULT,
            STGM_CREATE | STGM_READWRITE | STGM_SHARE_EXCLUSIVE,
            &pPropStg );
        if( FAILED(hr) ) 
            throw L"Failed IPropertySetStorage::Create (%08x)";

        // Success. The caller must now call Release on both
        // pPropSetStg and pStg.

    }
    catch( const WCHAR *pwszError )
    {
        wprintf( L"Error: %s (%08x)\n", pwszError, hr );
    }

    if( NULL != pPropSetStg )
        pPropSetStg->Release();

    return( pPropStg );
}


extern "C" void wmain()
{
    HRESULT hr = S_OK;
    IStorage *pStg = NULL;
    IPropertyStorage *pPropStg = NULL;

    try
    {
        // Create an object with an IStorage interface. It is not 
        // necessary that it be a system-provided storage, such as 
        // that obtained by this call.  Any object that implements 
        // IStorage can be used.

        hr = StgCreateStorageEx( NULL,  // Create a temporary storage.
                                 STGM_CREATE
                                    | STGM_READWRITE
                                    | STGM_SHARE_EXCLUSIVE,
                                 STGFMT_STORAGE,
                                 0, NULL, NULL,
                                 IID_IStorage,
                                 reinterpret_cast<void**>(&pStg) );
        if( FAILED(hr) ) throw L"Failed StgCreateStorageEx";

        // Get and use an IPropertySetStorage that represents this 
        // IStorage.

        pPropStg = CreatePropertySetInStorage( pStg, 
                                        FMTID_SummaryInformation );
        if( NULL == pPropStg ) 
           throw L"Failed CreatePropertySetInStorage";

        // Here you could call IPropertyStorage methods, such as 
        // WriteMultiple andReadMultiple, using the pPropStg pointer.

        printf( "Success\n" );
    }
    catch( const WCHAR *pwszError )
    {
        wprintf( L"Error: %s (%08x)\n", pwszError, hr );
    }

    if( NULL != pPropStg )
        pPropStg->Release();
    if( NULL != pStg )
        pStg->Release();

}
```



 

 




