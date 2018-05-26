---
title: Adding an Object to a Collection
description: Adding an Object to a Collection
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fc62698d-0bb9-478c-91cf-9f8fec36dba4
ms.prod: windows-server-dev
ms.technology: network-policy-and-access-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding an Object to a Collection

The following code adds a new policy to the IAS policies collection. The variable pClientsCollection points to an [**ISdoCollection**](https://msdn.microsoft.com/library/bb960640) interface for the collection. See [Retrieving a Collection](https://msdn.microsoft.com/library/bb960708) for information on how to retrieve the collection object.


```C++
   HRESULT hr;
   _bstr_t      bstrClientName = L"Test Client";
   VARIANT_BOOL vbNameUnique = VARIANT_FALSE;

   //
   // Check if the new client's name is unique
   //

   hr = pClientsCollection->IsNameUnique(bstrClientName, &amp;vbNameUnique);
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
   hr = pClientsCollection->Add(bstrClientName, &amp;pClientDispatch);
   if (FAILED(hr))
   {
      return hr;
   }

   CComPtr<ISdo> pClientSDO;
   hr = pClientDispatch->QueryInterface(
      __uuidof(ISdo),
      (void**) &amp;pClientSDO
   );
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Set the address for the client
   //
   _variant_t  vtClientAddress = L"127.0.0.1";
   hr = pClientSDO->PutProperty(PROPERTY_CLIENT_ADDRESS, &amp;vtClientAddress);
   if (FAILED(hr))
   {
      return hr;
   }
       
   //
   // Set the shared secret for the client
   //
   _variant_t  vtClientSecret = L">@U#'6cc='5Ly9O5QKEj2RTJr*fM";
   hr = pClientSDO->PutProperty(PROPERTY_CLIENT_SHARED_SECRET, &amp;vtClientSecret);
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

[\_bstr\_t](Http://go.microsoft.com/fwlink/p/?linkid=83856)
</dt> <dt>

[**ISdoCollection::Add**](https://msdn.microsoft.com/library/bb960641)
</dt> <dt>

[**ISdoCollection::IsNameUnique**](https://msdn.microsoft.com/library/bb960644)
</dt> <dt>

[Retrieving a Collection](https://msdn.microsoft.com/library/bb960708)
</dt> <dt>

[**VARIANT**](e305240e-9e11-4006-98cc-26f4932d2118)
</dt> </dl>

 

 




