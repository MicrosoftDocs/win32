---
title: Creating a File-Handler Instance in a DLL
description: Creating a File-Handler Instance in a DLL
ms.assetid: '0cf7ef72-c675-4a67-97b3-18cccfb7ddc1'
---

# Creating a File-Handler Instance in a DLL

When an application specifies your file-handler DLL or stream handler, the system looks it up in the registry by its class identifier and loaded. The system then calls the [**DllGetClassObject**](dllgetclassobject.md) function of the DLL to create an instance of the file or stream handler. The following example (written in C++) shows how a file handler creates an instance.


```C++
// Main DLL entry point. 
STDAPI DllGetClassObject(const CLSID FAR&amp; rclsid, 
    const IID FAR&amp; riid, void FAR* FAR* ppv) 
{ 
    HRESULT hresult; 
    hresult = CAVIFileCF::Create(rclsid, riid, ppv); 
    return hresult; 
} 
HRESULT CAVIFileCF::Create(const CLSID FAR&amp;   rclsid, 
    const IID FAR&amp; riid, void FAR* FAR*   ppv) 
{ 
// The following is the class factory creation and not an 
// actual PAVIFile. 
    CAVIFileCF FAR*   pAVIFileCF; 
    IUnknown FAR*   pUnknown; 
    HRESULT hresult; 
 
// Create the instance. 
    pAVIFileCF = new FAR CAVIFileCF(rclsid, &amp;pUnknown); 
    if (pAVIFileCF == NULL) 
        return ResultFromScode(E_OUTOFMEMORY); 
 
// Set the interface pointer. 
    hresult = pUnknown->QueryInterface(riid, ppv); 
    if (FAILED(GetScode(hresult))) 
        delete pAVIFileCF; 
    return hresult; 
} 

```



 

 




