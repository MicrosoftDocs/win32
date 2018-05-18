---
Description: 'Creates a kernel-side representation of the Microsoft DirectDraw object.'
ms.assetid: 'e380f948-35a0-4cf0-9b69-ab2bd4f9a161'
title: NtGdiDdCreateDirectDrawObject function
---

# NtGdiDdCreateDirectDrawObject function

\[This function is subject to change with each operating system revision. Instead, use the DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Creates a kernel-side representation of the Microsoft DirectDraw object.

## Syntax


```C++
HANDLE APIENTRY NtGdiDdCreateDirectDrawObject(
  _In_ HDC hdc
);
```



## Parameters

<dl> <dt>

*hdc* \[in\]
</dt> <dd>

Any DC display device for which the DirectDraw object should be created.

</dd> </dl>

## Return value

If successful, this function returns a handle to the kernel-mode object representation; otherwise it returns **NULL**.

## Remarks

Applications are advised to use the DirectDraw and [Direct3D](http://msdn.microsoft.com/en-us/library/bb205147(VS.85).aspx) APIs to create and manage graphics device objects. These constructs abstract the device creation process in a simplified and operating-system-independent way.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Ntgdi.h</dt> </dl> |



## See also

<dl> <dt>

[Graphics Low Level Client Support](-dxgkernel-low-level-client-support.md)
</dt> <dt>

[**DdCreateDirectDrawObject**](-dxgkernel-ddcreatedirectdrawobject.md)
</dt> </dl>

 

 




