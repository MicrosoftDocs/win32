---
Description: Notifies the driver that this motion compensation object will no longer be used. The driver now needs to perform any necessary cleanup.
ms.assetid: 1d86a564-efe1-4971-99ec-2c9a6aa59c89
title: NtGdiDdDestroyMoComp function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NtGdiDdDestroyMoComp function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Notifies the driver that this motion compensation object will no longer be used. The driver now needs to perform any necessary cleanup.

## Syntax


```C++
DWORD APIENTRY NtGdiDdDestroyMoComp(
  _In_    HANDLE                hMoComp,
  _Inout_ PDD_DESTROYMOCOMPDATA puBeginFrameData
);
```



## Parameters

<dl> <dt>

*hMoComp* \[in\]
</dt> <dd>

Handle to a [**DD\_MOTIONCOMP\_LOCAL**](ddstrcts_cc4890b6-b2b6-484c-b979-4627fa902d7d.xml) structure that contains a description of the motion compensation object to be destroyed.

</dd> <dt>

*puBeginFrameData* \[in, out\]
</dt> <dd>

Pointer to a [**DD\_DESTROYMOCOMPDATA**](ddstrcts_1a3d548c-c0f7-4334-b0c6-b63c155d854c.xml) structure that contains the information needed to finish motion compensation.

</dd> </dl>

## Return value

**NtGdiDdDestroyMoComp** returns one of the following callback codes.



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

 

 




