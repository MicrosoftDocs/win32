---
title: MDM_Policy_Result01_Connectivity02 class
description: The MDM\_Policy\_Result01\_Connectivity02 class represents the connection policies available.
ms.assetid: af5f21f8-8010-4e5a-b75f-30032333d87d
keywords:
- MDM_Policy_Result01_Connectivity02 class
- MDM_Policy_Result01_Connectivity02 class, described
topic_type:
- apiref
api_name:
- MDM_Policy_Result01_Connectivity02
- MDM_Policy_Result01_Connectivity02.InstanceID
- MDM_Policy_Result01_Connectivity02.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MDM\_Policy\_Result01\_Connectivity02 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_Policy\_Result01\_Connectivity02** class represents the connection policies available.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_Policy_Result01_Connectivity02
{
  string InstanceID;
  string ParentID;
  sint32 AllowBluetooth;
  sint32 AllowCellularData;
  sint32 AllowCellularDataRoaming;
  sint32 AllowVPNOverCellular;
  sint32 AllowVPNRoamingOverCellular;
  string DisableInternetDownloadForWebPublishingAndOnlineOrderingWizards;
  string DisableDownloadingOfPrintDriversOverHTTP;
  string DiablePrintingOverHTTP;
  string HardenedUNCPaths;
  string ProhibitInstallationAndConfigurationOfNetworkBridge;
  sint32 DisallowNetworkConnectivityActiveTests;
  sint32 AllowConnectedDevices;
};
```

## Members

The **MDM\_Policy\_Result01\_Connectivity02** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_Policy\_Result01\_Connectivity02** class has these properties.

<dl> <dt>

[AllowBluetooth](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-allowbluetooth)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowCellularData](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-allowcellulardata)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowCellularDataRoaming](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-allowcellulardataroaming)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowConnectedDevices](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-allowconnecteddevices)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowVPNOverCellular](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-allowvpnovercellular)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[AllowVPNRoamingOverCellular](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-allowvpnroamingovercellular)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DiablePrintingOverHTTP](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-diableprintingoverhttp)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisableDownloadingOfPrintDriversOverHTTP](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-disabledownloadingofprintdriversoverhttp)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisableInternetDownloadForWebPublishingAndOnlineOrderingWizards](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-disableinternetdownloadforwebpublishingandonlineorderingwizards)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[DisallowNetworkConnectivityActiveTests](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-disallownetworkconnectivityactivetests)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[HardenedUNCPaths](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-hardeneduncpaths)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "Connectivity".

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/Policy/Result"

</dd> <dt>

[ProhibitInstallationAndConfigurationOfNetworkBridge](https://docs.microsoft.com/windows/client-management/mdm/policy-csp-connectivity#connectivity-prohibitinstallationandconfigurationofnetworkbridge)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM\\DMMap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](https://msdn.microsoft.com/library/windows/hardware/mt614877)
</dt> </dl>

 

 





