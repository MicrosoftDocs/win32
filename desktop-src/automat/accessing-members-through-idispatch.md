---
title: Accessing Members Through IDispatch
description: Demonstrates how to access members through IDispatch.
ms.assetid: 'f537070d-0dcc-407f-8620-890c337dc1fa'
---

# Accessing Members Through IDispatch

To bind to exposed objects at run time, use the **IDispatch** interface.

**To create an ActiveX client using IDispatch**

1.  Initialize OLE.

2.  Create an instance of the object you want to access. The object's ActiveX component creates the object.

3.  Obtain a reference to the object's **IDispatch** interface (if it has implemented one).

4.  Manipulate the object through the methods and properties exposed in its [**IDispatch**](idispatch.md) interface.

5.  Terminate the object by invoking the appropriate method in its [**IDispatch**](idispatch.md) interface, or by releasing all references to the object.

6.  Uninitialize OLE.

The following table shows the minimum set of functions necessary to manipulate a remote object through [**IDispatch**](idispatch.md).



| Function                                                    | Purpose                                                                                                                                                              | Interface                                 |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| **OleInitialize**<br/>                                | Initializes OLE.<br/>                                                                                                                                          | OLE API function<br/>               |
| **CoCreateInstance**<br/>                             | Creates an instance of the class **IDispatch::GetTypeInforesented** by the specified CLSID, and returns a pointer to the object's **IUnknown** interface.<br/> | Component object API function<br/>  |
| **QueryInterface**<br/>                               | Checks whether [**IDispatch**](idispatch.md) has been implemented for the object. If so, returns a pointer to the **IDispatch** implementation.<br/>          | **IUnknown**<br/>                   |
| [**GetIDsOfNames**](idispatch-getidsofnames.md)<br/> | Returns dispatch identifiers (DISPIDs) for properties and methods and their parameters.<br/>                                                                   | [**IDispatch**](idispatch.md)<br/> |
| [**Invoke**](idispatch-invoke.md)<br/>               | Invokes a method, or sets or gets a property of the remote object.<br/>                                                                                        | [**IDispatch**](idispatch.md)<br/> |
| **Release**<br/>                                      | Decrements the reference count for an **IUnknown** or [**IDispatch**](idispatch.md) object.<br/>                                                              | **IUnknown**<br/>                   |
| **OleUninitialize**<br/>                              | Uninitializes OLE.<br/>                                                                                                                                        | OLE API function<br/>               |



 

The following code examples are from a generalized Windows-based ActiveX client. The controller relies on helper functions provided in the file Invhelp.cpp, available in the COM Fundamentals Browse sample. The two functions that follow initialize OLE, and then create an instance of an object and get a pointer to the object's [**IDispatch**](idispatch.md) interface (Invhelp.cpp):


```C++
BOOL InitOle(void)
{
    if(OleInitialize(NULL) != 0)
        return FALSE;

    return TRUE;
}
HRESULT CreateObject(LPSTR pszProgID, IDispatch ** ppdisp)
{
    CLSID clsid;                  // CLSID of ActiveX object.
    HRESULT hr;
    LPUNKNOWN punk = NULL;        // IUnknown of ActiveX object.
    LPDISPATCH pdisp = NULL;      // IDispatch of ActiveX object.

   if (ppdisp == NULL) {
      return E_INVALIDARG;
    *ppdisp = NULL;

    // Retrieve CLSID from the ProgID that the user specified.
    hr = CLSIDFromProgID(pszProgID, &amp;clsid);
    if (FAILED(hr))
        goto error;

    // Create an instance of the ActiveX object.
    hr = CoCreateInstance(clsid, NULL, CLSCTX_SERVER, 
                            IID_IUnknown, (void **)&amp;punk);
    if (FAILED(hr))
        goto error;

      // Ask the ActiveX object for the IDispatch interface.
    hr = punk->QueryInterface(IID_IDispatch, (void **)&amp;pdisp);
    if (FAILED(hr))
        goto error;

    *ppdisp = pdisp;
    punk->Release();
    return NOERROR;
    
error:
    if (punk) punk->Release();
    if (pdisp) pdisp->Release();
    return hr;
}
```



The **CreateObject** function is passed a ProgID and returns a pointer to the [**IDispatch**](idispatch.md) implementation of the specified object. **CreateObject** calls the OLE API [**CLSIDFromProgID**](https://msdn.microsoft.com/library/windows/desktop/ms688386) to get the CLSID that corresponds to the requested object, and then passes the CLSID to **CoCreateInstance** to create an instance of the object and get a pointer to the object's **IUnknown** interface. With this pointer, **CreateObject** calls **IUnknown::QueryInterface**, specifying IID\_IDispatch, to get a pointer to the object's **IDispatch** interface.


```C++
HRESULT 
Invoke(LPDISPATCH pdisp,
    WORD wFlags,
    LPVARIANT pvRet,
    EXCEPINFO * pexcepinfo,
    UINT * pnArgErr,
    LPOLESTR pszName,
    LPCTSTR pszFmt,
    ...)
{
    va_list argList;
    va_start(argList, pszFmt);
    DISPID dispid;
    HRESULT hr;
    VARIANTARG* pvarg = NULL;

    if (pdisp == NULL)
        return E_INVALIDARG;

    // Get DISPID of property/method.
    hr = pdisp->GetIDsOfNames(IID_NULL, &amp;pszName, 1,
        LOCALE_USER_DEFAULT, &amp;dispid);
    if(FAILED(hr))
        return hr;

    DISPPARAMS dispparams;
    _fmemset(&amp;dispparams, 0, sizeof dispparams);

    // Determine number of arguments.
    if (pszFmt != NULL)
        // The source code for CountArgsInFormat is available in InvHelp.cpp
        CountArgsInFormat(pszFmt, &amp;dispparams.cArgs);

    // Property puts have a named argument that represents the value
    // being assigned to the property.
    DISPID dispidNamed = DISPID_PROPERTYPUT;
    if (wFlags & DISPATCH_PROPERTYPUT)
    {
        if (dispparams.cArgs == 0)
            return E_INVALIDARG;
        dispparams.cNamedArgs = 1;
        dispparams.rgdispidNamedArgs = &amp;dispidNamed;
    }
    if (dispparams.cArgs != 0)
    {
        // Allocate memory for all VARIANTARG parameters.
        pvarg = new VARIANTARG[dispparams.cArgs];
        if(pvarg == NULL)
            return E_OUTOFMEMORY;
        dispparams.rgvarg = pvarg;
        _fmemset(pvarg, 0, sizeof(VARIANTARG) * dispparams.cArgs);

        // Get ready to traverse the vararg list.
        LPCTSTR psz = pszFmt;
        pvarg += dispparams.cArgs - 1;   // Params go in opposite order.

        while (psz = GetNextVarType(psz, &amp;pvarg->vt))
        {
            if (pvarg < dispparams.rgvarg)
            {
                hr = E_INVALIDARG;
                goto cleanup;  
            }
            switch (pvarg->vt)
            {
            case VT_I2:
                V_I2(pvarg) = va_arg(argList, short);
                break;
            case VT_I4:
                V_I4(pvarg) = va_arg(argList, long);
                break;
            // Additional cases omitted to save space.
            default:
                {
                    hr = E_INVALIDARG;
                    goto cleanup;  
                }
                break;
            } // switch
            --pvarg;             // Get ready to fill next argument.
        } //while
    } //if

    // Initialize return variant, in case caller forgot. Caller can pass
    // Null if no return value is expected.
    if (pvRet)
        VariantInit(pvRet);
    // Make the call.
    hr = pdisp->Invoke(dispid, IID_NULL, LOCALE_USER_DEFAULT, wFlags,
        &amp;dispparams, pvRet, pexcepinfo, pnArgErr);

cleanup:
    // Clean up any arguments that need it.
    if (dispparams.cArgs != 0)
    {
        VARIANTARG * pvarg = dispparams.rgvarg;
        UINT cArgs = dispparams.cArgs;
        while (cArgs--)
        {
            switch (pvarg->vt)
            {
            case VT_BSTR:
                VariantClear(pvarg);
                break;
            }
            ++pvarg;
        }
    }
    delete dispparams.rgvarg;
    va_end(argList);
    return hr;
}
```



In this example, the [**Invoke**](idispatch-invoke.md) function is a general-purpose function that calls [IDispatch::Invoke](964ADE8E-9D8A-4D32-BD47-AA678912A54D) to invoke a property or method of an ActiveX object. As arguments, it accepts the object's [**IDispatch**](idispatch.md) implementation, the name of the member to invoke, flags that control the invocation, and a variable list of the member's arguments. It can be found in the Browse sample in the file Invhelp.cpp.

Using the object's [**IDispatch**](idispatch.md) implementation and the name of the member, it calls [**GetIDsOfNames**](idispatch-getidsofnames.md) to get the DISPID of the requested member. The member's DISPID must be used later, in the call to [**Invoke**](idispatch-invoke.md).

The invocation flags specify whether a method, PROPERTYPUT, or PROPERTYGET function is being invoked. The helper function simply passes these flags directly to [**Invoke**](idispatch-invoke.md).

The helper function next fills in the DISPPARAMS structure with the parameters of the member. DISPPARAMS structures have the following form:


```C++
typedef struct tagDISPPARAMS{
    VARIANTARG * rgvarg;           // Array of arguments.
    DISPID * rgdispidNamedArgs;    // DISPIDs of named arguments.
    UINT cArgs;                       // Number of arguments.
    UINT cNamedArgs;                  // Number of named arguments.
} DISPPARAMS;
```



The **rgvarg** field is a pointer to an array of VARIANTARG structures. Each element of the array specifies an argument, whose position in the array corresponds to its position in the parameter list of the method definition. The **cArgs** field specifies the total number of arguments, and the **cNamedArgs** field specifies the number of named arguments.

For methods and property get functions, all arguments can be accessed as positional, or they can be accessed as named arguments. Property put functions have a named argument that is the new value for the property. The DISPID of this argument is DISPID\_PROPERTYPUT.

To build the **rgvarg** array, the [**Invoke**](idispatch-invoke.md) helper function retrieves the parameter values and types from its own argument list, and constructs a VARIANTARG structure for each one. (For a description of the format string that specifies the types of the parameters, see the file Invhelp.cpp.) Parameters are put in the array in reverse order, so that the last parameter is in **rgvarg**\[0\], and so forth. Although VARIANTARG has the following five fields, only the first and fifth are used.


```C++
typedef VARIANT VARIANTARG;
typedef struct tagVARIANT VARIANT;

struct tagVARIANT
{
    VARTYPE vt;
    WORD wReserved1;
    WORD wReserved2;
    WORD wReserved3;
    union {
        SHORT        iVal;        /* VT_I2        */
.
.    // The rest of this union specifies numerous other types.
.

    };
} ;
```



The first field contains the argument's type, and the fifth contains its value. To pass a long integer, for example, the **vt** and **iVal** fields of the VARIANTARG structure would be filled with VT\_I4 (long integer) and the actual value of the long integer.

In addition, for property put functions, the first element of the **rgdispidNamedArgs** array must contain DISPID\_PROPERTYPUT.

After filling the DISPPARAMS structure, the [**Invoke**](idispatch-invoke.md) helper function initializes pvRet, a variant in which [IDispatch::Invoke](964ADE8E-9D8A-4D32-BD47-AA678912A54D) returns a value from the method or property. The following is the actual call to **Invoke**:


```C++
hr = pdisp->Invoke(dispid, IID_NULL, LOCALE_USER_DEFAULT, wFlags,
        &amp;dispparams, pvRet, pexcepinfo, pnArgErr);
```



The variable pdisp is a pointer to the object's [**IDispatch**](idispatch.md) interface. DISPID indicates the method or property being invoked. The value IID\_NULL must be specified for all [IDispatch::Invoke](964ADE8E-9D8A-4D32-BD47-AA678912A54D) calls, and LOCALE\_USER\_DEFAULT is a constant denoting the default locale identifier (LCID) for the current user. In the final two arguments, pexcepinfo and pnArgErr, [**Invoke**](idispatch-invoke.md) can return error information.

If the invoked member has defined an exception handler, it returns exception information in pexcepinfo. If certain errors occur in the argument vector, pnArgErr points to the errant argument. The function return value hr is an HRESULT that indicates success or various types of failure.

For more information, including how to pass optional arguments, see [IDispatch::Invoke](964ADE8E-9D8A-4D32-BD47-AA678912A54D) and [Dispatch Interface and API Functions](75BFF268-BD85-49C4-B761-B557F4B1C588).

 

 





