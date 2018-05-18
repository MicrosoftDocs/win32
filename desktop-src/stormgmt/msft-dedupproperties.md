---
title: MSFT\_DedupProperties class
description: Volume deduplication properties.
ms.assetid: 'BE95BD75-F45E-494B-9091-558815543801'
keywords: ["MSFT_DedupProperties class Windows Storage Management API", "MSFT_DedupProperties class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_DedupProperties
- MSFT_DedupProperties.UnoptimizedSize
- MSFT_DedupProperties.SavingsSize
- MSFT_DedupProperties.SavingsRate
- MSFT_DedupProperties.OptimizedFilesCount
- MSFT_DedupProperties.OptimizedFilesSize
- MSFT_DedupProperties.OptimizedFilesSavingsRate
- MSFT_DedupProperties.InPolicyFilesCount
- MSFT_DedupProperties.InPolicyFilesSize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_DedupProperties class

Volume deduplication properties.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_DedupProperties
{
  UInt64 UnoptimizedSize;
  UInt64 SavingsSize;
  UInt32 SavingsRate;
  UInt64 OptimizedFilesCount;
  UInt64 OptimizedFilesSize;
  UInt32 OptimizedFilesSavingsRate;
  UInt64 InPolicyFilesCount;
  UInt64 InPolicyFilesSize;
};
```

## Members

The **MSFT\_DedupProperties** class has these types of members:

-   [Properties](#msft-dedupproperties-class)

### Properties

The **MSFT\_DedupProperties** class has these properties.

<dl> <dt>

**InPolicyFilesCount**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of files that currently qualify for optimization.

</dd> <dt>

**InPolicyFilesSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The aggregate size of all files that currently qualify for optimization.

</dd> <dt>

**OptimizedFilesCount**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of optimized files on the volume.

</dd> <dt>

**OptimizedFilesSavingsRate**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ratio of deduplication savings to the logical size of all optimized files on the volume, expressed as a percentage.

</dd> <dt>

**OptimizedFilesSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total logical size of all optimized files on the volume, in bytes.

</dd> <dt>

**SavingsRate**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ratio of deduplication savings to the logical size of all of the files on the volume, expressed as a percentage.

</dd> <dt>

**SavingsSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The difference between the logical size of the optimized files and the logical size of the store (the deduplicated user data plus deduplication metadata).

</dd> <dt>

**UnoptimizedSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total logical size of all files on the volume, in bytes. This is an estimate of the volume's used space if the deduplication feature were disabled.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





