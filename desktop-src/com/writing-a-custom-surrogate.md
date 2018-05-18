---
title: Writing a Custom Surrogate
description: Writing a Custom Surrogate
ms.assetid: '510e38e5-1965-46f4-b09c-6fa585cff993'
---

# Writing a Custom Surrogate

While the system-supplied surrogate will be more than adequate for most situations, there are some cases where writing a custom surrogate could be worthwhile. Following are some examples:

-   A custom surrogate could provide some optimizations or semantics not present in the system surrogate.
-   If an in-process DLL contains code that depends on being in the same process as the client, the DLL server will not function correctly if it is running in the system surrogate. A custom surrogate could be tailored to a specific DLL to deal with this.
-   The system surrogate supports a mixed-threading model so that it can load both free and apartment model DLLs. A custom surrogate might be tailored to load only apartment DLLs for reasons of efficiency or to accept a command-line argument for the type of DLL it is allowed to load.
-   A custom surrogate could take extra command-line parameters that the system surrogate does not.
-   The system surrogate calls [**CoInitializeSecurity**](coinitializesecurity.md) and tells it to use any existing security settings found under the [AppID](appid-key.md) key in the registry. A custom surrogate could use another security context.
-   Interfaces that aren't remotable (such as those for recent OCXs) will not work with the system surrogate. A custom surrogate could wrap the DLL's interfaces with its own implementation and use proxy/stub DLLs with a remotable IDL definition that would allow the interface to be remoted.

The main surrogate thread should typically perform the following setup steps:

1.  Call [**CoInitializeEx**](coinitializeex.md) to initialize the thread and set the threading model.
2.  If you want the DLL servers that are to run in the server to be able to use the security settings in the **AppID** registry key, call [**CoInitializeSecurity**](coinitializesecurity.md) with the EOAC\_APPID capability. Otherwise, legacy security settings will be used.
3.  Call [**CoRegisterSurrogate**](coregistersurrogate.md) to register the surrogate interface to COM.
4.  Call [**ISurrogate::LoadDllServer**](isurrogate-loaddllserver.md) for the requested CLSID.
5.  Put main thread in a loop to call [**CoFreeUnusedLibraries**](cofreeunusedlibraries.md) periodically.
6.  When COM calls [**ISurrogate::FreeSurrogate**](isurrogate-freesurrogate.md), revoke all class factories and exit.

A surrogate process must implement the [**ISurrogate**](isurrogate.md) interface. This interface should be registered when a new surrogate is started and after calling [**CoInitializeEx**](coinitializeex.md). As indicated in the preceding steps, the **ISurrogate** interface has two methods that COM calls: [**LoadDllServer**](isurrogate-loaddllserver.md), to dynamically load new DLL servers into existing surrogates; and [**FreeSurrogate**](isurrogate-freesurrogate.md), to free the surrogate.

The implementation of [**LoadDllServer**](isurrogate-loaddllserver.md), which COM calls with a load request, must first create a class factory object that supports [**IUnknown**](iunknown.md), [**IClassFactory**](iclassfactory.md), and [**IMarshal**](imarshal.md), and then call [**CoRegisterClassObject**](coregisterclassobject.md) to register the object as the class factory for the requested CLSID.

The class factory registered by the surrogate process is not the actual class factory implemented by the DLL server but is a generic class factory implemented by the surrogate process that supports [**IClassFactory**](iclassfactory.md) and [**IMarshal**](imarshal.md). Because it is the surrogate's class factory, rather than that of the DLL server that is being registered, the surrogate's class factory will need to use the real class factory to create an instance of the object for the registered CLSID. The surrogate's [**IClassFactory::CreateInstance**](iclassfactory-createinstance.md) should look something like the following example:


```C++
STDMETHODIMP CSurrogateFactory::CreateInstance(
  IUnknown* pUnkOuter, 
  REFIID iid, 
  void** ppv)
{
    void* pcf;
    HRESULT hr;
 
    hr = CoGetClassObject(clsid, CLSCTX_INPROC_SERVER, NULL, IID_IClassFactory, &amp;pcf);
    if ( FAILED(hr) )
        return hr;
    hr = ((IClassFactory*)pcf)->CreateInstance(pUnkOuter, iid, ppv);
    ((IClassFactory*)pcf)->Release();
    return hr;
}
 
```



The surrogate's class factory must also support [**IMarshal**](imarshal.md) because a call to [**CoGetClassObject**](cogetclassobject.md) can request any interface from the registered class factory, not just [**IClassFactory**](iclassfactory.md). Further, since the generic class factory supports only [**IUnknown**](iunknown.md) and **IClassFactory**, requests for other interfaces must be directed to the real object. Thus, there should be a [**MarshalInterface**](imarshal-marshalinterface.md) method which should be similar to the following:


```C++
STDMETHODIMP CSurrogateFactory::MarshalInterface(
  IStream *pStm,  
  REFIID riid, void *pv, 
  WORD dwDestContext, 
  void *pvDestContext, 
  DWORD mshlflags )
{   
    void * pCF = NULL;
    HRESULT hr;
 
    hr = CoGetClassObject(clsid, CLSCTX_INPROC_SERVER, NULL, riid, &amp;pCF);
    if ( FAILED(hr) )
        return hr;   
    hr = CoMarshalInterface(pStm, riid, (IUnknown*)pCF, dwDestContext, pvDestContext,  mshlflags);
    ((IUnknown*)pCF)->Release();
    return S_OK;
 
```



The surrogate that houses a DLL server must publish the DLL server's class object(s) with a call to [**CoRegisterClassObject**](coregisterclassobject.md). All class factories for DLL surrogates should be registered as REGCLS\_SURROGATE. REGCLS\_SINGLUSE and REGCLS\_MULTIPLEUSE should not be used for DLL servers loaded into surrogates.

Following these guidelines for creating a surrogate process when it is necessary to do so should ensure proper behavior.

## Related topics

<dl> <dt>

[DLL Surrogates](dll-surrogates.md)
</dt> </dl>

 

 




