---
title: IADsDNWithString Property Methods (Iads.h)
description: The property method of the IADsDNWithString interface sets the property described in the following table. For more information, see Interface Property Methods.
ms.assetid: d3fb67b6-9f7d-4de5-bf01-f9c5b9e4f086
ms.tgt_platform: multiple
keywords:
- IADsDNWithString Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsDNWithString Property Methods
- IADsDNWithString.StringValue
- IADsDNWithString.get_StringValue
- IADsDNWithString.put_StringValue
- IADsDNWithString.DNString
- IADsDNWithString.get_DNString
- IADsDNWithString.put_DNString
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADsDNWithString Property Methods

The property method of the [**IADsDNWithString**](/windows/desktop/api/Iads/nn-iads-iadsdnwithstring) interface sets the property described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**DNString**
</dt> <dd> <dl>

The DN string associated with a string value.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DNString(
  [out] BSTR* retval
);
HRESULT put_DNString(
  [in] BSTR bstrDN
);
```


</dt> </dl> </dd> <dt>

**StringValue**
</dt> <dd> <dl>

The string value associated with a DN of an object.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_StringValue(
  [out] BSTR* retVal
);
HRESULT put_StringValue(
  [in] BSTR varBV
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADsDNWithString is defined as 370DF02E-F934-11D2-BA96-00C04FB6D0D1<br/>     |



## See also

<dl> <dt>

[**IADsDNWithString**](/windows/desktop/api/Iads/nn-iads-iadsdnwithstring)
</dt> <dt>

[**ADS\_DN\_WITH\_STRING**](/windows/win32/api/iads/ns-iads-ads_dn_with_string)
</dt> </dl>

 

 





