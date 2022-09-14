---
description: The IHWEventHandler interface can be registered in the running object table (ROT) so that running applications have access to AutoPlay events.
ms.assetid: 6FEFFB5D-DD8B-4FEA-B273-D32FC30CAFEA
title: How to Use AutoPlay Events in Running Applications
ms.topic: article
ms.date: 05/31/2018
---

# How to Use AutoPlay Events in Running Applications

The [**IHWEventHandler**](/windows/desktop/api/Shobjidl/nn-shobjidl-ihweventhandler) interface can be registered in the running object table (ROT) so that running applications have access to AutoPlay events.

The following instructions describe how to use AutoPlay events in running applications.

## Instructions

### Step 1:

Create a new component that implements the [**IHWEventHandler**](/windows/desktop/api/Shobjidl/nn-shobjidl-ihweventhandler) interface.

### Step 2:

Initialize the new component with the InitCmdLine value from the particular handler's entry under the **Handlers** key.

This step is required because Autoplay does not call the Initialize method.

### Step 3:

Call the [**CreateHardwareEventMoniker**](createhardwareeventmoniker.md) function to get a moniker that represents your component and the event handler that you want to call.

### Step 4:

Use the *ppmoniker* parameter to register your component in the ROT.

## Remarks

> [!Note]  
> [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) can pose security risks. Refer to the **LoadLibrary** documentation for information on how to correctly load DLLs with different versions of Windows.

```cpp
typedef HRESULT (*CREATEHARDWAREEVENTMONIKER)(REFCLSID clsid, LPCWSTR pszEventHandler, IMoniker **ppmoniker);

HRESULT RegisterComponent(IUnknown* punk, DWORD* dpwToken)
{
    HRESULT hr = E_FAIL;
    HINSTANCE hinstShSvcs = LoadLibrary(TEXT("shsvcs.dll"));
    
    if (hinstShSvcs)
    {   
        CREATEHARDWAREEVENTMONIKER fct = (CREATEHARDWAREEVENTMONIKER)GetProcAddress(hinstShSvcs, "CreateHardwareEventMoniker");
        if (fct)
        {
            IMoniker* pmoniker;
            
            hr = fct(CLSID_App, TEXT("VideoCameraArrival"), &pmoniker);

            if (SUCCEEDED(hr))
            {
                IRunningObjectTable *prot;
                    
                if (SUCCEEDED(GetRunningObjectTable(0, &prot)))
                {
                    hr = prot->Register(ROTFLAGS_ALLOWANYCLIENT | ROTFLAGS_REGISTRATIONKEEPSALIVE, punk, pmoniker, &_dwRegisterROT);
                    prot->Release();
                }
                pmoniker->Release();
            }
            CoRegisterClassObject(CLSID_App, static_cast<IClassFactory *>(this), CLSCTX_LOCAL_SERVER, REGCLS_MULTIPLEUSE, &_dwRegisterClass;
        }
        FreeLibrary(hinstShSvcs);
    }
    return hr;
}
```

The call to [**IRunningObjectTable::Register**](/windows/win32/api/objidl/nf-objidl-irunningobjecttable-register) requires that the component have the following **AppID** information in the registry.

```
HKEY_CLASSES_ROOT
   AppID
      MyApp.exe
         (Default) = MyApplication
         AppID [REG_SZ] = {Your GUID here}
```

```
HKEY_CLASSES_ROOT
   AppID
      {The same GUID here}
         (Default) = MyApplication
         RunAs = Interactive User
```

## Related topics

[**IHWEventHandler**](/windows/desktop/api/Shobjidl/nn-shobjidl-ihweventhandler)

[**CreateHardwareEventMoniker**](createhardwareeventmoniker.md)
