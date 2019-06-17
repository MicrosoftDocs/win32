---
title: Retrieving an Object from a Collection
description: Retrieving an Object from a Collection
ms.assetid: df7cbff5-2d09-4031-8f41-3f4eea51598f
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving an Object from a Collection

The following code retrieves the IP address of a client from a collection of clients. The variable pClientsCollection points to an [**ISdoCollection**](https://docs.microsoft.com/windows/desktop/api/sdoias/nn-sdoias-isdocollection) interface for the collection. See [Retrieving a Collection](https://docs.microsoft.com/windows/desktop/Nps/sdo-retrieving-a-collection) for information on how to retrieve the collection object.


```C++
   HRESULT hr
   _variant_t vtClientName = L"Test Client";
   
   //
   // Get the client "Test Client" from the collection of clients
   //
   CComPtr<IDispatch> pFoundClientDispatch;
   hr = pClientsCollection->Item(&vtClientName, &pFoundClientDispatch);
   if (FAILED(hr))
   {
      return hr;
   }

   CComPtr<ISdo> pFoundClientSdo;
   hr = pFoundClientDispatch->QueryInterface(
      __uuidof(ISdo),
      (void **) &pFoundClientSdo
   );
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Get the IP address of that client 
   //
   _variant_t vtAddress;
   hr = pFoundClientSdo->GetProperty(PROPERTY_CLIENT_ADDRESS ,&vtAddress);
   if (FAILED(hr))
   {
      return hr;
   }
```



## Related topics

<dl> <dt>

[**ISdoCollection::Item**](https://docs.microsoft.com/windows/desktop/api/sdoias/nf-sdoias-isdocollection-item)
</dt> <dt>

[Retrieving a Collection](https://docs.microsoft.com/windows/desktop/Nps/sdo-retrieving-a-collection)
</dt> <dt>

[**SysAllocString**](https://msdn.microsoft.com/en-us/library/ms221458(v=VS.71).aspx)
</dt> <dt>

[**SysFreeString**](https://msdn.microsoft.com/en-us/library/ms221481(v=VS.71).aspx)
</dt> <dt>

[**VARIANT**](https://msdn.microsoft.com/en-us/library/ms221627(v=VS.71).aspx)
</dt> </dl>

 

 




