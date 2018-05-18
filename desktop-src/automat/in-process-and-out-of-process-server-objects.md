---
title: In-Process and Out-of-Process Server Objects
description: ActiveX objects can exist in the same process as their controller, or in a different process.
ms.assetid: 'ebd6559d-6e49-4722-a789-38eb5194ab40'
---

# In-Process and Out-of-Process Server Objects

ActiveX objects can exist in the same process as their controller, or in a different process.*In-process server* objects are implemented in a dynamic-link library (DLL) and are run in the process space of the controller. Because they are contained in a DLL, they cannot be run as stand-alone objects. *Out-of-process server* objects are implemented in an executable file and are run in a separate process space. Access to in-process objects is much faster than to out-of-process server objects because Automation does not need to make remote procedure calls across the process boundary.

The access mechanism ([**IDispatch**](idispatch.md) or VTBL) and the location of an object (in-process or out-of-process server) determine the fixed overhead required for access. The most important factor in performance, however, is the quantity and nature of the work performed by the methods and procedures that are invoked. If a method is time consuming or requires remote procedure calls, the overhead of the call to **IDispatch** may make a call to VTBL more appropriate.

 

 




