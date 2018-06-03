---
title: Hello Sample
description: The Hello sample is an Automation application with one object.
ms.assetid: 593c87c4-e555-4549-b723-c592903587a1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Hello Sample

The Hello sample is an Automation application with one object. It has these characteristics:

-   Supports VTBL binding.

-   Permits multiple instances of its exposed object to exist at the same time.

-   Implements **IErrorInfo** for exception handling.

This sample has been simplified for demonstration purposes. It has the following limitations:

-   Has only one object.

-   Uses only scalar argument types. Automation also supports methods and properties that accept arguments of complex types, including arrays, references to objects, and formatted data, but not structures.

-   Supports one national language.

The sections that follow demonstrate how the Hello sample exposes a simple class. The code is abridged to illustrate the essential parts. For a complete listing, see the source code in the *COM Programmer's Reference*.

-   [Initializing OLE](#initializing-ole)
-   [Registering the Active Object](#registering-the-active-object)
-   [Registering the Hello Application](#registering-the-hello-application)
-   [Implementing IDispatch](#implementing-idispatch)
-   [Implementing IUnknown](#implementing-iunknown)
-   [Implementing IClassFactory](#implementing-iclassfactory)
-   [Implementing VTBL Binding](#implementing-vtbl-binding)
-   [Registering the Interface for VTBL Binding](#registering-the-interface-for-vtbl-binding)
-   [Handling Errors](#handling-errors)
-   [Releasing Objects and OLE](#releasing-objects-and-ole)
-   [Creating Type Information](#creating-type-information)
-   [Creating the Hello Registration File](#creating-the-hello-registration-file)

## Initializing OLE

When the Hello application starts, it initializes OLE and then creates the object to be exposed through Automation. For example (Main.cpp):


```C++
BOOL InitInstance (HINSTANCE hinst)
{
    HRESULT hr;
    TCHAR ach[STR_LEN]; 

    // Intialize OLE.
    hr = OleInitialize(NULL);
    if (FAILED(hr))
        return FALSE;

    // Create an instance of the Hello Application object. The object is
    // created with refcount 0.
    if (!LoadString(hinst, IDS_HelloMessage, ach, sizeof(ach)))
         return FALSE;
    hr = CHello::Create(hinst, ach, &amp;g_phello);
    if (FAILED(hr))
        return FALSE;
    return TRUE;
}
 
```



This function calls **OleInitialize** to initialize OLE. It loads the string ach with the initial Hello message, obtained from the string table through the constant IDS\_HelloMessage. Then it calls CHello::Create to create a single, global instance of the application object, passing it the initial Hello message and receiving a value for g\_phello, a pointer to the instance. If the function is successful, it returns a value of **True**.

## Registering the Active Object

After Hello creates an instance of the object, it exposes and registers the class factory (if necessary) and registers the active object (Main.cpp):


```C++
BOOL ProcessCmdLine(LPSTR pCmdLine, 
                    LPDWORD pdwRegisterCF, 
                    LPDWORD pdwRegisterActiveObject, 
                    int nCmdShow)
{
    LPCLASSFACTORY pcf = NULL;
    HRESULT hr;

    // Pointer arguments are not allowed to be null.
    if (pdwRegisterCF == NULL ||
        pdwRegisterActiveObject == NULL ||
        pCmdLine == NULL)
        return FALSE;

    *pdwRegisterCF = 0;
    *pdwRegisterActiveObject = 0;

    // Expose class factory for application object if command line
    // contains the /Automation switch.
    if (_fstrstr(pCmdLine, "-Automation") != NULL
        || _fstrstr(pCmdLine, "/Automation") != NULL)
    {
        pcf = new CHelloCF;
        if (!pcf)
            goto error;
        pcf->AddRef();
        hr = CoRegisterClassObject(CLSID_Hello, pcf,
                                    CLSCTX_LOCAL_SERVER,
                                    REGCLS_SINGLEUSE,
                                    pdwRegisterCF);
        if (hr != NOERROR)
            goto error;
        pcf->Release();
    }
    else g_phello->ShowWindow(nCmdShow); //Show if started stand-alone.

    hr = RegisterActiveObject(g_phello, CLSID_Hello, ACTIVEOBJECT_WEAK,
                    pdwRegisterActiveObject);
    if (hr != NOERROR)
        goto error;
    return TRUE;

error:
    if (pcf)
        pcf->Release();
    return FALSE;
}
 
```



The sample first checks the command line for the **/Automation** switch. This switch indicates that the application should be started for programmatic access, so that ActiveX clients can create additional instances of the application's class. In this case, the class factory must be created and registered. If the switch is present, the Hello sample creates a new CHelloCF object and calls its **AddRef** method, thereby creating the class factory.

Next, the sample calls **CoRegisterClassObject** to register the class factory. It passes the object's CLSID (CLSID\_Hello), a pointer to the CHelloCF object (pcf), and two constants (CLSCTX\_LOCAL\_SERVER and REGCLS\_SINGLEUSE) that govern the class factory's use.

-   CLSCTX\_LOCAL\_SERVER indicates that the executable code for the object runs in a separate process space from the controller.

-   REGCLS\_SINGLEUSE allows only one ActiveX client to use each instance of the class factory. The value returned through pdwRegisterCF must later be used to revoke the class factory.

The example specifies weak registration (ACTIVEOBJECT\_WEAK), which means that OLE will release the object when all external connections to it have disappeared. You should always give ActiveX objects weak registration. For more information, see [**RegisterActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registeractiveobject) and [Dispatch Interface and API Functions](https://msdn.microsoft.com/windows/desktop/75BFF268-BD85-49C4-B761-B557F4B1C588).

The *COM Programmer's Reference* provides more information on the functions **OleInitialize** and **CoRegisterClassObject**. *Inside OLE, Second Edition*, published by Microsoft Press, provides more information about verifying application entries in the registration database.

## Registering the Hello Application

Finally, the sample registers the Hello application object in the running object table (ROT). Registering an active object allows ActiveX clients to retrieve an object that is already running, rather than create a new instance of the object. Use weak registration (ACTIVEOBJECT\_WEAK) so that the running object table releases its reference when all external references are released. If strong registration is used (the default), the running object table will not release the reference until [**RevokeActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-revokeactiveobject) is called. For more information, refer to [Dispatch Interface and API Functions](https://msdn.microsoft.com/windows/desktop/75BFF268-BD85-49C4-B761-B557F4B1C588).

The following sample shows the registration entries for the Hello object.


```C++
REGEDIT
; Registration information for Automation Hello 2.0 Application.

; Version independent registration. Points to Version 2.0.
HKEY_CLASSES_ROOT\Hello.Application = Automation Hello Application
HKEY_CLASSES_ROOT\Hello.Application\Clsid = {F37C8061-4AD5-101B-B826-00DD01103DE1}

; Version 2.0 registration.
HKEY_CLASSES_ROOT\Hello.Application.2 = Automation Hello 2.0 Application
HKEY_CLASSES_ROOT\Hello.Application.2\Clsid = {F37C8061-4AD5-101B-B826-00DD01103DE1}
 
```



## Implementing IDispatch

The **IDispatch** interface provides access to and information about an object. The interface requires the member functions [**GetTypeInfoCount**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-gettypeinfocount), [**GetTypeInfo**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-gettypeinfo), **GetIdsOfNames**, and [**Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke). The Hello sample implements **IDispatch** as follows (Hello.cpp):


```C++
STDMETHODIMP
CHello::GetTypeInfoCount(UINT * pctinfo)
{
   if ( pctinfo == NULL) 
      return E_NOTIMPL;

   *pctinfo = 1;
   return NOERROR;
}

STDMETHODIMP
CHello::GetTypeInfo(
      UINT itinfo,
      LCID lcid,
      ITypeInfo ** pptinfo)
{
   if (pptinfo == NULL)
      return E_INVALIDARG;

   if(itinfo != 0)
      return DISP_E_BADINDEX;

   *pptinfo = NULL;

   m_ptinfo->AddRef();
   *pptinfo = m_ptinfo;

   return NOERROR;
}

STDMETHODIMP
CHello::GetIDsOfNames(
      REFIID riid,
      OLECHAR ** rgszNames,
      UINT cNames,
      LCID lcid,
      DISPID * rgdispid)
{
// We are delegating input validation to DispGetIDsOfNames.
// Real-world applications may require additional validation.
   return DispGetIDsOfNames(m_ptinfo, rgszNames, cNames, rgdispid);
}

STDMETHODIMP
CHello::Invoke(
      DISPID dispidMember,
      REFIID riid,
      LCID lcid,
      WORD wFlags,
      DISPPARAMS * pdispparams,
      VARIANT * pvarResult,
      EXCEPINFO * pexcepinfo,
      UINT * puArgErr)
{
// We are delegating input validation to DispInvoke.
// Real-world applications may require additional validation.

      return DispInvoke(
      this, m_ptinfo,
      dispidMember, wFlags, pdispparams,
      pvarResult, pexcepinfo, puArgErr);
}
 
```



Automation includes two functions, **DispGetIDOfNames** and [**DispInvoke**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-dispinvoke), which provide standard implementations for [**GetIDsOfNames**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-getidsofnames), and [**IDispatch::Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke). The Hello sample uses these two functions to simplify the code.

## Implementing IUnknown

Every OLE object must implement the **IUnknown** interface, which allows controllers to query the object to find out what interfaces it supports. **IUnknown** has three member functions: **QueryInterface**, **AddRef**, and **Release**. The Hello sample implements these functions for the CHello object as follows (Hello.cpp):


```C++
STDMETHODIMP
CHello::QueryInterface(REFIID iid, void ** ppv)
{
   if (ppv == NULL)
      return E_INVALIDARG;
   *ppv = NULL;
   if (iid == IID_IUnknown || iid == IID_IDispatch || iid == IID_IHello  ) 
      *ppv = this;   
   else if (iid == IID_ISupportErrorInfo)
      *ppv = &amp;m_SupportErrorInfo;
   else return E_NOINTERFACE; 
   AddRef();
   return NOERROR;
}

STDMETHODIMP_(ULONG)
CHello::AddRef(void)
{
   return ++m_cRef;
}

STDMETHODIMP_(ULONG)
CHello::Release(void)
{
if (--m_cRef == 0)
   {
      delete this;
      return 0;
   }
   return m_cRef;
}
 
```



## Implementing IClassFactory

A class factory is a class that is capable of creating instances of another class. The Hello sample implements a single class factory named CHelloCF, as follows (HelloCf.cpp):


```C++
CHelloCF::CHelloCF(void)
{
   m_cRef = 0; 
}

STDMETHODIMP
CHelloCF::QueryInterface(REFIID iid, void ** ppv)
{
   if (ppv == NULL)
      return E_INVALIDARG;

   *ppv = NULL;
   if (iid == IID_IUnknown || iid == IID_IClassFactory)
      *ppv = this;
   else 
      return E_NOINTERFACE;
   AddRef();
   return NOERROR;
}

STDMETHODIMP_(ULONG)
CHelloCF::AddRef(void)
{
   return ++m_cRef;
}

STDMETHODIMP_(ULONG)
CHelloCF::Release(void)
{
   if (--m_cRef == 0)
   {
      delete this;
      return 0;
   }
   return m_cRef;
}

STDMETHODIMP
CHelloCF::CreateInstance(IUnknown * punkOuter,
                  REFIID riid,
                  void ** ppv)
{
   HRESULT hr;

   if (ppv == NULL)
      return E_INVALIDARG;

   *ppv = NULL;

   // This implementation doesn't allow aggregation.
   if (punkOuter)
      return CLASS_E_NOAGGREGATION;

   hr = g_phello->QueryInterface(riid, ppv);
   if (FAILED(hr)) 
   {
      g_phello->Quit();
      return hr;
   }
   return NOERROR;
}
STDMETHODIMP
CHelloCF::LockServer(BOOL fLock)
{
   CoLockObjectExternal(g_phello, fLock, TRUE);
   return NOERROR;
}
 
```



The function CHelloCF::CHelloCF is a C++ constructor function. By default, the constructor function initializes the object's VTBLs; CHelloCF::CHelloCF also initializes the reference count for the class.

The class factory supports six member functions. **QueryInterface**, **AddRef**, and **Release** are the required **IUnknown** members, and [**CreateInstance**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-itypeinfo-createinstance) and **LockServer** are the required **IClassFactory** members.

## Implementing VTBL Binding

In addition to the [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface, the Hello sample supports VTBL binding. When a member is invoked, objects that support a VTBL interface return an HRESULT instead of a value, and pass their return value as the last parameter. Objects may also accept a LCID parameter, which allows them to parse strings correctly for the local language. The following example shows how the **Visible** property is implemented (Hello.cpp):


```C++
STDMETHODIMP
CHello::put_Visible(BOOL bVisible)
{
   ShowWindow(bVisible ? SW_SHOW : SW_HIDE);
   return NOERROR;
}

STDMETHODIMP
CHello::get_Visible(BOOL * pbool)
{
   if (pbool == NULL)
      return E_INVALIDARG;

   *pbool =  m_bVisible;
   return NOERROR;
}
 
```



Additional information must be specified in the .odl file to create a [dual](dual.md) interface, as shown in [Creating Type Information](#creating-type-information).

## Registering the Interface for VTBL Binding

The following lines from the Hello.reg file register the interface for VTBL binding. In the example, "ProxyStubClsid" refers to the proxy and stub implementation of [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch).


```C++
HKEY_CLASSES_ROOT\Interface\{F37C8062-4AD5-101B-B826-00DD01103DE1} = IHello
HKEY_CLASSES_ROOT\Interface\{F37C806 2-4AD5-101B-B826-00DD01103DE1}\TypeLib = {F37C8060-4AD5-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{F37C8062-4AD5-101B-B826-00DD01103DE1}\ProxyStubClsid32 = {00020424-0000-0000-C000-000000000046}
 
```



## Handling Errors

The Hello sample includes an exception handler that passes exceptions through [**IDispatch::Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke), and supports rich error information through VTBLs (Main.cpp):


```C++
// STR_LEN is a #defined constant = 100
HRESULT RaiseException(int nID, REFGUID rguid) 
{
   extern SCODE g_scodes[];
   TCHAR szError[STR_LEN];   
   ICreateErrorInfo *pcerrinfo;  
   IErrorInfo *perrinfo;
   HRESULT hr;
   BSTR bstrDescription = NULL;
   
   if (LoadString(g_phello->m_hinst, nID, szError, sizeof(szError)))
      bstrDescription = SysAllocString(TO_OLE_STRING(szError));    
   
   // Set ErrorInfo object so that vtable binding controller can get
   // rich error information. If the controller is using IDispatch
   // to access properties or methods, DispInvoke will fill the
   // EXCEPINFO structure using the values specified in the ErrorInfo
   // object and DispInvoke will return DISP_E_EXCEPTION. The property
   // or method must return a failure SCODE for DispInvoke to do this.
   hr = CreateErrorInfo(&amp;pcerrinfo); 
   if (SUCCEEDED(hr))
   {
      pcerrinfo->SetGUID(rguid);
      pcerrinfo->SetSource(g_phello->m_bstrProgID);
      if (bstrDescription)
         pcerrinfo->SetDescription(bstrDescription);  
      hr = pcerrinfo->QueryInterface(IID_IErrorInfo, (LPVOID *) &amp;perrinfo);
      if (SUCCEEDED(hr))
{
         SetErrorInfo(0, perrinfo);
         perrinfo->Release();
      }  
      pcerrinfo->Release();
   }  
   
   if (bstrDescription)
      SysFreeString(bstrDescription);

   return ResultFromScode(g_scodes[nID-1001]);
}  
```



The member functions of the Hello sample call this routine when an exception occurs. **RaiseException** sets the system's error object so that controller applications that call through VTBLs can retrieve rich error information. Controllers that call through [**IDispatch::Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke) will be returned with this error information by [**DispInvoke**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-dispinvoke) through the EXCEPINFO structure.

Hello also implements the [**ISupportErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-isupporterrorinfo) interface, which allows ActiveX clients to query whether an error object will be available (Hello.cpp):


```C++
CSupportErrorInfo::CSupportErrorInfo(IUnknown * punkObject,
                           REFIID riid)
{
   m_punkObject = punkObject;
   m_iid = riid;
}

STDMETHODIMP
CSupportErrorInfo::QueryInterface(REFIID iid, void ** ppv)
{
   return m_punkObject->QueryInterface(iid, ppv);
}

STDMETHODIMP_(ULONG)
CSupportErrorInfo::AddRef(void)
{
   return m_punkObject->AddRef();
}

STDMETHODIMP_(ULONG)
CSupportErrorInfo::Release(void)
{
   return m_punkObject->Release();
}

STDMETHODIMP
CSupportErrorInfo::InterfaceSupportsErrorInfo(REFIID riid)
{
   return (riid == m_iid) ? NOERROR : S_FALSE;
}
 
```



## Releasing Objects and OLE

When the Hello application ends, it revokes the class factory and the active object, and uninitializes OLE. For example (Main.cpp):


```C++
void Uninitialize(DWORD dwRegisterCF, DWORD dwRegisterActiveObject)
{
   if (dwRegisterCF != 0)
      CoRevokeClassObject(dwRegisterCF);
   if (dwRegisterActiveObject != 0)
      RevokeActiveObject(dwRegisterActiveObject, NULL);
   OleUninitialize();
}
 
```



## Creating Type Information

Type information for the Hello sample is described in ODL. The MIDL compiler uses the .odl file to create a type library (Hellotl.tlb) and a header file (Hellotl.h).

The following example shows the description for the Hello type library, interface, and Application object (Hello.odl):


```C++
[
   uuid(F37C8060-4AD5-101B-B826-00DD01103DE1),      // LIBID_Hello.
   helpstring("Hello 2.0 Type Library"),
   version(2.0)
]
library Hello
{
   importlib("stdole32.tlb"); 
   [
   uuid(F37C8062-4AD5-101B-B826-00DD01103DE1),   // IID_Ihello.
   helpstring("Application object for the Hello application."),
   oleautomation,
   dual
   ]
   interface IHello : IDispatch
   {
      [propget, helpstring("Returns the application of the object.")]
      HRESULT Application([out, retval] IHello** retval);

   [propget,
      helpstring("Returns the full name of the application.")]
      HRESULT FullName([out, retval] BSTR* retval);

      [propget, id(0), 
      helpstring("Returns the name of the application.")]
      HRESULT Name([out, retval] BSTR* retval);

      [propget, helpstring("Returns the parent of the object.")]
      HRESULT Parent([out, retval] IHello** retval);

      [propput]
      HRESULT Visible([in] VARIANT_BOOL VisibleFlag);
      [propget,
      helpstring
      ("Sets or returns whether the main window is visible.")]
      HRESULT Visible([out, retval] VARIANT_BOOL* retval);

      [helpstring("Exits the application.")]
      HRESULT Quit();

      [propput,
      helpstring("Sets or returns the hello message to be used.")]
      HRESULT HelloMessage([in] BSTR Message);
      [propget] 
      HRESULT HelloMessage([out, retval] BSTR *retval);

      [helpstring("Say Hello using HelloMessage.")]
      HRESULT SayHello();
   }


   [
      uuid(F37C8061-4AD5-101B-B826-00DD01103DE1),      // CLSID_Hello.
      helpstring("Hello Class"),
      appobject
   ]
   coclass Hello
   {
      [default]      interface IHello;
                     interface IDispatch;
   }
}
 
```



The items enclosed by square brackets are *attributes*, which provide further information about the objects in the file. The [oleautomation Attribute](oleautomation.md) and [dual Attribute](dual.md) attributes, for example, indicate that the IHello interface supports both [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) and VTBL binding. The [appobject Attribute](appobject.md) attribute indicates that Hello is the Application object.

For more information about attributes, refer to [Type Libraries and the Object Description Language](type-libraries-and-the-object-description-language.md).

## Creating the Hello Registration File

The system registration database lists all the OLE objects in the system. OLE uses this database to locate objects and determine their capabilities. The registration file registers the application, the type library, and the exposed classes of the sample (Hello.reg):


```C++
REGEDIT
; Registration information for Automation Hello 2.0 Application.

; Version independent registration. Points to Version 2.0.
HKEY_CLASSES_ROOT\Hello.Application = Hello 2.0 Application
HKEY_CLASSES_ROOT\Hello.Application\Clsid = {F37C8061-4AD5-101B-B826-00DD01103DE1}

; Version 2.0 registration
HKEY_CLASSES_ROOT\Hello.Application.2 = Hello 2.0 Application
HKEY_CLASSES_ROOT\Hello.Application.2\Clsid = {F37C8061-4AD5-101B-B826-00DD01103DE1} 
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1} = Hello 2.0 Application
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1}\ProgID = Hello.Application.2
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1}\VersionIndependentProgID = Hello.Application
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1}\LocalServer = hello.exe /Automation
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1}\TypeLib = {F37C8061-4AD5-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1}\Programmable

; Type library registration information
HKEY_CLASSES_ROOT\TypeLib\{F37C8060-4AD5-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\TypeLib\{F37C8060-4AD5-101B-B826-00DD01103DE1}\2.0 = Hello 2.0 Type Library
HKEY_CLASSES_ROOT\TypeLib\{F37C8060-4AD5-101B-B826-00DD01103DE1}\2.0\HELPDIR =
; English
HKEY_CLASSES_ROOT\TypeLib\{F37C8060-4AD5-101B-B826-00DD01103DE1}\2.0\9\win32 = hello.tlb

;Interface registration. All interfaces that support vtable binding ;must be registered as follows. RegisterTypeLib & LoadTypeLib will do ;this automatically.

; IID_IHello = {F37C8062-4AD5-101B-B826-00DD01103DE1}
; LIBID_Hello = {F37C8060-4AD5-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{F37C8062-4AD5-101B-B826-00DD01103DE1} = IHello
HKEY_CLASSES_ROOT\Interface\{F37C8062-4AD5-101B-B826-00DD01103DE1}\TypeLib = {F37C8060-4AD5-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{F37C8062-4AD5-101B-B826-00DD01103DE1}\ProxyStubClsid32 = {00020424-0000-0000-C000-000000000046}
 
```



To merge an object's registration information with the system registry, the object should expose the **DLLRegisterServer** API, as described in the *COM Programmer's Reference*. **DLLRegisterServer** should call [**RegisterTypeLib**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registertypelib) to register the type library and the interfaces supported by the application. This only applies to in-process servers. Out-of-process servers such as the Hello sample do not export **DLLRegisterServer**.

 

 




