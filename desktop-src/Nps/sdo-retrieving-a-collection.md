---
title: Retrieving a Collection
description: Retrieving a Collection
ms.assetid: b9090ad5-564c-4f48-b7bd-24617d582d2e
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
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
      (void**) &pSdo
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
      &vtProtocolsCollection
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
      (void **) &pProtocolsCollection
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
   hr = pProtocolsCollection->Item(&vtProtocolName, &pRadiusDispatch);
   if (FAILED(hr))
   {
      return hr;
   }

   CComPtr<ISdo> pRadiusSdo;
   hr = pRadiusDispatch->QueryInterface(      
      __uuidof(ISdo), 
      (void **) &pRadiusSdo
   );

   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Then retrieve the clients collection
   //
   _variant_t  vtClientsCollection;
   hr = pRadiusSdo->GetProperty(PROPERTY_RADIUS_CLIENTS_COLLECTION, &vtClientsCollection);
   if (FAILED(hr))
   {
      return hr;
   }

   CComPtr<ISdoCollection> pClientsCollection;
   hr = vtClientsCollection.pdispVal->QueryInterface(      
      __uuidof(ISdoCollection), 
      (void **) &pClientsCollection
   );

   if (FAILED(hr))
   {
      return hr;
   }

```



## Remarks

The pSdoServiceControl variable contains a pointer to a Server Data Object for NPS. For more information, see the topic [Retrieving a Service SDO](/windows/desktop/Nps/sdo-retrieving-a-service-sdo).

The vtClientsCollection variable is of type [\_variant\_t](/previous-versions/visualstudio/visual-studio-6.0/aa278648(v=vs.60)). A \_variant\_t object encapsulates, or encloses, the [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) data type. The class manages resource allocation and deallocation, and makes function calls to [**VariantInit**](/windows/win32/api/oleauto/nf-oleauto-variantinit) and [**VariantClear**](/windows/win32/api/oleauto/nf-oleauto-variantclear) as appropriate.

After the call to "pSdo->GetProperty()", the vtProtocolsCollection variable specifies an object. The **pdispVal** member of vtProtocolsCollection contains a pointer to the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface for the object.

The above sample code can be adapted to retrieve other NPS collections, for example the NPS Request Handlers collections. The [**IASPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-iasproperties) enumeration type enumerated values that correspond to the available NPS collections.

## Related topics

<dl> <dt>

[\_variant\_t](/previous-versions/visualstudio/visual-studio-6.0/aa278648(v=vs.60))
</dt> <dt>

[**IASPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-iasproperties)
</dt> <dt>

[**ISdo::GetProperty**](/windows/desktop/api/sdoias/nf-sdoias-isdo-getproperty)
</dt> <dt>

[**ISdoCollection**](/windows/desktop/api/sdoias/nn-sdoias-isdocollection)
</dt> <dt>

[Retrieving a Service SDO](/windows/desktop/Nps/sdo-retrieving-a-service-sdo)
</dt> <dt>

[**VariantClear**](/windows/win32/api/oleauto/nf-oleauto-variantclear)
</dt> <dt>

[**VariantInit**](/windows/win32/api/oleauto/nf-oleauto-variantinit)
</dt> <dt>

[**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant)
</dt> </dl>

 

 