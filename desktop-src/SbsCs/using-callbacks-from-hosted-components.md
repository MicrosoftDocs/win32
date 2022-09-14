---
description: Callbacks from hosted components are what make hosting possible. However, it is possible that the component you are hosting has activated another activation context that it uses to access plug-ins or components of its own.
ms.assetid: 794a2e2f-ba1f-48ad-a435-244fc7936097
title: Using Callbacks From Hosted Components
ms.topic: article
ms.date: 05/31/2018
---

# Using Callbacks From Hosted Components

Callbacks from hosted components are what make hosting possible. However, it is possible that the component you are hosting has activated another activation context that it uses to access plug-ins or components of its own. In this case, if the hosted component leaves an activation context on the stack that refers to its own COM object, the hosting application might call [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to get an object that it expects to be its own implementation and instead receive the hosted component's object. To prevent this inheritance of activation contexts, a good hosting applications should activate its own well-known activation context first during a callback.

Consider the following example that protects the hosting application's code:

``` syntax
HRESULT STDCALL 
CHostingAppFirewall::ITheInterface::FunctWrapper()
{
    ULONG_PTR ulpCookie;
    HRESULT hRes = E_FAIL;
    if (!ActivateActCtx(this->m_hHostingAppContext, &ulpCookie))
        return HRESULT_FROM_WIN32(GetLastError());
    __try 
        {
        hRes = this->m_ITheInterface->Funct();
    } 
        __finally 
        {
        if (!DeactivateActCtx(0, ulpCookie))
            hRes = HRESULT_FROM_WIN32(GetLastError());
    }
    return hRes;
}
```

This ensures that a proper activation context is set before passing the request on to some inner implementation of **Funct**. Your own implementation can have the actual implementation inline, but the preceding method ensures easier interoperability by just creating delegated wrappers. It is recommended to use a similar method when exposing normal (non-COM) callbacks.

 

 
