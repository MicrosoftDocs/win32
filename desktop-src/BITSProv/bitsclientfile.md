---
title: BitsClientFile class
description: The BitsClientFile class provides information about a file for a BITS transfer job.
ms.assetid: f32acff8-3d8f-4cec-aba1-182ad73f33cd
keywords:
- BitsClientFile class
- BitsClientFile class, described
topic_type:
- apiref
api_name:
- BitsClientFile
- BitsClientFile.RemoteUrl
- BitsClientFile.LocalFile
- BitsClientFile.BytesTotal
- BitsClientFile.BytesTransferred
- BitsClientFile.Completed
api_location:
- Root\microsoft\bits
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BitsClientFile class

The **BitsClientFile** class provides information about a file for a BITS transfer job.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class BitsClientFile
{
  string  RemoteUrl;
  string  LocalFile;
  uint64  BytesTotal;
  uint64  BytesTransferred;
  boolean Completed;
};
```

## Members

The **BitsClientFile** class has these types of members:

-   [Properties](#properties)

### Properties

The **BitsClientFile** class has these properties.

<dl> <dt>

**BytesTotal**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the total number of bytes to transfer for the file.

</dd> <dt>

**BytesTransferred**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the number of bytes that were transferred for the file.

</dd> <dt>

**Completed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the file was transferred successfully.

</dd> <dt>

**LocalFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property specifies the name of local file.

</dd> <dt>

**RemoteUrl**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property defines the remote URL for the file transfer.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



 

 





