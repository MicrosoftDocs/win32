---
Description: 'Describes the NCSI Policy settings.'
ms.assetid: '71876e4a-c938-4307-b730-48b1f5000f12'
title: 'MSFT\_NCSIPolicyConfiguration class'
---

# MSFT\_NCSIPolicyConfiguration class

Describes the NCSI Policy settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetNCCim")]
class MSFT_NCSIPolicyConfiguration : MSFT_NetSettingData
{
  string CorporateDNSProbeHostAddress;
  string CorporateDNSProbeHostName;
  string CorporateSitePrefixList;
  string CorporateWebsiteProbeURL;
  string DomainLocationDeterminationURL;
  string PolicyStore;
};
```

## Members

The **MSFT\_NCSIPolicyConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NCSIPolicyConfiguration** class has these methods.



| Method                                                                       | Description                                                          |
|:-----------------------------------------------------------------------------|:---------------------------------------------------------------------|
| [**GetConfig**](https://msdn.microsoft.com/library/hh832863) | Obtains the configuration given a specified policy store.<br/> |



 

### Properties

The **MSFT\_NCSIPolicyConfiguration** class has these properties.

<dl> <dt>

**CorporateDNSProbeHostAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the expected address of the host name used as for the DNS probe.

</dd> <dt>

**CorporateDNSProbeHostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the host name of a PC known to be on the corporate network.

</dd> <dt>

**CorporateSitePrefixList**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the list of IPv6 corporate site prefixes that should be monitored for corporate connectivity.

</dd> <dt>

**CorporateWebsiteProbeURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the URL of the corporate website being used to perform an active probe against.

</dd> <dt>

**DomainLocationDeterminationURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the HTTPS URL of the corporate website being used to determine whether the current domain location is inside or outside the corporate domain.

</dd> <dt>

**PolicyStore**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the store from which to retrieve the NCSI configuration policy.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetNCCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetNCCim.dll</dt> </dl> |



 

 




