---
Description: 'Resource statistics gathered by the D3DDEVINFO\_ResourceManager when using the asynchronous query mechanism.'
ms.assetid: 'f4d9c6db-4002-439c-9a88-485763badc82'
title: D3DRESOURCESTATS structure
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

Type: **[**BOOL**](winprog.windows_data_types)**

</dd> <dd>

Indicates if thrashing is occurring.

</dd> <dt>

**ApproxBytesDownloaded**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Approximate number of bytes downloaded by the resource manager.

</dd> <dt>

**NumEvicts**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Number of objects evicted.

</dd> <dt>

**NumVidCreates**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Number of objects created in video memory.

</dd> <dt>

**LastPri**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Priority of last object evicted.

</dd> <dt>

**NumUsed**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Number of objects set to the device.

</dd> <dt>

**NumUsedInVidMem**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Number of objects set to the device, which are already in video memory.

</dd> <dt>

**WorkingSet**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Number of objects in video memory.

</dd> <dt>

**WorkingSetBytes**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Number of bytes in video memory.

</dd> <dt>

**TotalManaged**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

</dd> <dd>

Total number of managed objects.

</dd> <dt>

**TotalBytes**
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

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

 

 




