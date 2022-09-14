---
title: IADsNetAddress Property Methods (Iads.h)
description: The property method of the IADsNetAddress interface sets the property described in the following table. For more information, see Interface Property Methods.
ms.assetid: 1da493d6-5660-4054-8d28-89db0b56f30f
ms.tgt_platform: multiple
keywords:
- IADsNetAddress Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsNetAddress Property Methods
- IADsNetAddress.AddressType
- IADsNetAddress.get_AddressType
- IADsNetAddress.put_AddressType
- IADsNetAddress.Address
- IADsNetAddress.get_Address
- IADsNetAddress.put_Address
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADsNetAddress Property Methods

The property method of the [**IADsNetAddress**](/windows/desktop/api/Iads/nn-iads-iadsnetaddress) interface sets the property described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**Address**
</dt> <dd> <dl>

A network address.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Address(
  [out] VARIANT* retval
);
HRESULT put_Address(
  [in] VARIANT vAddress
);
```


</dt> </dl> </dd> <dt>

**AddressType**
</dt> <dd> <dl>

A type of communication protocols.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_AddressType(
  [out] LONG* retVal
);
HRESULT put_AddressType(
  [in] LONG lnAddressType
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
| IID<br/>                      | IID\_IADsNetAddress is defined as B21A50A9-4080-11D1-A3AC-00C04FB950DC<br/>       |



## See also

<dl> <dt>

[**IADsNetAddress**](/windows/desktop/api/Iads/nn-iads-iadsnetaddress)
</dt> <dt>

[**ADS\_NETADDRESS**](/windows/win32/api/iads/ns-iads-ads_netaddress)
</dt> </dl>

 

 





