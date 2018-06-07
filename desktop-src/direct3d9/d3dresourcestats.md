---
Description: Resource statistics gathered by the D3DDEVINFO\_ResourceManager when using the asynchronous query mechanism.
ms.assetid: f4d9c6db-4002-439c-9a88-485763badc82
title: D3DRESOURCESTATS structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# D3DRESOURCESTATS structure

Resource statistics gathered by the [**D3DDEVINFO\_ResourceManager**](d3ddevinfo-resourcemanager.md) when using the asynchronous query mechanism.

## Syntax


```C++
typedef struct D3DRESOURCESTATS {
  BOOL  bThrashing;
  DWORD ApproxBytesDownloaded;
  DWORD NumEvicts;
  DWORD NumVidCreates;
  DWORD LastPri;
  DWORD NumUsed;
  DWORD NumUsedInVidMem;
  DWORD WorkingSet;
  DWORD WorkingSetBytes;
  DWORD TotalManaged;
  DWORD TotalBytes;
} D3DRESOURCESTATS, *LPD3DRESOURCESTATS;
```



## Members

<dl> <dt>

**bThrashing**
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Indicates if thrashing is occurring.

</dd> <dt>

**ApproxBytesDownloaded**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Approximate number of bytes downloaded by the resource manager.

</dd> <dt>

**NumEvicts**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Number of objects evicted.

</dd> <dt>

**NumVidCreates**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Number of objects created in video memory.

</dd> <dt>

**LastPri**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Priority of last object evicted.

</dd> <dt>

**NumUsed**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Number of objects set to the device.

</dd> <dt>

**NumUsedInVidMem**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Number of objects set to the device, which are already in video memory.

</dd> <dt>

**WorkingSet**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Number of objects in video memory.

</dd> <dt>

**WorkingSetBytes**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Number of bytes in video memory.

</dd> <dt>

**TotalManaged**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Total number of managed objects.

</dd> <dt>

**TotalBytes**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

</dd> <dd>

Total number of bytes of managed objects.

</dd> </dl>

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> <dt>

[Asynchronous Notification (Direct3D 9)](asynchronous-notification.md)
</dt> </dl>

 

 




