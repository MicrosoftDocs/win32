---
title: MSFT\_ServerFeature class
description: Represents a server feature on the managed node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 05b22ce0-fdef-4ddf-95e7-6628408766d6
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_ServerFeature class
- MSFT_ServerFeature class, described
topic_type:
- apiref
api_name:
- MSFT_ServerFeature
- MSFT_ServerFeature.Id
- MSFT_ServerFeature.ParentName
- MSFT_ServerFeature.UniqueName
- MSFT_ServerFeature.DisplayName
- MSFT_ServerFeature.State
- MSFT_ServerFeature.Type
- MSFT_ServerFeature.ConfigurationStatus
- MSFT_ServerFeature.EventQuery
- MSFT_ServerFeature.Services
- MSFT_ServerFeature.BpaModels
api_location:
- MgmtProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_ServerFeature class

Represents a server feature on the managed node.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mgmtprovider"), AMENDMENT]
class MSFT_ServerFeature
{
  sint32 Id;
  string ParentName;
  string UniqueName;
  string DisplayName;
  uint8  State;
  uint8  Type;
  uint8  ConfigurationStatus;
  string EventQuery;
  string Services[];
  string BpaModels[];
};
```

## Members

The **MSFT\_ServerFeature** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerFeature** class has these properties.

<dl> <dt>

**BpaModels**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the BPA models of the feature.

</dd> <dt>

**ConfigurationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The configuration status of the feature.

<dt>

<span id="Configuration_Failed"></span><span id="configuration_failed"></span><span id="CONFIGURATION_FAILED"></span>

**Configuration Failed** (0)


</dt> <dd></dd> <dt>

<span id="Not_Configured"></span><span id="not_configured"></span><span id="NOT_CONFIGURED"></span>

**Not Configured** (1)


</dt> <dd></dd> <dt>

<span id="Configured"></span><span id="configured"></span><span id="CONFIGURED"></span>

**Configured** (2)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The localized name of the feature.

</dd> <dt>

**EventQuery**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file name of the event query for the feature.

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the feature.

</dd> <dt>

**ParentName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The feature's parent name.

</dd> <dt>

**Services**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the services for the feature.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The install state of the feature.

<dt>

<span id="Available"></span><span id="available"></span><span id="AVAILABLE"></span>

**Available** (0)


</dt> <dd></dd> <dt>

<span id="Installed"></span><span id="installed"></span><span id="INSTALLED"></span>

**Installed** (1)


</dt> <dd></dd> <dt>

<span id="Uninstall_Pending"></span><span id="uninstall_pending"></span><span id="UNINSTALL_PENDING"></span>

**Uninstall Pending** (2)


</dt> <dd></dd> <dt>

<span id="Install_Pending"></span><span id="install_pending"></span><span id="INSTALL_PENDING"></span>

**Install Pending** (3)


</dt> <dd></dd> <dt>

<span id="Not_Present"></span><span id="not_present"></span><span id="NOT_PRESENT"></span>

**Not Present** (4)


</dt> <dd></dd> <dt>

<span id="Removed"></span><span id="removed"></span><span id="REMOVED"></span>

**Removed** (5)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of the feature.

<dt>

<span id="Role"></span><span id="role"></span><span id="ROLE"></span>

**Role** (0)


</dt> <dd></dd> <dt>

<span id="Role_Service"></span><span id="role_service"></span><span id="ROLE_SERVICE"></span>

**Role Service** (1)


</dt> <dd></dd> <dt>

<span id="Feature"></span><span id="feature"></span><span id="FEATURE"></span>

**Feature** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**UniqueName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the feature.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



 

 





