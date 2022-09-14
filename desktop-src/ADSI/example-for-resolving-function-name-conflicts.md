---
title: Example for Resolving Function Name Conflicts
description: This topic describes how to resolve function name conflicts when creating an extension for ADSI.
ms.assetid: 8121f037-3845-44ba-a2cd-8d7f15e0beb2
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,example code Visual Basic ,resolving function name conflicts
- resolving function name conflicts ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Example for Resolving Function Name Conflicts

Consider the following:

-   IADs0 does not support Func0.
-   IADs1 supports Func1 and Func0.
-   IADs2 supports Func2 and Func0.

All three interfaces are dual interfaces.


```C++
IADs0 : IDispatch
{
    OtherFunc();
}

IADs1 : IDispatch
{
    Func0() 
    Func1();
}

IADs2 : IDispatch
{
    Func0()
    Func2();
}
```




```VB
Dim myInf1 as IADs1
 
myInf1.Func1  ' IADs1::Func1 is invoked using direct vtable access 
 
myInf1.Func2  ' IADs2::Func2 is invoked using GetIDsOfNames/Invoke
```



Be aware that even though IADs1 does not support Func2, an ADSI client recognizes one [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) that supports all the dual and dispatch interfaces in the model. Thus, the ADSI client can directly call Func2 using myInf1.Func2 without resolving which interface supports Func2.


```VB
myInf1.Func2
```



Both IADs1 and IADs2 have a function called Func0, but IADs1::Func0 is invoked directly using vtable access, because both of following apply to the client:

-   The client has a pointer to dual interface IADs1 object, which has a function called Func0.
-   Visual Basic supports direct vtable access, assuming that type of data is available through the type library.

In the next code example, the client has a dual interface pointer to IADs2 instead of IADs1. Therefore, IADs2::Func0 is invoked using direct vtable access.


```VB
Dim myInf2 as IADs2
Set myInf2 = myInf1 ' Query for pointer to IADs2 
myInf2.Func0
```



Again, in the next code example, both IADs1 and IADs2 have a function called Func0, but, here, the client has a pointer to a dual interface, IADs0, which does not have a function called Func0. Therefore, no direct vtable access can be performed. Instead, [**IDispatch::GetIDsOfNames**](/windows/win32/api/oaidl/nf-oaidl-idispatch-getidsofnames) and [**Invoke**](/windows/win32/api/oaidl/nf-oaidl-idispatch-invoke) are called to invoke Func0.


```VB
Dim myInfNone as IADs0
Set myInfNone = myInf1    ' The aggregated object that 
   ' supports IADs1 and IADs2.
myInfNone.Func0
```



Consider these two cases:

-   IADs1 and IADs2 are implemented by two COM components, Ext1 and Ext2, respectively. If Ext1 comes before Ext2 in the registry, IADs1::Func0 is invoked. However, if Ext2 comes first in the registry, IADs2::Func0 is invoked.
-   If IADs1 and ADs2 are implemented by the same extension object, Func0 is always invoked by the extension's [**IADsExtension::PrivateGetIDsOfNames**](/windows/desktop/api/Iads/nf-iads-iadsextension-privategetidsofnames) and [**PrivateInvoke**](/windows/desktop/api/Iads/nf-iads-iadsextension-privateinvoke) methods.

The extension developer must determine how to resolve conflicts of functions, or properties, of different dual [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interfaces that have the same name in an extension. The implementation of [**IADsExtension::PrivateGetIDsOfNames**](/windows/desktop/api/Iads/nf-iads-iadsextension-privategetidsofnames) and [**PrivateInvoke**](/windows/desktop/api/Iads/nf-iads-iadsextension-privateinvoke) methods should resolve this conflict. For example, if you use IMyInterface1::Func1 and IMyInterface2::Func1, where IMyInterface1 and IMyInterface2 are dual **IDispatch** interfaces supported by the same extension object. The **PrivateGetIDsOfNames** and **PrivateInvoke** methods must determine which Func1 should always be called.

The same applies to conflicting DISPIDs in different dual or [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interfaces.

For example, the DISPID of IMyInterface1::Y is 2 in the file imyinterface1.odl, or imyinterface1.idl. The DISPID of IMyInterface2::X is also 2 in iMyInterface2.odl. [**IADsExtension::PrivateGetIDsOfNames**](/windows/desktop/api/Iads/nf-iads-iadsextension-privategetidsofnames) must return a unique DISPID, within the extension itself, for each, instead of returning the same DISPID for both.

ADSI resolves the first problem by not supporting multiple interfaces with conflicting function or property names. It resolves the second problem by adding a unique, that is within the same extension object, interface number to the unused bits of the DISPID.

 

 