---
title: Service Object Error Handling
description: When an error occurs in a service object, the return value for the call IDispatch Invoke should be DISP\_E\_EXCEPTION, and the pExceptInfo parameter pointer to an EXCEPTINFO structure in the should be filled in.
ms.assetid: '1b08c404-69f2-4b0d-9231-c2bd242e124d'
---

# Service Object Error Handling

When an error occurs in a service object, the return value for the call [**IDispatch::Invoke**](964ade8e-9d8a-4d32-bd47-aa678912a54d) should be DISP\_E\_EXCEPTION, and the *pExceptInfo* parameter pointer to an [**EXCEPTINFO**](29583e58-10a6-4679-a5c6-d51f2b50b074) structure in the should be filled in.

Specifically, the **bstrSource**, and **bstrDescription** members of the [**EXCEPTINFO**](29583e58-10a6-4679-a5c6-d51f2b50b074) structure are used by the Device Host with UPnP technology to create a UPnP Fault response; **bstrSource** is the error code and **bstrDescription** is the error description.

 

 




