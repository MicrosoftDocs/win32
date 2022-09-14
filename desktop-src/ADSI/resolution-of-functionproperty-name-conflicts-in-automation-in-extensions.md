---
title: Resolution of Function/Property Name Conflicts in Automation in Extensions
description: In this topic, \ 0034;object \ 0034; indicates the object, as a whole, as an ADSI client views it. That is, ADSI and all its extensions.
ms.assetid: 76207326-879e-408b-8004-06d940401a41
ms.tgt_platform: multiple
keywords:
- Resolution of Function and Property Name Conflicts in Automation in Extensions
- extensions ADSI , resolving function and property name conflicts in Automation
ms.topic: article
ms.date: 05/31/2018
---

# Resolution of Function/Property Name Conflicts in Automation in Extensions

In this topic, "object" indicates the object, as a whole, as an ADSI client views it. That is, ADSI and all its extensions.

## Same Function Name With the Same Parameters

If two or more dual [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interfaces in an object support a property or method of the same name, for example, **Func1**, invocation is determined using the following criteria. If the client has a pointer to one of the dual interfaces that support a method called **Func1** and if the Automation environment supports vtable access, **Func1** is invoked directly through ADSI vtable access.

If either of the conditions above is false, [**IDispatch::GetIDsOfNames**](/windows/win32/api/oaidl/nf-oaidl-idispatch-getidsofnames) and [**IDispatch::Invoke**](/windows/win32/api/oaidl/nf-oaidl-idispatch-invoke) are called to invoke **Func1**.

For more information and a brief explanation about how a client can add a pointer to a dual interface, and a description of the types of environments that support vtable access, see [Late Binding versus Vtable Access in the ADSI Extension Model](late-binding-vs--vtable-access-in-the-adsi-extension-model.md).

Because all extension objects redirect the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) functions back to the aggregator, the aggregator controls which **Func1** is invoked. The rules are:

-   If any interface, and there will be only one, if any, in the aggregator (ADSI) supports a function called **Func1**, the aggregator invokes its own **Func1**.
-   Otherwise, the aggregator goes through each of its extensions, in the order listed in the registry, and finds the first extension that implements a function called **Func1**. It is possible, but unlikely, that multiple dual [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interfaces in this first extension have a function called **Func1**. The extension must determine which **Func1** should always be invoked in Automation.

## Same Function Name With Different Parameters

The previous section discussed how to resolve function name conflicts, that is, function names that have the same function name and same parameter list, such as number, type and order, when it occurs in Automation. What if two functions have the same name but different parameters? If an ADSI client invokes the function using [**IDispatch::GetIDsOfNames**](/windows/win32/api/oaidl/nf-oaidl-idispatch-getidsofnames) without using multiple names to specify the parameters, the ADSI extension model cannot disambiguate the functions. Based on the resolution scheme discussed in above, the first extension in the registry that supports this function through one of its interfaces has its version of this function invoked, and the call may fail or yield incorrect results.

For example:

-   Extn1 (first in the registry under class CA – higher priority) supports **IInterface1**.
-   Extn2 (third in the registry under class CA – lower priority) supports **IInterface2**.
-   **IInterface1** supports **Method1(int param1, int param2)**.
-   **IInterface2** supports **Method1(int param1)**.

An ADSI client has an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface pointer to an object of class CA. It wants to invoke **IInterface2::Method1**. If the client calls "pDispatch->GetIDsOfNames(IID\_NULL, rgszNames, 1, MY\_LCID, rgDispId)" by just storing the function name "Method1" in *rgszNames\[0\]*, then **IInterface1::Method1** instead of the desired **IInterface2::Method1** is invoked, and the function fails because the number of parameters are different.

To minimize this problem, extension developers can prefix their function names with their own specific identifiers and avoid interface designs that use functions of the same name, but different parameters.

If a name conflict does occur, ADSI clients can avoid the problem by direct vtable access if the interface is a dual interface. If direct vtable access is not possible, ADSI clients should call [**IDispatch::GetIDsOfNames**](/windows/win32/api/oaidl/nf-oaidl-idispatch-getidsofnames) with multiple names, specifying the function names as well as the parameters in the array *rgszNames* described previously.

Visual Basic 5 does not call the [**IDispatch::GetIDsOfNames**](/windows/win32/api/oaidl/nf-oaidl-idispatch-getidsofnames) function with multiple names. That is, it passes only the function name to **GetIDsOfNames**, but not arguments. However, Visual Basic 5 allows users to invoke a function by direct vtable access, instead of invoking the **IDispatch::GetIDsOfNames** function if the interface is a dual interface. Developers should use direct vtable access, if possible.

For more information about name conflict resolution, see [Example for Resolving Function Name Conflicts](example-for-resolving-function-name-conflicts.md).

 

 