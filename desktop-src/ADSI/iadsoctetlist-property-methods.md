---
title: IADsOctetList Property Methods
description: The property method of the IADsOctetList interface sets the property described in the following table. For more information, see Interface Property Methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '6fe29a0d-dd53-4cc2-8152-22a0a2756c2c'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["IADsOctetList Property Methods ADSI"]
topic_type:
- apiref
api_name:
- IADsOctetList Property Methods
- IADsOctetList.OctetList
- IADsOctetList.get_OctetList
- IADsOctetList.put_OctetList
api_location:
- Activeds.dll
api_type:
- COM
---

# IADsOctetList Property Methods

The property method of the [**IADsOctetList**](iadsoctetlist.md) interface sets the property described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**OctetList**
</dt> <dd> <dl>

An ordered sequence of byte arrays.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_OctetList(
  [out] VARIANT* retVal
);
HRESULT put_OctetList(
  [in] VARIANT vOctetList
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADsOctetList is defined as 7B28B80F-4680-11D1-A3B4-00C04FB950DC<br/>        |



## See also

<dl> <dt>

[**IADsOctetList**](iadsoctetlist.md)
</dt> <dt>

[**ADS\_OCTET\_LIST**](ads-octet-list.md)
</dt> </dl>

 

 





