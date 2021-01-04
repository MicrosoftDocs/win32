---
title: VirtualChannelGetInstance entry point
description: Called to have the plug-in create an instance of the IWTSPlugin interface for all plug-ins implemented by the DLL.
ms.assetid: B81BD61E-1F43-42C9-8839-30F4F4C3973C
ms.tgt_platform: multiple
keywords:
- VirtualChannelGetInstance entry point Remote Desktop Services
topic_type:
- apiref
api_name:
- VirtualChannelGetInstance
api_type:
- UserDefined
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# VirtualChannelGetInstance entry point

Called to have the plug-in create an instance of the [**IWTSPlugin**](/windows/desktop/api/TsVirtualChannels/nn-tsvirtualchannels-iwtsplugin) interface for all plug-ins implemented by the DLL.

> [!Note]
>
> This function is implemented by the plug-in and must be exported by name such that an application can use the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to the function.
>
> The prototype for this function is not contained in any public header file, so you must declare it exactly as shown.

 

## Syntax


```C++
HRESULT VCAPITYPE VirtualChannelGetInstance(
  _In_    REFIID refiid,
  _Inout_ ULONG  *pNumObjs,
  _Out_   VOID   **ppObjArray
);
```



## Parameters

<dl> <dt>

*refiid* \[in\]
</dt> <dd>

Specifies the type of interface to return. This must be **IID\_IWTSPlugin**.

</dd> <dt>

*pNumObjs* \[in, out\]
</dt> <dd>

The address of a **ULONG** variable that receives the number of interfaces retrieved.

</dd> <dt>

*ppObjArray* \[out\]
</dt> <dd>

The address of an array of pointers that receives the interface pointers. If this parameter is **NULL**, the implementation must put the number of plug-ins implemented by the DLL in the *pNumObjs* parameter. This allows the caller to allocate the proper size array for *ppObjArray*.

</dd> </dl>

## Return value

If this entry point succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



 

