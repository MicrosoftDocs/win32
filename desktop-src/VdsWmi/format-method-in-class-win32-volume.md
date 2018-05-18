---
title: Format method of the Win32\_Volume class
description: The Format method formats the volume.This topic uses Managed Object Format (MOF) syntax.
ms.assetid: 'b8c325d7-3d78-4989-8209-2dad359ca9bb'
keywords: ["Format method", "Format method, Win32_Volume class", "Win32_Volume class, Format method"]
topic_type:
- apiref
api_name:
- Win32_Volume.Format
api_location:
- Vdswmi.dll
api_type:
- COM
---

# Format method of the Win32\_Volume class

The **Format** method formats the volume.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832). The **Format** method, like the [**Defrag**](defrag-method-in-class-win32-volume.md) method, can run for a very long time. These methods are normally called asynchronously. If your code cancels the call by calling [**IWbemServices::CancelAsyncCall**](https://msdn.microsoft.com/library/aa392094) (or [**SWbemSink.Cancel**](https://msdn.microsoft.com/library/aa393878) in script or Visual Basic), then the provider is not notified and the operation continues to completion.

## Syntax


```mof
uint32 Format(
  [in] string FileSystem = "NTFS",
  [in] boolean QuickFormat,
  [in] uint32 ClusterSize = 4096,
  [in] string Label = "",
  [in] boolean EnableCompression = false
);
```



## Parameters

<dl> <dt>

*FileSystem* \[in\]
</dt> <dd>

File system format to use for this volume. The default is "NTFS".

The following list identifies the possible values for this parameter.

"NTFS"

"FAT32"

"FAT"

</dd> <dt>

*QuickFormat* \[in\]
</dt> <dd>

If **true**, formats the volume with a quick format by removing files from the disk without scanning the disk for bad sectors. Use this option only if the disk has been previously formatted, and you know that the disk is not damaged. The default is **false**.

</dd> <dt>

*ClusterSize* \[in\]
</dt> <dd>

Disk allocation unit size—cluster size. All of the file systems used by this version of Windows organize the hard disk based on cluster size, which represents the smallest amount of disk space that can be allocated to hold a file. The smaller the cluster size you use, the more efficiently your disk stores information. If no cluster size is specified during format, Windows picks defaults based on the size of the volume. These defaults have been selected to reduce the amount of space lost and to reduce fragmentation. For general use, the default settings are strongly recommended.

</dd> <dt>

*Label* \[in\]
</dt> <dd>

Label to use for the new volume. The volume label can contain up to 11 characters for FAT and FAT32 volumes, and up to 32 characters for NTFS file system volumes.

</dd> <dt>

*EnableCompression* \[in\]
</dt> <dd>

Not implemented.

</dd> </dl>

## Return value



| Return code                                                                       | Description                                   |
|-----------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**0**</dt> </dl>  | Success<br/>                            |
| <dl> <dt>**1**</dt> </dl>  | Unsupported file system<br/>            |
| <dl> <dt>**2**</dt> </dl>  | Incompatible media in drive<br/>        |
| <dl> <dt>**3**</dt> </dl>  | Access denied<br/>                      |
| <dl> <dt>**4**</dt> </dl>  | Call canceled<br/>                      |
| <dl> <dt>**5**</dt> </dl>  | Call cancellation request too late<br/> |
| <dl> <dt>**6**</dt> </dl>  | Volume write protected<br/>             |
| <dl> <dt>**7**</dt> </dl>  | Volume lock failed<br/>                 |
| <dl> <dt>**8**</dt> </dl>  | Unable to quick format<br/>             |
| <dl> <dt>**9**</dt> </dl>  | Input/Output (I/O) error<br/>           |
| <dl> <dt>**10**</dt> </dl> | Invalid volume label<br/>               |
| <dl> <dt>**11**</dt> </dl> | No media in drive<br/>                  |
| <dl> <dt>**12**</dt> </dl> | Volume is too small<br/>                |
| <dl> <dt>**13**</dt> </dl> | Volume is too large<br/>                |
| <dl> <dt>**14**</dt> </dl> | Volume is not mounted<br/>              |
| <dl> <dt>**15**</dt> </dl> | Cluster size is too small<br/>          |
| <dl> <dt>**16**</dt> </dl> | Cluster size is too large<br/>          |
| <dl> <dt>**17**</dt> </dl> | Cluster size is beyond 32 bits<br/>     |
| <dl> <dt>**18**</dt> </dl> | Unknown error<br/>                      |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vds.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vdswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Volume**](win32-volume.md)
</dt> </dl>

 

 





