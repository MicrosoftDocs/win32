---
title: BFT Constants (Ntdsbcli.h)
description: The BFT constants are used as bit flags to identify different file types in an Active Directory Domain Services backup.
ms.assetid: 3658a657-d9e3-4fbf-9120-4b0205b81a36
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- BFT_LOG_DIRECTORY
- BFT_DATABASE_DIRECTORY
- BFT_DIRECTORY
- BFT_LOG
- BFT_LOG_DIR
- BFT_CHECKPOINT_DIR
- BFT_NTDS_DATABASE
- BFT_PATCH_FILE
- BFT_UNKNOWN
api_location:
- Ntdsbcli.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BFT Constants

The BFT constants are used as bit flags to identify different file types in an Active Directory Domain Services backup.

<dl> <dt>

<span id="BFT_LOG_DIRECTORY"></span><span id="bft_log_directory"></span>**BFT\_LOG\_DIRECTORY**
</dt> <dd> <dl> <dt>

0x20
</dt> <dt>



The file belongs in the log directory.


</dt> </dl> </dd> <dt>

<span id="BFT_DATABASE_DIRECTORY"></span><span id="bft_database_directory"></span>**BFT\_DATABASE\_DIRECTORY**
</dt> <dd> <dl> <dt>

0x40
</dt> <dt>



The file belongs in the database directory.


</dt> </dl> </dd> <dt>

<span id="BFT_DIRECTORY"></span><span id="bft_directory"></span>**BFT\_DIRECTORY**
</dt> <dd> <dl> <dt>

0x80
</dt> <dt>



The path specified is a directory and not a file name.


</dt> </dl> </dd> <dt>

<span id="BFT_LOG"></span><span id="bft_log"></span>**BFT\_LOG**
</dt> <dd> <dl> <dt>

0x21
</dt> <dt>



Specifies a log file that belongs in the log directory.


</dt> </dl> </dd> <dt>

<span id="BFT_LOG_DIR"></span><span id="bft_log_dir"></span>**BFT\_LOG\_DIR**
</dt> <dd> <dl> <dt>

0x22
</dt> <dt>



The file is the path of the log directory.


</dt> </dl> </dd> <dt>

<span id="BFT_CHECKPOINT_DIR"></span><span id="bft_checkpoint_dir"></span>**BFT\_CHECKPOINT\_DIR**
</dt> <dd> <dl> <dt>

0x23
</dt> <dt>



The file is the path of the checkpoint directory.


</dt> </dl> </dd> <dt>

<span id="BFT_NTDS_DATABASE"></span><span id="bft_ntds_database"></span>**BFT\_NTDS\_DATABASE**
</dt> <dd> <dl> <dt>

0x44
</dt> <dt>



The file is a directory service database that belongs in the database directory.


</dt> </dl> </dd> <dt>

<span id="BFT_PATCH_FILE"></span><span id="bft_patch_file"></span>**BFT\_PATCH\_FILE**
</dt> <dd> <dl> <dt>

0x25
</dt> <dt>



The file is a patch file that belongs in the log directory.


</dt> </dl> </dd> <dt>

<span id="BFT_UNKNOWN"></span><span id="bft_unknown"></span>**BFT\_UNKNOWN**
</dt> <dd> <dl> <dt>

0x0F
</dt> <dt>



The file cannot be recognized. The file does not coincide with the known file names and file types.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl> |



 

 





