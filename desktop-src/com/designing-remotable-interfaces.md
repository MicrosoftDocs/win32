---
title: Designing Remotable Interfaces
description: With the advent of the distributed component object model, it is important that your custom interface be remotable, even if you intend to use it in-process only.
ms.assetid: 2ee4d950-dfd5-4965-bd77-a600e878be59
ms.topic: article
ms.date: 05/31/2018
---

# Designing Remotable Interfaces

With the advent of the distributed component object model, it is important that your custom interface be remotable, even if you intend to use it in-process only.

MIDL is more than just a way to generate header files for your interfaces. It is a programming language for remoting that allows you to use your interfaces across machine, process, and thread boundaries. This means that you need to verify the behavior of your MIDL-defined interfaces under those conditions before you release your program to customers. If you made a mistake in your IDL and the interface is not remoted correctly, it can be difficult to remedy that mistake. Either you have to revise your interface with a new IID and leave the old one in for backward compatibility or you have to convert every client and every server machine everywhere at the same time.

Even if your interface will never be used out-of-process, it may be used cross-thread. The worst problem for an unchecked IDL file can arise for in-process servers that do not support multiple [single-threaded apartments](single-threaded-apartments.md)). A server that does not specify a threading model is implicitly single-threaded. Everything marked single-threaded is forced over to the thread that first called [**CoInitialize**](/windows/desktop/api/Objbase/nf-objbase-coinitialize) or [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex). If some other thread was the one that activated the object, all the interfaces on that single-threaded server must be remoted back to the activating thread, which can result in a return of REGDB\_E\_IIDNOTREG in response to a call to [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q))). Unless you can absolutely assert that your interface is both in-process and always going to be called on the same thread, you will get remoted at some time.

Finally, as an interface designer, you need to consider how client applications will use your interface. Two things, together, determine whether an interface will be efficient across process and machine boundaries: the frequency of method calls across the interface boundary, and the amount of data to be transferred in a given method call. Although COM makes cross-process and cross-network calls transparent to programs, it cannot make high-frequency and high-bandwidth calls efficient across address spaces. In some cases, it is more appropriate to design interfaces that will normally be implemented only as in-process servers while other interfaces are more appropriate for remote use.

 

 




