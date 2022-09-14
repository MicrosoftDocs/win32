---
title: Create New Interfaces to the Same Object
description: Create New Interfaces to the Same Object
ms.assetid: 127c44b6-51a6-4fd6-9edc-9fbe0d08d458
ms.topic: article
ms.date: 05/31/2018
---

# Create New Interfaces to the Same Object

In this scenario, the server responds to each [**OBJID\_CLIENT**](object-identifiers.md) request by obtaining a new interface pointer to the same object.

In the following example code, *m\_pUIObj* is a pointer to an object that supports more than one Component Object Model (COM) interface. Even though an existing object is reused, a new interface pointer is created each time the object is retrieved, so the reference count must be decremented.


```C++
case WM_GETOBJECT:
   if ((DWORD)lParam == OBJID_CLIENT)
   {
      // Get a new interface to the same object. 
      IAccessible *pAcc = NULL;
      // The following increments the reference count. 
      m_pUIObj->QueryInterface(IID_IAccessible, (LPVOID*)&pAcc); 
      LRESULT lAcc = LresultFromObject(IID_IAccessible, wParam, 
            (LPUNKNOWN) &pAcc); 
      // Release our reference to the object.             
      pAcc->Release();               
      return lAcc;
   }
   break;  // Fall through to DefWindowProc. 
   
```



 

 




