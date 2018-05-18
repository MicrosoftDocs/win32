---
title: CIM\_SettingData class
description: The SettingData class represents configuration-related and operational parameters for one or more ManagedElements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '66df1be8-103b-45ea-a209-9a62ee3e33b5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_SettingData class iSCSI Software Target API", "CIM_SettingData class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_SettingData
- CIM_SettingData.Caption
- CIM_SettingData.Description
- CIM_SettingData.InstanceID
- CIM_SettingData.ElementName
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_SettingData class

The SettingData class represents configuration-related and operational parameters for one or more ManagedElements. A ManagedElement can have multiple SettingData objects associated with it. The current operational values for the parameters of the element are reflected by properties in the Element itself or by properties in its associations. These properties do not have to be the same values that are present in the SettingData object. For example, a modem might have a SettingData baud rate of 56Kb/sec but be operating at 19.2Kb/sec.

Note: The CIM\_SettingData class is very similar to CIM\_Setting, yet both classes are present in the model because many implementations have successfully used CIM\_Setting. However, issues have arisen that could not be resolved without defining a new class. Therefore, until a new major release occurs, both classes will exist in the model. Refer to the Core White Paper for additional information. SettingData instances can be aggregated together into higher- level SettingData objects using ConcreteComponent associations.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::Settings")]
class CIM_SettingData : CIM_ManagedElement
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
};
```

## Members

The **CIM\_SettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SettingData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("ElementName")
</dt> </dl>

The user-friendly name for this instance of SettingData. In addition, the user-friendly name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.)

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon (:), and where &lt;OrgID&gt; must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance.

For DMTF-defined instances, the "preferred" algorithm must be used with the &lt;OrgID&gt; set to CIM.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

 





