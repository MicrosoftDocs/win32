---
Description: View is an abstract class that provides a common superclass for classes providing de-normalized, aggregate representations of managed resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5c6ce984-8fc2-405c-a60c-dd2208ab6425
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_View class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_View class

View is an abstract class that provides a common superclass for classes providing de-normalized, aggregate representations of managed resources. The definition of each sub-class will include properties propagated from the graph of classes that are used to model the resource in the normalized view. The classes may be resource classes or associations. The definition of how a value is propagated (i.e. source class and value transformations) is required to be specified. Sub-classes may be explicitly constrained to be read only. If a sub-class is not constrained as read only, the designers are strongly encouraged to carefully consider the data synchronization and consistencies issues that may result. The ElementView association may be used to find the instances that form the normalized view of the managed resource.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), Abstract, Version("2.26.0"), AMENDMENT]
class CIM_View : CIM_ManagedElement
{
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **CIM\_View** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_View** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM\_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: &lt;OrgID&gt;:&lt;LocalID&gt; Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon (:), and where &lt;OrgID&gt; must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;. &lt;LocalID&gt; is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the &lt;OrgID&gt; set to CIM.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>Pcsvdevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



 

 




