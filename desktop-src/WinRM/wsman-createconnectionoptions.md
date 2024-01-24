---
title: WSMan.CreateConnectionOptions method (WSManDisp.h)
description: Creates a ConnectionOptions object that specifies the user name and password used when creating a session.
ms.assetid: 3669a5fe-8305-4fa3-aa75-fafefcd8b33d
ms.tgt_platform: multiple
keywords:
- CreateConnectionOptions method Windows Remote Management
- CreateConnectionOptions method Windows Remote Management , WSMan object
- WSMan object Windows Remote Management , CreateConnectionOptions method
topic_type:
- apiref
api_name:
- WSMan.CreateConnectionOptions
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WSMan.CreateConnectionOptions method

Creates a [**ConnectionOptions**](connectionoptions.md) object that specifies the user name and password used when creating a session.

## Syntax


```VB
WSMan.CreateConnectionOptions()
```



## Parameters

This method has no parameters.

## Return value

A [**ConnectionOptions**](connectionoptions.md) object used to specify a user name and password pair that is used to identify a user for authentication.

## Remarks

The following syntax is used to call this method.


```VB
Set options = wsman.CreateConnectionOptions
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**WSMan**](wsman.md)
</dt> <dt>

[**ConnectionOptions**](connectionoptions.md)
</dt> </dl>

 

 





