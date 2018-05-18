---
title: PSGUID\_STORAGE
description: PSGUID\_STORAGE
ms.assetid: '6c095e28-ca06-43b1-8d3a-b481e8417625'
keywords: ["PSGUID_STORAGE"]
---

# PSGUID\_STORAGE

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The PSGUID\_STORAGE property set defines storage properties found for files in a file system.

``` syntax
#define PSGUID_STORAGE \
    { 0xb725f130, 0x47ef, 0x101a, \
        { 0xa5, 0xf1, 0x02, 0x60, 0x8c, 0x9e, 0xeb, 0xac } }
```

### Remarks

The PSGUID\_STORAGE property set contains the following property constants:

<dl> <dt>

<span id="PID_STG_DIRECTORY"></span><span id="pid_stg_directory"></span>PID\_STG\_DIRECTORY
</dt> <dd>

Property ID 2. The directory in which a file is located. Default type is VT\_LPWSTR. The Indexing Service friendly name is "directory".

</dd> <dt>

<span id="PID_STG_CLASSID"></span><span id="pid_stg_classid"></span>PID\_STG\_CLASSID
</dt> <dd>

Property ID 3. CLID of a file. Default type is VT\_CLSID. The Indexing Service friendly name is "classid".

</dd> <dt>

<span id="PID_STG_STORAGETYPE"></span><span id="pid_stg_storagetype"></span>PID\_STG\_STORAGETYPE
</dt> <dd>

Property ID 4. Storage type for this file.

</dd> <dt>

<span id="PID_STG_VOLUME_ID"></span><span id="pid_stg_volume_id"></span>PID\_STG\_VOLUME\_ID
</dt> <dd>

Property ID 5. Volume ID of the disk.

</dd> <dt>

<span id="PID_STG_PARENT_WORKID"></span><span id="pid_stg_parent_workid"></span>PID\_STG\_PARENT\_WORKID
</dt> <dd>

Property ID 6. Internal work ID for the parent or folder for this file.

</dd> <dt>

<span id="PID_STG_SECONDARYSTORE"></span><span id="pid_stg_secondarystore"></span>PID\_STG\_SECONDARYSTORE
</dt> <dd>

Property ID 7. Whether the file has been placed in secondary storage.

</dd> <dt>

<span id="PID_STG_FILEINDEX"></span><span id="pid_stg_fileindex"></span>PID\_STG\_FILEINDEX
</dt> <dd>

Property ID 8. Internal file index for this file.

</dd> <dt>

<span id="PID_STG_LASTCHANGEUSN"></span><span id="pid_stg_lastchangeusn"></span>PID\_STG\_LASTCHANGEUSN
</dt> <dd>

Property ID 9. Last change Update Sequence Number (USN) for this file.

</dd> <dt>

<span id="PID_STG_NAME"></span><span id="pid_stg_name"></span>PID\_STG\_NAME
</dt> <dd>

Property ID 0x0a. The name of the file. Default type is VT\_LPWSTR. The Indexing Service friendly name is "filename".

</dd> <dt>

<span id="PID_STG_PATH"></span><span id="pid_stg_path"></span>PID\_STG\_PATH
</dt> <dd>

Property ID 0x0b. The complete path for a file. Default type is VT\_LPWSTR. The Indexing Service friendly name is "path".

</dd> <dt>

<span id="PID_STG_SIZE"></span><span id="pid_stg_size"></span>PID\_STG\_SIZE
</dt> <dd>

Property ID 0x0c. The size of a file. Default type is VT\_I8. The Indexing Service friendly name is "size".

</dd> <dt>

<span id="PID_STG_ATTRIBUTES"></span><span id="pid_stg_attributes"></span>PID\_STG\_ATTRIBUTES
</dt> <dd>

Property ID 0x0d. The attribute flags for a file. Default type is VT\_UI4. The Indexing Service friendly name is "attrib".

</dd> <dt>

<span id="PID_STG_WRITETIME"></span><span id="pid_stg_writetime"></span>PID\_STG\_WRITETIME
</dt> <dd>

Property ID 0x0e. The date and time of the last write to the file. Default type is VT\_FILETIME. The Indexing Service friendly name is "write".

</dd> <dt>

<span id="PID_STG_CREATETIME"></span><span id="pid_stg_createtime"></span>PID\_STG\_CREATETIME
</dt> <dd>

Property ID 0x0f. The date and time the file was created. Default type is VT\_FILETIME. The Indexing Service friendly name is "create".

</dd> <dt>

<span id="PID_STG_ACCESSTIME"></span><span id="pid_stg_accesstime"></span>PID\_STG\_ACCESSTIME
</dt> <dd>

Property ID 0x10.The time of the last access to the file. Default type is VT\_FILETIME. The Indexing Service friendly name is "access".

</dd> <dt>

<span id="PID_STG_CHANGETIME"></span><span id="pid_stg_changetime"></span>PID\_STG\_CHANGETIME
</dt> <dd>

Property ID 0x11.The time of the last change to a file in an NTFS file system, including changes in the main data stream and secondary streams. Default type is VT\_FILETIME. The Indexing Service friendly name is "change".

</dd> <dt>

<span id="PID_STG_ALLOCSIZE"></span><span id="pid_stg_allocsize"></span>PID\_STG\_ALLOCSIZE
</dt> <dd>

Property ID 0x12. File allocation size.

</dd> <dt>

<span id="PID_STG_CONTENTS"></span><span id="pid_stg_contents"></span>PID\_STG\_CONTENTS
</dt> <dd>

Property ID 0x13. The contents of the file. This property is for query restrictions only; it cannot be retrieved in a query result. Default type is VT\_LPWSTR. The Indexing Service friendly name is "contents".

</dd> <dt>

<span id="PID_STG_SHORTNAME"></span><span id="pid_stg_shortname"></span>PID\_STG\_SHORTNAME
</dt> <dd>

Property ID 0x14. The short (8.3) file name for the file. Default type is VT\_LPWSTR. The Indexing Service friendly name is "shortname".

</dd> <dt>

<span id="PID_STG_MAX"></span><span id="pid_stg_max"></span>PID\_STG\_MAX
</dt> <dd>

Property ID 0x14. Identifies the last PID\_STG constant assigned.

</dd> </dl>

## Related topics

<dl> <dt>

[OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md)
</dt> </dl>

 

 




