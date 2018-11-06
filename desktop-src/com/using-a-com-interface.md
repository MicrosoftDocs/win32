---
title: Using a COM Interface
description: Using a COM Interface
ms.assetid: 44e1aeac-585c-4856-8c4d-1adb5b307b74
ms.topic: article
ms.date: 05/31/2018
---

# Using a COM Interface

The client code is the user of the COM interface. To use any COM interface, custom or standard, a client must know its IID. In the following example, the driver that calls CustomRpt passes it the name of the object that is converted to a wide-character format. The object name is fed to [**CreateFileMoniker**](/windows/desktop/api/Objbase/nf-objbase-createfilemoniker) so that a file moniker can be created and the client can bind to the running object. After the object is running, CustomRpt can access a pointer to either an interface in the standard proxy/stub, such as [**IPersistFile**](/windows/desktop/api/ObjIdl/nn-objidl-ipersistfile), or to the custom interface, ICustomInterface.


```C++
void CustomRpt(char *pszObject) 
{ 
    HRESULT             hr; 
    WCHAR               wszObject[128]; 
    WCHAR               wszMsg[128] = {L"Your Message Here...\n"}; 
    IMoniker            *pmkObject = NULL; 
    IUnknown            *pIUnk = NULL; 
    IPersistFile        *pIPersistFile = NULL; 
    ICustomInterface    *pICustomInterface = NULL; 
 
    // Create a wide-character version of the object's file name. 
    StringCchPrintf(wszObject, 128, L"%hs", pszObject); 
 
    // Get a file moniker for the object (a *.smp file). 
    hr = CreateFileMoniker(wszObject, &pmkObject); 
 
    if(FAILED(hr)) 
    { 
        printf("Client: CreateFileMoniker for Object failed"); 
        return; 
    } 
 
    // BindMoniker is equivalent to calling CreateBindCtx() followed by 
    // a call to BindToObject(). It has the net result of binding the 
    // interface (specified by the IID) to the moniker. 
 
    hr = BindMoniker(pmkObject, 0, IID_IUnknown, (void **)&pIUnk); 
    if (FAILED(hr)) 
    { 
        printf("Client: BindMoniker failed (%x)\n", hr); 
        return; 
    } 
 
    // Try a couple QueryInterface calls into the object code; first a 
    // QueryInterface to IPersistFile... 
 
    hr = pIUnk->QueryInterface(IID_IPersistFile, (void **)&pIPersistFile); 
 
    if (FAILED(hr)) { 
        printf("Client: QueryInterface IPersistFile failed (%x)\n", hr); 
        pIUnk->Release(); 
        return; 
    } 
 
    // Followed by a QueryInterface to ICustomInterface. 
    hr = pIUnk->QueryInterface(IID_ICustomInterface, (void **)&pICustomInterface); 
 
    if (FAILED(hr)) { 
        printf("Client: QueryInterface failed (%x)\n", hr); 
        pIUnk->Release(); 
        pIPersistFile->Release(); 
        return; 
    } 
 
    // CustomReport() is the object function that displays the time and 
    // date information on the object. 
    hr = pICustomInterface->CustomReport(); 
 
    if (FAILED(hr)) 
    { 
        printf("Client: pICustomInterface->CustomReport failed (%x)\n", hr); 
        pIUnk->Release(); 
        pIPersistFile->Release(); 
        return; 
    } 
 
    // Clean up resources by calling release on each of the interfaces. 
    pIPersistFile->Release(); 
    pICustomInterface->Release(); 
    pIUnk->Release(); 
    return; 
} 
```



 

 




