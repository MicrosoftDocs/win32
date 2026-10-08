---
title: QueryInterface Navigating in an Object
description: QueryInterface Navigating in an Object
ms.assetid: 7dec015f-7609-40eb-a71e-f6e9c9b9f8ff
ms.topic: concept-article
ms.date: 01/08/2025
---

# QueryInterface: Navigating in an Object

> [!TIP]
> **Modern QueryInterface patterns — use `IID_PPV_ARGS` and smart pointers.** Raw `QueryInterface` calls are error-prone (mismatched IID and pointer type). Modern C++ code should use type-safe helpers:
>
> ```cpp
> #include <wrl/client.h>  // Microsoft::WRL::ComPtr
>
> Microsoft::WRL::ComPtr<IUnknown> unknown = /* ... */;
> Microsoft::WRL::ComPtr<IPersistFile> persistFile;
>
> // ✅ Best — ComPtr::As() handles QI + type safety + Release automatically
> HRESULT hr = unknown.As(&persistFile);
>
> // ✅ Good — IID_PPV_ARGS macro ensures IID matches the pointer type
> hr = unknown->QueryInterface(IID_PPV_ARGS(&persistFile));
>
> // ❌ Dangerous — IID and pointer type can mismatch silently
> hr = unknown->QueryInterface(IID_IPersistFile, (void**)&persistFile);
> ```
>
> **C++/WinRT equivalent:**
> ```cpp
> #include <winrt/base.h>
>
> winrt::com_ptr<IUnknown> unknown = /* ... */;
> auto persistFile = unknown.as<IPersistFile>();      // throws on failure
> auto maybePF = unknown.try_as<IPersistFile>();      // returns nullptr on failure
> ```
>
> **Key rules:** Never cast interface pointers without `QueryInterface` — COM identity rules require that every interface pointer is obtained via QI or `CoCreateInstance`. Direct casts (`static_cast`, `reinterpret_cast`) produce undefined behavior.

After you have an initial pointer to an interface on an object, COM has a very simple mechanism to find out whether the object supports another specific interface and, if so, to get a pointer to it. (For information about getting an initial pointer to an interface on an object, see [Getting a Pointer to an Object](getting-a-pointer-to-an-object.md).) This mechanism is the [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) method of the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface. If the object supports the requested interface, the method must return a pointer to that interface. This permits an object to navigate freely through the interfaces that an object supports. **QueryInterface** separates the request "Do you support a given contract?" from the high-performance use of that contract once negotiations have been successful.

When a client initially gains access to an object, that client will receive, at a minimum, an [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface pointer (the most fundamental interface) through which it can control the lifetime of the object—by telling the object when it is done using the object—and invoke [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)). The client is programmed to ask each object it manages to perform some operations, but the **IUnknown** interface has no functions for those operations. Instead, those operations are expressed through other interfaces. The client is thus programmed to negotiate with objects for those interfaces. Specifically, the client will call **QueryInterface** to ask an object for an interface through which the client may invoke the desired operations.

Because the object implements [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)), it has the ability to accept or reject the request. If the object accepts the client's request, **QueryInterface** returns a new pointer to the requested interface to the client. Through that interface pointer, the client has access to the methods of that interface. If, on the other hand, the object rejects the client's request, **QueryInterface** returns a null pointer—an error—and the client has no pointer through which to call the desired functions. In this case, the client must deal gracefully with that possibility. For example, suppose a client has a pointer to interface A on an object and asks for interfaces B and C. Suppose also that the object supports interface B but does not support interface C. The result is that the object returns a pointer to B and reports that C is not supported.

A key point is that when an object rejects a call to [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)), it is impossible for the client to ask the object to perform the operations expressed through the requested interface. A client must have an interface pointer to invoke methods in that interface. If the object refuses to provide the requested pointer, the client must be prepared to do without, either by not doing whatever it had intended to do with that object or by attempting to fall back on another, perhaps less powerful, interface. This feature of COM functionality works well in comparison with other object-oriented systems in which you cannot know whether a function will work until you call that function, and even then, handling failure is uncertain. **QueryInterface** provides a reliable and consistent way to know whether an object supports an interface before attempting to call its methods.

The [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) method also provides a robust and reliable way for an object to indicate that it does not support a given contract. That is, if in a call to **QueryInterface** one asks an "old" object whether it supports a "new" interface (one, for example, that was invented after the old object had been shipped), the old object will reliably, without causing a crash, answer "no." The technology that supports this is the algorithm by which IIDs are allocated. While this may seem like a small point, it is extremely important to the overall architecture of the system, and the ability to inquire of legacy elements about new functionality is, surprisingly, a feature not present in most other object architectures.

## Related topics

<dl> <dt>

[Using and Implementing IUnknown](using-and-implementing-iunknown.md)
</dt> </dl>

 

 




