---
title: Building and Registering a Proxy DLL
description: If you chose proxy/stub marshaling for your application, the .c and .h files that MIDL generated must be compiled and linked to create a proxy DLL, and that DLL must be entered into the system registry so that clients can locate your interfaces.
ms.assetid: 939e6eed-2a2d-4d90-8fbb-c07142e7ba70
ms.topic: article
ms.date: 05/31/2018
---

# Building and Registering a Proxy DLL

If you chose proxy/stub marshaling for your application, the .c and .h files that MIDL generated must be compiled and linked to create a proxy DLL, and that DLL must be entered into the system registry so that clients can locate your interfaces. The MIDL-generated file Dlldata.c contains the necessary routines and other information to build and register a proxy/stub DLL.

The first step in building the DLL is to write a module definition file for the linker, as shown in the following example:

``` syntax
LIBRARY        example.dll
DESCRIPTION    'generic proxy/stub DLL'
EXPORTS        DllGetClassObject      @1 PRIVATE
               DllCanUnloadNow        @2 PRIVATE
               DllRegisterServer      @4 PRIVATE
               DllUnregisterServer    @5 PRIVATE
 
```

Alternatively, you can specify these exported functions on the LINK command line of your makefile.

The exported functions are declared in Rpcproxy.h, which Dlldata.c includes, and default implementations are part of the RPC run-time library. COM uses these functions to create a class factory, unload DLLs (after making sure that no objects or locks exist), retrieve information about the proxy DLL, and to self-register and unregister the proxy DLL. To take advantage of these predefined functions, you need to invoke the Cpreprocessor /D (or -D) option when you compile the Dlldata.c and Example\_p.c files, as shown in the following makefile:

``` syntax
example.h example.tlb example_p.c example_i.c dlldata.c : example.idl
    midl example.idl
dlldata.obj : dlldata.c
    CL /c /DWIN32 /DREGISTER_PROXY_DLL dlldata.c
example.obj : example_p.c
    CL /c /DWIN32 /DREGISTER_PROXY_DLL example_p.c
iids.obj : example_i.c
PROXYSTUBOBJS = dlldata.obj example.obj iids.obj
PROXYSTUBLIBS = kernel32.lib rpcndr.lib rpcns4.lib rpcrt4.lib uuid.lib
proxy.dll : $(PROXYSTUBOBJS) example.def
    link /dll /out:proxy.dll /def:example.def
        $(PROXYSTUBOBJS) $(PROXYSTUBLIBS)
    regsvr32 /s proxy.dll
 
```

If you do not specify these preprocessor definitions at compile time, these functions are not automatically defined. (That is, the macros in Rpcproxy.c expand to nothing.) You would have to have defined them explicitly in another source file, whose module would also be included in the final linking and compilation on the C compiler command line.

When REGISTER\_PROXY\_DLL is defined, Rpcproxy.h provides for additional conditional compilation control with PROXY\_CLSID=*guid*, PROXY\_CLSID\_IS=*explicit value of guid*, and ENTRY\_PREFIX=*prefix string*. These macro definitions are described in greater detail in [C-Compiler Definitions for Proxy/Stubs](/windows/desktop/Midl/c-compiler-definitions-for-proxy-stubs) in the MIDL Programmer's Guide.

## Manually Registering the Proxy DLL

If for some reason you cannot use the default proxy stub registration routines, you can manually register the DLL by adding the following entries to the system registry, using Regedt32.exe.

```
HKEY_CLASSES_ROOT
   Interface
      iid
         (Default) = ICustomInterfaceName
         ProxyStubClsid32 = {clsid}
```

```
HKEY_CLASSES_ROOT
   CLSID
      clsid
         (Default) = ICustomInterfaceName_PSFactory
         InprocServer32 = proxstub.dll
```

## Related topics

<dl> <dt>

[C-Compiler Definitions for Proxy/Stubs](/windows/desktop/Midl/c-compiler-definitions-for-proxy-stubs)
</dt> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> <dt>

[Self-Registration](self-registration.md)
</dt> </dl>

 

 
