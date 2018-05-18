---
title: Properties Item method
description: The Item method returns the Property object specified by the name of the property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'eec98db9-5774-4749-9121-8c7a2ef4341a'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Item method MMC", "Item method MMC , Properties object", "Properties object MMC , Item method", "Item method MMC , Properties interface", "Properties interface MMC , Item method"]
topic_type:
- apiref
api_name:
- Properties.Item
- Properties.Item
api_location:
- Mmcndmgr.dll
api_type:
- COM
---

# Properties::Item method

The **Item** method returns the [**Property object**](property-object.md) specified by the name of the property.

## Syntax


```VB
Properties.Item( _
  ByVal Name As String _
) As Property
```



## Parameters

<dl> <dt>

*Name* 
</dt> <dd>

The name of the [**Property**](property-object.md) being retrieved.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Properties is defined as 2886ABC2-A425-42b2-91C6-E25C0E04581C<br/>           |



## See also

<dl> <dt>

[**Property object**](property-object.md)
</dt> <dt>

[**Properties.Count**](properties-count.md)
</dt> </dl>

 

 





