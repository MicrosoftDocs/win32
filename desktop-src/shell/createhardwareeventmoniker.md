---
Description: Creates a moniker representing a hardware component and its associated event handler. AutoPlay uses this function to allow applications to use AutoPlay events.
title: CreateHardwareEventMoniker function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateHardwareEventMoniker function

\[This function is available through Windows XP with Service Pack 2 (SP2) and Windows Server 2003. It might be altered or unavailable in subsequent versions of Windows.\]

Creates a moniker representing a hardware component and its associated event handler. AutoPlay uses this function to allow applications to use AutoPlay events.

## Syntax


```C++
HRESULT CreateHardwareEventMoniker(
  _In_  REFCLSID clsid,
  _In_  LPCTSTR  pszEventHandler,
  _Out_ IMoniker **ppmoniker
);
```



## Parameters

<dl> <dt>

*clsid* \[in\]
</dt> <dd>

Type: **REFCLSID**

The ID of the class to which the moniker binds.

</dd> <dt>

*pszEventHandler* \[in\]
</dt> <dd>

Type: **LPCTSTR**

The name of the event handler.

</dd> <dt>

*ppmoniker* \[out\]
</dt> <dd>

Type: **[**IMoniker**](https://msdn.microsoft.com/windows/desktop/17f4c1df-7a9c-42ef-a888-70cd8d85f070)\*\***

The address of a pointer variable that receives the [**IMoniker**](https://msdn.microsoft.com/windows/desktop/17f4c1df-7a9c-42ef-a888-70cd8d85f070) interface pointer.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Use **CreateHardwareEventMoniker** when registering running applications so that those applications have access to AutoPlay events. To use AutoPlay events in running applications, you must first create a new component that implements the [**IHWEventHandler**](/windows/desktop/api/Shobjidl/nn-shobjidl-ihweventhandler) interface. Initialize this interface with the InitCmdLine value from the particular handler's entry under the **Handlers** key, because AutoPlay does not call the [**Initialize**](/windows/desktop/api/Shobjidl/nf-shobjidl-ihweventhandler-initialize) method.

You should call **CreateHardwareEventMoniker** to get a moniker that represents your component and its event handler. Then, use the value returned in the *ppmoniker* parameter to register your component in the running object table (ROT) as shown in the example.

Note that **CreateHardwareEventMoniker** is not defined in a header file. To use it in your code, you must obtain a handle to the Shsvcs.dll file through a call to [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65). You then use that handle in a call to [**GetProcAddress**](https://msdn.microsoft.com/windows/desktop/a0d7fc09-f888-4f46-a571-d3719a627597) to obtain an instance of the **CreateHardwareEventMoniker** function.

The call to [**IRunningObjectTable::Register**](https://msdn.microsoft.com/windows/desktop/40f815b2-dfea-416c-aae1-7ba3a710ad91) requires that you enter the following **AppID** information in the registry.

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

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>None</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Shsvcs.dll</dt> </dl> |



 

 




