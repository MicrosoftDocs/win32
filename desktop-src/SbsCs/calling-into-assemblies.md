---
description: When calling into the entrypoints of an assembly, it is recommended that you use the same activation context that was active when searching for the assembly.
ms.assetid: 8b2de5f5-ea95-441f-9345-b64de53ea05f
title: Calling Into Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Calling Into Assemblies

When calling into the entrypoints of an assembly, it is recommended that you use the same activation context that was active when searching for the assembly. At minimum, ensure that the component loading the assembly does not accidentally get the activation context your application is using. Leaking activation context across DLL boundaries can lead to unexpected dependencies. This is not a problem if your application compiles ISOLATION\_AWARE\_ENABLED because in that case no activation context is active by default. If you do not compile with ISOLATION\_AWARE\_ENABLED defined, you should activate the **NULL** activation context or the same activation context that was used to load the assembly.

The following example ensures that the hosted DLL runs in a context that it recognizes:

``` syntax
ULONG_PTR ulpCookie;
ActivateActCtx(hTheActCtxForMyDll, &ulpCookie);
__try 
{
        MyDllIsolatedFunction();
    myDllIsolatedComInterface->Funct();
}
__finally 
{
    DeactivateActCtx(0, ulpCookie);
}
```

 

 



