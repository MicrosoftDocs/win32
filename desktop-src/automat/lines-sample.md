---
title: Lines Sample
description: The Lines sample is an ActiveX component application that implements collections.
ms.assetid: 04fdf5ae-c2a4-4638-998b-148dc0319112
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Lines Sample

The Lines sample is an ActiveX component application that implements collections. This sample allows a collection of lines to be drawn on a pane using Automation. This sample implements the following features:

-   *Dual* interfaces that allow access to automation properties and methods through VTBL binding and [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch).

-   Rich error information for VTBL-binding controllers implemented by [**ISupportErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-isupporterrorinfo) and [**IErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ierrorinfo).

-   Two collections.

-   Active object registration using [**RegisterActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-registeractiveobject) and [**RevokeActiveObject**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-revokeactiveobject).

-   Correct shutdown behavior.

-   A registration file that contains Lines.Application as the ProgID.

-   Initial invisibility.

<!-- -->

-   [Initializing OLE](#initializing-ole)
-   [Initializing the Active Object](#initializing-the-active-object)
-   [Registering the Active Object](#registering-the-active-object)
-   [Creating the Lines Registration File](#creating-the-lines-registration-file)
-   [Registering the Lines Application Files](#registering-the-lines-application-files)
-   [Creating the IUnknown Interface for the Lines Application](#creating-the-iunknown-interface-for-the-lines-application)
-   [Creating the IDispatch Interface for the Lines Application](#creating-the-idispatch-interface-for-the-lines-application)
    -   [Implementing IDispatch by Calling CreateStdDispatch](#implementing-idispatch-by-calling-createstddispatch)
    -   [Implementing IDispatch by Delegating](#implementing-idispatch-by-delegating)
-   [Implementing the Class Factory for the Lines Application](#implementing-the-class-factory-for-the-lines-application)
-   [Setting Up the VTBL Interface](#setting-up-the-vtbl-interface)
-   [Implementing the Value Property](#implementing-the-value-property)
-   [Restricting Access to Objects](#restricting-access-to-objects)
-   [Creating Collection Objects](#creating-collection-objects)
-   [Implementing the IEnumVARIANT Interface for the Lines Application](#implementing-the-ienumvariant-interface-for-the-lines-application)
-   [Implementing the \_NewEnum Property for the Lines Application](#implementing-the--newenum-property-for-the-lines-application)
-   [Returning Errors](#returning-errors)
-   [Passing Exceptions Through VTBLs](#passing-exceptions-through-vtbls)
-   [Releasing OLE on Exit](#releasing-ole-on-exit)
-   [Writing an Object Description Script](#writing-an-object-description-script)

## Initializing OLE

The following routine initializes OLE, and then creates an instance of the Lines Application object (Main.cpp):


```C++
BOOL InitInstance (HINSTANCE hinst)
{
   HRESULT hr;

   // Intialize OLE.
   hr = OleInitialize(NULL);
   if (FAILED(hr))
      return FALSE;

   // Create an instance of the Lines Application object. The object is
   // created with refcount 0.
   hr = CApplication::Create(hinst, &amp;g_pApplication);
   if (FAILED(hr))
      return FALSE;
   return TRUE;
}
 
```



## Initializing the Active Object

The following function creates and registers the application's class factory, and then registers the Lines Application object as the active object (Main.cpp):


```C++
BOOL ProcessCmdLine(LPSTR lpCmdLine, LPDWORD pdwRegisterCF,
               LPDWORD pdwRegisterActiveObject, int nCmdShow)
{
   LPCLASSFACTORY pcf = NULL;
   HRESULT hr; 
   if (lpCmdLine == NULL ||
      pdwRegisterCF == NULL ||
      pdwRegisterActiveObject == NULL)
   return E_INVALIDARG;

   *pdwRegisterCF = 0;
   *pdwRegisterActiveObject = 0;

   // Expose class factory for application object if command line
   // contains the /Automation switch.
   if (_fstrstr(lpCmdLine, "-Automation") != NULL
      || _fstrstr(lpCmdLine, "/Automation") != NULL)
   {
      pcf = new CApplicationCF;
      if (!pcf)
         goto error;
      pcf->AddRef();
      hr = CoRegisterClassObject(CLSID_Lines, pcf,
                        CLSCTX_LOCAL_SERVER, REGCLS_SINGLEUSE,
                        pdwRegisterCF);
      if (hr != NOERROR)
         goto error;
      pcf->Release();
   }
   else            // Show window if started as stand-alone. 
   g_pApplication->ShowWindow(nCmdShow );

// Register Lines Application object in the running object table 
// (ROT). Use weak registration so that the ROT releases its reference
// when all external references are released.
   hr = RegisterActiveObject(g_pApplication, CLSID_Lines, ACTIVEOBJECT_WEAK,
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



## Registering the Active Object

The sample application exposes the class factory for the Lines application, **CApplicationCF**, if the command line contains the **/Automation** switch. The switch indicates that the application was started for programmatic access, and therefore OLE needs to register the class factory and create an instance of the Application object. OLE applies this switch if it appears on the command line or in the application's registration file. OLE also supports the **/Embedding** switch, which indicates that an application has been started by a container application.

You should register the class factory for the Application object only if the application is launched with the **/Automation** switch. When **/Automation** is not specified, the application has been started for some reason other than programmatic access through Automation. If the class factory is registered under these circumstances, and a user later requests a new instance of the Application object, Automation will return the existing instance instead of creating a new one.

The sample calls **CoRegisterClassObject** to register the class factory as the active object. The CLSCTX\_LOCAL\_SERVER flag means the code that creates and manages Application objects will run in a separate process space.

Because the Application object's class factory is exposed, the call specifies the REGCLS\_SINGLEUSE flag. When a multiple-document interface (MDI) application starts, it typically registers the class factory for its Document object, specifying REGCLS\_MULTIPLEUSE. This flag, defined in the REGCLS enumeration, allows the existing application instance to be used later, when instances of the document objects need to be created. Each new Application object, however, requires a new instance of the application to be launched, and should therefore specify REGCLS\_SINGLEUSE. If the application registered its class factory using REGCLS\_MULTIPLEUSE, then the next **CreateObject** call that tries to create the application will get an existing copy.

In the following example, the macro defines a CLSID for Lines (Tlb.h):


```C++
DEFINE_GUID(CLSID_Lines,0x3C591B21,0x1F13,0x101B,0xB8,0x26,0x00,0xDD,0x01,0x10,0x3D,0xE1);
 
```



When the MIDL compiler creates the optional header file (Tlb.h), it inserts DEFINE\_GUID macros for each library, interface, and each class in an application.

## Creating the Lines Registration File

The registration file provides information about the application, the Application object, classes of objects, type libraries, and interfaces. Entries for objects and interfaces start with the constant HKEY\_CLASSES\_ROOT, which **IDispatch::GetTypeInforesents** the root key of the entire registration database. Entries for type libraries start with HKEY\_TYPELIB\_ROOT. After the constant, each entry supplies specific information about an object, type library, or interface.

Use the following steps to create the registration file:

1.  Copy the file Lines.reg.

2.  Rename and edit this file, adding entries for the application.

## Registering the Lines Application Files

The Lines sample uses the following entries to register its Application object (Lines.Application) and its type library with the system (Lines.reg):


```C++
REGEDIT
; Registration information for the Lines Application object. Version
; independent registration.

HKEY_CLASSES_ROOT\Lines.Application = Lines
HKEY_CLASSES_ROOT\Lines.Application\Clsid = {3C591B21-1F13-101B-B826-00DD01103DE1}

; Version 1.0 registration
HKEY_CLASSES_ROOT\Lines.Application.1 = Lines 1.0
HKEY_CLASSES_ROOT\Lines.Application.1\Clsid = {3C591B21-1F13-101B-B826-00DD01103DE1}
   
HKEY_CLASSES_ROOT\CLSID\{3C591B21-1F13-101B-B826-00DD01103DE1} = Lines 1.0
HKEY_CLASSES_ROOT\CLSID\{3C591B21-1F13-101B-B826-00DD01103DE1}\ProgID = Lines.Application.1
HKEY_CLASSES_ROOT\CLSID\{3C591B21-1F13-101B-B826-00DD01103DE1}\VersionIndependentProgID = Lines.Application
HKEY_CLASSES_ROOT\CLSID\{3C591B21-1F13-101B-B826-00DD01103DE1}\LocalServer32 = lines.exe /Automation
HKEY_CLASSES_ROOT\CLSID\{3C591B21-1F13-101B-B826-00DD01103DE1}\TypeLib = {3C591B20-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\CLSID\{3C591B21-1F13-101B-B826-00DD01103DE1}\Programmable

; Type library registration information.
HKEY_CLASSES_ROOT\TypeLib\{3C591B20-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\TypeLib\{3C591B20-1F13-101B-B826-00DD01103DE1}\1.0 = Lines 1.0 Type Library
HKEY_CLASSES_ROOT\TypeLib\{3C591B20-1F13-101B-B826-00DD01103DE1}\1.0\HELPDIR =
;English     
HKEY_CLASSES_ROOT\TypeLib\{3C591B20-1F13-101B-B826-00DD01103DE1}\1.0\9\win32 = lines.tlb 

; Interface registration. All interfaces that support VTBL binding
; must be registered as follows. RegisterTypeLib will do this 
; automatically.

; LIBID_Lines = {3C591B20-1F13-101B-B826-00DD01103DE1}

; IID_IPoint = {3C591B25-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B25-1F13-101B-B826-00DD01103DE1} = IPoint
HKEY_CLASSES_ROOT\Interface\{3C591B25-1F13-101B-B826-00DD01103DE1}\TypeLib = {3C591B20-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B25-1F13-101B-B826-00DD01103DE1}\ProxyStubClsid32 = {00020424-0000-0000-C000-000000000046}

; IID_ILine = {3C591B24-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B24-1F13-101B-B826-00DD01103DE1} = ILine
HKEY_CLASSES_ROOT\Interface\{3C591B24-1F13-101B-B826-00DD01103DE1}\TypeLib = {3C591B20-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B24-1F13-101B-B826-00DD01103DE1}\ProxyStubClsid32 = {00020424-0000-0000-C000-000000000046}

; IID_ILines = {3C591B26-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B26-1F13-101B-B826-00DD01103DE1} = ILines
HKEY_CLASSES_ROOT\Interface\{3C591B26-1F13-101B-B826-00DD01103DE1}\TypeLib = {3C591B20-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B26-1F13-101B-B826-00DD01103DE1}\ProxyStubClsid32 = {00020424-0000-0000-C000-000000000046}

; IID_IPoints = {3C591B27-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B27-1F13-101B-B826-00DD01103DE1} = IPoints
HKEY_CLASSES_ROOT\Interface\{3C591B27-1F13-101B-B826-00DD01103DE1}\TypeLib = {3C591B20-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B27-1F13-101B-B826-00DD01103DE1}\ProxyStubClsid32 = {00020424-0000-0000-C000-000000000046}

; IID_IPane = {3C591B23-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B23-1F13-101B-B826-00DD01103DE1} = IPane
HKEY_CLASSES_ROOT\Interface\{3C591B23-1F13-101B-B826-00DD01103DE1}\TypeLib = {3C591B20-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B23-1F13-101B-B826-00DD01103DE1}\ProxyStubClsid32 = {00020424-0000-0000-C000-000000000046}

; IID_IApplication = {3C591B22-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B22-1F13-101B-B826-00DD01103DE1} = IApplication
HKEY_CLASSES_ROOT\Interface\{3C591B22-1F13-101B-B826-00DD01103DE1}\TypeLib = {3C591B20-1F13-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\Interface\{3C591B22-1F13-101B-B826-00DD01103DE1}\ProxySt
 
```



## Creating the IUnknown Interface for the Lines Application

The **IUnknown** interface for the Lines object looks like this (Lines.cpp):


```C++
STDMETHODIMP
CLine::QueryInterface(REFIID iid, void ** ppv)
{
   if (ppv == NULL)
      return E_INVALIDARG;

   *ppv = NULL;
   
   if (iid == IID_IUnknown || iid == IID_IDispatch || iid == IID_ILine)
      *ppv = this; 
   else if (iid == IID_ISupportErrorInfo)
      *ppv = &amp;m_SupportErrorInfo;
   else return E_NOINTERFACE; 

   AddRef();
   return NOERROR;
}

STDMETHODIMP_(ULONG)
CLine::AddRef(void)
{
   return ++m_cRef;
}

STDMETHODIMP_(ULONG)
CLine::Release(void)
{
   if(--m_cRef == 0)
   {
      delete this;
      return 0;
   }
   return m_cRef;
}
 
```



## Creating the IDispatch Interface for the Lines Application

The following sections explain how to implement [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) by using [**CreateStdDispatch**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-createstddispatch) and [**DispInvoke**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-dispinvoke).

-   [Implementing IDispatch by Calling CreateStdDispatch](#implementing-idispatch-by-calling-createstddispatch)
-   [Implementing IDispatch by Delegating](#implementing-idispatch-by-delegating)

### Implementing IDispatch by Calling CreateStdDispatch

The simplest way to implement the [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface is to call [**CreateStdDispatch**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-createstddispatch). This approach works for ActiveX objects that return only the standard dispatch exception codes, support a single national language, and do not support dual interfaces.

[**CreateStdDispatch**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-createstddispatch) returns a pointer to the created [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface. It takes three pointers as input: a pointer to the object's **IUnknown** interface, a pointer to the object to expose, and a pointer to the type information for the object. The following example is taken from the COM Fundamentals DspCalc2 sample shipped with the Platform SDK. This example implements **IDispatch** for an object named CCalc by calling **CreateStdDispatch** on the loaded type information:


```C++
CCalc *
CCalc::Create()
{
   HRESULT hresult;
   CCalc * pcalc;
   ITypeLib * ptlib;
   ITypeInfo * ptinfo;
   IUnknown * punkStdDisp;

   ptlib = NULL;
   ptinfo = NULL;


   if ((pcalc = new CCalc()) == NULL)
      return NULL;
   pcalc->AddRef();

   // Load the type library from the information in the registry.
   if ((hresult = LoadRegTypeLib(LIBID_DspCalc2, 1, 0, 0x0409, &amp;ptlib))
      !=    NOERROR){ 
      goto LError0;
   }
   if ((hresult = ptlib->GetTypeInfoOfGuid(IID_ICalculator, &amp;ptinfo))
      != NOERROR){
      goto LError0;
   }

   // Create an aggregate with an instance of the default
   // implementation of IDispatch that is initialized with our
   // TypeInfo.
   //
   hresult = CreateStdDispatch(
         pcalc,                  // Controlling unknown.
         &amp;(pcalc->m_arith),         // VTBL pointer to dispatch on.
         ptinfo,
         &amp;punkStdDisp);
   if(hresult != NOERROR)
      goto LError0;
   pcalc->m_punkStdDisp = punkStdDisp;

ptinfo->Release();
ptlib->Release();

LError0:; 
   pcalc->Release();
   if (ptinfo != NULL)
      ptinfo->Release();
   if (ptlib != NULL) 
      ptlib->Release();
}
 
```



### Implementing IDispatch by Delegating

Another way to implement [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) is to use the dispatch functions [**DispInvoke**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-dispinvoke) and [**DispGetIDsOfNames**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-dispgetidsofnames). These functions give you the option of supporting multiple national languages and creating application-specific exceptions that are passed back to ActiveX clients.

The Lines sample implements [**IDispatch::GetIDsOfNames**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-getidsofnames) and [**IDispatch::Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke) using these functions (Lines.cpp):


```C++
STDMETHODIMP 
CLines::GetIDsOfNames(
      REFIID riid,
      char ** rgszNames,
      UINT cNames,
      LCID lcid,
      DISPID * rgdispid)
{
// We are delegating input validation to DispGetIDsOfNames.
// Real-world applications may require additional validation.

   return DispGetIDsOfNames(m_ptinfo, rgszNames, cNames, rgdispid);
}

STDMETHODIMP
CLines::Invoke(
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



The Lines object implements the **IID\_ILine** *dual* interface for VTBL binding. It also implements the **IID\_ISupportErrorInfo** interface so that it can return rich, contextual error information through VTBLs.

## Implementing the Class Factory for the Lines Application

The Lines sample implements a class factory for its Application object, as follows (Appcf.cpp):


```C++
STDMETHODIMP
CApplicationCF::CreateInstance(IUnknown * punkOuter,
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

   // This is REGCLS_SINGLEUSE class factory, so CreateInstance will be
   // called at most once. An application object has a REGCLS_SINGLEUSE 
   // class factory. The global application object has already been 
   // created when CreateInstance is called. A REGCLS_MULTIPLEUSE class 
   // factory's CreateInstance would be called multiple times and would 
   // create a new object each time. An MDI application would have a 
   // REGCLS_MULTIPLEUSE class factory for its document objects.
   
   hr = g_pApplication->QueryInterface(riid, ppv);
   if (FAILED(hr)) 
   {
      g_pApplication->Quit();
      return hr;
   }
   return NOERROR;
}

STDMETHODIMP
CApplicationCF::LockServer(BOOL fLock)
{
   CoLockObjectExternal(g_pApplication, fLock, TRUE);
   return NOERROR;
}
 
```



The object's class factory must also implement an **IUnknown** interface. For example (Appcf.cpp):


```C++
STDMETHODIMP
CApplicationCF::QueryInterface(REFIID iid, void ** ppv)
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
CApplicationCF::AddRef(void)
{
   return ++m_cRef;
}

STDMETHODIMP_(ULONG)
CApplicationCF::Release(void)
{
   if(--m_cRef == 0)
   {
      delete this;
      return 0;
   }
   return m_cRef;
}
 
```



## Setting Up the VTBL Interface

The Lines sample supports VTBL binding as well as the **IDispatch** interface. By supporting this [dual](dual.md) interface, the sample allows ActiveX clients both the flexibility of the [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface and the speed of VTBLs. Controllers that know the names of the members can compile directly against the function pointers in the VTBL. Controllers that do not have this information can use **IDispatch** at run time.

To have a *dual* interface, an interface must:

-   Declare all of its members to return an HRESULT, and pass their actual return values as the last parameter.

-   Have only Automation-compatible parameters and return types, as described in [Conversion and Manipulation Functions](conversion-and-manipulation-functions.md).

-   Specify the **dual** attribute on the interface description in the .odl file.

-   Initialize the VTBLs with the appropriate member function pointers.

In the Lines sample, the interfaces **IPoint**, **IPoints**, **ILine**, **ILines**, **IPane**, and **IApplication** are all dual interfaces. The **IPoint** interface defines functions that get and put the values of the **X** and **Y** properties, as follows (Point.cpp).u The Lines.h header file contains the declarations for the m\_nX and m\_nY private variables which hold the x and y coordinates of a point object.


```C++
STDMETHODIMP
CPoint::get_x(int * pnX)
{
   if (pnX == NULL)
      return E_INVALIDARG;

   *pnX = m_nX;
   return NOERROR;
}

STDMETHODIMP
CPoint::put_x(int nX)
{
   m_nX = nX;
   return NOERROR;
}

STDMETHODIMP
CPoint::get_y(int * pnY)
{
   if (pnY == NULL)
      return E_INVALIDARG;

   *pnY = m_nY; 
   return NOERROR;
}

STDMETHODIMP
CPoint::put_y(int nY)
{
   m_nY = nY; 
   return NOERROR;
}
 
```



The **get\_x** and **get\_y** accessor functions pass their return values in the parameters *pnX* and *pnY*, and return an HRESULT as the function value.

In the .odl file, the interface is described as follows (Lines.odl):


```C++
[
      uuid(3C591B25-1F13-101B-B826-00DD01103DE1),    // IID_IPoint.
      helpstring("Point object."),
      oleautomation,
      dual
   ]
   interface IPoint : IDispatch
   {
      [propget, helpstring("Returns and sets x coordinate.")]
      HRESULT x([out, retval] int* retval); 
      [propput, helpstring("Returns and sets x coordinate.")]
      HRESULT x([in] int Value);

      [propget, helpstring("Returns and sets y coordinate.")]
      HRESULT y([out, retval] int* retval); 
      [propput, helpstring("Returns and sets y coordinate.")]
      HRESULT y([in] int Value);
   }
 
```



The attributes [oleautomation](oleautomation.md) and [dual](dual.md) indicate that the interface supports both **IDispatch** and VTBL binding. All of the member functions are declared with HRESULT return values. The **Get** accessor functions, indicated by the [propget](propget.md) attribute, return their value in the last parameter. This parameter has the [out](out.md) and [retval](retval.md) attributes.

The Application object exposes the following method (App.cpp):


```C++
STDMETHODIMP
CApplication::CreatePoint(IPoint ** ppPoint)
{
   CPoint * ppoint = NULL;
   HRESULT hr;

   if (ppPoint == NULL)
      return E_INVALIDARG;

   // Create new item and QueryInterface for IDispatch.

   hr = CPoint::Create(&amp;ppoint);
   if (FAILED(hr))
   {
      hr = RaiseException(IDS_OutOfMemory, IID_IApplication); 
      goto error;
   }          

   hr = ppoint->QueryInterface(IID_IDispatch, (void **)ppPoint); 
   if (FAILED(hr))
   {
      hr = RaiseException(IDS_Unexpected, IID_IApplication);
      goto error;
   }
    return NOERROR;
    
error:
   if (ppoint)
      delete ppoint;
   return hr;
}
 
```



The **CreatePoint** method creates a new point and returns a pointer to it in the parameter ppPoint. The source code for the **RaiseException** function can be found in the Lines sample file Main.cpp

In the Lines sample, the CLine object exposes the **Color** property. The Lines.h header file contains the declaration for the m\_colorref private variable which holds the RGB color of a line object. The Color property is implemented by the following accessor functions (Lines.cpp):


```C++
STDMETHODIMP
CLine::get_Color(long * plColorref)
{
   if (plColorref == NULL)    
      return E_INVALIDARG;

   *plColorref = m_colorref;
   return NOERROR;
}
STDMETHODIMP
CLine::put_Color(long lColorref)
{
   m_colorref = (COLORREF)lColorref;
   return NOERROR;
}
 
```



## Implementing the Value Property

In the Lines sample, ILines.Item, IPoints.Item, and IApplication.Name are the Value properties of the objects ILines, IPoints, and IApplication, respectively. The ILines.Item object is described as follows:


```C++
interface ILines : IDispatch
   {
.
.// Some descriptions omitted for brevity.
.
   [propget, id(0), helpstring(
"Given an integer index, returns one of the lines in the collection")]
   HRESULT Item([in] long Index,[out, retval] ILine** retval); 
// ...
}
```



Using this property, a user can refer to the fourth line in the collection as `ILines(4).Item` or simply as `ILines(4)`.

For more information on recommended objects, properties, and methods, see [Standard Objects and Naming Guidelines](standard-objects-and-naming-guidelines.md).

## Restricting Access to Objects

Automation provides several ways of restricting access to objects. The simplest approach is not to document the properties and methods you do not want users to see. Alternatively, you can prevent a property or method from appearing in type library browsers by specifying the [hidden](hidden.md) attribute in the .odl file.

The [restricted](restricted.md) attribute goes one step further, preventing user calls from binding to the property or method, as well as hiding it from type browsers. For example, the following restricts access to the **\_NewEnum** property of the ILines object:


```C++
[propget, restricted, id(DISPID_NEWENUM)]        // Must be propget.
   HRESULT _NewEnum( [out, retval] IUnknown** retval);
 
```



Restricted properties and methods can be invoked by ActiveX clients, but are not visible to the user who may be using a language such as Visual Basic. In addition, they cannot be bound to by user calls.

## Creating Collection Objects

A collection object contains a group of exposed objects of the same type and can iterate over them. Collection objects do not need an **IClassFactory** implementation, because they are accessed from elements that have their own class factories.

For example, the Lines sample has a collection object named CLines that iterates over a group of Line objects. The following routine creates and initializes the CLines collection object (Lines.cpp):


```C++
STDMETHODIMP
CLines::Create(ULONG lMaxSize, long lLBound, CPane * pPane,
            CLines ** ppLines)
{
   HRESULT hr;
   CLines * pLines = NULL;
   SAFEARRAYBOUND sabound[1];
   if (ppLines == NULL || pPane == NULL)
      return E_INVALIDARG;
   *ppLines = NULL;

   // Create new collection.
   pLines = new CLines();
   if (pLines == NULL)
      goto error;

   pLines->m_cMax = lMaxSize;
   pLines->m_cElements = 0;
   pLines->m_lLBound = lLBound;
   pLines->m_pPane = pPane;

   // Load type information for the Lines collection from type library.
   hr = LoadTypeInfo(&amp;pLines->m_ptinfo, IID_ILines);
   if (FAILED(hr))
      goto error;

   // Create a safe array of variants used to implement the collection.
   sabound[0].cElements = lMaxSize;
   sabound[0].lLbound = lLBound;
   pLines->m_psa = SafeArrayCreate(VT_VARIANT, 1, sabound);
   if (pLines->m_psa == NULL)
   {
      hr = E_OUTOFMEMORY;
      goto error;
   }

   *ppLines = pLines;
   return NOERROR;

error:
   if (pLines == NULL)
      return E_OUTOFMEMORY;
   if (pLines->m_ptinfo)
      pLines->m_ptinfo->Release();
   if (pLines->m_psa)
      SafeArrayDestroy(pLines->m_psa);

   pLines->m_psa = NULL;
   pLines->m_ptinfo = NULL;

   delete pLines;
   return hr;
}
 
```



The parameters to **CLines::Create** specify the maximum number of lines that the collection can contain, the lower bound of the indexes of the collection, and a pointer to a pane, which contains the lines and points in the sample.

## Implementing the IEnumVARIANT Interface for the Lines Application

In the Lines sample, **CEnumVariant** implements the [**Next**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-ienumvariant-next), **Skip**, **Reset**, and [**Clone**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-ienumvariant-clone) member functions (Enumvar.cpp):


```C++
STDMETHODIMP
CEnumVariant::Next(ULONG cElements, VARIANT * pvar,
               ULONG * pcElementFetched)
{
   HRESULT hr;
   ULONG l;
   long l1;
   ULONG l2;

   if (pvar == NULL)
      return E_INVALIDARG;

   if (pcElementFetched != NULL)
      *pcElementFetched = 0;

   // Retrieve the next cElements.
   for (l1=m_lCurrent, l2=0; l1<(long)(m_lLBound+m_cElements) &amp;&amp;
      l2<cElements; l1++, l2++)
   {
      hr = SafeArrayGetElement(m_psa, &amp;l1, &amp;pvar[l2]);
      if (FAILED(hr))
         goto error;
   }
   // Set count of elements retrieved.
   if (pcElementFetched != NULL)
      *pcElementFetched = l2;
   m_lCurrent = l1;

   return (l2 < cElements) ? S_FALSE : NOERROR;
error:
   for (l=0; l<cElements; l++)
      VariantClear(&amp;pvar[l]);
   return hr;
}

STDMETHODIMP
CEnumVariant::Skip(ULONG cElements)
{
   m_lCurrent += cElements; 
   if (m_lCurrent > (long)(m_lLBound+m_cElements))
   {
      m_lCurrent =  m_lLBound+m_cElements;
      return S_FALSE;
   }
   else return NOERROR;
}

STDMETHODIMP
CEnumVariant::Reset()
{
   m_lCurrent = m_lLBound;
   return NOERROR;
}

STDMETHODIMP
CEnumVariant::Clone(IEnumVARIANT ** ppenum)
{
   CEnumVariant * penum = NULL;
   HRESULT hr;
   if (ppenum == NULL) 
      return E_INVALIDARG;

   *ppenum = NULL;
   
   hr = CEnumVariant::Create(m_psa, m_cElements, &amp;penum);
   if (FAILED(hr))
      goto error;
   penum->AddRef();
   penum->m_lCurrent = m_lCurrent;

   *ppenum = penum;
   return NOERROR;
error:
   if (penum)
      penum->Release();
   return hr;
}
 
```



## Implementing the \_NewEnum Property for the Lines Application

The Lines sample contains two collections, Lines and Points, and implements a **\_NewEnum** property for each. Both are restricted properties, available to ActiveX clients, but invisible to users of scripting or macro languages supported by ActiveX clients. The property returns an enumerator ([**IEnumVARIANT**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ienumvariant)) for the items in the collection.

The following code implements the **\_NewEnum** property for the Lines collection (Lines.cpp). The source code for the **RaiseException** function can be found in the Lines sample file Main.cpp.


```C++
STDMETHODIMP
CLines::get__NewEnum(IUnknown ** ppunkEnum)
{
   CEnumVariant * penum = NULL;;
   HRESULT hr;
   if (ppunkEnum == NULL) 
      return E_INVALIDARG;

   *ppunkEnum = NULL;

   // Create a new enumerator for items currently in the collection and 
   // QueryInterface for IUnknown.
   // m_psa is a safe array that holds the collection.
   // m_cElements contains the numer of elements in the collection.
   hr = CEnumVariant::Create(m_psa, m_cElements, &amp;penum);
   if (FAILED(hr))
   {
      hr = RaiseException(IDS_OutOfMemory, IID_ILines); 
      goto error;
   }        
   hr = penum->QueryInterface(IID_IUnknown, (VOID **)ppunkEnum);    
   if (FAILED(hr)) 
   {
      hr = RaiseException(IDS_Unexpected, IID_ILines); 
      goto error;
   }  
   return NOERROR;


error:
   if (penum)
      delete penum;
   return hr;
}
 
```



## Returning Errors

The Lines sample defines an exception handler that fills the EXCEPINFO structure and signals [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) to return DISP\_E\_EXCEPTION (Main.cpp):


```C++
STDMETHODIMP
HRESULT RaiseException (int nID, Refguid rguid)
{
   extern  SCODE g_scodes[];
   TCHAR szError[STR_LEN];
   ICreateErrorInfo *pcerrinfo;
   IErrorInfo *perrinfo;
   HRESULT hr;
   BSTR bstrDescription = NULL;

   if (LoadString(g_pApplication->m_hinst, nID, szError, sizeof(szError)))
      bstrDescription =   SysAllocString(TO_OLE_STRING(szError));

   // Set ErrInfo object so that VTBL binding controllers can get
   // rich error information. If the controller is using IDispatch to 
   // access properties or methods, DispInvoke will fill the EXCEPINFO 
   // structure using the values specified in the ErrorInfo object and 
   // DispInvoke will return DISP_e_EXCEPTION. The property or method 
   // must return a failure return value for DispInvoke to do this.

   hr = CreateErrorInfo(&amp;pcerrinfo);
   if (SUCCEEDED(hr))
   {
      pcerrinfo->SetGUID(rguid);
      pcerrinfo->SetSource(g_pApplication->m_bstrProgID);
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
   return g_scodes[nID-1001];
}
```



Properties and methods in the Lines sample call this routine when an exception occurs. **RaiseException** sets the system's error object, so that controller applications that call through VTBLs can retrieve rich error information. Controllers that call through [**IDispatch::Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke) will be returned with this error information by [**DispInvoke**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-dispinvoke) through the EXCEPINFO structure.

## Passing Exceptions Through VTBLs

The Lines sample also provides rich error information for members invoked through VTBLs. Because VTBL-bound calls bypass the [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface, they cannot return exceptions through **IDispatch**. Instead, they must use the error handling interfaces in Automation. The **RaiseException** function shown in the example calls [**CreateErrorInfo**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-createerrorinfo) to create an error object, then fills the object's data fields with information about the error. When all of the information has been successfully recorded, it calls [**SetErrorInfo**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-seterrorinfo) to associate the error object with the current thread of execution.

ActiveX objects similar to the collection object (CApplication), which use the error interfaces, must also implement the [**ISupportErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-isupporterrorinfo) interface. This interface identifies the object as supporting the error interfaces, and ensures that error information can be propagated correctly up the call chain. The following example shows how the Lines sample implements this interface (Errinfo.cpp):


```C++
STDMETHODIMP
CSupportErrorInfo::CSupportErrorInfo(IUnknown * punkObject,
      REFIID riid)
{
   m_punkObject = punkObject;
   m_iid = riid;
}

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



[**ISupportErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-isupporterrorinfo) has the **QueryInterface**, **AddRef**, and **Release** methods inherited from the **IUnknown** interface, along with the [**InterfaceSupportsErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-isupporterrorinfo-interfacesupportserrorinfo) method. ActiveX clients call **InterfaceSupportsErrorInfo** to check whether the ActiveX object supports the [**IErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ierrorinfo) interface, so they can access the error object. For details, see [Error Handling Interfaces](error-handling-interfaces.md).

## Releasing OLE on Exit

The following code revokes an active Lines object, revokes the Lines class, and then uninitializes OLE (Main.cpp):


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



## Writing an Object Description Script

An object description script is essentially an annotated header file, written in ODL. The following example shows a portion of Lines.odl, the object description script for the Lines sample.


```C++
[
   uuid(3C591B20-1F13-101B-B826-00DD01103DE1),      // LIBID_Lines.
   helpstring("Lines 1.0 Type Library"),

   version(1.0)
]

library Lines
{
   importlib("stdole.tlb");
   #define DISPID_NEWENUM -4
.
.
.
 
```



The preceding entry describes the type library (Lines.tlb) created by the sample. The items in square brackets are attributes, which provide additional information about the library. In the example, the attributes give the library's UUID, a Help string, an LCID, and a version number.

The **importlib** directive is similar to the C or C++ **\#include** directive. It allows access to the type descriptions in the file Stdole.tlb from the Lines library. However, it does not copy those types into the Lines.tlb. To use Lines.tlb, both the Lines.tlb and Stdole.tlb files must be available.

By default, .odl files are preprocessed with the C preprocessor, so the **\#include** and **\#define** directives can be used.

The object description script continues with information on the objects in the type library:


```C++
   [
      uuid(3C591B25-1F13-101B-B826-00DD01103DE1),      // IID_Ipoint.
      helpstring("Point object."),
      oleautomation,
      dual
   ]
   interface IPoint : IDispatch
   {
      [propget, helpstring("Returns and sets x coordinate.")]
      HRESULT x( [out, retval] int* retval);
      [propput, helpstring("Returns and sets x coordinate.")]
      HRESULT x([in] int Value);

      [propget, helpstring("Returns and sets y coordinate.")]
      HRESULT y( [out, retval] int* retval);
      [propput, helpstring("Returns and sets y coordinate.")]
      HRESULT y([in] int Value);
   }
   // .
   // Additional definitions omitted for brevity.
   // .
}
 
```



This entry describes the **IPoint** interface. The interface has the attributes [oleautomation](oleautomation.md) and [dual](dual.md), indicating that the types of all its properties and methods are compatible with Automation, and that it supports binding through both **IDispatch** and VTBLs. The **IPoint** interface has two pairs of property accessor functions, which set and return the **X** and **Y** properties.

The *Value* parameter of both the **X** and **Y** properties has the [in](in.md) attribute. These parameters supply a value and are read-only. Conversely, the *retval* parameter of each property has the [out](out.md) and [retval](retval.md) attributes, indicating that it returns the value of the property.

Because **IPoint** supports VTBL binding and rich error information, its properties return HRESULTs and pass their function return values through *retval* parameters. For more information, see [Type Libraries and the Object Description Language](type-libraries-and-the-object-description-language.md).


```C++
[
      uuid(3C591B21-1F13-101B-B826-00DD01103DE1),      // CLSID_Lines.
      helpstring("Lines Class"),
      appobject
   ]
   coclass Lines
   {
      [default] interface IApplication;
         interface IDispatch;
   }
}
 
```



The file concludes with the description of the Lines Application object, as specified by the [appobject](appobject.md) attribute. The [default](default.md) attribute applies to the **IApplication** interface, indicating that this interface will be returned by default.

 

 




