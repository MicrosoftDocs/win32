---
title: Retrieving a User SDO
description: Retrieving a User SDO
ms.assetid: 440628f8-081b-4e7f-bdb2-760ff9bd0d77
ms.tgt_platform: multiple
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

[Attaching to an SDO-Enabled Computer](https://docs.microsoft.com/windows/desktop/Nps/sdo-attaching-to-an-sdo-enabled-computer)
</dt> <dt>

[**ISdo**](https://docs.microsoft.com/windows/desktop/api/sdoias/nn-sdoias-isdo)
</dt> <dt>

[**ISdoMachine**](https://docs.microsoft.com/windows/desktop/api/sdoias/nn-sdoias-isdomachine)
</dt> <dt>

[**ISdoMachine::GetUserSDO**](https://docs.microsoft.com/windows/desktop/api/sdoias/nf-sdoias-isdomachine-getusersdo)
</dt> <dt>

[**SysAllocString**](https://msdn.microsoft.com/en-us/library/ms221458(v=VS.71).aspx)
</dt> <dt>

[**SysFreeString**](https://msdn.microsoft.com/en-us/library/ms221481(v=VS.71).aspx)
</dt> </dl>

 

 




