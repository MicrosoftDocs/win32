---
title: Mount method of the MSFT\_DiskImage class
description: Mounts the disk image.
ms.assetid: CD233786-8087-4093-834B-096FE2ADBEB1
keywords:
- Mount method Windows Storage Management API
- Mount method Windows Storage Management API , MSFT_DiskImage class
- MSFT_DiskImage class Windows Storage Management API , Mount method
topic_type:
- apiref
api_name:
- MSFT_DiskImage.Mount
api_location:
- vds.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Mount method of the MSFT\_DiskImage class

Mounts the disk image.

## Syntax


```mof
UInt32 Mount(
  [in] UInt16  Access,
  [in] Boolean NoDriveLetter
);
```



## Parameters

<dl> <dt>

*Access* \[in\]
</dt> <dd>

The access for the disk image.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>**Read Write** (2)
</dt> <dt>

<span id="Read-Only"></span><span id="read-only"></span><span id="READ-ONLY"></span>**Read-Only** (3)
</dt> </dl> </dd> <dt>

*NoDriveLetter* \[in\]
</dt> <dd>

If **TRUE**, the disk image shouldn't be assigned a drive letter.

</dd> </dl>

## Return value

If *Access* is not **DEVICE\_ACCESS\_READ\_ONLY** or **DEVICE\_ACCESS\_READ\_WRITE**, this method returns **E\_INVALIDARG**.

Otherwise, this method returns [**OpenVirtualDisk**](https://msdn.microsoft.com/library/windows/desktop/dd323680) and [**AttachVirtualDisk**](https://msdn.microsoft.com/library/windows/desktop/dd323692) error codes converted to **HRESULT** codes.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| Header<br/>                   | <dl> <dt>Vds.h</dt> </dl>          |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DiskImage**](msft-diskimage.md)
</dt> </dl>

 

 





