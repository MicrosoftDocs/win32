---
title: Creating an Application Directory Partition
description: An application directory partition is represented by a domainDNS object with an instanceType attribute value of DS\_INSTANCETYPE\_IS\_NC\_HEAD combined with DS\_INSTANCETYPE\_NC\_IS\_WRITEABLE.
ms.assetid: 5e90f316-9d67-484d-98b8-0632dd3c2c43
ms.tgt_platform: multiple
keywords:
- Creating an Application Directory Partition AD
- Application Directory Partitions AD , Creating
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Application Directory Partition

An application directory partition is represented by a [**domainDNS**](/windows/desktop/ADSchema/c-domaindns) object with an [**instanceType**](/windows/desktop/ADSchema/a-instancetype) attribute value of **DS\_INSTANCETYPE\_IS\_NC\_HEAD** combined with **DS\_INSTANCETYPE\_NC\_IS\_WRITEABLE**. This **domainDNS** object represents the application directory partition root (NC head), and is named similar to a regular domain partition, for example, "DC=dynamicdata,DC=fabrikam,DC=com", which corresponds to a DNS name of "dynamicdata.fabrikam.com". An application directory partition can, therefore, be instantiated anywhere a domain partition can be instantiated. There is no NetBIOS name associated with an application directory partition.

It is possible to nest application directory partitions, that is, an application directory partition can have child application directory partitions. Searches with subtree scope rooted at an application directory partition head will generate continuation references to the child application directory partitions.

An application directory partition replica can only be created on a domain controller that is running on Windows Server 2003 and later and only while the Domain-Naming FSMO role is held by a Windows Server 2003 and later domain controller. In a mixed forest that has both Windows Server 2003 domain controllers and down-level domain controllers (Windows 2000 domain controllers or Windows NT 4.0 primary domain controllers), an attempt to create an application directory partition replica on a down-level domain controller will fail.

An application directory partition also has a corresponding [**crossRef**](/windows/desktop/ADSchema/c-crossref) object in the Partitions container of the configuration partition. The **crossRef** can be pre-created manually before creating the [**domainDNS**](/windows/desktop/ADSchema/c-domaindns) object. The pre-created **crossRef** object must have the attribute values shown in the following table or the partition creation will fail. If the **crossRef** object does not exist, the Active Directory server will create one when the application directory partition is created.

| Attribute                          | Description                                                                                                                               |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**dnsRoot**](/windows/desktop/ADSchema/a-dnsroot) | Contains the DNS path of the domain controller that the application directory partition will be created on.                               |
| [**Enabled**](/windows/desktop/ADSchema/a-enabled) | Contains **FALSE**.                                                                                                                       |
| [**nCName**](/windows/desktop/ADSchema/a-ncname)   | Contains the distinguished name of the partition. In the example above, this attribute would contain "DC=dynamicdata,DC=mydomain,DC=com". |



 

**To create a new application directory partition with its first replica, perform the following steps**

1.  Bind to the namespace for the new partition, specifying the domain controller that will host the application directory partition in the ADsPath. For example, to create a partition with an ADsPath of "DC=dynamicdata,DC=mydomain,DC=com", the binding ADsPath would be "LDAP://\<domain controller\>/DC=mydomain,DC=com", where "&lt;domain controller&gt;" is the DNS name of the domain controller that will host the partition.

    The bind operation must specify the fast and delegation options. The fast option allows the bind to succeed even if the namespace does not exist. The delegation option is required to allow the domain controller to contact the Domain-Naming FSMO role holder using the same credentials.

    The system version of the domain controller must be Windows Server 2003 operating system and later.

2.  Create a [**domainDNS**](/windows/desktop/ADSchema/c-domaindns) object with an appropriate name for the partition, for example, "DC=dynamicdata", to represent the naming context head for the new partition. The **domainDNS** object must have an [**instanceType**](/windows/desktop/ADSchema/a-instancetype) attribute with a value of 5 (**DS\_INSTANCETYPE\_IS\_NC\_HEAD** \| **DS\_INSTANCETYPE\_NC\_IS\_WRITEABLE**). The **instanceType** attribute can only be set at creation time because it is a system-only attribute.

When the [**domainDNS**](/windows/desktop/ADSchema/c-domaindns) object is created, the Active Directory server will perform the following steps:

1.  Searches for a [**crossRef**](/windows/desktop/ADSchema/c-crossref) object in the Partitions container that has an [**nCName**](/windows/desktop/ADSchema/a-ncname) attribute value that matches the distinguished name of the partition and, if a match is found, modifies the **crossRef** object to represent the application directory partition. If a matching **crossRef** object is not found, the Active Directory server creates a new **crossRef** object to represent the application directory partition.

    The following table lists important attributes of the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object.

    | Attribute                                                              | Description                                                                                                                                        |
    |------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
    | [**nCName**](/windows/desktop/ADSchema/a-ncname)                                       | Contains the distinguished name of the partition.                                                                                                  |
    | [**dnsRoot**](/windows/desktop/ADSchema/a-dnsroot)                                     | Contains the DNS name of the partition.                                                                                                            |
    | [**msDS-NC-Replica-Locations**](/windows/desktop/ADSchema/a-msds-nc-replica-locations) | The distinguished name of the [**nTDSDSA**](/windows/desktop/ADSchema/c-ntdsdsa) object of the domain controller for the first replica is added to this attribute. |

    

     

2.  Initiate a synchronization of the configuration partition and wait for completion. This enables the client application to modify configuration parameters for the newly created application directory partition while bound to the same domain controller used for creating the application directory partition.
3.  Create the [**domainDNS**](/windows/desktop/ADSchema/c-domaindns) object with the **DS\_INSTANCETYPE\_IS\_NC\_HEAD** and **DS\_INSTANCETYPE\_NC\_IS\_WRITEABLE** flags set on the [**instanceType**](/windows/desktop/ADSchema/a-instancetype) property. The **instanceType** property may contain other, private flags as well.
4.  Populate the [**ms-DS-Has-Master-NCs**](/windows/desktop/ADSchema/a-msds-hasmasterncs) attribute of the [**nTDSDSA**](/windows/desktop/ADSchema/c-ntdsdsa) object for the target domain controller with the distinguished name of the newly created application directory partition.

When the application directory partition is created, or when a new replica of the application directory partition is added and fully synchronized, the Active Directory server correctly registers the replica with NetLogon and DNS. For more information, and a list of the registered SRV records, see [Locating an Application Directory Partition Host Server](locating-an-application-directory-partition-host-server.md).

For more information about creating an application directory partition, see [Example Code for Creating an Application Directory Partition](example-code-for-creating-an-application-directory-partition.md).

## Locating the Partitions Container

The distinguished name of the Partitions container can be found in one of two ways. The first is more complicated to perform, but will always provide an accurate result:

1.  Bind to RootDSE and obtain the **configurationNamingContext** attribute.
2.  Use the **configurationNamingContext** attribute to bind to the configuration container.
3.  Search in the configuration container for an object that is of the [**crossRefContainer**](/windows/desktop/ADSchema/c-crossrefcontainer) type.
4.  Obtain the **distinguishedName** attribute value of the [**crossRefContainer**](/windows/desktop/ADSchema/c-crossrefcontainer) object. This will be the distinguished name of the Partitions container.

For more information and a code example that shows this method for locating the Partitions container, see the **GetPartitionsDNSearch** function in [Example Code for Locating the Partitions Container](example-code-for-locating-the-partitions-container.md).

The second method is easier to implement, but relies on the Partitions container having a particular relative distinguished name. It is not currently possible to change the name of the Partitions container, but if this capability is added in the future, the procedure below will not work correctly if the Partitions container has been renamed.

1.  Bind to RootDSE and obtain the **configurationNamingContext** attribute.
2.  Combine the string "CN=Partitions," followed by the **configurationNamingContext** attribute to form the distinguished name of the Partitions container. The distinguished name will be in the form "CN=Partitions,\<configuration DN\>".

For more information and a code example that shows this method for locating the Partitions container, see the **GetPartitionsDNManual** function in [Example Code for Locating the Partitions Container](example-code-for-locating-the-partitions-container.md).

 

 