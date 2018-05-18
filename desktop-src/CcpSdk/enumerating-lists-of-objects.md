---
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'deb78fce-f029-4a71-b70b-0915dba0db8e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Enumerating Lists of Objects
---

# Enumerating Lists of Objects

HPC defines the following types of collections:

-   [**ISchedulerCollection**](ischedulercollection.md) (generic collection of objects)
-   [**IStringCollection**](istringcollection.md) (collection of strings)
-   [**IIntCollection**](iintcollection.md) (collection of integers)
-   [**INameValueCollection**](inamevaluecollection2.md) (collection of name/value pairs)

For C++ users, there are two ways to enumerate the items in a generic collection. The first is to get an enumerator and use it to enumerate the items in the collection, and the second is to use the count and indexer properties to enumerate the items.

The items in a generic collection are variants. The type of data in a generic collection determines which member of the variant you use to access the item data. For collections of objects, query the **pdispVal** member for the desired interface; for collections of strings, access the **bstrVal** member; and for long integer values, access the **lval** member.

The [**INameValueCollection**](inamevaluecollection2.md) collection does not contain an indexer, so you must use the enumerator to enumerate items in the collection. If you use the indexer for the [**IStringCollection**](istringcollection.md) and [**IIntCollection**](iintcollection.md) collections, the data is returned as a string or integer, respectively.

The following example shows the different ways to enumerate items in a collection for C++ users.


```C++
#include <windows.h>
#include <stdio.h>

// The Microsoft.Hpc.Scheduler.tlb and Microsoft.Hpc.Scheduler.Properties.tlb type
// libraries are included in the Microsoft HPC Pack 2008 SDK. The type libraries are
// located in the "Microsoft HPC Pack 2008 SDK\Lib\i386" or \amd64 folder. Include the rename 
// attributes to avoid name collisions.
#import <Microsoft.Hpc.Scheduler.tlb> named_guids no_namespace raw_interfaces_only \
    rename("SetEnvironmentVariable","SetHpcEnvironmentVariable") \
    rename("AddJob", "AddHpcJob")
#import <Microsoft.Hpc.Scheduler.Properties.tlb> named_guids no_namespace raw_interfaces_only 

void EnumerateUsingEnumerator(ISchedulerCollection* pCollection);
void EnumerateUsingIndexer(ISchedulerCollection* pNodes);
void EnumeratingStringCollections(IStringCollection* pNodeGroups);

void main(void)
{
    HRESULT hr = S_OK;
    IScheduler* pScheduler = NULL;
    ISchedulerCollection* pCollection = NULL;

    CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);

    // Get an instance of the Scheduler object. 
    hr = CoCreateInstance( __uuidof(Scheduler), // CLSID_Scheduler, 
                           NULL,
                           CLSCTX_INPROC_SERVER,
                           __uuidof(IScheduler), // IID_IScheduler, 
                           reinterpret_cast<void **> (&amp;pScheduler) );

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(IScheduler) failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pScheduler->Connect(_bstr_t(L"localhost"));
    if (FAILED(hr))
    {
        wprintf(L"pScheduler->Connect failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Connected to localhost\n\n");

    hr = pScheduler->GetNodeList(NULL, NULL, &amp;pCollection);
    if (FAILED(hr))
    {
        wprintf(L"pScheduler->GetNodeList failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Enumerating a list using an enumerator...\n");
    EnumerateUsingEnumerator(pCollection);

    wprintf(L"\nEnumerating a list using an indexer...\n");
    EnumerateUsingIndexer(pCollection);

cleanup:

    // Before exiting, release your instance of IScheduler.
    if (pScheduler)
        pScheduler->Release();

    if (pCollection)
        pCollection->Release();

    CoUninitialize();
}


void EnumerateUsingEnumerator(ISchedulerCollection* pCollection)
{
    HRESULT hr = S_OK;
    IEnumVARIANT* pNodes = NULL;
    ISchedulerNode* pNode = NULL;
    IStringCollection* pNodeGroups = NULL;
    VARIANT var;
    BSTR bstr = NULL;

    hr = pCollection->GetEnumerator(&amp;pNodes);
    if (FAILED(hr))
    {
        wprintf(L"pCollection->GetEnumerator failed with 0x%x.\n", hr);
        goto cleanup;
    }

    VariantInit(&amp;var);

    while (S_OK == (hr = pNodes->Next(1, &amp;var, NULL)))
    {
        // The type of data in the collection determines which member of
        // the variant you use to access the item data. For collections of
        // objects, query the pdispVal member for the desired interface; for 
        // collections of strings, access the bstrVal member; and for long 
        // integer values, access the lval member.

        var.pdispVal->QueryInterface(IID_ISchedulerNode, reinterpret_cast<void **>(&amp;pNode));
        VariantClear(&amp;var);

        hr = pNode->get_Name(&amp;bstr);
        if (FAILED(hr))
        {
            wprintf(L"pNode->get_Name failed with 0x%x.\n", hr);
            goto cleanup;
        }

        wprintf(L"%s\n", bstr);
        SysFreeString(bstr);

        hr = pNode->get_NodeGroups(&amp;pNodeGroups);
        if (FAILED(hr))
        {
            wprintf(L"pNode->get_NodeGroups failed with 0x%x.\n", hr);
            goto cleanup;
        }

        EnumeratingStringCollections(pNodeGroups);

        // TODO: Use pNode to retrieve the properties of the node.

        pNode->Release();
        pNode = NULL;
        VariantClear(&amp;var);
    }

    if (S_FALSE != hr)
    {
        wprintf(L"pNodes->Next failed with 0x%x.\n", hr);
        goto cleanup;
    }

cleanup:

    if (pNodes)
        pNodes->Release();;

    if (pNode)
        pNode->Release();

    if (pNodeGroups)
        pNodeGroups->Release();
}


void EnumerateUsingIndexer(ISchedulerCollection* pNodes)
{
    HRESULT hr = S_OK;
    ISchedulerNode* pNode = NULL;
    IStringCollection* pNodeGroups = NULL;
    VARIANT var;
    BSTR bstr = NULL;
    long count = 0;

    hr = pNodes->get_Count(&amp;count);
    if (FAILED(hr))            
    {
        wprintf(L"pNodes->get_Count failed with 0x%x.\n", hr);
        goto cleanup;
    }

    VariantInit(&amp;var);

    for (long i = 0; i < count; i++)
    {
        hr = pNodes->get_Item(i, &amp;var);
        if (FAILED(hr))
        {
            wprintf(L"pNodes->get_Item failed with 0x%x.\n", hr);
            goto cleanup;
        }

        // The type of data in the collection determines which member of
        // the variant you use to access the item data. For collections of
        // objects, query the pdispVal member for the desired interface; for 
        // collections of strings, access the bstrVal member; and for long 
        // integer values, access the lval member.

        var.pdispVal->QueryInterface(IID_ISchedulerNode, reinterpret_cast<void **>(&amp;pNode));
        VariantClear(&amp;var);

        hr = pNode->get_Name(&amp;bstr);
        if (FAILED(hr))
        {
            wprintf(L"pNode->get_Name failed with 0x%x.\n", hr);
            goto cleanup;
        }

        wprintf(L"%s\n", bstr);
        SysFreeString(bstr);

        hr = pNode->get_NodeGroups(&amp;pNodeGroups);
        if (FAILED(hr))
        {
            wprintf(L"pNode->get_NodeGroups failed with 0x%x.\n", hr);
            goto cleanup;
        }

        EnumeratingStringCollections(pNodeGroups);

        // TODO: Use pNode to retrieve the properties of the node.

        pNode->Release();
        pNode = NULL;
    }

cleanup:

    if (pNodes)
        pNodes->Release();;

    if (pNode)
        pNode->Release();

    if (pNodeGroups)
        pNodeGroups->Release();
}


void EnumeratingStringCollections(IStringCollection* pNodeGroups)
{
    HRESULT hr = S_OK;
    BSTR bstr = NULL;
    long count = 0;

    wprintf(L"The node belongs to the following node groups:\n");


    hr = pNodeGroups->get_Count(&amp;count);
    if (FAILED(hr))
    {
        wprintf(L"pNodeGroups->get_Count failed with 0x%x.\n", hr);
    }

    for (long i = 0; i < count; i++)
    {
        hr = pNodeGroups->get_Item(i, &amp;bstr);
        if (FAILED(hr))
        {
            wprintf(L"pNodeGroups->get_Item failed with 0x%x.\n", hr);
            break;
        }

        wprintf(L"\t%s\n", bstr);
        SysFreeString(bstr);
        bstr = NULL;
    }
}
```



## Related topics

<dl> <dt>

[Using HPC](using-hpc.md)
</dt> </dl>

 

 



