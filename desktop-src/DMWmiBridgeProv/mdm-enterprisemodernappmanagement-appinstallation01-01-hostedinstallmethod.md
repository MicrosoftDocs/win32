---
title: HostedInstallMethod method of the MDM_EnterpriseModernAppManagement_AppInstallation01_01 class
description: Method to perform an install of an app package from a hosted location, such as a local drive, a UNC, or HTTPS data source. See also, HostedInstall.
ms.assetid: 1ec16315-75ce-4613-804e-6b587c4071d6
keywords:
- HostedInstallMethod method
- HostedInstallMethod method, MDM_EnterpriseModernAppManagement_AppInstallation01_01 class
- MDM_EnterpriseModernAppManagement_AppInstallation01_01 class, HostedInstallMethod method
topic_type:
- apiref
api_name:
- MDM_EnterpriseModernAppManagement_AppInstallation01_01.HostedInstallMethod
api_location:
- DMWmiBridgeProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# HostedInstallMethod method of the MDM\_EnterpriseModernAppManagement\_AppInstallation01\_01 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Method to perform an install of an app package from a hosted location, such as a local drive, a UNC, or HTTPS data source. See also, [HostedInstall](/windows/client-management/mdm/enterprisemodernappmanagement-csp).

## Syntax


```mof
uint32 HostedInstallMethod(
  [in] string param
);
```



## Parameters

<dl> <dt>

*param* \[in\]
</dt> <dd></dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MDM\_EnterpriseModernAppManagement\_AppInstallation01\_01**](mdm-enterprisemodernappmanagement-appinstallation01-01.md)
</dt> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

