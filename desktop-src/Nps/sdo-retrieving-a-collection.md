---
title: Retrieving a Collection
description: Retrieving a Collection
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b9090ad5-564c-4f48-b7bd-24617d582d2e
ms.prod: windows-server-dev
ms.technology: network-policy-and-access-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Retrieving a Collection

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

The following code retrieves the clients collection for the Network Policy Server.


```C++
// Retrieve the clients collection 
   HRESULT hr;
   CComPtr<ISdo>  pSdo;
   hr = pSdoServiceControl->QueryInterface(
      __uuidof(ISdo),
      (void**) &amp;pSdo
   );
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // First Retrieve the protocols collection
   //
   _variant_t  vtProtocolsCollection;
   hr = pSdo->GetProperty(
      PROPERTY_IAS_PROTOCOLS_COLLECTION,
      &amp;vtProtocolsCollection
   );
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Get the ISdoCollection interface 
   // for the object.
   //
   CComPtr<ISdoCollection>  pProtocolsCollection;
   hr = vtProtocolsCollection.pdispVal->QueryInterface(
      __uuidof(ISdoCollection), 
      (void **) &amp;pProtocolsCollection
   );
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Then retrieve the RADIUS protocol
   //
   CComPtr<IDispatch> pRadiusDispatch;
   _variant_t  vtProtocolName = L"Microsoft Radius Protocol";
   hr = pProtocolsCollection->Item(&amp;vtProtocolName, &amp;pRadiusDispatch);
   if (FAILED(hr))
   {
      return hr;
   }

   CComPtr<ISdo> pRadiusSdo;
   hr = pRadiusDispatch->QueryInterface(      
      __uuidof(ISdo), 
      (void **) &amp;pRadiusSdo
   );

   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Then retrieve the clients collection
   //
   _variant_t  vtClientsCollection;
   hr = pRadiusSdo->GetProperty(PROPERTY_RADIUS_CLIENTS_COLLECTION, &amp;vtClientsCollection);
   if (FAILED(hr))
   {
      return hr;
   }

   CComPtr<ISdoCollection> pClientsCollection;
   hr = vtClientsCollection.pdispVal->QueryInterface(      
      __uuidof(ISdoCollection), 
      (void **) &amp;pClientsCollection
   );

   if (FAILED(hr))
   {
      return hr;
   }

```



## Remarks

The pSdoServiceControl variable contains a pointer to a Server Data Object for NPS. For more information, see the topic [Retrieving a Service SDO](https://msdn.microsoft.com/library/bb960709).

The vtClientsCollection variable is of type [\_variant\_t](Http://go.microsoft.com/fwlink/p/?linkid=83857). A \_variant\_t object encapsulates, or encloses, the [**VARIANT**](e305240e-9e11-4006-98cc-26f4932d2118) data type. The class manages resource allocation and deallocation, and makes function calls to [**VariantInit**](96aeb671-5528-4d3c-8e70-313716550b42) and [**VariantClear**](28741d81-8404-4f85-95d3-5c209ec13835) as appropriate.

After the call to "pSdo-&gt;GetProperty()", the vtProtocolsCollection variable specifies an object. The **pdispVal** member of vtProtocolsCollection contains a pointer to the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface for the object.

The above sample code can be adapted to retrieve other NPS collections, for example the NPS Request Handlers collections. The [**IASPROPERTIES**](https://msdn.microsoft.com/library/bb960636) enumeration type enumerated values that correspond to the available NPS collections.

## Related topics

<dl> <dt>

[\_variant\_t](Http://go.microsoft.com/fwlink/p/?linkid=83857)
</dt> <dt>

[**IASPROPERTIES**](https://msdn.microsoft.com/library/bb960636)
</dt> <dt>

[**ISdo::GetProperty**](https://msdn.microsoft.com/library/bb960671)
</dt> <dt>

[**ISdoCollection**](https://msdn.microsoft.com/library/bb960640)
</dt> <dt>

[Retrieving a Service SDO](https://msdn.microsoft.com/library/bb960709)
</dt> <dt>

[**VariantClear**](28741d81-8404-4f85-95d3-5c209ec13835)
</dt> <dt>

[**VariantInit**](96aeb671-5528-4d3c-8e70-313716550b42)
</dt> <dt>

[**VARIANT**](e305240e-9e11-4006-98cc-26f4932d2118)
</dt> </dl>

 

 




