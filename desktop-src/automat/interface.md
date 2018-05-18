---
title: interface
description: This statement defines an interface, which is a set of function definitions. An interface can inherit from any base interface.
ms.assetid: '0606fe11-59e3-4ce1-bde1-a34cfbf0b093'
---

# interface

This statement defines an interface, which is a set of function definitions. An interface can inherit from any base interface.

## Syntax

``` syntax
[attributes]
interface interfacename [:baseinterface] {
   functionlist
};
```

<dl> <dt>

<span id="attributes"></span><span id="ATTRIBUTES"></span>*attributes*
</dt> <dd>

The attributes dual, helpstring, helpcontext, hidden, odl, oleautomation, uuid, and version are accepted before interface. If the interface is a member of a coclass, the attributes source, default, and restricted are also accepted.

</dd> <dt>

<span id="interfacename_"></span><span id="INTERFACENAME_"></span>*interfacename* 
</dt> <dd>

The name by which the interface is known in the type library.

</dd> <dt>

<span id="baseinterface"></span><span id="BASEINTERFACE"></span>*baseinterface*
</dt> <dd>

The name of the interface that is the base class for this interface.

</dd> <dt>

<span id="functionlist"></span><span id="FUNCTIONLIST"></span>*functionlist*
</dt> <dd>

The list of function prototypes for each function in the interface. Any number of function definitions can appear in the function list. A function in the function list has the following form:

\[attributes\] *returntype* \[*calling convention*\] *funcname*(*params*);

The following attributes are accepted on a function in an interface: helpstring,helpcontext, string, propget, propput, propputref, bindable, defaultbind, displaybind, and vararg. If vararg is specified, the last parameter must be a safe array of VARIANT type. The optional calling convention can be \_\_pascal/\_pascal/pascal, \_\_cdecl/\_cdecl/cdecl, or \_\_stdcall/\_stdcall/stdcall. The calling convention specification can include up to two leading underscores.

The parameter list is a comma-delimited list, as follows:

\[attributes\] *typeparamname*

The *type* can be any previously declared type, built-in type, a pointer to any type, or a pointer to a built-in type. Attributes on parameters are in, out, optional, and string.

If optional is used, it must be specified only on the right-most parameters, and the types of those parameters must be VARIANT.

</dd> </dl>

## Remarks

Because the functions described by the interface statement are in the VTBL, [**DispInvoke**](dispinvoke.md) and [**CreateStdDispatch**](createstddispatch.md) can be used to provide an implementation of [**IDispatch::Invoke**](idispatch-invoke.md). For this reason, interface is more commonly used than dispinterface to describe the properties and methods of an object.

Functions in interfaces are the same as described in the module statement except that the entry attribute is not allowed.

Members of interfaces that need to raise exceptions should return an HRESULT and specify a retval parameter for the actual return value. The retval parameter is always the last parameter in the list.

## Examples

The following example defines an interface named Hello with two member functions, HelloProc and Shutdown:


```C++
[uuid(BFB73347-822A-1068-8849-00DD011087E8), version(1.0)]
interface hello : IUnknown
{
void HelloProc([in, string] unsigned char * pszString);
void Shutdown(void);
};
```



The next example defines a dual interface named IMyInt, which has a pair of accessor functions for the MyMessage property, and a method that returns a string.


```C++
[dual]
interface IMyInt : IDispatch
{
   // A property that is a string.
   [propget] HRESULT MyMessage([in, lcid] LCID lcid,
                        [out, retval] BSTR *pbstrRetVal);
   [propput] HRESULT MyMessage([in] BSTR rhs, [in, lcid] DWORD lcid);
   
   // A method returning a string.
   HRESULT SayMessage([in] long NumTimes,
                  [in, lcid] DWORD lcid,
                  [out, retval] BSTR *pbstrRetVal);
}
```



The members of this interface return error information and function return values through the HRESULT values and retval parameters, respectively. Tools that access the members can return the HRESULT to their users, or can simply expose the retvalparameter as the return value, and handle the HRESULT transparently.

A dual interface must derive from [**IDispatch**](idispatch.md).

 

 




