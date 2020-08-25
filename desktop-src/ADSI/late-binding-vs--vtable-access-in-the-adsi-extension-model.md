---
title: Late Binding vs. Vtable Access in the ADSI Extension Model
description: A dual interface enables direct vtable access to all its functions while a dispatch interface does not.
ms.assetid: 6ecc0821-7cf0-4075-81c0-8bebaedab2a4
ms.tgt_platform: multiple
keywords:
- late binding vs. vtable access in the ADSI Extension Model ADSI
- extensions ADSI , late binding vs. vtable access in the ADSI extension model
- ADSI ADSI , example code Visual Basic , using IADsDualInf
ms.topic: article
ms.date: 05/31/2018
---

# Late Binding vs. Vtable Access in the ADSI Extension Model

A dual interface enables direct vtable access to all its functions while a dispatch interface does not. A C/C++ client can query for a dual interface pointer and use direct vtable access to invoke its functions. This provides faster access than invoking the function using the [**IDispatch::GetIDsOfNames**](/windows/win32/api/oaidl/nf-oaidl-idispatch-getidsofnames) and [**IDispatch::Invoke**](/windows/win32/api/oaidl/nf-oaidl-idispatch-invoke) functions. This is especially true in the extension model, because all dual interfaces in an extension object must delegate their **GetIDsOfNames** and **Invoke** functions back to the aggregator (ADSI) first. The aggregator then must perform extra internal steps to identify which extension object, possibly including the aggregator itself, provides support for the function called and redirect the call to the appropriate object.

Visual Basic also invokes a dual-interface function using direct access to a vtable, if it has a pointer to the interface and access to type data from the type library. ADSI clients written in Visual Basic can specify a pointer to a dual interface, for example, [**IADs**](/windows/desktop/api/Iads/nn-iads-iads), explicitly, and thus enable vtable access to functions in the interface.


```VB
Dim inf as IADs
 
Set inf = GetObject("LDAP://CN=jeffsmith,DC=fabrikam,DC=com") ' An object that supports IADsDualInf.
inf.Get("name") 'IADs.Get() will be invoked through direct vtable access.
```



Because an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface does not support vtable access, this example does not apply. That is, a dispatch function is always invoked through the [**IDispatch::GetIDsOfNames**](/windows/win32/api/oaidl/nf-oaidl-idispatch-getidsofnames) and [**IDispatch::Invoke**](/windows/win32/api/oaidl/nf-oaidl-idispatch-invoke) functions only.

Current releases of VBScript and JScript also do not support vtable access. Therefore, a dual interface in a VBScript or JScript environment performs like a dispatch interface.

 

 