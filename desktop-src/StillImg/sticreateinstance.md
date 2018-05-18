---
title: StiCreateInstance function
description: The StiCreateInstance function is used to obtain a pointer to the IStillImage interface.
ms.assetid: 'dff6e565-8faa-4fb9-ab90-5106c4d977f2'
keywords: ["StiCreateInstance function Still Image"]
topic_type:
- apiref
api_name:
- StiCreateInstance
- StiCreateInstanceA
- StiCreateInstanceW
api_location:
- sti.dll
api_type:
- DllExport
---

# StiCreateInstance function

The **StiCreateInstance** function is used to obtain a pointer to the **IStillImage** interface. All other Still Image methods are called through the pointer obtained from this function. Calling this function is similar to calling the standard COM [**CoCreateInstance**](_com_CoCreateInstance) and [**CoInitialize**](_com_CoInitialize) functions.

## Syntax


```C++
HRESULT StiCreateInstance(
  _In_  HINSTANCE hinst,
  _In_  DWORD     dwVer,
  _Out_ PSTI      *ppSti,
  _In_  LPUNKNOWN punkOuter
);
```



## Parameters

<dl> <dt>

*hinst* \[in\]
</dt> <dd>

Instance handle to the application or DLL that creates the **IStillImage** object.

STI uses this value to determine whether the application or DLL has been certified.

</dd> <dt>

*dwVer* \[in\]
</dt> <dd>

Version number of the Sti.h header file that was used. This value must be **STI\_VERSION**. Still Image uses this value to determine for what version of STI the application or DLL was designed.

</dd> <dt>

*ppSti* \[out\]
</dt> <dd>

Pointer to a pointer to the **IStillImage** interface. This is an output parameter. When the function returns, this parameter contains a pointer to an **IStillImage** interface if the function is successful.

</dd> <dt>

*punkOuter* \[in\]
</dt> <dd>

Pointer to the controlling [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface of the COM aggregate object, or **NULL** if the interface is not aggregated. Most callers pass **NULL**. See the section on [Aggregation](_com_aggregation) in Component Services for more information.

> [!Note]  
> If aggregation is requested, the object returned in *ppSti* is a pointer to an [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) rather than an **IStillImage** , as required by COM aggregation.

 

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**.

If the function fails, the return value is the appropriate COM error.

## Remarks

Calling this function with *punkOuter* = **NULL** is similar to creating the object with `CoCreateInstance (&CLSID_Sti, punkOuter, CLSCTX_INPROC_SERVER, &IID_IStillImage, ppSti);` then initializing it with [**CoInitialize**](_com_CoInitialize).

Calling this function with *punkOuter* != **NULL** is similar to creating the object with `CoCreateInstance (&CLSID_Sti, punkOuter, CLSCTX_INPROC_SERVER, &IID_IUnknown, ppSti)`. The aggregated object must be initialized manually.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Sti.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Sti.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sti.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **StiCreateInstanceW** (Unicode) and **StiCreateInstanceA** (ANSI)<br/>      |



## See also

<dl> <dt>

[About Still Image](about-still-image.md)
</dt> <dt>

[Making an Application Still Image-Aware](making-an-application-still-image-aware.md)
</dt> </dl>

 

 





