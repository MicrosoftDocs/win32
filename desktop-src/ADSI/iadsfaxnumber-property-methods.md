---
title: IADsFaxNumber Property Methods
description: The property method of the IADsFaxNumber interface sets the property described in the following table. For more information, see Interface Property Methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f4d46b9d-8db2-47b3-b489-9ffc363e6ac6
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- IADsFaxNumber Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsFaxNumber Property Methods
- IADsFaxNumber.TelephoneNumber
- IADsFaxNumber.get_TelephoneNumber
- IADsFaxNumber.put_TelephoneNumber
- IADsFaxNumber.Parameters
- IADsFaxNumber.get_Parameters
- IADsFaxNumber.put_Parameters
api_location:
- Activeds.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IADsFaxNumber Property Methods

The property method of the [**IADsFaxNumber**](/windows/win32/Iads/nn-iads-iadsfaxnumber?branch=master) interface sets the property described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**Parameters**
</dt> <dd> <dl>

The parameters for the fax machine.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Parameters(
  [out] VARIANT* retval
);
HRESULT put_Parameters(
  [in] VARIANT vParameters
);
```


</dt> </dl> </dd> <dt>

**TelephoneNumber**
</dt> <dd> <dl>

The telephone number of the fax machine.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_TelephoneNumber(
  [out] BSTR* retVal
);
HRESULT put_TelephoneNumber(
  [in] BSTR bstrTelephoneNumber
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
| IID<br/>                      | IID\_IADsFaxNumber is defined as A910DEA9-4680-11D1-0A3B-00C04FB950DC<br/>        |



## See also

<dl> <dt>

[**IADsFaxNumber**](/windows/win32/Iads/nn-iads-iadsfaxnumber?branch=master)
</dt> <dt>

[**ADS\_FAXNUMBER**](/windows/win32/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0013?branch=master)
</dt> </dl>

 

 





