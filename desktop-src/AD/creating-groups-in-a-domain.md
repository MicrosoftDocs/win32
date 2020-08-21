---
title: Creating Groups in a Domain
description: A group object is created in Active Directory Domain Services in the domain container where the new group will be contained.
ms.assetid: 40792878-4219-4242-8cf7-b092b28f2ff4
ms.tgt_platform: multiple
keywords:
- groups AD ,creating groups in a domain
ms.topic: article
ms.date: 05/31/2018
---

# Creating Groups in a Domain

A group object is created in Active Directory Domain Services in the domain container where the new group will be contained. Groups can be created at the root of the domain, within an organizational unit, or within a container. To create a group object, use the [**IADsContainer::Create**](/windows/desktop/api/iads/nf-iads-iadscontainer-create) or the [**IDirectoryObject::CreateDSObject**](/windows/desktop/api/iads/nf-iads-idirectoryobject-createdsobject) method.

The following attributes are required to make the group object a legal group that the Active Directory server and the Windows security system will recognize:

<dl> <dt>

<span id="cn"></span><span id="CN"></span>**cn**
</dt> <dd>

Specifies the name of the group object in the directory. This will be the object's relative distinguished name within the container where the group is created.

</dd> <dt>

<span id="groupType"></span><span id="grouptype"></span><span id="GROUPTYPE"></span>**groupType**
</dt> <dd>

Contains an integer that specifies the group type and scope. The [**ADS\_GROUP\_TYPE\_ENUM**](/windows/win32/api/iads/ne-iads-ads_group_type_enum) enumeration defines the possible values for the **groupType** attribute.

The following list defines common group types and values for this attribute.

<dl> <dt>

<span id="Domain_Local_Distribution"></span><span id="domain_local_distribution"></span><span id="DOMAIN_LOCAL_DISTRIBUTION"></span>Domain Local Distribution
</dt> <dd>

**ADS\_GROUP\_TYPE\_DOMAIN\_LOCAL\_GROUP**

</dd> <dt>

<span id="Domain_Local_Security"></span><span id="domain_local_security"></span><span id="DOMAIN_LOCAL_SECURITY"></span>Domain Local Security
</dt> <dd>

**ADS\_GROUP\_TYPE\_DOMAIN\_LOCAL\_GROUP** \| **ADS\_GROUP\_TYPE\_SECURITY\_ENABLED**

</dd> <dt>

<span id="Global_Distribution"></span><span id="global_distribution"></span><span id="GLOBAL_DISTRIBUTION"></span>Global Distribution
</dt> <dd>

**ADS\_GROUP\_TYPE\_GLOBAL\_GROUP**

</dd> <dt>

<span id="Global_Security"></span><span id="global_security"></span><span id="GLOBAL_SECURITY"></span>Global Security
</dt> <dd>

**ADS\_GROUP\_TYPE\_GLOBAL\_GROUP** \| **ADS\_GROUP\_TYPE\_SECURITY\_ENABLED**

</dd> <dt>

<span id="Universal_Distribution"></span><span id="universal_distribution"></span><span id="UNIVERSAL_DISTRIBUTION"></span>Universal Distribution
</dt> <dd>

**ADS\_GROUP\_TYPE\_UNIVERSAL\_GROUP**

</dd> <dt>

<span id="Universal_Security"></span><span id="universal_security"></span><span id="UNIVERSAL_SECURITY"></span>Universal Security
</dt> <dd>

**ADS\_GROUP\_TYPE\_UNIVERSAL\_GROUP** \| **ADS\_GROUP\_TYPE\_SECURITY\_ENABLED**

</dd> <dt>


</dt> <dd>

</dd> </dl>

If the group is intended for setting access control on directory objects, the group should be a Global Security or Universal Security group.

Be aware that Universal Security groups can only be created on Windows 2000 domains running in native mode. For more information about detecting mixed and native mode, see [Detecting the Operation Mode of a Domain](detecting-the-operation-mode-of-a-domain.md).

</dd> <dt>

<span id="sAMAccountName"></span><span id="samaccountname"></span><span id="SAMACCOUNTNAME"></span>**sAMAccountName**
</dt> <dd>

Contains a string that is the name used to support clients and servers from a previous version. The **sAMAccountName** should be less than 20 characters to support clients of a previous version of Windows.

The **sAMAccountName** must be unique among all security principal objects within the domain. A query should be performed against the domain to verify that the **sAMAccountName** is unique within the domain.

</dd> </dl>

The members of the group can be added at creation time using the [**IDirectoryObject::CreateDSObject**](/windows/desktop/api/iads/nf-iads-idirectoryobject-createdsobject) method. Optionally, members can be added to the group after creation using the [**IADsGroup::Add**](/windows/desktop/api/iads/nf-iads-iadsgroup-add) method. For more information about adding members to a group, see [Adding Members to Groups in a Domain](adding-members-to-groups-in-a-domain.md).

 

 