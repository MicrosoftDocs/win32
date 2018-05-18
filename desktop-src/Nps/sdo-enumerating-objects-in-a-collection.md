---
title: Enumerating Objects in a Collection
description: Enumerating Objects in a Collection
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '664e4d99-48ed-4948-b816-e92ad1ca3ece'
ms.prod: 'windows-server-dev'
ms.technology: 'network-policy-and-access-services'
ms.tgt_platform: multiple
---

# Enumerating Objects in a Collection

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

The following code enumerates the protocols in the NPS protocols collection.


```C++
   HRESULT hr;

   //
   // Retrieve the protocols collection object
   //
   _variant_t vtIASProtocolsCollection;
   hr = pSdo->GetProperty(
      PROPERTY_IAS_PROTOCOLS_COLLECTION,
      &amp;vtIASProtocolsCollection
   );
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Retrieve the ISdoCollection interface 
   // for the object.
   //
   CComPtr<ISdoCollection> pIASProtocolsCollection;
   hr = vtIASProtocolsCollection.pdispVal->QueryInterface(
      __uuidof(ISdoCollection), 
      (void **) &amp;pIASProtocolsCollection
   );
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Retrieve the enumeration interface, IEnumVARIANT
   //
   CComPtr<IUnknown> pUnknownProtocol;
   hr = pIASProtocolsCollection->get__NewEnum(&amp;pUnknownProtocol);
   if (FAILED(hr))
   {
      return hr;
   }

   CComPtr<IEnumVARIANT> pEnumProtocols;
   hr = pUnknownProtocol->QueryInterface(
      __uuidof(IEnumVARIANT), 
      (void **) &amp;pEnumProtocols
   );
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Retrieve the first protocol from the collection
   //
   DWORD      dwRetrieved = 1;
   _variant_t vtProtocol;
   hr = pEnumProtocols->Next(1, &amp;vtProtocol, &amp;dwRetrieved);
   if (FAILED(hr))
   {
      return hr;
   }

   while (hr != S_FALSE) {
      // 
      // Retrieve the name of the protocol
      //
      CComPtr<ISdo> pLocalSdo;
      hr = vtProtocol.pdispVal->QueryInterface(
         __uuidof(ISdo), 
         (void**)&amp;pLocalSdo
      );
      if (FAILED(hr))
      {
         return hr;
      }

      _variant_t vtName;
      hr = pLocalSdo->GetProperty(PROPERTY_SDO_NAME, &amp;vtName);
      if (FAILED(hr))
      {
         return hr;
      }

      vtProtocol.Clear();
      vtName.Clear();

      //
      // Retrieve the next protocol from the collection
      //
      dwRetrieved = 1;
      hr = pEnumProtocols->Next(1, &amp;vtProtocol, &amp;dwRetrieved);
      if (FAILED(hr))
      {
         return hr;
      }
   }

```



## Remarks

The vtName and vtProtocol variables are of type [\_variant\_t](Http://go.microsoft.com/fwlink/p/?linkid=83857). A [\_variant\_t](Http://go.microsoft.com/fwlink/p/?linkid=83857) object encapsulates, or encloses, the **VARIANT** data type. The class manages resource allocation and deallocation, and makes function calls to [**VariantInit**](96aeb671-5528-4d3c-8e70-313716550b42) and [**VariantClear**](28741d81-8404-4f85-95d3-5c209ec13835) as appropriate.

## Related topics

<dl> <dt>

[\_variant\_t](Http://go.microsoft.com/fwlink/p/?linkid=83857)
</dt> <dt>

[Adding a Client](https://msdn.microsoft.com/library/bb960607)
</dt> <dt>

[**IASCOMMONPROPERTIES**](https://msdn.microsoft.com/library/bb960631)
</dt> <dt>

[**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e)
</dt> <dt>

[**ISdo::GetProperty**](https://msdn.microsoft.com/library/bb960671)
</dt> <dt>

[Retrieving a Service SDO](https://msdn.microsoft.com/library/bb960709)
</dt> <dt>

[**VariantClear**](28741d81-8404-4f85-95d3-5c209ec13835)
</dt> <dt>

[**VariantInit**](96aeb671-5528-4d3c-8e70-313716550b42)
</dt> <dt>

[**VARIANT**](e305240e-9e11-4006-98cc-26f4932d2118)
</dt> </dl>

 

 




