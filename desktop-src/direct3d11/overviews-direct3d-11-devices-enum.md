---
title: How To Enumerate Adapters
description: This topic shows how to use Microsoft DirectX Graphics Infrastructure (DXGI) to enumerate the available graphics adapters on a computer.
ms.assetid: f8ef981c-363e-4ac8-8734-69c68f346950
ms.topic: article
ms.date: 05/31/2018
---

# How To: Enumerate Adapters

This topic shows how to use Microsoft DirectX Graphics Infrastructure (DXGI) to enumerate the available graphics adapters on a computer. Direct3D 10 and 11 can use DXGI to enumerate adapters.

You generally need to enumerate adapters for these reasons:

-   To determine how many graphics adapters are installed on a computer.
-   To help you choose which adapter to use to create a Direct3D device.
-   To retrieve an [**IDXGIAdapter**](/windows/desktop/api/dxgi/nn-dxgi-idxgiadapter) object that you can use to retrieve device capabilities.

**To enumerate adapters**

1.  Create an [**IDXGIFactory**](/windows/desktop/api/dxgi/nn-dxgi-idxgifactory) object by calling the [**CreateDXGIFactory**](/windows/desktop/api/dxgi/nf-dxgi-createdxgifactory) function. The following code example demonstrates how to initialize an **IDXGIFactory** object.
    ```
    IDXGIFactory * pFactory = NULL;

    CreateDXGIFactory(__uuidof(IDXGIFactory) ,(void**)&pFactory)
    ```

    

2.  Enumerate through each adapter by calling the [**IDXGIFactory::EnumAdapters**](/windows/desktop/api/dxgi/nf-dxgi-idxgifactory-enumadapters) method. The *Adapter* parameter allows you to specify a zero-based index number of the adapter to enumerate. If no adapter is available at the specified index, the method returns [**DXGI\_ERROR\_NOT\_FOUND**](/windows/desktop/direct3ddxgi/dxgi-error).

    The following code example demonstrates how to enumerate through the adapters on a computer.

    ```
    for (UINT i = 0; 
         pFactory->EnumAdapters(i, &pAdapter) != DXGI_ERROR_NOT_FOUND; 
         ++i) 
    { ... }
    ```

    

The following code example demonstrates how to enumerate all adapters on a computer.

> [!Note]  
> For Direct3D 11.0 and later, we recommend that apps always use [**IDXGIFactory1**](/windows/desktop/api/dxgi/nn-dxgi-idxgifactory1) and [**CreateDXGIFactory1**](/windows/desktop/api/dxgi/nf-dxgi-createdxgifactory1) instead.

 


```C++
std::vector <IDXGIAdapter*> EnumerateAdapters(void)
{
    IDXGIAdapter * pAdapter; 
    std::vector <IDXGIAdapter*> vAdapters; 
    IDXGIFactory* pFactory = NULL; 
    

    // Create a DXGIFactory object.
    if(FAILED(CreateDXGIFactory(__uuidof(IDXGIFactory) ,(void**)&pFactory)))
    {
        return vAdapters;
    }


    for ( UINT i = 0;
          pFactory->EnumAdapters(i, &pAdapter) != DXGI_ERROR_NOT_FOUND;
          ++i )
    {
        vAdapters.push_back(pAdapter); 
    } 


    if(pFactory)
    {
        pFactory->Release();
    }

    return vAdapters;

}
```



## Related topics

<dl> <dt>

[How to Use Direct3D 11](how-to-use-direct3d-11.md)
</dt> </dl>

 

 