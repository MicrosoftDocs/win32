---
title: Passing Parameters
description: Arguments to the method or property being invoked are passed in the DISPPARAMS Data Type structure.
ms.assetid: 'f0b7c325-844b-42c3-9581-ec025111a898'
---

# Passing Parameters

Arguments to the method or property being invoked are passed in the [**DISPPARAMS Data Type**](dispparams.md) structure. This structure consists of a pointer to an array of arguments represented as variants, a pointer to an array of [**DISPID Data Type**](dispid-constants.md) values for named arguments, and the number of arguments in each array.

``` syntax
typedef struct tagDISPPARAMS{
    VARIANTARG *rgvarg;          // Array of arguments.
    DISPID *rgdispidNamedArgs;   // Dispatch IDs of named arguments.
    UINT cArgs;                  // Number of arguments.
    UINT cNamedArgs;             // Number of named arguments.
} DISPPARAMS;
```

The arguments are passed in the array rgvarg\[ \], with the number of arguments passed in cArgs. The arguments in the array should be placed from last to first, so rgvarg\[0\] has the last argument and rgvarg\[cArgs -1\] has the first argument. The method or property may change the values of elements within the array rgvarg, but only if it has set the VT\_BYREF flag. Otherwise, consider the elements as read-only.

A dispatch invocation can have named arguments as well as positional arguments. If cNamedArgs is 0, all the elements of rgvarg\[ \] represent positional arguments. If cNamedArgs is not 0, each element of rgdispidNamedArgs\[ \] contains the DISPID of a named argument, and the value of the argument is in the matching element of rgvarg\[ \]. The DISPIDs of the named arguments are always contiguous in rgdispidNamedArgs, and their values are in the first cNamedArgs elements of rgvarg. Named arguments cannot be accessed positionally, and positional arguments cannot be named.

The DISPID of an argument is its zero-based position in the argument list. For example, the following method takes three arguments.


```C++
BOOL _export CDECL
CCredit::CheckCredit(BSTR bstrCustomerID,  // DISPID = 0.
    BSTR bstrLenderID,                     // DISPID = 1.
    CURRENCY cLoanAmt)                     // DISPID = 2.
{
// Code omitted.
}
```



If you include the DISPID with each named argument, you can pass the named arguments to [**Invoke**](idispatch-invoke.md) in any order. For example, if a method is to be invoked with two positional arguments, followed by three named arguments (A, B, and C), using the following hypothetical syntax, then cArgs would be 5, and cNamedArgs would be 3.


```C++
object.method("arg1", "arg2", A := "argA", B := "argB", C := "argC")
```



The first positional argument would be in rgvarg\[4\]. The second positional argument would be in rgvarg\[3\]. The ordering of named arguments is not important to the [**IDispatch**](idispatch.md) implementation, but these arguments are generally passed in reverse order. The argument A would be in rgvarg\[2\], with the DISPID of A in rgdispidNamedArgs\[2\]. The argument B would be in rgvarg\[1\], with the corresponding DISPID in rgdispidNamedArgs\[1\]. The argument C would be in rgvarg\[0\], with the DISPID corresponding to C in rgdispidNamedArgs\[0\]. The following diagram illustrates the arrays and their contents.

You can also use [**Invoke**](idispatch-invoke.md) on members with optional arguments, but all optional arguments must be of type VARIANT. As with required arguments, the contents of the argument vector depend on whether the arguments are positional or named. The invoked member must ensure that the arguments are valid. **Invoke** merely passes the DISPPARAMS structure it receives.

Omitting named arguments is straightforward. You would pass the arguments in rgvarg and their DISPIDs in rgdispidNamedArgs. To omit the argument named B (in the preceding example) you would set rgvarg\[0\] to the value of C, with its DISPID in rgdispidNamedArgs\[0\]; and rgvarg\[1\] to the value of A, with its DISPID in rgdispidNamedArgs\[1\]. The subsequent positional arguments would occupy elements 2 and 3 of the arrays. In this case, cArgs is 4 and cNamedArgs is 2.

If the arguments are positional (unnamed), you would set cArgs to the total number of possible arguments, cNamedArgs to 0, and pass VT\_ERROR as the type of the omitted arguments, with the status code DISP\_E\_PARAMNOTFOUND as the value. For example, the following code invokes ShowMe (,1).


```C++
VARIANT *pVarResult;
EXCEPINFO *pExcepInfo;
unsigned int *puArgErr;
DISPPARAMS dispparams; 

// Code omitted for brevity.

szMember = "ShowMe";
hresult = pdisp->GetIDsOfNames(IID_NULL, &amp;szMember, 1,
    LOCALE_USER_DEFAULT, &amp;dispid) ;
dispparams.rgvarg[0].vt = VT_I2;
dispparams.rgvarg[0].ival = 1;
dispparams.rgvarg[1].vt = VT_ERROR;
dispparams.rgvarg[1].scode = DISP_E_PARAMNOTFOUND;
dispparams.cArgs = 2;
dispparams.cNamedArgs = 0;

hresult = pdisp->Invoke(
    dispid,
    IID_NULL,
    LOCALE_USER_DEFAULT,
    DISPATCH_METHOD,
    &amp;dispparams, pVarResult, pExcepInfo, puArgErr);
```



The example takes two positional arguments, but omits the first. Therefore, rgvarg\[0\] contains 1, the value of the last argument in the argument list, and rgvarg\[1\] contains VT\_ERROR and the error return value, indicating the omitted first argument.

The calling code is responsible for releasing all strings and objects referred to by rgvarg\[ \] or placed in \*pVarResult. As with other parameters that are passed by value, if the invoked member must maintain access to a string after returning, you should copy the string. Similarly, if the member needs access to a passed-object pointer after returning, it must call the **AddRef** function on the object. A common example occurs when an object property is changed to refer to a new object, using the DISPATCH\_PROPERTYPUTREF flag.

For those implementing [**Invoke**](idispatch-invoke.md), Automation provides the [**DispGetParam**](dispgetparam.md) function to retrieve parameters from the argument vector and coerce them to the proper type.

 

 




