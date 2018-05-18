---
title: STORAGE\_DIAGNOSTIC\_LEVEL enumeration
description: The STORAGE\_DIAGNOSTIC\_LEVEL enumeration specifies the target type of a storage diagnostic.
ms.assetid: 'BB05D543-7B99-481E-8CDB-AE350CBCCA2A'
keywords: ["STORAGE_DIAGNOSTIC_LEVEL enumeration Storage Devices", "PSTORAGE_DIAGNOSTIC_LEVEL enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_DIAGNOSTIC_LEVEL
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_DIAGNOSTIC\_LEVEL enumeration

The **STORAGE\_DIAGNOSTIC\_LEVEL** enumeration specifies the target type of a storage diagnostic.

## Syntax


```C++
typedef enum _STORAGE_DIAGNOSTIC_LEVEL { 
  StorageDiagnosticLevelDefault  = 0,
  StorageDiagnosticLevelMax
} STORAGE_DIAGNOSTIC_LEVEL, *PSTORAGE_DIAGNOSTIC_LEVEL;
```



## Constants

<dl> <dt>

<span id="StorageDiagnosticLevelDefault"></span><span id="storagediagnosticleveldefault"></span><span id="STORAGEDIAGNOSTICLEVELDEFAULT"></span>**StorageDiagnosticLevelDefault**
</dt> <dd>

Specifies the default diagnostic level.

</dd> <dt>

<span id="StorageDiagnosticLevelMax"></span><span id="storagediagnosticlevelmax"></span><span id="STORAGEDIAGNOSTICLEVELMAX"></span>**StorageDiagnosticLevelMax**
</dt> <dd>

Specifies the max diagnostic level.

</dd> </dl>

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 10, version 1709.<br/>                          |
| Header<br/>  | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DIAGNOSTIC_LEVEL%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





