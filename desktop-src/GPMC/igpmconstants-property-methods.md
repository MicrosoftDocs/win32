---
title: IGPMConstants Property Methods
description: The property methods of the IGPMConstants interface get the properties that are described in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '93221fe3-bce8-4a36-8e6d-a43d37872295'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
keywords: ["IGPMConstants Property Methods GPMC"]
topic_type:
- apiref
api_name:
- IGPMConstants Property Methods
- IGPMConstants.DestinationOptionByRelativeName
- IGPMConstants.get_DestinationOptionByRelativeName
- IGPMConstants.DestinationOptionNone
- IGPMConstants.get_DestinationOptionNone
- IGPMConstants.DestinationOptionSameAsSource
- IGPMConstants.get_DestinationOptionSameAsSource
- IGPMConstants.DestinationOptionSet
- IGPMConstants.get_DestinationOptionSet
- IGPMConstants.EntryTypeComputer
- IGPMConstants.get_EntryTypeComputer
- IGPMConstants.EntryTypeGlobalGroup
- IGPMConstants.get_EntryTypeGlobalGroup
- IGPMConstants.EntryTypeLocalGroup
- IGPMConstants.get_EntryTypeLocalGroup
- IGPMConstants.EntryTypeUniversalGroup
- IGPMConstants.get_EntryTypeUniversalGroup
- IGPMConstants.EntryTypeUNCPath
- IGPMConstants.get_EntryTypeUNCPath
- IGPMConstants.EntryTypeUnknown
- IGPMConstants.get_EntryTypeUnknown
- IGPMConstants.EntryTypeUser
- IGPMConstants.get_EntryTypeUser
- IGPMConstants.PermGPOApply
- IGPMConstants.get_PermGPOApply
- IGPMConstants.PermGPOCustom
- IGPMConstants.get_PermGPOCustom
- IGPMConstants.PermGPOEdit
- IGPMConstants.get_PermGPOEdit
- IGPMConstants.PermGPOEditSecurityAndDelete
- IGPMConstants.get_PermGPOEditSecurityAndDelete
- IGPMConstants.PermGPORead
- IGPMConstants.get_PermGPORead
- IGPMConstants.PermSOMGPOCreate
- IGPMConstants.get_PermSOMGPOCreate
- IGPMConstants.PermSOMLink
- IGPMConstants.get_PermSOMLink
- IGPMConstants.PermSOMLogging
- IGPMConstants.get_PermSOMLogging
- IGPMConstants.PermSOMPlanning
- IGPMConstants.get_PermSOMPlanning
- IGPMConstants.PermSOMWMICreate
- IGPMConstants.get_PermSOMWMICreate
- IGPMConstants.PermSOMWMIFullControl
- IGPMConstants.get_PermSOMWMIFullControl
- IGPMConstants.PermWMIFilterCustom
- IGPMConstants.get_PermWMIFilterCustom
- IGPMConstants.PermWMIFilterEdit
- IGPMConstants.get_PermWMIFilterEdit
- IGPMConstants.PermWMIFilterFullControl
- IGPMConstants.get_PermWMIFilterFullControl
- IGPMConstants.SearchPropertyBackupMostRecent
- IGPMConstants.get_SearchPropertyBackupMostRecent
- IGPMConstants.SearchPropertyGPOComputerExtensions
- IGPMConstants.get_SearchPropertyGPOComputerExtensions
- IGPMConstants.SearchPropertyGPODisplayName
- IGPMConstants.get_SearchPropertyGPODisplayName
- IGPMConstants.SearchPropertyGPODomain
- IGPMConstants.get_SearchPropertyGPODomain
- IGPMConstants.SearchPropertyGPOEffectivePermissions
- IGPMConstants.get_SearchPropertyGPOEffectivePermissions
- IGPMConstants.SearchPropertyGPOID
- IGPMConstants.get_SearchPropertyGPOID
- IGPMConstants.SearchPropertyGPOPermissions
- IGPMConstants.get_SearchPropertyGPOPermissions
- IGPMConstants.SearchPropertyGPOUserExtensions
- IGPMConstants.get_SearchPropertyGPOUserExtensions
- IGPMConstants.SearchPropertyGPOWMIFilter
- IGPMConstants.get_SearchPropertyGPOWMIFilter
- IGPMConstants.SearchPropertySOMLinks
- IGPMConstants.get_SearchPropertySOMLinks
- IGPMConstants.SearchOpContains
- IGPMConstants.get_SearchOpContains
- IGPMConstants.SearchOpEquals
- IGPMConstants.get_SearchOpEquals
- IGPMConstants.SearchOpNotContains
- IGPMConstants.get_SearchOpNotContains
- IGPMConstants.SearchOpNotEquals
- IGPMConstants.get_SearchOpNotEquals
- IGPMConstants.SOMDomain
- IGPMConstants.get_SOMDomain
- IGPMConstants.SOMOU
- IGPMConstants.get_SOMOU
- IGPMConstants.SOMSite
- IGPMConstants.get_SOMSite
- IGPMConstants.DoNotValidateDC
- IGPMConstants.get_DoNotValidateDC
- IGPMConstants.UseAnyDC
- IGPMConstants.get_UseAnyDC
- IGPMConstants.DoNotUseW2KDC
- IGPMConstants.get_DoNotUseW2KDC
- IGPMConstants.UsePDC
- IGPMConstants.get_UsePDC
- IGPMConstants.SecurityFlags
- IGPMConstants.get_SecurityFlags
- IGPMConstants.RSOPModePlanning
- IGPMConstants.get_RSOPModePlanning
- IGPMConstants.RSOPModeLogging
- IGPMConstants.get_RSOPModeUnknown
- IGPMConstants.RsopLoggingNoComputer
- IGPMConstants.get_RsopLoggingNoComputer
- IGPMConstants.RsopLoggingNoUser
- IGPMConstants.get_RsopLoggingNoUser
- IGPMConstants.RsopPlanningAssumeSlowLink
- IGPMConstants.get_RsopPlanningAssumeSlowLink
- IGPMConstants.RsopPlanningLoopbackOption
- IGPMConstants.get_RsopPlanningLoopbackOption
- IGPMConstants.RsopPlanningAssumeUserWQLFilterTrue
- IGPMConstants.get_RSOPModeUnknown
- IGPMConstants.RsopPlanningAssumeCompWQLFilterTrue
- IGPMConstants.get_RSOPModeUnknown
- IGPMConstants.MigrationTableOnly
- IGPMConstants.get_MigrationTableOnly
- IGPMConstants.ProcessSecurity
- IGPMConstants.get_ProcessSecurity
api_location:
- Gpmgmt.dll
api_type:
- COM
---

# IGPMConstants Property Methods

The property methods of the [**IGPMConstants**](igpmconstants.md) interface get the properties that are described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the Active Directory Service Interfaces (ADSI) documentation.

The [**IGPMConstants**](igpmconstants.md) interface defines the following properties.

## Properties

<dl> <dt>

**DestinationOptionByRelativeName**
</dt> <dd> <dl>

Value that corresponds to the **GPMDestinationOption** of opDestinationByRelativeName.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DestinationOptionByRelativeName(
  [out] GPMDestinationOption* pVal
);
```


</dt> </dl> </dd> <dt>

**DestinationOptionNone**
</dt> <dd> <dl>

Value that corresponds to the **GPMDestinationOption** of **opDestinationNone**.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DestinationOptionNone(
  [out] GPMDestinationOption* pVal
);
```


</dt> </dl> </dd> <dt>

**DestinationOptionSameAsSource**
</dt> <dd> <dl>

Value that corresponds to the GPMDestinationOption option of **opDestinationSameAsSource**.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DestinationOptionSameAsSource(
  [out] GPMDestinationOption* pVal
);
```


</dt> </dl> </dd> <dt>

**DestinationOptionSet**
</dt> <dd> <dl>

Value that corresponds to the **GPMDestinationOption** option of **opDestinationSet**.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DestinationOptionSet(
  [out] GPMDestinationOption* pVal
);
```


</dt> </dl> </dd> <dt>

**DoNotUseW2KDC**
</dt> <dd> <dl>

Value that corresponds to the **DoNotUseW2KDC** property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DoNotUseW2KDC(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**DoNotValidateDC**
</dt> <dd> <dl>

Value that corresponds to the **DoNotValidateDC** property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DoNotValidateDC(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**EntryTypeComputer**
</dt> <dd> <dl>

Value that corresponds to the **GPMEntryType** of **typeComputer**.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_EntryTypeComputer(
  [out] GPMEntryType* pVal
);
```


</dt> </dl> </dd> <dt>

**EntryTypeGlobalGroup**
</dt> <dd> <dl>

Value that corresponds to the **GPMEntryType** of **typeGlobalGroup**.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_EntryTypeGlobalGroup(
  [out] GPMEntryType* pVal
);
```


</dt> </dl> </dd> <dt>

**EntryTypeLocalGroup**
</dt> <dd> <dl>

Value that corresponds to the **GPMEntryType** of **typeLocalGroup**.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_EntryTypeLocalGroup(
  [out] GPMEntryType* pVal
);
```


</dt> </dl> </dd> <dt>

**EntryTypeUNCPath**
</dt> <dd> <dl>

Value that corresponds to the **GPMEntryType** of **typeUNCPath**.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_EntryTypeUNCPath(
  [out] GPMEntryType* pVal
);
```


</dt> </dl> </dd> <dt>

**EntryTypeUniversalGroup**
</dt> <dd> <dl>

Value that corresponds to the **GPMEntryType** of **typeUniversalGroup**.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_EntryTypeUniversalGroup(
  [out] GPMEntryType* pVal
);
```


</dt> </dl> </dd> <dt>

**EntryTypeUnknown**
</dt> <dd> <dl>

Value that corresponds to the **GPMEntryType** of **typeUnknown**.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_EntryTypeUnknown(
  [out] GPMEntryType* pVal
);
```


</dt> </dl> </dd> <dt>

**EntryTypeUser**
</dt> <dd> <dl>

Value that corresponds to the **GPMEntryType** of **typeUser**.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_EntryTypeUser(
  [out] GPMEntryType* pVal
);
```


</dt> </dl> </dd> <dt>

**MigrationTableOnly**
</dt> <dd> <dl>

Value that corresponds to the **GPM\_MIGRATIONTABLE\_ONLY** constant.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_MigrationTableOnly(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**PermGPOApply**
</dt> <dd> <dl>

Constant value that corresponds to the **permGPOApply** permission type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermGPOApply(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermGPOCustom**
</dt> <dd> <dl>

Constant value that corresponds to the **permGPOCustom** permission type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermGPOCustom(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermGPOEdit**
</dt> <dd> <dl>

Constant value that corresponds to the **permGPOEdit** permission type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermGPOEdit(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermGPOEditSecurityAndDelete**
</dt> <dd> <dl>

Constant value that corresponds to the **permGPOEditSecurityAndDelete** permission type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermGPOEditSecurityAndDelete(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermGPORead**
</dt> <dd> <dl>

Constant value that corresponds to the **permGPORead** permission type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermGPORead(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermSOMGPOCreate**
</dt> <dd> <dl>

Constant value that corresponds to the **permSOMGPOCreate** permission type. Applies to domains only.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermSOMGPOCreate(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermSOMLink**
</dt> <dd> <dl>

Constant value that corresponds to the **permSOMLink** permission type. Applies to sites, domains, and organizational units (OUs).

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermSOMLink(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermSOMLogging**
</dt> <dd> <dl>

Constant value that corresponds to the **permSOMLogging** permission type. Applies to domains and OUs.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermSOMLogging(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermSOMPlanning**
</dt> <dd> <dl>

Constant value that corresponds to the **permSOMPlanning** permission type. Applies to domains and OUs.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermSOMPlanning(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermSOMWMICreate**
</dt> <dd> <dl>

Constant value that corresponds to the **permSOMWMICreate** permission type. Applies to domains only.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermSOMWMICreate(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermSOMWMIFullControl**
</dt> <dd> <dl>

Constant value that corresponds to the **permSOMWMIFullControl** permission type. Applies to domains only.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermSOMWMIFullControl(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermWMIFilterCustom**
</dt> <dd> <dl>

Constant value that corresponds to the **permWMIFilterCustom** permission type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermWMIFilterCustom(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermWMIFilterEdit**
</dt> <dd> <dl>

Constant value that corresponds to the **permWMIFilterEdit** permission type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermWMIFilterEdit(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**PermWMIFilterFullControl**
</dt> <dd> <dl>

Constant value that corresponds to the **permWMIFilterFullControl** permission type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PermWMIFilterFullControl(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**ProcessSecurity**
</dt> <dd> <dl>

Value that corresponds to the **GPM\_PROCESS\_SECURITY** constant.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ProcessSecurity(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

[**ReportHTML**](igpmconstants.md)
</dt> <dd> <dl>

Value that corresponds to the **ReportHTML** property. Passed to **GenerateReport** methods to generate a report in HTML.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ReportHTML(
  [out] GPMReportType* pVal
);
```


</dt> </dl> </dd> <dt>

[**ReportXML**](igpmconstants.md)
</dt> <dd> <dl>

Value that corresponds to the **ReportXML** property. Passed to **GenerateReport** methods to generate a report in XML.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ReportXML(
  [out] GPMReportType* pVal
);
```


</dt> </dl> </dd> <dt>

**RsopLoggingNoComputer**
</dt> <dd> <dl>

Value that corresponds to the **RSOP\_NO\_USER** constant.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_RsopLoggingNoComputer(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**RsopLoggingNoUser**
</dt> <dd> <dl>

Value that corresponds to the **RSOP\_NO\_USER** constant.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_RsopLoggingNoUser(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**RSOPModeLogging**
</dt> <dd> <dl>

Value that corresponds to the **RSOPModeLogging** property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_RSOPModeUnknown(
  [out] GPMRSOPMode* pVal
);
```


</dt> </dl> </dd> <dt>

**RSOPModePlanning**
</dt> <dd> <dl>

Value that corresponds to the **RSOPModePlanning** property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_RSOPModePlanning(
  [out] GPMRSOP* pVal
);
```


</dt> </dl> </dd> <dt>

[**RSOPModeUnknown**](igpmconstants.md)
</dt> <dd> <dl>

Value that corresponds to the **RSOPModeUnknown** property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_RSOPModeUnknown(
  [out] GPMRSOPMode* pVal
);
```


</dt> </dl> </dd> <dt>

**RsopPlanningAssumeCompWQLFilterTrue**
</dt> <dd> <dl>

Value that corresponds to the **RSOP\_PLANNING\_ASSUME\_COMP\_WQLFILTER\_TRUE** constant.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_RSOPModeUnknown(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**RsopPlanningAssumeSlowLink**
</dt> <dd> <dl>

Value that corresponds to the **RSOP\_PLANNING\_ASSUME\_SLOW\_LINK** constant.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_RsopPlanningAssumeSlowLink(
  [out] long pVal
);
```


</dt> </dl> </dd> <dt>

**RsopPlanningAssumeUserWQLFilterTrue**
</dt> <dd> <dl>

Value that corresponds to the **RSOP\_PLANNING\_ASSUME\_USER\_WQLFILTER\_TRUE** constant.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_RSOPModeUnknown(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**RsopPlanningLoopbackOption**
</dt> <dd> <dl>

If *vbMerge* is **VARIANT\_TRUE**, *pval* corresponds to the **RSOP\_PLANNING\_ASSUME\_LOOPBACK\_MERGE** constant. If *vbMerge* is **VARIANT\_FALSE**, *pval* corresponds to the **RSOP\_PLANNING\_ASSUME\_LOOPBACK\_REPLACE** constant.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_RsopPlanningLoopbackOption(
  [in] VARIANT_BOOL vbMerge,
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchOpContains**
</dt> <dd> <dl>

Constant value that corresponds to the **opContains** search operator.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchOpContains(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchOpEquals**
</dt> <dd> <dl>

Constant value that corresponds to the **opEquals** search operator.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchOpEquals(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchOpNotContains**
</dt> <dd> <dl>

Constant value that corresponds to the **opNotContains** search operator.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchOpNotContains(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchOpNotEquals**
</dt> <dd> <dl>

Constant value that corresponds to the **opNotEquals** search operator.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchOpNotEquals(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchPropertyBackupMostRecent**
</dt> <dd> <dl>

Constant value that corresponds to the **backupMostRecent** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyBackupMostRecent(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchPropertyGPOComputerExtensions**
</dt> <dd> <dl>

Constant value that corresponds to the **gpoComputerExtensions** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyGPOComputerExtensions(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchPropertyGPODisplayName**
</dt> <dd> <dl>

Constant value that corresponds to the **gpoDisplayName** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyGPODisplayName(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchPropertyGPODomain**
</dt> <dd> <dl>

Constant value that corresponds to the **gpoDomain** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyGPODomain(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchPropertyGPOEffectivePermissions**
</dt> <dd> <dl>

Constant value that corresponds to the **gpoEffectivePermissions** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyGPOEffectivePermissions(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchPropertyGPOID**
</dt> <dd> <dl>

Constant value that corresponds to the **gpoID** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyGPOID(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchPropertyGPOPermissions**
</dt> <dd> <dl>

Constant value that corresponds to the **gpoPermissions** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyGPOPermissions(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchPropertyGPOUserExtensions**
</dt> <dd> <dl>

Constant value that corresponds to the **gpoUserExtensions** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyGPOUserExtensions(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchPropertyGPOWMIFilter**
</dt> <dd> <dl>

Constant value that corresponds to the **gpoWMIFilter** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertyGPOWMIFilter(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SearchPropertySOMLinks**
</dt> <dd> <dl>

Constant value that corresponds to the **somLinks** search property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SearchPropertySOMLinks(
  [out] GPMSearchProperty* pVal
);
```


</dt> </dl> </dd> <dt>

**SecurityFlags**
</dt> <dd> <dl>

The value of the [**SecurityFlags**](igpmconstants-get-securityflags.md) property, which represents the portion of the security descriptor that you want to retrieve or set for a Group Policy object (GPO); for example, the discretionary access control list (DACL), the system access control list (SACL), the group, or the owner. You can pass the returned value in the *ulFlags* parameter to the [**IGPMGPO::GetSecurityDescriptor**](igpmgpo-getsecuritydescriptor.md) and [**IGPMGPO::SetSecurityDescriptor**](igpmgpo-setsecuritydescriptor.md) functions.

This property takes four parameters. Pass in the boolean values that represent the portions of the security descriptor that you want to retrieve or set. For example, a call to this property using VBScript as follows.

`SecurityFlags = GPMConstants.SecurityFlags(bOwner, bGroup, bDACL, bSACL)`

For more information about the **SecurityFlags** property, see [**get\_SecurityFlags**](igpmconstants-get-securityflags.md).

<dt>

Access type: Read/write
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SecurityFlags(
  [in] VARIANT_BOOL vbOwner,
  [in] VARIANT_BOOL vbGroup,
  [in] VARIANT_BOOL vbDACL,
  [in] VARIANT_BOOL vbSACL,
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**SOMDomain**
</dt> <dd> <dl>

Constant value that corresponds to the **somDomain** SOM type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SOMDomain(
  [out] GPMSOMType* pVal
);
```


</dt> </dl> </dd> <dt>

**SOMOU**
</dt> <dd> <dl>

Constant value that corresponds to the **somOU** SOM type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SOMOU(
  [out] GPMSOMType* pVal
);
```


</dt> </dl> </dd> <dt>

**SOMSite**
</dt> <dd> <dl>

Constant value that corresponds to the **somSite** SOM type.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_SOMSite(
  [out] GPMSOMType* pVal
);
```


</dt> </dl> </dd> <dt>

**UseAnyDC**
</dt> <dd> <dl>

Value that corresponds to the **UseAnyDC** property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_UseAnyDC(
  [out] long* pVal
);
```


</dt> </dl> </dd> <dt>

**UsePDC**
</dt> <dd> <dl>

Value that corresponds to the **UsePDC** property.

<dt>

Access type: Read-only
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_UsePDC(
  [out] long* pVal
);
```


</dt> </dl> </dd> </dl>

 

## Remarks

Properties that begin with **PermGPO** apply only to Group Policy objects (GPOs). Properties that begin with **PermWMIFilter** apply only to Windows Management Instrumentation (WMI) filters.

For more information about policy-related permissions, see [**IGPM::CreatePermission**](igpm-createpermission.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl> |
| IID<br/>                      | IID\_IGPMConstants is defined as 50EF73E6-D35C-4C8D-BE63-7EA5D2AAC5C4<br/>      |



## See also

<dl> <dt>

[**IGPMConstants**](igpmconstants.md)
</dt> <dt>

[**IGPM**](igpm.md)
</dt> </dl>

 

 





