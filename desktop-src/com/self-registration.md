---
title: Self-Registration
description: Self-registration is the standard means through which a server module can package its own registry operations, both registration and unregistration, into the module itself.
ms.assetid: fb5dcb2b-b0e3-4f37-a8e7-b84b9a265227
ms.topic: article
ms.date: 05/31/2018
---

# Self-Registration

As component software continues to grow as a market, there will be more and more instances where a user obtains a new software component as a single DLL or EXE module, such as when downloading a new component from an on-line service or receiving one from a friend on a floppy disk. In these cases, it is not practical to require the user to go through a lengthy installation procedure or setup program. Besides the licensing issues, which are handled through [**IClassFactory2**](/windows/desktop/api/OCIdl/nn-ocidl-iclassfactory2), an installation procedure typically creates the necessary registry entries for a component to run properly in the COM and OLE context.

Self-registration is the standard means through which a server module can package its own registry operations, both registration and unregistration, into the module itself. When used with licensing handled through [**IClassFactory2**](/windows/desktop/api/OCIdl/nn-ocidl-iclassfactory2), a server can become an entirely self-contained module with no need for external installation programs or .reg files.

Any self-registering module, DLL or EXE, should first include an "OleSelfRegister" string in the [StringFileInfo](/windows/desktop/menurc/stringfileinfo-block) section of its version information resource, as shown here.

``` syntax
VS_VERSION_INFO VERSIONINFO 
 
 ... 
 
 BEGIN 
   BLOCK "StringFileInfo" 
    BEGIN 
#ifdef UNICODE 
     BLOCK "040904B0" // Lang=US English, CharSet=Unicode 
#else 
     BLOCK "040904E4" // Lang=US English, CharSet=Windows Multilingual 
#endif 
      BEGIN 
       ... 
       VALUE "OLESelfRegister", "\0" 
      END 
 
   ... 
 
   END 
 
 ... 
 
 END 
 
```

The existence of this data allows any interested party, such as an application that wishes to integrate this new component, to determine whether the server supports self-registration without having to load the DLL or EXE first.

If the server is packaged in a DLL module, the DLL must export the functions [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver) and [**DllUnregisterServer**](/windows/win32/api/olectl/nf-olectl-dllunregisterserver). Any application that wishes to instruct the server to register itself (that is, all its CLSIDs and type library IDs) can obtain a pointer to **DllRegisterServer** through the [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) function. Within **DllRegisterServer**, the DLL creates all its necessary registry entries, storing the correct path to the DLL for all [InprocServer32](inprocserver32.md) or [InprocHandler32](inprochandler32.md) entries.

When an application wishes to remove the component from the system, it should unregister that component by calling [**DllUnregisterServer**](/windows/win32/api/olectl/nf-olectl-dllunregisterserver). Within this call, the server removes exactly those entries it previously created in [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver). The server should not blindly remove all entries for its classes because other software may have stored additional entries, such as a [TreatAs](treatas.md) key.

If the server is packaged in an EXE module, the application wishing to register the server launches the EXE server with the command-line argument **/RegServer** or **-RegServer** (case-insensitive). If the application wishes to unregister the server, it launches the EXE with the command-line argument **/UnregServer** or **-UnregServer**. The self-registering EXE detects these command-line arguments and invokes the same operations as a DLL would within [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver)and [**DllUnregisterServer**](/windows/win32/api/olectl/nf-olectl-dllunregisterserver), respectively, registering its module path under [LocalServer32](localserver32.md) instead of **InprocServer32** or **InprocHandler32**.

The server must register the full path to the installation location of the DLL or EXE module for their respective **InprocServer32**, **InprocHandler32**, and **LocalServer32** keys in the registry. The module path is easily obtained through the [**GetModuleFileName**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getmodulefilenamea) function.

## Related topics

<dl> <dt>

[Installing as a Service Application](installing-as-a-service-application.md)
</dt> <dt>

[Registering a Class at Installation](registering-a-class-at-installation.md)
</dt> <dt>

[Registering a Running EXE Server](registering-a-running-exe-server.md)
</dt> <dt>

[Registering Objects in the ROT](registering-objects-in-the-rot.md)
</dt> </dl>

 

 