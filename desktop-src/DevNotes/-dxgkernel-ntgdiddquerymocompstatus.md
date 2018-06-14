---
Description: Queries the status of the most recent rendering operation to the specified surface.
ms.assetid: bc7f8f84-119e-4c09-87f5-6b122e9f9821
title: NtGdiDdQueryMoCompStatus function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NtGdiDdQueryMoCompStatus function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Queries the status of the most recent rendering operation to the specified surface.

## Syntax


```C++
DWORD APIENTRY NtGdiDdQueryMoCompStatus(
  _In_    HANDLE                    hMoComp,
  _Inout_ PDD_QUERYMOCOMPSTATUSDATA puQueryMoCompStatusData
);
```



## Parameters

<dl> <dt>

*hMoComp* \[in\]
</dt> <dd>

Pointer to a [**DD\_MOTIONCOMP\_LOCAL**](https://msdn.microsoft.com/en-us/library/Ff551663(v=VS.85).aspx) structure that contains a description of the motion compensation being requested.

</dd> <dt>

*puQueryMoCompStatusData* \[in, out\]
</dt> <dd>

Pointer to a [**DD\_QUERYMOCOMPSTATUSDATA**](https://msdn.microsoft.com/en-us/library/Ff551691(v=VS.85).aspx) structure that contains the information needed to query the status.

</dd> </dl>

## Return value

**NtGdiDdQueryMoCompStatus** returns one of the following callback codes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDHAL\_DRIVER\_HANDLED**</dt> </dl>    | The driver has performed the operation and returned a valid return code for that operation. If this code is DD\_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function.<br/>                                                                                 |
| <dl> <dt>**DDHAL\_DRIVER\_NOTHANDLED**</dt> </dl> | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation.<br/> |



 

## Remarks

For more information, see the Microsoft DirectX Video Acceleration Driver Development Kit (DDK).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Ntgdi.h</dt> </dl> |



## See also

<dl> <dt>

[Graphics Low Level Client Support](-dxgkernel-low-level-client-support.md)
</dt> </dl>

 

 




