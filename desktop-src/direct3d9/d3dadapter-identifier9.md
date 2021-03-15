---
description: Contains information identifying the adapter.
ms.assetid: d0d59df9-c512-4d69-b0a0-7d87d7a380f6
title: D3DADAPTER_IDENTIFIER9 structure (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DADAPTER_IDENTIFIER9
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DADAPTER\_IDENTIFIER9 structure

Contains information identifying the adapter.

## Syntax


```C++
typedef struct D3DADAPTER_IDENTIFIER9 {
  char          Driver[MAX_DEVICE_IDENTIFIER_STRING];
  char          Description[MAX_DEVICE_IDENTIFIER_STRING];
  char          DeviceName[32];
  LARGE_INTEGER DriverVersion;
  DWORD         DriverVersionLowPart;
  DWORD         DriverVersionHighPart;
  DWORD         VendorId;
  DWORD         DeviceId;
  DWORD         SubSysId;
  DWORD         Revision;
  GUID          DeviceIdentifier;
  DWORD         WHQLLevel;
} D3DADAPTER_IDENTIFIER9, *LPD3DADAPTER_IDENTIFIER9;
```



## Members

<dl> <dt>

**Driver**
</dt> <dd>

Type: **char**

</dd> <dd>

Used for presentation to the user. This should not be used to identify particular drivers, because many different strings might be associated with the same device and driver from different vendors.

</dd> <dt>

**Description**
</dt> <dd>

Type: **char**

</dd> <dd>

Used for presentation to the user.

</dd> <dt>

**DeviceName**
</dt> <dd>

Type: **char**

</dd> <dd>

Device name for GDI.

</dd> <dt>

**DriverVersion**
</dt> <dd>

Type: **[**LARGE\_INTEGER**](/windows/win32/api/winnt/ns-winnt-large_integer-r1)**

</dd> <dd>

Identify the version of the Direct3D driver. It is legal to do less than and greater than comparisons on the 64-bit signed integer value. However, exercise caution if you use this element to identify problematic drivers. Instead, you should use DeviceIdentifier. See Remarks.

</dd> <dt>

**DriverVersionLowPart**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Identify the version of the Direct3D driver. It is legal to do < and > comparisons on the 64-bit signed integer value. However, exercise caution if you use this element to identify problematic drivers. Instead, you should use DeviceIdentifier. See Remarks.

</dd> <dt>

**DriverVersionHighPart**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Identify the version of the Direct3D driver. It is legal to do < and > comparisons on the 64-bit signed integer value. However, exercise caution if you use this element to identify problematic drivers. Instead, you should use DeviceIdentifier. See Remarks.

</dd> <dt>

**VendorId**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Can be used to help identify a particular chip set. Query this member to identify the manufacturer. The value can be zero if unknown.

</dd> <dt>

**DeviceId**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Can be used to help identify a particular chip set. Query this member to identify the type of chip set. The value can be zero if unknown.

</dd> <dt>

**SubSysId**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Can be used to help identify a particular chip set. Query this member to identify the subsystem, typically the particular board. The value can be zero if unknown.

</dd> <dt>

**Revision**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Can be used to help identify a particular chip set. Query this member to identify the revision level of the chip set. The value can be zero if unknown.

</dd> <dt>

**DeviceIdentifier**
</dt> <dd>

Type: **[**GUID**](guid.md)**

</dd> <dd>

Can be queried to check changes in the driver and chip set. This GUID is a unique identifier for the driver and chip set pair. Query this member to track changes to the driver and chip set in order to generate a new profile for the graphics subsystem. DeviceIdentifier can also be used to identify particular problematic drivers.

</dd> <dt>

**WHQLLevel**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Used to determine the Windows Hardware Quality Labs (WHQL) validation level for this driver and device pair. The DWORD is a packed date structure defining the date of the release of the most recent WHQL test passed by the driver. It is legal to perform < and > operations on this value. The following illustrates the date format.



|       |                                               |
|-------|-----------------------------------------------|
| Bits  |                                               |
| 31-16 | The year, a decimal number from 1999 upwards. |
| 15-8  | The month, a decimal number from 1 to 12.     |
| 7-0   | The day, a decimal number from 1 to 31.       |



 

The following values are also used.



|     |                                                       |
|-----|-------------------------------------------------------|
| 0   | Not certified.                                        |
| 1   | WHQL validated, but no date information is available. |



 

Differences between Direct3D 9 and Direct3D 9Ex:

For Direct3D9Ex running on Windows Vista, Windows Server 2008, Windows 7, and Windows Server 2008 R2 (or more current operating system), [**IDirect3D9::GetAdapterIdentifier**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-getadapteridentifier) returns 1 for the WHQL level without checking the status of the driver.

</dd> </dl>

## Remarks

The following pseudocode example illustrates the version format encoded in the DriverVersion, DriverVersionLowPart, and DriverVersionHighPart members.


```
Product = HIWORD(DriverVersion.HighPart)
Version = LOWORD(DriverVersion.HighPart)
SubVersion = HIWORD(DriverVersion.LowPart)
Build = LOWORD(DriverVersion.LowPart)
```



See the Platform SDK for more information about the HIWORD macro, the LOWORD macro, and the LARGE\_INTEGER structure.

MAX\_DEVICE\_IDENTIFIER\_STRING is a constant with the following definition.


```
#define MAX_DEVICE_IDENTIFIER_STRING        512
```



The VendorId, DeviceId, SubSysId, and Revision members can be used in tandem to identify particular chip sets. However, use these members with caution.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 
