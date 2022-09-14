---
title: C-Compiler Definitions for Proxy/Stubs
description: The header file Rpcproxy.h includes the following macro definitions, each of which may be convenient when building distributed COM application. These macros are invoked with the /D (or -D) preprocessor switch at the C-compile time.
ms.assetid: 697f0b63-76ae-410d-8bbf-bb95295ffba9
keywords:
- MIDL compiler MIDL , C-compiler, definitions for proxy/stubs
ms.topic: article
ms.date: 05/31/2018
---

# C-Compiler Definitions for Proxy/Stubs

The header file Rpcproxy.h includes the following macro definitions, each of which may be convenient when building distributed COM application. These macros are invoked with the [**/D**](-d.md) (or -D) preprocessor switch at the C-compile time.



| MACRO                                                                                                                                                                                           | Description                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REGISTER\_PROXY\_DLL                                                                                                                                                                            | Generates **DllMain**, **DllRegisterServer**, and **DllUnregisterServer** functions for automatically registering a proxy DLL.                                                                                       |
| PROXY\_CLSID=&lt;clsid&gt;                                                                                                                                                                      | Specifies a class identifier for the server. If this macro is not defined, the default CLSID is the first interface identifier that the MIDL compiler encounters in the IDL specification for the Proxy/Stub server. |
| PROXY\_CLSID\_IS={0x*8hexdigits*, 0x*4hexdigits*,0x*4hexdigits*, {0x*2hexdigits*,0x*2hexdigits*, 0x*2hexdigits*,0x*2hexdigits*, 0x*2hexdigits*,0x*2hexdigits*, 0x*2hexdigits*,0x*2hexdigits*,}} | Specifies the value of the server's class identifier in binary hex format.                                                                                                                                           |



 

By defining the **REGISTER\_PROXY\_DLL** macro when compiling Dlldata.c, your proxy/stub marshaling DLL will automatically include default definitions for the **DllMain**, **DllRegisterServer**, and **DllUnregisterServer** functions. You can use these functions to self-register your proxy DLL in the system registry.

This default registration code uses the GUID of the first interface encountered as the CLSID for registering the entire proxy/stub DLL server. COM later uses this CLSID to locate and load the compiled proxy/stub server for the marshaling of any of the interfaces the server is registered to handle. When an application makes an interface method call that crosses thread, process, or computer boundaries, COM uses the interface identifier registry entry to locate the CLSID registry entry for the proxy/stub marshaling server. It then uses this CLSID to load the server (if it isn't already loaded) so that the interface call can then be marshaled.

Use the **PROXY\_CLSID**=&lt;clsid&gt; macro when you want to explicitly specify the proxy/stub server's CLSID rather than rely on the default CLSID. For example, if you are building a standard marshaling DLL as your own in-process COM server, or if you need to define your own **DllMain** to handle DLL\_PROCESS\_ATTACH.

Use **PROXY\_CLSID\_IS**= macro instead of **PROXY\_CLSID** to define the value of the CLSID in the binary hexadecimal format that the **DEFINE\_GUID** macro uses.

Also note that when the default **DllRegisterServer** function runs, it registers the server with ThreadingModel=Both.

The following makefile example uses the **REGISTER\_PROXY\_DLL** and **PROXY\_CLSID**= macros:

``` syntax
example.h example.tlb example_p.c example_i.c dlldata.c : example.idl
    midl example.idl
dlldata.obj : dlldata.c
    CL /c /DWIN32 /DREGISTER_PROXY_DLL dlldata.c
example.obj : example_p.c
    CL /c /DWIN32 /DREGISTER_PROXY_DLL \
    /DPROXY_CLSID=7a98c250-6808-11cf-b73b-00aa00b677a7
example_p.c
iids.obj : example_i.c
PROXYSTUBOBJS = dlldata.obj example.obj iids.obj
PROXYSTUBLIBS = kernel32.lib rpcns4.lib rpcrt4.lib uuid.lib
proxy.dll : $(PROXYSTUBOBJX) example.def
    link /dll /out:proxy.dll /def:example.def
        $(PROXYSTUBOBJS) $(PROXYSTUBLIBS)
    regsvr32 /s proxy.dll
```

For more information on the [**/D**](-d.md) preprocessor option, see your C compiler documentation.

 

 




