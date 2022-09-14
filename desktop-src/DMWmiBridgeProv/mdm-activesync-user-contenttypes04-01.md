---
title: MDM_ActiveSync_User_ContentTypes04_01 class
description: The MDM\_ActiveSync\_User\_ContentTypes04\_01 class defines the type of content to be individually enabled/disabled for sync.
ms.assetid: 82759cf9-ea2a-4d75-bb07-6832c3005074
keywords:
- MDM_ActiveSync_User_ContentTypes04_01 class
- MDM_ActiveSync_User_ContentTypes04_01 class, described
topic_type:
- apiref
api_name:
- MDM_ActiveSync_User_ContentTypes04_01
- MDM_ActiveSync_User_ContentTypes04_01.InstanceID
- MDM_ActiveSync_User_ContentTypes04_01.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_ActiveSync\_User\_ContentTypes04\_01 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_ActiveSync\_User\_ContentTypes04\_01** class defines the type of content to be individually enabled/disabled for sync.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-user"), dynamic, provider("DMWmiBridgeProv")]
class MDM_ActiveSync_User_ContentTypes04_01
{
  string InstanceID;
  string ParentID;
  string Enabled;
  string Name;
};
```

## Members

The **MDM\_ActiveSync\_User\_ContentTypes04\_01** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_ActiveSync\_User\_ContentTypes04\_01** class has these properties.

<dl> <dt>

[Enabled](/windows/client-management/mdm/activesync-csp#options-contenttypes-content-type-guid-enabled)
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

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the name of the parent node.

</dd> <dt>

[Name](/windows/client-management/mdm/activesync-csp#options-contenttypes-content-type-guid-name)
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

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/ActiveSync/Accounts/*GUID*/Options"

</dd> </dl>

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

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

