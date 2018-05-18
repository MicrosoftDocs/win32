---
title: IGPMWMIFilter Property Methods
description: The property methods of the IGPMWMIFilter interface get and set the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation .
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '237f235f-f6b1-41b5-95cf-73f512484a68'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
keywords: ["IGPMWMIFilter Property Methods GPMC"]
topic_type:
- apiref
api_name:
- IGPMWMIFilter Property Methods
- IGPMWMIFilter.Description
- IGPMWMIFilter.put_Description
- IGPMWMIFilter.get_Description
- IGPMWMIFilter.Name
- IGPMWMIFilter.put_Name
- IGPMWMIFilter.get_Name
- IGPMWMIFilter.Path
- IGPMWMIFilter.get_Path
api_location:
- Gpmgmt.dll
api_type:
- COM
---

# IGPMWMIFilter Property Methods

The property methods of the [**IGPMWMIFilter**](igpmwmifilter.md) interface get and set the properties described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation .

## Properties

<dl> <dt>

**Description**
</dt> <dd> <dl>

Description of the WMI filter.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_Description(
  [in] BSTR newVal
);
HRESULT get_Description(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**Name**
</dt> <dd> <dl>

Name of the WMI filter.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_Name(
  [in] BSTR newVal
);
HRESULT get_Name(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**Path**
</dt> <dd> <dl>

WMI path to the instance of the WMI filter; for example, MSFT\_SomFilter.ID="{&lt;Guid&gt;}",Domain="&lt;Domain DNS Name&gt;".

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Path(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> </dl>

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl> |
| IID<br/>                      | IID\_IGPMWMIFilter is defined as EF2FF9B4-3C27-459A-B979-038305CEC75D<br/>      |



## See also

<dl> <dt>

[**IGPMWMIFilter**](igpmwmifilter.md)
</dt> <dt>

[**IGPMWMIFilterCollection**](igpmwmifiltercollection.md)
</dt> </dl>

 

 





