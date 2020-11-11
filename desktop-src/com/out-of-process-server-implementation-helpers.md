---
title: Out-of-Process Server Implementation Helpers
description: Out-of-Process Server Implementation Helpers
ms.assetid: 18641a84-56f8-4d27-9ddb-fa64011ac8ba
ms.topic: article
ms.date: 05/31/2018
---

# Out-of-Process Server Implementation Helpers

Four helper functions that can be called by out-of-process servers are available to simplify the job of writing server code. COM clients and COM in-process servers typically would not call them. These functions are designed to help prevent race conditions in server activation when the servers have multiple apartments or multiple class objects. They can also, however, as easily be used for single-threaded and single class object servers. The functions are as follows:

-   [**CoAddRefServerProcess**](/windows/desktop/api/combaseapi/nf-combaseapi-coaddrefserverprocess)
-   [**CoReleaseServerProcess**](/windows/desktop/api/combaseapi/nf-combaseapi-coreleaseserverprocess)
-   [**CoSuspendClassObjects**](/windows/desktop/api/combaseapi/nf-combaseapi-cosuspendclassobjects)
-   [**CoResumeClassObjects**](/windows/desktop/api/combaseapi/nf-combaseapi-coresumeclassobjects)

To shut down properly, a COM server must keep track of how many object instances it has instantiated and how many times its [**IClassFactory::LockServer**](/windows/win32/api/unknwn/nf-unknwn-iclassfactory-lockserver) method has been called. Only when both of these counts reach zero can a server shut down. In single-threaded COM servers, the decision to shut down was coordinated with incoming activation requests, which were serialized by the message queue. The server, upon receiving a release on its final object instance and deciding to shut down, would revoke its class objects before any more activation requests were dispatched. If an activation request did come in after this point, COM would recognize that the class objects were revoked and would return an error to the Service Control Manager (SCM), which would then cause a new instance of the local server process to be run.

However, in an apartment model server, in which different class objects are registered on different apartments, and in all free-threaded servers, this decision to shut down must be coordinated with activation requests across multiple threads so that one thread of the server does not decide to shut down while another thread of the server is busy handing out class objects or object instances. One classical but cumbersome approach to solving this is to have the server, after it has revoked its class objects, recheck its instance count and stay alive until all instances have been released.

To make it easier for server writers to handle these types of race conditions, COM provides two reference counting functions:

-   [**CoAddRefServerProcess**](/windows/desktop/api/combaseapi/nf-combaseapi-coaddrefserverprocess) increments a global per-process reference count.
-   [**CoReleaseServerProcess**](/windows/desktop/api/combaseapi/nf-combaseapi-coreleaseserverprocess) decrements the global per-process reference count.

When the global per-process reference count reaches zero, COM automatically calls [**CoSuspendClassObjects**](/windows/desktop/api/combaseapi/nf-combaseapi-cosuspendclassobjects), which prevents any new activation requests from coming in. The server can then deregister its various class objects from its various threads at leisure without worry that another activation request may come in. All new activation requests are henceforth handled by the SCM launching a new instance of the local server process.

The simplest way for a local server application to make use of these functions is to call [**CoAddRefServerProcess**](/windows/desktop/api/combaseapi/nf-combaseapi-coaddrefserverprocess) in the constructor for each of its instance objects and in each of its [**IClassFactory::LockServer**](/windows/win32/api/unknwn/nf-unknwn-iclassfactory-lockserver) methods when the *fLock* parameter is **TRUE**. The server application should also call [**CoReleaseServerProcess**](/windows/desktop/api/combaseapi/nf-combaseapi-coreleaseserverprocess) in the destructor of each of its instance objects and in each of its IClassFactory::**LockServer** methods when the *fLock* parameter is **FALSE**.

Finally, the server application should pay attention to the return code from [**CoReleaseServerProcess**](/windows/desktop/api/combaseapi/nf-combaseapi-coreleaseserverprocess), and if it returns 0, the server application should initiate its cleanup, which, for a server with multiple threads, typically means that it should signal its various threads to exit their message loops and call [**CoAddRefServerProcess**](/windows/desktop/api/combaseapi/nf-combaseapi-coaddrefserverprocess) and [**CoReleaseServerProcess**](/windows/desktop/api/combaseapi/nf-combaseapi-coreleaseserverprocess). If the server process lifetime management functions are used, they must be used in both the object instances and the [**LockServer**](/windows/win32/api/unknwn/nf-unknwn-iclassfactory-lockserver) method; otherwise, the server application may be shut down prematurely.

When a [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject) request is made, COM contacts the server, marshals the [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) interface of the class object, returns to the client process, unmarshals the **IClassFactory** interface, and returns this to the client. At this point, clients typically call [**LockServer**](/windows/win32/api/unknwn/nf-unknwn-iclassfactory-lockserver) with **TRUE** to prevent the server process from shutting down. However, there is a window of time between when the class object is marshaled and when the client calls **LockServer** in which another client could connect to the same server, get an instance, and release that instance, thus causing the server to shut down and leaving the first client high and dry with a disconnected **IClassFactory** pointer. To prevent this race condition, COM adds an implicit call to **LockServer** with **TRUE** to the class object when it marshals the **IClassFactory** interface and an implicit call to **LockServer** with **FALSE** when the client releases the **IClassFactory** interface. Therefore, it is not necessary to remote **LockServer** calls back to the server, and the proxy for **LockServer** simply returns S\_OK without actually remoting the call.

There is another activation-related race condition during initialization of an out-of-process server process. A COM server that registers multiple classes typically calls [**CoRegisterClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-coregisterclassobject) with REGCLS\_LOCAL\_SERVER for each CLSID it supports. After it has done this for all classes, the server enters its message loop. For a single-threaded COM server, all activation requests are blocked until the server enters the message loop. However, for an apartment model server that registers different class objects in different apartments and for all free-threaded servers, activation requests can arrive earlier than this. In the case of apartment model servers, activation requests could arrive as soon as any one thread has entered its message loop. In the case of free-threaded servers, an activation request could arrive as soon as the first class object is registered. Since an activation can happen this early, it is also possible for the final release to occur (and therefore cause the server to begin shutting down) before the rest of the server has had a chance to finish initializing.

To eliminate these race conditions and simplify the job of the server writer, any server that wants to register multiple class objects with COM should call [**CoRegisterClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-coregisterclassobject) with REGCLS\_LOCAL\_SERVER \| REGCLS\_SUSPENDED for each different CLSID the server supports. After all classes have been registered and the server process is ready to accept incoming activation requests, the server should make one call to [**CoResumeClassObjects**](/windows/desktop/api/combaseapi/nf-combaseapi-coresumeclassobjects). This function tells COM to inform the SCM about all the registered classes, and it begins letting activation requests into the server process. Using these functions provides the following advantages:

-   Only one call is made to the SCM, regardless of how many CLSIDs are registered, thus reducing the overall registration time (and hence startup time of the server application).
-   If the server has multiple apartments and different CLSIDs are registered in different apartments, or if the server is a free-threaded server, no activation requests will come in until the server calls [**CoResumeClassObjects**](/windows/desktop/api/combaseapi/nf-combaseapi-coresumeclassobjects), giving the server a chance to register all of its CLSIDs and get properly set up before having to deal with activation requests and possible shut down requests.

## Related topics

<dl> <dt>

[COM Server Responsibilities](com-server-responsibilities.md)
</dt> </dl>

 

 