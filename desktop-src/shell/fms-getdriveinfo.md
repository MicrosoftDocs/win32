---
description: Contains information about the drive selected in the active File Manager window (the directory window or the Search Results window).
title: FMS_GETDRIVEINFO structure (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FMS_GETDRIVEINFO
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: 14f8a90b-d0ed-4818-a719-8fc4ea617bef

---

# FMS\_GETDRIVEINFO structure

Contains information about the drive selected in the active File Manager window (the directory window or the Search Results window).

## Syntax


```C++
typedef struct _FMS_GETDRIVEINFO {
  DWORD dwTotalSpace;
  DWORD dwFreeSpace;
  TCHAR szPath[260];
  TCHAR szVolume[14];
  TCHAR szShare[128];
} FMS_GETDRIVEINFO;
```



## Members

<dl> <dt>

**dwTotalSpace**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The total amount of storage space, in bytes, on the disk associated with the drive.

</dd> <dt>

**dwFreeSpace**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

The amount of free storage space, in bytes, on the disk associated with the drive.

</dd> <dt>

**szPath**
</dt> <dd>

Type: **TCHAR\[260\]**

</dd> <dd>

the null-terminated path of the current directory.

</dd> <dt>

**szVolume**
</dt> <dd>

Type: **TCHAR\[14\]**

</dd> <dd>

The null-terminated volume label of the disk associated with the drive.

</dd> <dt>

**szShare**
</dt> <dd>

Type: **TCHAR\[128\]**

</dd> <dd>

The null-terminated name of the network resource (if the drive is being accessed through a network).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMExtensionProc**](fmextensionproc.md)
</dt> <dt>

[**FM\_GETDRIVEINFO**](fm-getdriveinfo.md)
</dt> </dl>

 

 




