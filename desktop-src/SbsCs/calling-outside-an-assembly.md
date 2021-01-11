---
description: Calling Outside An Assembly
ms.assetid: 7a59f707-fb89-4899-891f-4cd556b62b26
title: Calling Outside An Assembly
ms.topic: article
ms.date: 05/31/2018
---

# Calling Outside An Assembly

Hosted components should ensure that the correct activation context is active when calling outside the component. Calls into outside code that was found by calling [**CreateActCtx**](/windows/desktop/api/Winbase/nf-winbase-createactctxa) and then [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance), should be called with the same context that was used to find it. Calls into code that was found outside of activation contexts, or calls back into the hosting application should be called with the application default activation context.

Compiling with ISOLATION\_AWARE\_ENABLED defined may be useful when calling outside of hosted components. However this means that only calls to Windows APIs are isolated to the component's activation context. This is sufficient for most cases because calls to third-party functions do not have a context activated before being called. Compiling with ISOLATION\_AWARE\_ENABLED defined does not help if your component uses several activation contexts with various platform APIs.

To implement this, use an activation context activator like the example presented in [Isolating Components](isolating-components.md). Here externals.manifest is the set of dependencies outside those the component was built with; perhaps it contains some extendable list of components that are to be loaded and used during runtime. The internalcontext.manifest contains the set of dependencies that the component is sure to use during its lifetime, and which should be set in all entrypoints from the outside. Notice that this internal context is activated in all entrypoints, while the context activator is used with C++ scoping so that the proper context is set when calling out to the various outside code that this component uses.

``` syntax
CActivationContext s_InternalContext;
CActivationContext s_OutboundContext;
CActivationContext s_ExternalContext;

void MyInitializeFunction() 
{
    HANDLE hActCtx;
    ACTCTX actctx = {sizeof(actctx)};

    s_OutboundContext.Set(NULL);

    actctx.lpSource = TEXT("internalcontext.manifest");
    hActCtx = CreateActCtx(&actctx);
    s_InternalActCtx.Set(hActCtx);
    ReleaseActCtx(hActCtx);

    actctx.lpSource = TEXT("externals.manifest");
    hActCtx = CreateActCtx(&actctx);
    s_ExternalContext.Set(hActCtx);
    ReleaseActCtx(hActCtx);
}

void foo() 
{
    // Some code that makes a few calls
    {
        CActCtxActivator CallUnknown(s_OutboundContext);
        pfnUnknownImplementor(...);
    }
    {
        CActCtxActivator CallDependency(s_ExternalContext);
        KnownExternalDependencyPtr->Call();
    }
}

void WINAPI MyEntrypoint() 
{
    CActCtxActivator ContextFirewall(s_InternalContext);
    // Do some work here
    foo();
    // Some more work here
}
```

 

 
