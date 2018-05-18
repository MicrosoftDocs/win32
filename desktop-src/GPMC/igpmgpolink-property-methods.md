---
title: IGPMGPOLink Property Methods
description: The property methods of the IGPMGPOLink interface get and set the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4197b502-c797-4cba-a3f6-339af9208348'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
keywords: ["IGPMGPOLink Property Methods GPMC"]
topic_type:
- apiref
api_name:
- IGPMGPOLink Property Methods
- IGPMGPOLink.Enabled
- IGPMGPOLink.put_Enabled
- IGPMGPOLink.get_Enabled
- IGPMGPOLink.Enforced
- IGPMGPOLink.put_Enforced
- IGPMGPOLink.get_Enforced
- IGPMGPOLink.GPODomain
- IGPMGPOLink.get_GPODomain
- IGPMGPOLink.GPOID
- IGPMGPOLink.get_GPOID
- IGPMGPOLink.SOM
- IGPMGPOLink.get_SOM
- IGPMGPOLink.SOMLinkOrder
- IGPMGPOLink.get_SOMLinkOrder
api_location:
- Gpmgmt.dll
api_type:
- COM
---

# IGPMGPOLink Property Methods

The property methods of the [**IGPMGPOLink**](igpmgpolink.md) interface get and set the properties described in the following table. For a general discussion of property methods, see [**Interface Property Methods**](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation.

## Properties

<dl> <dt>

**Enabled**
</dt> <dd> <dl>

Value that specifies whether the GPO link is enabled.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Boolean**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_Enabled(
  [in] VARIANT_BOOL newVal
);
HRESULT get_Enabled(
  [out] VARIANT_BOOL* pVal
);
```


</dt> </dl> </dd> <dt>

**Enforced**
</dt> <dd> <dl>

Value that specifies whether the GPO link is enforced. If this property is equal to **VARIANT\_TRUE**, the GPO link is enforced and cannot be overridden.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **Boolean**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT put_Enforced(
  [in] VARIANT_BOOL newVal
);
HRESULT get_Enforced(
  [out] VARIANT_BOOL* pVal
);
```


</dt> </dl> </dd> <dt>

**GPODomain**
</dt> <dd> <dl>

Domain in which the GPO resides. This is a full DNS name, for example, example.microsoft.com.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_GPODomain(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**GPOID**
</dt> <dd> <dl>

ID of the GPO.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_GPOID(
  [out] BSTR* pVal
);
```


</dt> </dl> </dd> <dt>

**SOM**
</dt> <dd> <dl>

Returns a reference to the [**GPMSOM**](igpmsom.md) object to which the GPO link is attached.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SOM(
  [out] IGPMSOM** ppIGPMSOM
);
```


</dt> </dl> </dd> <dt>

**SOMLinkOrder**
</dt> <dd> <dl>

Position of the GPO link in relation to other GPO links for the scope of management (SOM).

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Long**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SOMLinkOrder(
  [out] LONG* lVal
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
| IID<br/>                      | IID\_IGPMGPOLink is defined as 434B99BD-5DE7-478A-809C-C251721DF70C<br/>        |



## See also

<dl> <dt>

[**IGPMGPOLink**](igpmgpolink.md)
</dt> <dt>

[**IGPMGPOLinksCollection**](igpmgpolinkscollection.md)
</dt> </dl>

 

 





