---
title: Writing a Custom Surrogate
description: Writing a Custom Surrogate
ms.assetid: 510e38e5-1965-46f4-b09c-6fa585cff993
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Custom Surrogate

While the system-supplied surrogate will be more than adequate for most situations, there are some cases where writing a custom surrogate could be worthwhile. Following are some examples:

-   A custom surrogate could provide some optimizations or semantics not present in the system surrogate.
-   If an in-process DLL contains code that depends on being in the same process as the client, the DLL server will not function correctly if it is running in the system surrogate. A custom surrogate could be tailored to a specific DLL to deal with this.
-   The system surrogate supports a mixed-threading model so that it can load both free and apartment model DLLs. A custom surrogate might be tailored to load only apartment DLLs for reasons of efficiency or to accept a command-line argument for the type of DLL it is allowed to load.
-   A custom surrogate could take extra command-line parameters that the system surrogate does not.
-   The system surrogate calls [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) and tells it to use any existing security settings found under the [AppID](appid-key.md) key in the registry. A custom surrogate could use another security context.
-   Interfaces that aren't remotable (such as those for recent OCXs) will not work with the system surrogate. A custom surrogate could wrap the DLL's interfaces with its own implementation and use proxy/stub DLLs with a remotable IDL definition that would allow the interface to be remoted.

The main surrogate thread should typically perform the following setup steps:

1.  Call [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex) to initialize the thread and set the threading model.
2.  If you want the DLL servers that are to run in the server to be able to use the security settings in the **AppID** registry key, call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) with the EOAC\_APPID capability. Otherwise, legacy security settings will be used.
3.  Call [**CoRegisterSurrogate**](/windows/desktop/api/combaseapi/nf-combaseapi-coregistersurrogate) to register the surrogate interface to COM.
4.  Call [**ISurrogate::LoadDllServer**](/windows/win32/api/objidlbase/nf-objidlbase-isurrogate-loaddllserver) for the requested CLSID.
5.  Put main thread in a loop to call [**CoFreeUnusedLibraries**](/windows/desktop/api/combaseapi/nf-combaseapi-cofreeunusedlibraries) periodically.
6.  When COM calls [**ISurrogate::FreeSurrogate**](/windows/win32/api/objidlbase/nf-objidlbase-isurrogate-freesurrogate), revoke all class factories and exit.

A surrogate process must implement the [**ISurrogate**](/windows/win32/api/objidlbase/nn-objidlbase-isurrogate) interface. This interface should be registered when a new surrogate is started and after calling [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex). As indicated in the preceding steps, the **ISurrogate** interface has two methods that COM calls: [**LoadDllServer**](/windows/win32/api/objidlbase/nf-objidlbase-isurrogate-loaddllserver), to dynamically load new DLL servers into existing surrogates; and [**FreeSurrogate**](/windows/win32/api/objidlbase/nf-objidlbase-isurrogate-freesurrogate), to free the surrogate.

The implementation of [**LoadDllServer**](/windows/win32/api/objidlbase/nf-objidlbase-isurrogate-loaddllserver), which COM calls with a load request, must first create a class factory object that supports [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown), [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory), and [**IMarshal**](/windows/win32/api/objidlbase/nn-objidlbase-imarshal), and then call [**CoRegisterClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-coregisterclassobject) to register the object as the class factory for the requested CLSID.

The class factory registered by the surrogate process is not the actual class factory implemented by the DLL server but is a generic class factory implemented by the surrogate process that supports [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) and [**IMarshal**](/windows/win32/api/objidlbase/nn-objidlbase-imarshal). Because it is the surrogate's class factory, rather than that of the DLL server that is being registered, the surrogate's class factory will need to use the real class factory to create an instance of the object for the registered CLSID. The surrogate's [**IClassFactory::CreateInstance**](/windows/desktop/api/Unknwn/nf-unknwn-iclassfactory-createinstance) should look something like the following example:


```C++
STDMETHODIMP CSurrogateFactory::CreateInstance(
  IUnknown* pUnkOuter, 
  REFIID iid, 
  void** ppv)
{
    void* pcf;
    HRESULT hr;
 
    hr = CoGetClassObject(clsid, CLSCTX_INPROC_SERVER, NULL, IID_IClassFactory, &pcf);
    if ( FAILED(hr) )
        return hr;
    hr = ((IClassFactory*)pcf)->CreateInstance(pUnkOuter, iid, ppv);
    ((IClassFactory*)pcf)->Release();
    return hr;
}
 
```



The surrogate's class factory must also support [**IMarshal**](/windows/win32/api/objidlbase/nn-objidlbase-imarshal) because a call to [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject) can request any interface from the registered class factory, not just [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory). Further, since the generic class factory supports only [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) and **IClassFactory**, requests for other interfaces must be directed to the real object. Thus, there should be a [**MarshalInterface**](/windows/win32/api/objidlbase/nf-objidlbase-imarshal-marshalinterface) method which should be similar to the following:


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
 
    hr = CoGetClassObject(clsid, CLSCTX_INPROC_SERVER, NULL, riid, &pCF);
    if ( FAILED(hr) )
        return hr;   
    hr = CoMarshalInterface(pStm, riid, (IUnknown*)pCF, dwDestContext, pvDestContext,  mshlflags);
    ((IUnknown*)pCF)->Release();
    return S_OK;
 
```



The surrogate that houses a DLL server must publish the DLL server's class object(s) with a call to [**CoRegisterClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-coregisterclassobject). All class factories for DLL surrogates should be registered as REGCLS\_SURROGATE. REGCLS\_SINGLUSE and REGCLS\_MULTIPLEUSE should not be used for DLL servers loaded into surrogates.

Following these guidelines for creating a surrogate process when it is necessary to do so should ensure proper behavior.

## Related topics

<dl> <dt>

[DLL Surrogates](dll-surrogates.md)
</dt> </dl>

 

 