---
title: IADsEmail Property Methods
description: The property method of the IADsEmail interface sets the property described in the following table. For more information, see Interface Property Methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 605ba62f-b15a-4411-839b-c4ad8acedd8a
ms.tgt_platform: multiple
keywords:
- IADsEmail Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsEmail Property Methods
- IADsEmail.Type
- IADsEmail.get_Type
- IADsEmail.put_Type
- IADsEmail.Address
- IADsEmail.get_Address
- IADsEmail.put_Address
api_location:
- Activeds.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IADsEmail Property Methods

The property method of the [**IADsEmail**](/windows/desktop/api/Iads/nn-iads-iadsemail) interface sets the property described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**Address**
</dt> <dd> <dl>

The email address of the user.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Address(
  [out] BSTR* retval
);
HRESULT put_Address(
  [in] BSTR bstrAddress
);
```


</dt> </dl> </dd> <dt>

**Type**
</dt> <dd> <dl>

The type of the email message.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Type(
  [out] LONG* retVal
);
HRESULT put_Type(
  [in] LONG lnType
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADsEmail is defined as 97AF011A-478E-11D1-A3B4-00C04FB950DC<br/>            |



## See also

<dl> <dt>

[**IADsEmail**](/windows/desktop/api/Iads/nn-iads-iadsemail)
</dt> <dt>

[**ADS\_EMAIL**](/windows/desktop/api/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0014)
</dt> </dl>

 

 





