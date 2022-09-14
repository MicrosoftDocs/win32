---
title: Rules for Managing Reference Counts
description: Using a reference count to manage an object's lifetime allows multiple clients to obtain and release access to a single object without having to coordinate with one another in managing the object's lifetime.
ms.assetid: bbe7d16c-fcb7-474d-a22d-5a3b33dd800e
ms.topic: article
ms.date: 05/31/2018
---

# Rules for Managing Reference Counts

Using a reference count to manage an object's lifetime allows multiple clients to obtain and release access to a single object without having to coordinate with one another in managing the object's lifetime. As long as the client object conforms to certain rules of use, the object, in effect, provides this management. These rules specify how to manage references between objects. (COM does not specify internal implementations of objects, although these rules are a reasonable starting point for a policy within an object.)

Conceptually, interface pointers can be thought of as residing within pointer variables that include all the internal computation state that holds an interface pointer. This would include variables in memory locations, in internal processor registers, and both programmer-generated and compiler-generated variables. Assignment to or initialization of a pointer variable involves creating a new copy of an already existing pointer. Where there was one copy of the pointer in some variable (the value used in the assignment/initialization), there are now two. An assignment to a pointer variable destroys the pointer copy presently in the variable, as does the destruction of the variable itself. (That is, the scope in which the variable is found, such as the stack frame, is destroyed.)

From a COM client's perspective, reference counting is always done for each interface. Clients should never assume that an object uses the same counter for all interfaces.

The default case is that [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) must be called for every new copy of an interface pointer and [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) must be called for every destruction of an interface pointer, except where the following rules permit otherwise:

-   **In-out parameters to functions.** The caller must call [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) on the parameter because it will be released (with a call to [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release)) in the implementing code when the out value is stored on top of it.
-   **Fetching a global variable.** When creating a local copy of an interface pointer from an existing copy of the pointer in a global variable, you must call [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) on the local copy because another function might destroy the copy in the global variable while the local copy is still valid.
-   **New pointers synthesized out of "thin air."** A function that synthesizes an interface pointer using special internal knowledge rather than obtaining it from some other source must call [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) initially on the newly synthesized pointer. Important examples of such routines include instance creation routines, implementations of [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)), and so on.
-   **Retrieving a copy of an internally stored pointer.** When a function retrieves a copy of a pointer that is stored internally by the object called, that object's code must call [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) on the pointer before the function returns. Once the pointer has been retrieved, the originating object has no other way of determining how its lifetime relates to that of the internally stored copy of the pointer.

The only exceptions to the default case require that the managing code know the relationships of the lifetimes of two or more copies of a pointer to the same interface on an object and simply ensure that the object is not destroyed by allowing its reference count to go to zero. There are generally two cases, as follows:

-   When one copy of a pointer already exists and a second is created subsequently and then is destroyed while the first copy still exists, calls to [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) and [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release)for the second copy can be omitted.
-   When one copy of a pointer exists and a second is created and then the first is destroyed before the second, the calls to [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref)for the second copy and to [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) for the first copy can be omitted.

The following are specific examples of these situations, the first two being especially common:

-   **In parameters to functions.** The lifetime of the copy of an interface pointer passed as a parameter to a function is nested in that of the pointer used to initialize the value, so there is no need for a separate reference count on the parameter.
-   **Out parameters from functions, including return values.** To set the out parameter, the function must have a stable copy of the interface pointer. On return, the caller is responsible for releasing the pointer. Therefore, the out parameter does not need a separate reference count.
-   **Local variables.** A method implementation has control of the lifetimes of each of the pointer variables allocated on the stack frame and can use this to determine how to omit redundant [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref)/[**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) pairs.
-   **Backpointers.** Some data structures contain two objects, each with a pointer to the other. If the lifetime of the first object is known to contain the lifetime of the second, it is not necessary to have a reference count on the second object's pointer to the first object. Often, avoiding this cycle is important in maintaining the appropriate deallocation behavior. However, uncounted pointers should be used with extreme caution because the portion of the operating system that handles remote processing has no way of knowing about this relationship. Therefore, in almost all cases, having the backpointer see a second, "friend" object of the first pointer (thus avoiding the circularity) is the preferred solution. COM's connectable objects architecture, for example, uses this approach.

When implementing or using reference-counted objects, it may be useful to apply *artificial reference counts*, which guarantee object stability during processing of a function. In implementing a method of an interface, you might call functions that have a chance of decrementing your reference count to an object, causing a premature release of the object and failure of the implementation. A robust way to avoid this is to insert a call to [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) at the beginning of the method implementation and pair it with a call to [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) just before the method returns.

In some situations, the return values of [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) and [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) may be unstable and should not be relied upon; they should be used only for debugging or diagnostic purposes.

## Related topics

<dl> <dt>

[Managing Object Lifetimes Through Reference Counting](managing-object-lifetimes-through-reference-counting.md)
</dt> </dl>

 

 