---
title: MDM\_EnterpriseModernAppManagement\_AppInstallation01\_01 class
description: The MDM\_EnterpriseModernAppManagement\_AppInstallation01\_01 class is used to install apps from the Windows Store or a hosted location.
ms.assetid: fc4c4c82-6f43-41fc-863b-940c0517f28b
keywords:
- MDM_EnterpriseModernAppManagement_AppInstallation01_01 class
- MDM_EnterpriseModernAppManagement_AppInstallation01_01 class, described
topic_type:
- apiref
api_name:
- MDM_EnterpriseModernAppManagement_AppInstallation01_01
- MDM_EnterpriseModernAppManagement_AppInstallation01_01.InstanceID
- MDM_EnterpriseModernAppManagement_AppInstallation01_01.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MDM\_EnterpriseModernAppManagement\_AppInstallation01\_01 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_EnterpriseModernAppManagement\_AppInstallation01\_01** class is used to install apps from the Windows Store or a hosted location.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system", "local-user"), dynamic, provider("DMWmiBridgeProv")]
class MDM_EnterpriseModernAppManagement_AppInstallation01_01
{
  string InstanceID;
  string ParentID;
  sint32 LastError;
  string LastErrorDesc;
  sint32 Status;
  sint32 ProgressStatus;
};
```

## Members

The **MDM\_EnterpriseModernAppManagement\_AppInstallation01\_01** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_EnterpriseModernAppManagement\_AppInstallation01\_01** class has these methods.



| Method                                                                                                    | Description                                                                                                                                |
|:----------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**HostedInstallMethod**](mdm-enterprisemodernappmanagement-appinstallation01-01-hostedinstallmethod.md) | Method to perform an install of an app package from a hosted location (this can be a local drive, a UNC, or https data source).<br/> |
| [**StoreInstallMethod**](mdm-enterprisemodernappmanagement-appinstallation01-01-storeinstallmethod.md)   | Method to perform an install of an app and a license from the Windows Store.<br/>                                                    |



 

### Properties

The **MDM\_EnterpriseModernAppManagement\_AppInstallation01\_01** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies the name of the parent node. For this class, the string is "AppInstallation".

</dd> <dt>

[LastError](https://docs.microsoft.com/windows/client-management/mdm/enterprisemodernappmanagement-csp#appinstallation-packagefamilyname-lasterror)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[LastErrorDesc](https://msdn.microsoft.com/windows/hardware/commercialize/customize/mdm/enterprisemodernappmanagement-csp#appinstallation-packagefamilyname-lasterrordescription)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/EnterpriseModernAppManagement/AppInstallation"

</dd> <dt>

[ProgressStatus](https://msdn.microsoft.com/windows/hardware/commercialize/customize/mdm/enterprisemodernappmanagement-csp#appinstallation-packagefamilyname-progessstatus)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[Status](https://docs.microsoft.com/windows/client-management/mdm/enterprisemodernappmanagement-csp#appinstallation-packagefamilyname-status)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](https://msdn.microsoft.com/library/windows/hardware/mt614877)
</dt> </dl>

 

 





