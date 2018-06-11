---
Description: Returns the number of the current physical scan line.
ms.assetid: 159d5ea0-25b8-4c2d-9cd4-cf4ee0ca0561
title: NtGdiDdGetScanLine function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NtGdiDdGetScanLine function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Returns the number of the current physical scan line.

## Syntax


```C++
DWORD APIENTRY NtGdiDdGetScanLine(
  _In_    HANDLE              hDirectDraw,
  _Inout_ PDD_GETSCANLINEDATA puGetScanLineData
);
```



## Parameters

<dl> <dt>

*hDirectDraw* \[in\]
</dt> <dd>

Handle to a [**DD\_DIRECTDRAW\_GLOBAL**](https://msdn.microsoft.com/windows/desktop/a59f064b-48cf-4491-82cd-84f59467af87) structure that represents the driver.

</dd> <dt>

*puGetScanLineData* \[in, out\]
</dt> <dd>

Pointer to a [**DD\_GETSCANLINEDATA**](https://msdn.microsoft.com/windows/desktop/92433daa-43da-40d3-a319-e0d70abd3cb0) structure in which the driver returns the number of the current scan line.

</dd> </dl>

## Return value

**NtGdiDdGetScanLine** returns one of the following callback codes.



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDHAL\_DRIVER\_HANDLED**</dt> </dl>    | The driver has performed the operation and returned a valid return code for that operation. If this code is DD\_OK, DirectDraw or Direct3D proceeds with the function. Otherwise, DirectDraw or Direct3D returns the error code provided by the driver and aborts the function.<br/>                                                                                 |
| <dl> <dt>**DDHAL\_DRIVER\_NOTHANDLED**</dt> </dl> | The driver has no comment on the requested operation. If the driver is required to have implemented a particular callback, DirectDraw or Direct3D reports an error condition. Otherwise, DirectDraw or Direct3D handles the operation as if the driver callback had not been defined by executing the DirectDraw or Direct3D device-independent implementation.<br/> |



 

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

 

 




