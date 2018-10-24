---
title: IADsTypedName Property Methods
description: The property method of the IADsTypedName interface sets the property described in the following table. For more information, see Interface Property Methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0097c7c0-91f9-4874-93f2-c24900054a49
ms.tgt_platform: multiple
keywords:
- IADsTypedName Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsTypedName Property Methods
- IADsTypedName.ObjectName
- IADsTypedName.get_ObjectName
- IADsTypedName.put_ObjectName
- IADsTypedName.Level
- IADsTypedName.get_Level
- IADsTypedName.put_Level
- IADsTypedName.Interval
- IADsTypedName.get_Interval
- IADsTypedName.put_Interval
api_location:
- Activeds.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IADsTypedName Property Methods

The property method of the [**IADsTypedName**](/windows/desktop/api/Iads/nn-iads-iadstypedname) interface sets the property described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**Interval**
</dt> <dd> <dl>

The frequency of reference of the object.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Interval(
  [out] LONG* retval
);
HRESULT put_Interval(
  [in] LONG lnInterval
);
```


</dt> </dl> </dd> <dt>

**Level**
</dt> <dd> <dl>

The priority level associated with the object.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Level(
  [out] LONG* retval
);
HRESULT put_Level(
  [in] LONG lnLevel
);
```


</dt> </dl> </dd> <dt>

**ObjectName**
</dt> <dd> <dl>

The name of an object.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ObjectName(
  [out] BSTR* retVal
);
HRESULT put_ObjectName(
  [in] BSTR bstrObjectName
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
| IID<br/>                      | IID\_IADsTypedName is defined as B371A349-4080-11D1-A3AC-00C04FB950DC<br/>        |



## See also

<dl> <dt>

[**IADsTypedName**](/windows/desktop/api/Iads/nn-iads-iadstypedname)
</dt> <dt>

[**ADS\_TYPEDNAME**](/windows/desktop/api/Iads/ns-iads-__midl___midl_itf_ads_0000_0000_0009)
</dt> </dl>

 

 





