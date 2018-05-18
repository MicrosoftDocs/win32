---
title: IGPMMapEntry Property Methods
description: The property methods of the IGPMMapEntry interface get and set the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4768a3be-1a8d-4168-acf9-758481bf4cca'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
keywords: ["IGPMMapEntry Property Methods GPMC"]
topic_type:
- apiref
api_name:
- IGPMMapEntry Property Methods
- IGPMWMIFilter.Source
- IGPMWMIFilter.get_Source
- IGPMWMIFilter.Destination
- IGPMWMIFilter.get_Destination
- IGPMWMIFilter.DestinationOption
- IGPMWMIFilter.get_DestinationOption
- IGPMWMIFilter.EntryType
- IGPMWMIFilter.get_EntryType
api_location:
- Gpmgmt.dll
api_type:
- COM
---

# IGPMMapEntry Property Methods

The property methods of the **IGPMMapEntry** interface get and set the properties described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation.

## Properties

<dl> <dt>

**Destination**
</dt> <dd> <dl>

Returns destination field of entry.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Destination(
  [in] BSTR* pbstrVal
);
```


</dt> </dl> </dd> <dt>

**DestinationOption**
</dt> <dd> <dl>

Returns the option set for the destination. The pdestOption parameter can have one of the following values: opDestinationSameAsSource=0, opDestinationNone, opDestinationByRelativeName, or opDestinationSet.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **GPMDestinationOption**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DestinationOption(
  [out] GPMDestinationOption* pdestOption
);
```


</dt> </dl> </dd> <dt>

**EntryType**
</dt> <dd> <dl>

Returns the type of Entry. Returns one of the following values: typeUser (value equals 0, typeComputer, typeLocalGroup, typeGlobalGroup, typeUniversalGroup, typeUNCPath, or typeUnknown.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **GPMEntryType**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_EntryType(
  [out] GPMEntryType* pgpmEntryType
);
```


</dt> </dl> </dd> <dt>

**Source**
</dt> <dd> <dl>

Returns the Source field of an entry.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Source(
  [out] BSTR* pbstrVal
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
| IID<br/>                      | IID\_IGPMMapEntry is defined as 8E79AD06-2381-4444-BE4C-FF693E6E6F2B<br/>       |



## See also

<dl> <dt>

[**IGPMMapEntry**](igpmmapentry.md)
</dt> </dl>

 

 





