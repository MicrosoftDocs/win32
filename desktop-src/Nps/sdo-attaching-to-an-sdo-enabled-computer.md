---
title: Attaching to an SDO-Enabled Computer
description: Attaching to an SDO-Enabled Computer
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '434e2e0c-075e-48a9-9617-bbe75716380d'
ms.prod: 'windows-server-dev'
ms.technology: 'network-policy-and-access-services'
ms.tgt_platform: multiple
---

# Attaching to an SDO-Enabled Computer

The following code attaches to the local computer as an SDO computer.


```C++
   HRESULT  hr;
   CComPtr<ISdoMachine> pSdoMachine;
   CLSID    clsid;

   hr = CLSIDFromProgID(TEXT("IAS.SdoMachine"), &amp;clsid);
   if (FAILED(hr))
   {
      return hr;
   }

   hr = CoCreateInstance(
      clsid,
      NULL,
      CLSCTX_INPROC_SERVER,
      __uuidof(ISdoMachine),
      (void**)&amp;pSdoMachine
   );
   if (FAILED(hr))
   {
      return hr;
   }

   //
   // Pass NULL to specify local computer.
   //
   hr = pSdoMachine->Attach(NULL); 
   if (FAILED(hr))
   {
      return hr;
   }

```



Attaching to a computer as an SDO computer is the first step in administering the computer through SDO.

For more information, see [**ISdoMachine**](https://msdn.microsoft.com/library/bb960655), [**ISdoMachine::Attach**](https://msdn.microsoft.com/library/bb960656).

 

 




