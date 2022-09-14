---
title: WINBIO_UNIT_SCHEMA structure (Winbio\_types.h)
description: Describes the capabilities of a biometric unit.
ms.assetid: b20adf18-2948-481f-9d12-8da17aa152f7
keywords:
- WINBIO_UNIT_SCHEMA structure Windows Biometric Framework API
- PWINBIO_UNIT_SCHEMA structure pointer Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_UNIT_SCHEMA
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_UNIT\_SCHEMA structure

The **WINBIO\_UNIT\_SCHEMA** structure describes the capabilities of a biometric unit. It is used by the [**WinBioEnumBiometricUnits**](/windows/desktop/api/Winbio/nf-winbio-winbioenumbiometricunits) function.

## Syntax


```C++
typedef struct _WINBIO_UNIT_SCHEMA {
  WINBIO_UNIT_ID                  UnitId;
  WINBIO_POOL_TYPE                PoolType;
  WINBIO_BIOMETRIC_TYPE           BiometricFactor;
  WINBIO_BIOMETRIC_SENSOR_SUBTYPE SensorSubType;
  WINBIO_CAPABILITIES             Capabilities;
  WINBIO_STRING                   DeviceInstanceId;
  WINBIO_STRING                   Description;
  WINBIO_STRING                   Manufacturer;
  WINBIO_STRING                   Model;
  WINBIO_STRING                   SerialNumber;
  WINBIO_VERSION                  FirmwareVersion;
} WINBIO_UNIT_SCHEMA, *PWINBIO_UNIT_SCHEMA;
```



## Members

<dl> <dt>

**UnitId**
</dt> <dd>

A value that identifies the biometric unit.

</dd> <dt>

**PoolType**
</dt> <dd>

A **ULONG** value that specifies the type of the biometric unit. This can be one of the following values:



| Value                                                                                                                                                                            | Meaning                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_POOL_UNKNOWN"></span><span id="winbio_pool_unknown"></span><dl> <dt>**WINBIO\_POOL\_UNKNOWN**</dt> </dl> | The type is unknown.<br/>                                                                            |
| <span id="WINBIO_POOL_SYSTEM"></span><span id="winbio_pool_system"></span><dl> <dt>**WINBIO\_POOL\_SYSTEM**</dt> </dl>    | The session connects to a shared collection of biometric units managed by the service provider.<br/> |
| <span id="WINBIO_POOL_PRIVATE"></span><span id="winbio_pool_private"></span><dl> <dt>**WINBIO\_POOL\_PRIVATE**</dt> </dl> | The session connects to a collection of biometric units that are managed by the caller.<br/>         |



 

</dd> <dt>

**BiometricFactor**
</dt> <dd>

A value that specifies the type of the biometric unit. Only **WINBIO\_TYPE\_FINGERPRINT** is currently supported.

</dd> <dt>

**SensorSubType**
</dt> <dd>

A sensor subtype defined for the biometric type specified by the **BiometricFactor** member. Only fingerprint types (**WINBIO\_TYPE\_FINGERPRINT**) are currently supported. The following subtypes are currently defined for fingerprints:

-   WINBIO\_SENSOR\_SUBTYPE\_UNKNOWN
-   WINBIO\_FP\_SENSOR\_SUBTYPE\_SWIPE
-   WINBIO\_FP\_SENSOR\_SUBTYPE\_TOUCH

</dd> <dt>

**Capabilities**
</dt> <dd>

A bitmask of the biometric sensor capabilities. This can be a bitwise **OR** of the following values:

-   WINBIO\_CAPABILITY\_SENSOR
-   WINBIO\_CAPABILITY\_MATCHING
-   WINBIO\_CAPABILITY\_DATABASE
-   WINBIO\_CAPABILITY\_PROCESSING
-   WINBIO\_CAPABILITY\_ENCRYPTION
-   WINBIO\_CAPABILITY\_NAVIGATION
-   WINBIO\_CAPABILITY\_INDICATOR
-   WINBIO\_CAPABILITY\_VIRTUAL\_SENSOR
    > [!Note]  
    > The **WINBIO\_CAPABILITY\_VIRTUAL\_SENSOR** constant applies only for Windows 10 and later.

     

</dd> <dt>

**DeviceInstanceId**
</dt> <dd>

A string value that contains the device ID. The string can contain up to 256 Unicode characters including a terminating **NULL** character.

</dd> <dt>

**Description**
</dt> <dd>

A string value that contains a description of the biometric unit. The string can contain up to 256 Unicode characters including a terminating **NULL** character.

</dd> <dt>

**Manufacturer**
</dt> <dd>

A string value that contains the name of the manufacturer. The string can contain up to 256 Unicode characters including a terminating **NULL** character.

</dd> <dt>

**Model**
</dt> <dd>

A string value that contains the model number of the biometric unit. The string can contain up to 256 Unicode characters including a terminating **NULL** character.

</dd> <dt>

**SerialNumber**
</dt> <dd>

A **NULL**-terminated Unicode string that contains the serial number of the biometric unit. The string can contain up to 256 Unicode characters including a terminating **NULL** character.

</dd> <dt>

**FirmwareVersion**
</dt> <dd>

A [**WINBIO\_VERSION**](winbio-version.md) structure that contains the major and minor version numbers for the biometric unit.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Structures](client-application-structures.md)
</dt> <dt>

[**WinBioEnumBiometricUnits**](/windows/desktop/api/Winbio/nf-winbio-winbioenumbiometricunits)
</dt> </dl>

 

 





