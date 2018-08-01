---
title: Retrieving a User SDO
description: Retrieving a User SDO
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 440628f8-081b-4e7f-bdb2-760ff9bd0d77
ms.prod: windows-server-dev
ms.technology: network-policy-and-access-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving a User SDO

The following code retrieves a Server Data Object (SDO) for the Administrator.


```C++
   HRESULT  hr;
   _bstr_t bstrUserName = L"Administrator";
   CComPtr<IUnknown> pUserUnknown;

   hr = pSdoMachine->GetUserSDO(
      DATA_STORE_LOCAL,
      bstrUserName,
      (IUnknown**) &pUserUnknown
   );
   if (FAILED(hr))
   {
      return hr;
   }

   CComPtr<ISdo> pUserSDO;
   hr = pUserUnknown->QueryInterface(
      __uuidof(ISdo),
      (void**) &pUserSDO
   );
   if (FAILED(hr))
   {
      return hr;
   }
```



## Related topics

<dl> <dt>

[Attaching to an SDO-Enabled Computer](https://msdn.microsoft.com/library/bb960609)
</dt> <dt>

[**ISdo**](https://msdn.microsoft.com/library/bb960639)
</dt> <dt>

[**ISdoMachine**](https://msdn.microsoft.com/library/bb960655)
</dt> <dt>

[**ISdoMachine::GetUserSDO**](https://msdn.microsoft.com/library/bb960662)
</dt> <dt>

[**SysAllocString**](https://msdn.microsoft.com/en-us/library/ms221458(v=VS.71).aspx)
</dt> <dt>

[**SysFreeString**](https://msdn.microsoft.com/en-us/library/ms221481(v=VS.71).aspx)
</dt> </dl>

 

 




