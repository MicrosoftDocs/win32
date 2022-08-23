---
title: In-Process Server Threading Issues
description: In-Process Server Threading Issues
ms.assetid: 7bd6f62f-8c91-44bd-9a7f-d47988180eed
ms.topic: article
ms.date: 05/31/2018
---

# In-Process Server Threading Issues

An in-process server does not call [**CoInitialize**](/windows/desktop/api/Objbase/nf-objbase-coinitialize), [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex), or [**OleInitialize**](/windows/desktop/api/Ole2/nf-ole2-oleinitialize) to mark its threading model. For thread-aware DLL-based or in-process objects, you need to set the threading model in the registry. The default model when you do not specify a threading model is single-thread-per-process. To specify a model, you add the **ThreadingModel** value to the [InprocServer32](inprocserver32.md) key in the registry.

DLLs that support instantiation of a class object must implement and export the functions [**DllGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-dllgetclassobject) and [**DllCanUnloadNow**](/windows/desktop/api/combaseapi/nf-combaseapi-dllcanunloadnow). When a client wants an instance of the class the DLL supports, a call to [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject) (either directly or through a call to [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance)) calls **DllGetClassObject** to get a pointer to its class object when the object is implemented in a DLL. **DllGetClassObject** should therefore be able to give away multiple class objects or a single thread-safe object (essentially just using [**InterlockedIncrement**](/windows/win32/api/winnt/nf-winnt-interlockedincrement)/[**InterlockedDecrement**](/windows/win32/api/winnt/nf-winnt-interlockeddecrement) on their internal reference counts).

As its name implies, [**DllCanUnloadNow**](/windows/desktop/api/combaseapi/nf-combaseapi-dllcanunloadnow) is called to determine whether the DLL that implements it is in use, enabling the caller to safely unload it if it is not. Calls to [**CoFreeUnusedLibraries**](/windows/desktop/api/combaseapi/nf-combaseapi-cofreeunusedlibraries) from any thread always route through the main apartment's thread to call **DllCanUnloadNow**.

Like other servers, in-process servers can be single-threaded, apartment-threaded, or free-threaded. These servers can be used by any OLE client, regardless of the threading model used by that client.

All combinations of threading model interoperability are allowed between clients and in-process objects. Interaction between a client and an in-process object that use different threading models is exactly like the interaction between clients and out-of-process servers. For an in-process server, when the threading model of the client and in-process server differ, COM must interpose itself between the client and the object.

When an in-process object that supports the single-threaded model is called simultaneously by multiple threads of a client, COM cannot allow the client threads to directly access the object's interfaceâ€”the object was not designed for such access. Instead, COM must ensure that calls are synchronized and are made only by the client thread that created the object. Therefore, COM creates the object in the client's main apartment and requires all the other client apartments to access the object by using proxies.

When a free-threaded apartment (multithreaded apartment model) in a client creates an apartment-threaded in-process server, COM spins up a single-threaded apartment model "host" thread in the client. This host thread will create the object, and the interface pointer will be marshaled back to the client's free-threaded apartment. Similarly, when a single-threaded apartment in an apartment-model client creates a free-threaded in-process server, COM spins up a free-threaded host thread (multithreaded apartment on which the object will be created and then marshaled back to the client single-threaded apartment).

> [!Note]  
> In general, if you design a custom interface on an in-process server, you should also provide the marshaling code for it so that COM can marshal the interface between client apartments.

 

COM helps protect access to objects provided by a single-threaded DLL by requiring access from the same client apartment in which they were created. In addition, all of the DLL entry points (like [**DllGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-dllgetclassobject) and [**DllCanUnloadNow**](/windows/desktop/api/combaseapi/nf-combaseapi-dllcanunloadnow)) and global data should always be accessed by the same apartment. COM creates such objects in the main apartment of the client, giving the main apartment direct access to the object's pointers. Calls from the other apartments use interthread marshaling to go from the proxy to the stub in the main apartment and then to the object. This allows COM to synchronize calls to the object. Interthread calls are slow, so it is recommended that these servers be rewritten to support multiple apartments.

Like a single-threaded in-process server, an object provided by an apartment model DLL must be accessed by the same client apartment from which it was created. However, objects provided by this server can be created in multiple apartments of the client, so the server must implement its entry points (like [**DllGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-dllgetclassobject) and [**DllCanUnloadNow**](/windows/desktop/api/combaseapi/nf-combaseapi-dllcanunloadnow)) for multithreaded use. For example, if two apartments of a client try to create two instances of the in-process object simultaneously, **DllGetClassObject** can be called simultaneously by both apartments. **DllCanUnloadNow** must be written so that the DLL does not unload while code is still executing in the DLL.

If the DLL provides only one instance of the class factory to create all the objects, the class factory implementation must also be designed for multithreaded use, because it will be accessed by multiple client apartments. If the DLL creates a new instance of the class factory each time [**DllGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-dllgetclassobject) is called, the class factory need not be thread-safe.

Objects created by the class factory need not be thread-safe. Once created by a thread, the object is always accessed through that thread and all calls to the object are synchronized by COM. The apartment model apartment of a client that creates this object will get a direct pointer to the object. Client apartments that are different from the apartment in which the object was created must access the object through proxies. These proxies are created when the client marshals the interface between its apartments.

When an in-process DLL **ThreadingModel** value is set to "Both", an object provided by this DLL can be created and used directly (without a proxy) in single-threaded or multithreaded client apartments. However, it can be used directly only within the apartment in which it was created. To give the object to any other apartment, the object must be marshaled. The DLL object must implement its own synchronization and can be accessed by multiple client apartments at the same time.

To speed performance for free-threaded access to in-process DLL objects, COM provides the [**CoCreateFreeThreadedMarshaler**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreatefreethreadedmarshaler) function. This function creates a free-threaded marshaling object that can be aggregated with an in-process server object. When a client apartment in the same process needs access to an object in another apartment, aggregating the free-threaded marshaler provides the client with a direct pointer to the server object, rather than to a proxy, when the client marshals the object's interface to a different apartment. The client does not need to do any synchronization. This works only within the same process; standard marshaling is used for a reference to the object that is sent to another process.

An object provided by an in-process DLL that supports only free threading is a free-threaded object. It implements its own synchronization and can be accessed by multiple client threads at the same time. This server does not marshal interfaces between threads, so this server can be created and used directly (without a proxy) only by multithreaded apartments in a client. Single-threaded apartments that create it will access it through a proxy.

## Related topics

<dl> <dt>

[Accessing Interfaces Across Apartments](accessing-interfaces-across-apartments.md)
</dt> <dt>

[Choosing the Threading Model](choosing-the-threading-model.md)
</dt> <dt>

[Multithreaded Apartments](multithreaded-apartments.md)
</dt> <dt>

[Processes, Threads, and Apartments](processes--threads--and-apartments.md)
</dt> <dt>

[Single-Threaded and Multithreaded Communication](single-threaded-and-multithreaded-communication.md)
</dt> <dt>

[Single-Threaded Apartments](single-threaded-apartments.md)
</dt> </dl>

 

 