---
title: Retrieving a Service SDO
description: Retrieving a Service SDO
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bac95c42-8f7e-4011-960c-8f18b4b7c088
ms.prod: windows-server-dev
ms.technology: network-policy-and-access-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving a Service SDO

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008.

 

The following code retrieves a Server Data Object (SDO) for the Network Policy Server .


```C++
   HRESULT hr;
   CComPtr<IUnknown> pServiceUnknown;
   _bstr_t bstrServiceName = L"IAS";

   hr = pSdoMachine->GetServiceSDO(
      DATA_STORE_LOCAL,
      bstrServiceName,
      (IUnknown**) &pServiceUnknown
   );
   if (FAILED(hr))
   {
      return hr;
   }

   CComPtr<ISdoServiceControl>  pSdoServiceControl;
   hr = pServiceUnknown->QueryInterface(
      __uuidof(ISdoServiceControl),
      (void**) &pSdoServiceControl
   );
   if (FAILED(hr))
   {
      return hr;
   }
```



## Remarks

You must [attach](https://msdn.microsoft.com/library/bb960609) to a computer before you can call any of the [**ISdoMachine**](https://msdn.microsoft.com/library/bb960655) methods.

## Related topics

<dl> <dt>

[Attaching to an SDO-Enabled Computer](https://msdn.microsoft.com/library/bb960609)
</dt> <dt>

[**ISdoMachine::GetServiceSDO**](https://msdn.microsoft.com/library/bb960661)
</dt> <dt>

[**ISdoServiceControl**](https://msdn.microsoft.com/library/bb960664)
</dt> </dl>

 

 




