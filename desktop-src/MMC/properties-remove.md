---
title: Properties Remove method
description: The Remove method removes the specified property from the collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7d5b605c-bdf0-4418-9ef0-4e6643f074e0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Remove method MMC
- Remove method MMC , Properties object
- Properties object MMC , Remove method
- Remove method MMC , Properties interface
- Properties interface MMC , Remove method
topic_type:
- apiref
api_name:
- Properties.Remove
- Properties.Remove
api_location:
- Mmcndmgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Properties::Remove method

The **Remove** method removes the specified property from the collection.

## Syntax


```VB
Properties.Remove( _
  ByVal Name As String _
)
```



## Parameters

<dl> <dt>

*Name* 
</dt> <dd>

The name of the property removed from this collection.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Properties is defined as 2886ABC2-A425-42b2-91C6-E25C0E04581C<br/>           |



## See also

<dl> <dt>

[**Property object**](property-object.md)
</dt> </dl>

 

 





