---
title: MSFT\_FileServerToFileShare class
description: Association between a MSFT\_FileServer and its MSFT\_FileShare objects.
ms.assetid: '9A76E1EA-50B1-49F2-8B0D-BB444CC89188'
keywords: ["MSFT_FileServerToFileShare class Windows Storage Management API", "MSFT_FileServerToFileShare class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_FileServerToFileShare
- MSFT_FileServerToFileShare.FileServer
- MSFT_FileServerToFileShare.FileShare
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_FileServerToFileShare class

Association between a [**MSFT\_FileServer**](msft-fileserver.md) and its [**MSFT\_FileShare**](msft-fileshare.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_FileServerToFileShare
{
  MSFT_FileServer REF FileServer;
  MSFT_FileShare  REF FileShare;
};
```

## Members

The **MSFT\_FileServerToFileShare** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FileServerToFileShare** class has these properties.

<dl> <dt>

**FileServer**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_FileServer**](msft-fileserver.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**FileShare**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_FileShare**](msft-fileshare.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_FileServer**](msft-fileserver.md)
</dt> <dt>

[**MSFT\_FileShare**](msft-fileshare.md)
</dt> </dl>

 

 





