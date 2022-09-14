---
description: Represents the type of path being used as an argument.
ms.assetid: f308c638-b383-432e-9dd3-edc33b792139
title: PATH_TYPE enumeration
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PATH_TYPE
api_type: 
- NA
api_location: 
---

# PATH\_TYPE enumeration

Represents the type of path being used as an argument.

## Syntax


```C++
typedef enum _PATH_TYPE { 
  DOS_PATH,
  NT_PATH
} PATH_TYPE;
```



## Constants

<dl> <dt>

<span id="DOS_PATH"></span><span id="dos_path"></span>**DOS\_PATH**
</dt> <dd>

Standard path.

</dd> <dt>

<span id="NT_PATH"></span><span id="nt_path"></span>**NT\_PATH**
</dt> <dd>

Internal path.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SdbCreateDatabase**](sdbcreatedatabase.md)
</dt> <dt>

[**SdbOpenDatabase**](sdbopendatabase.md)
</dt> </dl>

 

 




