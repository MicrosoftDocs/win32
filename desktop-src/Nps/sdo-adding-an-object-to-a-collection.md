---
title: Adding an Object to a Collection
description: Adding an Object to a Collection
ms.assetid: fc62698d-0bb9-478c-91cf-9f8fec36dba4
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Adding an Object to a Collection

The following code adds a new policy to the IAS policies collection. The variable pClientsCollection points to an [**ISdoCollection**](/windows/desktop/api/sdoias/nn-sdoias-isdocollection) interface for the collection. See [Retrieving a Collection](/windows/desktop/Nps/sdo-retrieving-a-collection) for information on how to retrieve the collection object.


```C++
   HRESULT hr;
   _bstr_t      bstrClientName = L"Test Client";
   VARIANT_BOOL vbNameUnique = VARIANT_FALSE;

   //
   // Check if the new client's name is unique
   //

   hr = pClientsCollection->IsNameUnique(bstrClientName, &vbNameUnique);
   if (FAILED(hr))
   {
      return hr;
   }

   if (VARIANT_FALSE == vbNameUnique)
   {
      //
      // The name is not unique. Handle the error
      //
      return E_FAIL;
   }

   //
   // Name is unique. Add the client.
   //
   CComPtr<IDispatch> pClientDispatch;
   pClientDispatch.p = NULL;
   hr = pClientsCollection->Add(bstrClientName, &pClientDispatch);
   if (FAILED(hr))
   {
      return hr;
   }

   CComPtr<ISdo> pClientSDO;
   hr = pClientDispatch->QueryInterface(
      __uuidof(ISdo),
      (void**) &pClientSDO
   );
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Set the address for the client
   //
   _variant_t  vtClientAddress = L"127.0.0.1";
   hr = pClientSDO->PutProperty(PROPERTY_CLIENT_ADDRESS, &vtClientAddress);
   if (FAILED(hr))
   {
      return hr;
   }
       
   //
   // Set the shared secret for the client
   //
   _variant_t  vtClientSecret = L">@U#'6cc='5Ly9O5QKEj2RTJr*fM";
   hr = pClientSDO->PutProperty(PROPERTY_CLIENT_SHARED_SECRET, &vtClientSecret);
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Apply the changes
   //
   hr = pClientSDO->Apply();
   if (FAILED(hr))
   {
      return hr;
   }   
    
   //
   // Refresh the service using a ISdoServiceControl interface retrieved
   // in the code sample "Retrieve a Service SDO"
   //
   hr = pSdoServiceControl->ResetService();
   if (FAILED(hr))
   {
      //
      // If IAS is not installed or is not running then ignore the error
      //  
   }


```



## Related topics

<dl> <dt>

[\_bstr\_t](/previous-versions/visualstudio/visual-studio-6.0/aa278286(v=vs.60))
</dt> <dt>

[**ISdoCollection::Add**](/windows/desktop/api/sdoias/nf-sdoias-isdocollection-add)
</dt> <dt>

[**ISdoCollection::IsNameUnique**](/windows/desktop/api/sdoias/nf-sdoias-isdocollection-isnameunique)
</dt> <dt>

[Retrieving a Collection](/windows/desktop/Nps/sdo-retrieving-a-collection)
</dt> <dt>

[**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant)
</dt> </dl>

 

 