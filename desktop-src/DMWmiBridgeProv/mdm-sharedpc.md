---
title: MDM_SharedPC class
description: The MDM\_SharedPC class is used to configure settings for shared PC usage.
ms.assetid: 90985c4d-601e-4827-aee0-13524a69f759
keywords:
- MDM_SharedPC class
- MDM_SharedPC class, described
topic_type:
- apiref
api_name:
- MDM_SharedPC
- MDM_SharedPC.InstanceID
- MDM_SharedPC.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_SharedPC class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The MDM\_SharedPC class is used to configure settings for shared PC usage.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv1")]
class MDM_SharedPC
{
  string  InstanceID;
  string  ParentID;
  boolean EnableSharedPCMode;
  boolean SetEduPolicies;
  boolean SetPowerPolicies;
  sint32  MaintenanceStartTime;
  boolean SignInOnResume;
  sint32  SleepTimeout;
  boolean EnableAccountManager;
  sint32  AccountModel;
  sint32  DeletionPolicy;
  sint32  DiskLevelDeletion;
  sint32  DiskLevelCaching;
  boolean RestrictLocalStorage;
  string  KioskModeAUMID;
  string  KioskModeUserTileDisplayText;
  sint32  InactiveThreshold;
  sint32  MaxPageFileSizeMB;
};
```

## Members

The **MDM\_SharedPC** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_SharedPC** class has these properties.

<dl> <dt>

[AccountModel](/windows/client-management/mdm/sharedpc-csp#accountmodel)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[DeletionPolicy](/windows/client-management/mdm/sharedpc-csp#deletionpolicy)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[DiskLevelCaching](/windows/client-management/mdm/sharedpc-csp#disklevelcaching)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[DiskLevelDeletion](/windows/client-management/mdm/sharedpc-csp#diskleveldeletion)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[EnableAccountManager](/windows/client-management/mdm/sharedpc-csp#enableaccountmanager)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[EnableSharedPCMode](/windows/client-management/mdm/sharedpc-csp#enablesharedpcmode)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[InactiveThreshold](/windows/client-management/mdm/sharedpc-csp#inactivethreshold)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

</dd> <dt>

[KioskModeAUMID](/windows/client-management/mdm/sharedpc-csp#kioskmodeaumid)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[KioskModeUserTileDisplayText](/windows/client-management/mdm/sharedpc-csp#kioskmodeusertiledisplaytext)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[MaintenanceStartTime](/windows/client-management/mdm/sharedpc-csp#maintenancestarttime)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[MaxPageFileSizeMB](/windows/client-management/mdm/sharedpc-csp#maxpagefilesizemb)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

</dd> <dt>

[RestrictLocalStorage](/windows/client-management/mdm/sharedpc-csp#restrictlocalstorage)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[SetEduPolicies](/windows/client-management/mdm/sharedpc-csp#setedupolicies)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[SetPowerPolicies](/windows/client-management/mdm/sharedpc-csp#setpowerpolicies)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[SignInOnResume](/windows/client-management/mdm/sharedpc-csp#signinonresume)
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> <dt>

[SleepTimeout](/windows/client-management/mdm/sharedpc-csp#sleeptimeout)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

For additional information, see [SharedPC CSP](/windows/client-management/mdm/sharedpc-csp).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | None supported<br/>                                                                       |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                              |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv1.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl>  |



 

