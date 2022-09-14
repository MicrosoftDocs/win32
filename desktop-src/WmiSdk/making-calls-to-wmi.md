---
description: Providers can call methods implemented by WMI from within their method implementations.
ms.assetid: 5bfd9d9b-ffe5-4def-a97d-85c4c01223f0
ms.tgt_platform: multiple
title: Making Calls to WMI
ms.topic: article
ms.date: 05/31/2018
---

# Making Calls to WMI

Providers can call methods implemented by WMI from within their method implementations. However, there are special considerations when a provider calls the WMI implementation of an [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) method from within its own implementation of the same method. These considerations are important regardless of whether the provider calls the synchronous or asynchronous version of the method.

Each [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) method that a provider can implement has a *pCtx* parameter, a pointer to an [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) interface implementation. When WMI calls the provider, WMI passes a valid pointer in this parameter. A provider must always pass this same pointer in any calls to WMI that they make while servicing requests. Neglecting to set *pCtx* appropriately can cause WMI to start an infinite loop.

The following code example shows the correct way to call the WMI implementation of [**GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) from within an implementation of [**GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync).


```C++
STDMETHODIMP CClassProv::GetObjectAsync (BSTR ObjectPath,
    long lFlags, IWbemContext *pCtx,
    IWbemObjectSink *pHandler)
{
  IWbemClassObject *pclObj = NULL;
  IWbemServices* m_pNamespace;
  HRESULT hr = m_pNamespace->GetObject(
      _bstr_t(L"AClass"), 0, pCtx, &pclObj, 
      NULL );
  pclObj->Release();
  return pHandler->SetStatus(0, hr, NULL, NULL);
}
```



The C++ code example in this topic requires the following references and \#include statements to compile correctly.


```C++
#define _WIN32_DCOM
#include <iostream>
using namespace std;
#include <comdef.h>
#include <Wbemidl.h>
#pragma comment(lib, "wbemuuid.lib")
```



Instance, class, and property providers must not issue any calls to WMI requesting the modification of data while servicing a read request. The only providers that are exceptions to this rule are push providers. A push provider is a class provider that stores data in the WMI repository and relies on WMI to handle requests from clients. While servicing a read request, a push provider can update the WMI repository, but must set the *lFlags* parameter to **WBEM\_FLAG\_OWNER\_UPDATE** in the appropriate [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) call.

Event providers must not make any class changes while servicing a call. They also cannot issue any event-related calls, such as modifying an event filter.

## Related topics

<dl> <dt>

[Developing a WMI Provider](developing-a-wmi-provider.md)
</dt> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dt>

[Securing Your Provider](securing-your-provider.md)
</dt> </dl>

 

 



