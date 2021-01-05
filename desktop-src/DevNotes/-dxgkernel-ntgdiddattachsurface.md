---
description: Attaches two kernel-mode surface representations.
ms.assetid: f1b1859f-8b62-4385-9e8a-296086446fe7
title: NtGdiDdAttachSurface function (Ntgdi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtGdiDdAttachSurface
api_type: 
- DllExport
api_location: 
- Ntgdi.h
- Ext-MS-Win-GDI-Internal-Desktop-L1-1-0.dll
- GDI32.dll
- GDI32Full.dll
---

# NtGdiDdAttachSurface function

\[This function is subject to change with each operating system revision. Instead, use the Microsoft DirectDraw and Microsoft Direct3DAPIs; these APIs insulate applications from such operating system changes, and hide many other difficulties involved in interacting directly with display drivers.\]

Attaches two kernel-mode surface representations.

## Syntax


```C++
BOOL APIENTRY NtGdiDdAttachSurface(
  _In_ HANDLE hSurfaceFrom,
  _In_ HANDLE hSurfaceTo
);
```



## Parameters

<dl> <dt>

*hSurfaceFrom* \[in\]
</dt> <dd>

Handle to kernel-mode surface object that will be the start point of the new attachment.

</dd> <dt>

*hSurfaceTo* \[in\]
</dt> <dd>

Handle to kernel-mode surface object that will be the end point of the new attachment.

</dd> </dl>

## Return value

**NtGdiDdAttachSurface** returns one of the following:



| Return code                                                                          | Description                             |
|--------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | The function call succeeded.<br/> |
| <dl> <dt>**FALSE**</dt> </dl> | The function call failed.<br/>    |



 

## Remarks

See the DirectDraw  software development kit (SDK) and Driver Development Kit (DDK) for a full description of surface attachments.

> [!Note]  
> As with other surface attachments, the resulting attachment is one-way. After this function is called, *hSurfaceTo* will not be attached to *hSurfaceFrom*.

 

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

 

 




