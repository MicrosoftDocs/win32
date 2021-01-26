---
description: Programming DirectX with COM.
title: Programming DirectX with COM
ms.topic: article
ms.date: 01/29/2019
---

# Programming DirectX with COM

The Microsoft Component Object Model (COM) is an object-oriented programming model used by several technologies, including the bulk of the DirectX API surface. For that reason, you (as a DirectX developer) inevitably use COM when you program DirectX.

> [!NOTE]
> The topic [Consume COM components with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/consume-com) shows how to consume DirectX APIs (and any COM API, for that matter) by using [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/). That's by far the most convenient and recommended technology to use.

Alternatively, you can use raw COM, and that's what this topic is about. You'll need a basic understanding of the principles and programming techniques involved in consuming COM APIs. Although COM has a reputation for being difficult and complex, the COM programming required by most DirectX applications is straightforward. In part, this is because you'll be consuming the COM objects provided by DirectX. There's no need for you to author your own COM objects, which is typically where the complexity arises.

## COM component overview

A COM object is essentially an encapsulated component of functionality that can be used by applications to perform one or more tasks. For deployment, one or more COM components are packaged into a binary called a COM server; more often than not a DLL.

A traditional DLL exports free functions. A COM server can do the same. But the COM components inside the COM server expose COM interfaces and member methods belonging to those interfaces. Your application creates instances of COM components, retrieves interfaces from them, and calls methods on those interfaces in order to benefit from the features implemented in the COM components.

In practice, this feels similar to calling methods on a regular C++ object. But there are some differences.

- A COM object enforces stricter encapsulation than a C++ object does. You can't just create the object, and then call any public method. Instead, a COM component's public methods are grouped into one or more COM interfaces. To call a method, you create the object and retrieve from the object the interface that implements the method. An interface typically implements a related set of methods that provide access to a particular feature of the object. For example, the [**ID3D12Device**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device) interface represents a virtual graphics adapter, and it contains methods that enable you create resources, for example, and many other adapter-related tasks.
- A COM object is not created in the same way as a C++ object. There are several ways to create a COM object, but all involve COM-specific techniques. The DirectX API includes a variety of helper functions and methods that simplify creating most of the DirectX COM objects.
- You must use COM-specific techniques to control the lifetime of a COM object.
- The COM server (typically a DLL) doesn't need to be explicitly loaded. Nor do you link to a static library in order to use a COM component. Each COM component has a unique registered identifier (a globally-unique identifier, or GUID), which your application uses to identify the COM object. Your application identifies the component, and the COM runtime automatically loads the correct COM server DLL.
- COM is a binary specification. COM objects can be written in and accessed from a variety of languages. You don't need to know anything about the object's source code. For example, Visual Basic applications routinely use COM objects that were written in C++.

## Component, object, and interface

It's important to understand the distinction between components, objects, and interfaces. In casual usage, you may hear a component or object referred to by the name of its principal interface. But the terms are not interchangeable. A component can implement any number of interfaces; and an object is an instance of a component. For example, while all components must implement the [**IUnknown interface**](/windows/desktop/api/unknwn/nn-unknwn-iunknown), they normally implement at least one additional interface, and they might implement many.

To use a particular interface method, you must not only instantiate an object, you must also obtain the correct interface from it.

In addition, more than one component might implement the same interface. An interface is a group of methods that perform a logically-related set of operations. The interface definition specifies only the syntax of the methods and their general functionality. Any COM component that needs to support a particular set of operations can do so by implementing a suitable interface. Some interfaces are highly specialized, and are implemented only by a single component; others are useful in a variety of circumstances, and are implemented by many components.

If a component implements an interface, it must support every method in the interface definition. In other words, you must be able to call any method and be confident that it exists. However, the details of how a particular method is implemented may vary from one component to another. For example, different components may use different algorithms to arrive at the final result. There is also no guarantee that a method will be supported in a nontrivial way. Sometimes, a component implements a commonly-used interface, but it needs to support only a subset of the methods. You will still be able to call the remaining methods successfully, but they will return an [**HRESULT**](#hresult-values) (which is a standard COM type representing a result code) containing the value **E_NOTIMPL**. You should refer to its documentation to see how an interface is implemented by any particular component.

The COM standard requires that an interface definition must not change once it has been published. The author cannot, for example, add a new method to an existing interface. The author must instead create a new interface. While there are no restrictions on what methods must be in that interface, a common practice is to have the next-generation interface include all the of the old interface's methods, plus any new methods.

It's not unusual for an interface to have several generations. Typically, all generations perform essentially the same overall task, but they're different in specifics. Often, a COM component implements every current and prior generation of a given interface's lineage. Doing so allows older applications to continue using the object's older interfaces, while newer applications can take advantage of the features of the newer interfaces. Typically, a descent group of interfaces all have the same name, plus an integer that indicates the generation. For example, if the original interface were named **IMyInterface** (implying generation 1), then the next two generations would be called **IMyInterface2** and **IMyInterface3**. In the case of DirectX interfaces, successive generations are typically named for the version number of DirectX.

## GUIDs

GUIDs are a key part of the COM programming model. At its most basic, a GUID is a 128-bit structure. However, GUIDs are created in such a way as to guarantee that no two GUIDs are the same. COM uses GUIDs extensively for two primary purposes.

- To uniquely identify a particular COM component. A GUID that is assigned to identify a COM component is called a class identifier (CLSID), and you use a CLSID when you want to create an instance of the associated COM component.
- To uniquely identify a particular COM interface. A GUID that is assigned to identify a COM interface is called an interface identifier (IID), and you use an IID when you request a particular interface from an instance of a component (an object). An interface's IID will be the same, regardless of which component implements the interface.

For convenience, the DirectX documentation normally refers to components and interfaces by their descriptive names (for example, **ID3D12Device**) rather than by their GUIDs. Within the context of the DirectX documentation, there is no ambiguity. It's technically possible for a third-party to author an interface with the descriptive name **ID3D12Device** (it would need to have a different IID in order to be valid). In the interest of clarity, though, we don't recommend that.

So, the only unambiguous way to refer to a particular object or interface is by its GUID.

Although a GUID is a structure, a GUID is often expressed in equivalent string form. The general format of the string form of a GUID is 32 hexadecimal digits, in the format 8-4-4-4-12. That is, {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}, where each x corresponds to a hexadecimal digit. For example, the string form of the IID for the **ID3D12Device** interface is {189819F1-1DB6-4B57-BE54-1821339B85F7}.

Because the actual GUID is somewhat clumsy to use and easy to mistype, an equivalent name is usually provided as well. In your code, you can use this name instead of the actual structure when you call functions, for example when you pass an argument for the `riid` parameter to [**D3D12CreateDevice**](/windows/desktop/api/d3d12/nf-d3d12-d3d12createdevice). The customary naming convention is to prepend either IID_ or CLSID_ to the descriptive name of the interface or object, respectively. For example, the name of the **ID3D12Device** interface's IID is IID_ID3D12Device.

> [!NOTE]
> DirectX applications should link with ``dxguid.lib`` and ``uuid.lib`` to provide definitions for the various interface and class GUIDs. Visual C++ and other compilers support the **__uuidof** operator language extension, but explicit C-style linkage with these link libraries is also supported and fully portable.

## HRESULT values

Most COM methods return a 32-bit integer called an **HRESULT**. With most methods, the HRESULT is essentially a structure that contains two primary pieces of information.
- Whether the method succeeded or failed.
- More detailed information about the outcome of the operation performed by the method.

Some methods return a **HRESULT** value from the standard set defined in `Winerror.h`. However, a method is free to return a custom **HRESULT** value with more specialized information. These values are normally documented on the method's reference page.

The list of **HRESULT** values that you find on a method's reference page is often only a subset of the possible values that may be returned. The list typically covers only those values that are specific to the method, as well as those standard values that have some method-specific meaning. You should assume that a method may return a variety of standard **HRESULT** values, even if they're not explicitly documented.

While **HRESULT** values are often used to return error information, you should not think of them as error codes. The fact that the bit that indicates success or failure is stored separately from the bits that contain the detailed information allows **HRESULT** values to have any number of success and failure codes. By convention, the names of success codes are prefixed by S_ and failure codes by E_. For example, the two most commonly used codes are S_OK and E_FAIL, which indicate simple success or failure, respectively.

The fact that COM methods may return a variety of success or failure codes means that you have to be careful how you test the **HRESULT** value. For example, consider a hypothetical method with documented return values of S_OK if successful and E_FAIL if not. However, remember that the method may also return other failure or success codes. The following code fragment illustrates the danger of using a simple test, where `hr` contains the **HRESULT** value returned by the method.

```cpp
if (hr == E_FAIL)
{
    // Handle the failure case.
}
else
{
    // Handle the success case.
}  
```

As long as, in the failure case, this method only ever return E_FAIL (and not some other failure code), then this test works. However, it's more realistic that a given method is implemented to return a set of specific failure codes, perhaps E_NOTIMPL or E_INVALIDARG. With the code above, those values would be incorrectly interpreted as a success.

If you need detailed information about the outcome of the method call, you need to test each relevant **HRESULT** value. However, you may be interested only in whether the method succeeded or failed. A robust way to test whether an **HRESULT** value indicates success or failure is to pass the value to the one of the following macros, defined in Winerror.h.

- The `SUCCEEDED` macro returns TRUE for a success code, and FALSE for a failure code.
- The `FAILED` macro returns TRUE for a failure code, and FALSE for a success code.

So, you can fix the preceding code fragment by using the `FAILED` macro, as shown in the following code.

```cpp
if (FAILED(hr))
{
    // Handle the failure case.
}
else
{
    // Handle the success case.
}  
```

This corrected code fragment properly treats E_NOTIMPL and E_INVALIDARG as failures.

Although most COM methods return structured **HRESULT** values, a small number use the **HRESULT** to return a simple integer. Implicitly, these methods are always successful. If you pass an **HRESULT** of this sort to the SUCCEEDED macro, then the macro always returns TRUE. An example of a commonly-called method that doesn't return an **HRESULT** is the **IUnknown::Release** method, which returns a ULONG. This method decrements an object's reference count by one and returns the current reference count. See [Managing a COM object's lifetime](#managing-a-com-objects-lifetime) for a discussion of reference counting.

## The address of a pointer

If you view a few COM method reference pages, you'll probably run across something like the following.

```cpp
HRESULT D3D12CreateDevice(
  IUnknown          *pAdapter,
  D3D_FEATURE_LEVEL MinimumFeatureLevel,
  REFIID            riid,
  void              **ppDevice
);
```

While a normal pointer is quite familiar to any C/C++ developer, COM often uses an additional level of indirection. This second level of indirection is indicated by two asterisks, `**`, following the type declaration, and the variable name typically has a prefix of `pp`. For the function above, the `ppDevice` parameter is typically referred to as the address of a pointer to a void. In practice, in this example, `ppDevice` is the address of a pointer to an **ID3D12Device** interface.

Unlike a C++ object, you don't access a COM object's methods directly. Instead, you must obtain a pointer to an interface that exposes the method. To invoke the method, you use essentially the same syntax as you would to invoke a pointer to a C++ method. For example, to invoke the **IMyInterface::DoSomething** method, you would use the following syntax.

```cpp
IMyInterface * pMyIface = nullptr;
...
pMyIface->DoSomething(...);
```

The need for a second level of indirection comes from the fact that you don't create interface pointers directly. You must call one of a variety of methods, such as the **D3D12CreateDevice** method shown above. To use such a method to obtain an interface pointer, you declare a variable as a pointer to the desired interface, and then you pass the address of that variable to the method. In other words, you pass the address of a pointer to the method. When the method returns, the variable points to the requested interface, and you can use that pointer to call any of the interface's methods.

```cpp
IDXGIAdapter * pIDXGIAdapter = nullptr;
...
ID3D12Device * pD3D12Device = nullptr;
HRESULT hr = ::D3D12CreateDevice(
    pIDXGIAdapter,
    D3D_FEATURE_LEVEL_11_0,
    IID_ID3D12Device,
    &pD3D12Device);
if (FAILED(hr)) return E_FAIL;

// Now use pD3D12Device in the form pD3D12Device->MethodName(...);
```

## Creating a COM object

There are several ways to create a COM object. These are the two most commonly used in DirectX programming.

- Indirectly, by calling a DirectX method or function that creates the object for you. The method creates the object, and returns an interface on the object. When you create an object this way, sometimes you can specify which interface should be returned, other times the interface is implied. The code example above shows how to indirectly create a Direct3D 12 device COM object.
- Directly, by passing the object's CLSID to the [**CoCreateInstance function**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance). The function creates an instance of the object, and it returns a pointer to an interface that you specify.

One time, before you create any COM objects, you must initialize COM by calling the [**CoInitializeEx function**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex). If you're creating objects indirectly, then the object creation method handles this task. But, if you need to create an object with **CoCreateInstance**, then you must call **CoInitializeEx** explicitly. When you're finished, COM must be uninitialized by calling [**CoUninitialize**](/windows/desktop/api/combaseapi/nf-combaseapi-couninitialize). If you make a call to **CoInitializeEx** then you must match it with a call to **CoUninitialize**. Typically, applications that need to explicitly initialize COM do so in their startup routine, and they uninitialize COM in their cleanup routine.

To create a new instance of a COM object with **CoCreateInstance**, you must have the object's CLSID. If this CLSID is publicly available, you will find it in the reference documentation or the appropriate header file. If the CLSID is not publicly available, then you can't create the object directly.

The **CoCreateInstance** function has five parameters. For the COM objects you will be using with DirectX, you can normally set the parameters as follows.

*rclsid*
Set this to the CLSID of the object that you want to create.

*pUnkOuter*
Set to `nullptr`. This parameter is used only if you are aggregating objects. A discussion of COM aggregation is outside the scope of this topic.

*dwClsContext*
Set to CLSCTX_INPROC_SERVER. This setting indicates that the object is implemented as a DLL and runs as part of your application's process.

*riid*
Set to the IID of the interface that you would like to have returned. The function will create the object and return the requested interface pointer in the ppv parameter.

*ppv*
Set this to the address of a pointer that will be set to the interface specified by `riid` when the function returns. This variable should be declared as a pointer to the requested interface, and the reference to the pointer in the parameter list should be cast as (LPVOID *).

Creating an object indirectly is usually much simpler, as we saw in the code example above. You pass the object creation method the address of an interface pointer, and the method then creates the object and returns an interface pointer. When you create an object indirectly, even if you can't choose which interface the method returns, often you can still specify a variety of things about how the object should be created.

For example, you can pass to **D3D12CreateDevice** a value specifying the minimum D3D feature level that the returned device should support, as shown in the code example above.

## Using COM interfaces

When you create a COM object, the creation method returns an interface pointer. You can then use that pointer to access any of the interface's methods. The syntax is identical to that used with a pointer to a C++ method.

## Requesting Additional Interfaces

In many cases, the interface pointer that you receive from the creation method may be the only one that you need. In fact, it's relatively common for an object to export only one interface other than **IUnknown**. However, many objects export multiple interfaces, and you may need pointers to several of them. If you need more interfaces than the one returned by the creation method, there's no need to create a new object. Instead, request another interface pointer by using the object's [**IUnknown::QueryInterface method**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(refiid_void)).

If you create your object with **CoCreateInstance**, then you can request an **IUnknown** interface pointer and then call **IUnknown::QueryInterface** to request every interface you need. However, this approach is inconvenient if you need only a single interface, and it doesn't work at all if you use an object creation method that doesn't allow you to specify which interface pointer should be returned. In practice, you usually don't need to obtain an explicit **IUnknown** pointer, because all COM interfaces extend the **IUnknown** interface.

Extending an interface is conceptually similar to inheriting from a C++ class. The child interface exposes all of the parent interface's methods, plus one or more of its own. In fact, you will often see "inherits from" used instead of "extends". What you need to remember is that the inheritance is internal to the object. Your application can't inherit from or extend an object's interface. However, you can use the child interface to call any of the methods of the child or parent.

Because all interfaces are children of **IUnknown**, you can call **QueryInterface** on any of the interface pointers that you already have for the object. When you do so, you must provide the IID of the interface that you're requesting and the address of a pointer that will contain the interface pointer when the method returns.

For example, the following code fragment calls **IDXGIFactory2::CreateSwapChainForHwnd** to create a primary swap chain object. This object exposes several interfaces. The **CreateSwapChainForHwnd** method returns an **IDXGISwapChain1** interface. The subsequent code then uses the **IDXGISwapChain1** interface to call **QueryInterface** to request an **IDXGISwapChain3** interface.

```cpp
HRESULT hr = S_OK;

IDXGISwapChain1 * pDXGISwapChain1 = nullptr;
hr = pIDXGIFactory->CreateSwapChainForHwnd(
    pCommandQueue, // For D3D12, this is a pointer to a direct command queue.
    hWnd,
    &swapChainDesc,
    nullptr,
    nullptr,
    &pDXGISwapChain1));
if (FAILED(hr)) return hr;

IDXGISwapChain3 * pDXGISwapChain3 = nullptr;
hr = pDXGISwapChain1->QueryInterface(IID_IDXGISwapChain3, (LPVOID*)&pDXGISwapChain3);
if (FAILED(hr)) return hr;
```

> [!NOTE]
> In C++ you can make use of the ``IID_PPV_ARGS`` macro rather than the explicit IID and cast pointer: ``pDXGISwapChain1->QueryInterface(IID_PPV_ARGS(&pDXGISwapChain3));``.
> This is often used for creation methods as well as **QueryInterface**. See [combaseapi.h](/windows/win32/api/combaseapi/nf-combaseapi-iid_ppv_args) for more information.

## Managing a COM object's lifetime

When an object is created, the system allocates the necessary memory resources. When an object is no longer needed, it should be destroyed. The system can use that memory for other purposes. With C++ objects, you can control the object's lifetime directly with the `new` and `delete` operators in cases where you're operating at that level, or just by using the stack and scope lifetime. COM doesn't enable you to directly create or destroy objects. The reason for this design is that the same object may be used by more than one part of your application or, in some cases, by more than one application. If one of those references were to destroy the object, then the other references would become invalid. Instead, COM uses a system of reference counting to control an object's lifetime.

An object's reference count is the number of times one of its interfaces has been requested. Each time that an interface is requested, the reference count is incremented. An application releases an interface when that interface is no longer needed, decrementing the reference count. As long as the reference count is greater than zero, the object remains in memory. When the reference count reaches zero, the object destroys itself. You don't need to know anything about the reference count of an object. As long as you obtain and release an object's interfaces properly, the object will have the appropriate lifetime.

Properly handling reference counting is a crucial part of COM programming. Failure to do so can easily create a memory leak or a crash. One of the most common mistakes that COM programmers make is failing to release an interface. When this happens, the reference count never reaches zero, and the object remains in memory indefinitely.

> [!NOTE]
> Direct3D 10 or later has slightly modified lifetime rules for objects. In particular, objects that are derived from **ID3DxxDeviceChild** never outlive their parent device (that is, if the owning **ID3DxxDevice** hits a 0 refcount, then all child objects are immediately invalid as well). Also, when you use **Set** methods to bind objects to the render pipeline, these references don't increase the reference count (that is, they are weak references). In practice, this is best handled by ensuring that you release all device child objects fully before you release the device.

## Incrementing and decrementing the reference count

Whenever you obtain a new interface pointer, the reference count must be incremented by a call to [**IUnknown::AddRef**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-addref). However, your application doesn't usually need to call this method. If you obtain an interface pointer by calling an object creation method, or by calling **IUnknown::QueryInterface**, then the object automatically increments the reference count. However, if you create an interface pointer in some other way, such as copying an existing pointer, then you must explicitly call **IUnknown::AddRef**. Otherwise, when you release the original interface pointer, the object may be destroyed even though you may still need to use the copy of the pointer.

You must release all interface pointers, regardless of whether you or the object incremented the reference count. When you no longer need an interface pointer, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) to decrement the reference count. A common practice is to initialize all interface pointers to `nullptr`, and then to set them back to `nullptr` when they are released. That convention allows you to test all interface pointers in your cleanup code. Those that are not `nullptr` are still active, and you need to release them before you terminate the application.

The following code fragment extends the sample shown earlier to illustrate how to handle reference counting.

```cpp
HRESULT hr = S_OK;

IDXGISwapChain1 * pDXGISwapChain1 = nullptr;
hr = pIDXGIFactory->CreateSwapChainForHwnd(
    pCommandQueue, // For D3D12, this is a pointer to a direct command queue.
    hWnd,
    &swapChainDesc,
    nullptr,
    nullptr,
    &pDXGISwapChain1));
if (FAILED(hr)) return hr;

IDXGISwapChain3 * pDXGISwapChain3 = nullptr;
hr = pDXGISwapChain1->QueryInterface(IID_IDXGISwapChain3, (LPVOID*)&pDXGISwapChain3);
if (FAILED(hr)) return hr;

IDXGISwapChain3 * pDXGISwapChain3Copy = nullptr;

// Make a copy of the IDXGISwapChain3 interface pointer.
// Call AddRef to increment the reference count and to ensure that
// the object is not destroyed prematurely.
pDXGISwapChain3Copy = pDXGISwapChain3;
pDXGISwapChain3Copy->AddRef();
...
// Cleanup code. Check to see whether the pointers are still active.
// If they are, then call Release to release the interface.
if (pDXGISwapChain1 != nullptr)
{
    pDXGISwapChain1->Release();
    pDXGISwapChain1 = nullptr;
}
if (pDXGISwapChain3 != nullptr)
{
    pDXGISwapChain3->Release();
    pDXGISwapChain3 = nullptr;
}
if (pDXGISwapChain3Copy != nullptr)
{
    pDXGISwapChain3Copy->Release();
    pDXGISwapChain3Copy = nullptr;
}
```

## COM Smart Pointers

The code so far has explicitly called ``Release`` and ``AddRef`` to maintain the reference counts using **IUnknown** methods. This pattern requires the programmer to be diligent in remembering to properly maintain the count in all possible codepaths. This can result in complicated error-handling, and with C++ exception handling enabled can be particularly difficult to implement. A better solution with C++ is to make use of a [smart pointer](/cpp/cpp/smart-pointers-modern-cpp).

* **winrt::com_ptr** is a smart pointer provided by the [C++/WinRT language projections](/uwp/cpp-ref-for-winrt/com-ptr). This is the recommended COM smart pointer to use for UWP apps. Note that C++/WinRT requires C++17.

* **Microsoft::WRL::ComPtr** is a smart pointer provided by the [Windows Runtime C++ Template Library (WRL)](/cpp/cppcx/wrl/comptr-class). This library is "pure" C++ so it can be utilized for Windows Runtime applications (via C++/CX or C++/WinRT) as well as classic Win32 desktop applications. This smart pointer also works on older versions of Windows that do not support the Windows Runtime APIs. For Win32 desktop applications, you can use ``#include <wrl/client.h>`` to only include this class and optionally define the preprocessor symbol ``__WRL_CLASSIC_COM_STRICT__`` as well. For more information, see [COM smart pointers revisited](/archive/msdn-magazine/2015/february/windows-with-c-com-smart-pointers-revisited).

* **CComPtr** is a smart pointer provided by the [Active Template Library (ATL)](/cpp/atl/reference/ccomptr-class). The **Microsoft::WRL::ComPtr** is a newer version of this implementation that addresses a number of subtle usage issues, so use of this smart pointer is not recommended for new projects. For more information, see [How to create and use CComPtr and CComQIPtr](/cpp/cpp/how-to-create-and-use-ccomptr-and-ccomqiptr-instances).


## Using ATL with DirectX 9

To use the Active Template Library (ATL) with DirectX 9, you must redefine the interfaces for ATL compatibility. This allows you to properly use the **CComQIPtr** class to obtain a pointer to an interface.

You'll know if you don't redefine the interfaces for ATL, because you'll see the following error message.

```
[...]\atlmfc\include\atlbase.h(4704) :   error C2787: 'IDirectXFileData' : no GUID has been associated with this object
```

The following code sample shows how to define the IDirectXFileData interface.

```cpp
// Explicit declaration
struct __declspec(uuid("{3D82AB44-62DA-11CF-AB39-0020AF71E433}")) IDirectXFileData;

// Macro method
#define RT_IID(iid_, name_) struct __declspec(uuid(iid_)) name_
RT_IID("{1DD9E8DA-1C77-4D40-B0CF-98FEFDFF9512}", IDirectXFileData);
```

After redefining the interface, you must use the **Attach** method to attach the interface to the interface pointer returned by **::Direct3DCreate9**. If you don't, then the **IDirect3D9** interface won't be properly released by the smart pointer class.

The **CComPtr** class internally calls **IUnknown::AddRef** on the interface pointer when the object is created and when an interface is assigned to the **CComPtr** class. To avoid leaking the interface pointer, don't call **IUnknown::AddRef on the interface returned from **::Direct3DCreate9**.

The following code properly releases the interface without calling **IUnknown::AddRef**.

```cpp
CComPtr<IDirect3D9> d3d;
d3d.Attach(::Direct3DCreate9(D3D_SDK_VERSION));
```

Use the previous code. Don't use the following code, which calls **IUnknown::AddRef** followed by **IUnknown::Release**, and doesn't release the reference added by **::Direct3DCreate9**.

```cpp
CComPtr<IDirect3D9> d3d = ::Direct3DCreate9(D3D_SDK_VERSION);
```

Note that this is the only place in Direct3D 9 where you'll have to use the **Attach** method in this manner.

For more information about the **CComPTR** and **CComQIPtr** classes, see their definitions in the `Atlbase.h` header file.
