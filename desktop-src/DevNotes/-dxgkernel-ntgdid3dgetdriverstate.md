---
description: Used by both the Microsoft DirectDraw and Microsoft Direct3D runtimes to obtain information from the driver about its current state.
ms.assetid: a7697e0c-9485-4a9c-b211-67ce07dc3604
title: NtGdiD3DGetDriverState function (Ntgdi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtGdiD3DGetDriverState
api_type: 
- HeaderDef
api_location: 
- Ntgdi.h
---

# NtGdiD3DGetDriverState function

\[This function is subject to change with each operating system revision. Instead, use the DirectDraw and Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Used by both the Microsoft DirectDraw and Microsoft Direct3D runtimes to obtain information from the driver about its current state.

## Syntax


```C++
DWORD APIENTRY NtGdiD3DGetDriverState(
  _Inout_ PDD_GETDRIVERSTATEDATA pdata
);
```



## Parameters

<dl> <dt>

*pdata* \[in, out\]
</dt> <dd>

Pointer to a [**DD\_GETDRIVERSTATEDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_getdriverstatedata) structure that describes the state of the driver.

</dd> </dl>

## Return value

**NtGdiD3DGetDriverState** returns one of the following callback codes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDHAL\_DRIVER\_HANDLED**</dt> </dl>    | The driver has performed the operation and returned a valid return code for that operation. If this code is DD\_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function.<br/>                                                                                 |
| <dl> <dt>**DDHAL\_DRIVER\_NOTHANDLED**</dt> </dl> | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Ntgdi.h</dt> </dl> |



## See also

<dl> <dt>

[Graphics Low Level Client Support](-dxgkernel-low-level-client-support.md)
</dt> </dl>

 

 
