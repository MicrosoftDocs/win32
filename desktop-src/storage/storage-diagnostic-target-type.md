---
title: STORAGE\_DIAGNOSTIC\_TARGET\_TYPE enumeration
description: The STORAGE\_DIAGNOSTIC\_TARGET\_TYPE enumeration specifies the target type of a storage diagnostic.
ms.assetid: 1A48FC0F-7ED2-4F9F-8B61-A498B0D13FE8
keywords:
- STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration Storage Devices
- PSTORAGE_DIAGNOSTIC_TARGET_TYPE enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_DIAGNOSTIC_TARGET_TYPE
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# STORAGE\_DIAGNOSTIC\_TARGET\_TYPE enumeration

The **STORAGE\_DIAGNOSTIC\_TARGET\_TYPE** enumeration specifies the target type of a storage diagnostic.

## Syntax


```C++
typedef enum _STORAGE_DIAGNOSTIC_TARGET_TYPE { 
  StorageDiagnosticTargetTypeUndefined    = 0,
  StorageDiagnosticTargetTypePort,
  StorageDiagnosticTargetTypeMiniport,
  StorageDiagnosticTargetTypeHbaFirmware,
  StorageDiagnosticTargetTypeMax
} STORAGE_DIAGNOSTIC_TARGET_TYPE, *PSTORAGE_DIAGNOSTIC_TARGET_TYPE;
```



## Constants

<dl> <dt>

<span id="StorageDiagnosticTargetTypeUndefined"></span><span id="storagediagnostictargettypeundefined"></span><span id="STORAGEDIAGNOSTICTARGETTYPEUNDEFINED"></span>**StorageDiagnosticTargetTypeUndefined**
</dt> <dd>

Specifies the target type is undefined.

</dd> <dt>

<span id="StorageDiagnosticTargetTypePort"></span><span id="storagediagnostictargettypeport"></span><span id="STORAGEDIAGNOSTICTARGETTYPEPORT"></span>**StorageDiagnosticTargetTypePort**
</dt> <dd>

Specifies the target type is a port driver.

</dd> <dt>

<span id="StorageDiagnosticTargetTypeMiniport"></span><span id="storagediagnostictargettypeminiport"></span><span id="STORAGEDIAGNOSTICTARGETTYPEMINIPORT"></span>**StorageDiagnosticTargetTypeMiniport**
</dt> <dd>

Specifies the target type is a Miniport driver.

</dd> <dt>

<span id="StorageDiagnosticTargetTypeHbaFirmware"></span><span id="storagediagnostictargettypehbafirmware"></span><span id="STORAGEDIAGNOSTICTARGETTYPEHBAFIRMWARE"></span>**StorageDiagnosticTargetTypeHbaFirmware**
</dt> <dd>

Specifies the target type is a Hba Firmware driver.

</dd> <dt>

<span id="StorageDiagnosticTargetTypeMax"></span><span id="storagediagnostictargettypemax"></span><span id="STORAGEDIAGNOSTICTARGETTYPEMAX"></span>**StorageDiagnosticTargetTypeMax**
</dt> <dd>

Specifies the target type is a Max driver.

</dd> </dl>

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 10, version 1709.<br/>                          |
| Header<br/>  | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DIAGNOSTIC_TARGET_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





