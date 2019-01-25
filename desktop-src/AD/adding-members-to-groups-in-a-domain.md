---
title: Adding Members to Groups in a Domain
description: This topic shows how to add members to groups in a domain.
ms.assetid: be65cd4e-df3e-416b-a673-774b71ab6996
ms.tgt_platform: multiple
keywords:
- Adding Members to Groups in a Domain AD
- Groups AD , Adding Members to Groups in a Domain
ms.topic: article
ms.date: 05/31/2018
---

# Adding Members to Groups in a Domain

A group can contain any number of users, contacts, or other groups as members. The following list lists the attributes of the group object that control group membership.



| Attribute                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**member**](https://msdn.microsoft.com/library/ms677097)<br/>     | The [**member**](https://msdn.microsoft.com/library/ms677097) attribute contains the distinguished names for the objects that are members of the group.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**memberOf**](https://msdn.microsoft.com/library/ms677099)<br/> | The [**memberOf**](https://msdn.microsoft.com/library/ms677099) attribute contains the distinguished names of groups that contain the group as a direct member. The **memberOf** attribute does not contain any inherited group membership data. For example, if GroupA is a member of GroupB and GroupB is a member of GroupC, the **memberOf** attribute for GroupA will contain GroupB, but not GroupC.<br/> The Active Directory server maintains this property. When a distinguished name is added to the [**member**](https://msdn.microsoft.com/library/ms677097) property of another group, that other group's distinguished name is added to this group's [**memberOf**](https://msdn.microsoft.com/library/ms677099) property.<br/> |



 

Each of the following methods can be used to add a member to a group. You can add a member by using the distinguished name of the member or binding to the member object and then adding the member object to the group object.

To add a member that belongs to a downlevel domain to a group in an uplevel domain, use the bindable form of the SID string for the distinguished name. For more information and a code example that shows how to convert an **objectSid** into a bindable string, see the **GetLDAPSidBindStringFromVariantSID** example function in [Example Code for Converting an objectSid into a Bindable String](example-code-for-converting-an-objectsid-into-a-bindable-string-.md).

<dl> <dt>

<span id="Adding_Members_to_a_Group_by_Using_IADsGroup"></span><span id="adding_members_to_a_group_by_using_iadsgroup"></span><span id="ADDING_MEMBERS_TO_A_GROUP_BY_USING_IADSGROUP"></span>Adding Members to a Group by Using IADsGroup
</dt> <dd>

The [**IADsGroup**](https://msdn.microsoft.com/library/aa706021) interface can be used to add members to a group by using the [**IADsGroup.Add**](https://msdn.microsoft.com/library/aa706022) method. Bind to and obtain the **IADsGroup** interface for the group object. Then the **IADsGroup.Add** method can be used to add members to the group.

</dd> <dt>

<span id="Adding_Members_to_a_Group_by_Using_IDirectoryObject"></span><span id="adding_members_to_a_group_by_using_idirectoryobject"></span><span id="ADDING_MEMBERS_TO_A_GROUP_BY_USING_IDIRECTORYOBJECT"></span>Adding Members to a Group by Using IDirectoryObject
</dt> <dd>

The [**IDirectoryObject**](https://msdn.microsoft.com/library/aa746355) interface can be used to add members to a group by using the [**IDirectoryObject::SetObjectAttributes**](https://msdn.microsoft.com/library/aa746360) method to modify the [**member**](https://msdn.microsoft.com/library/ms677097) attribute for the group. Bind to and obtain the **IDirectoryObject** interface for the group object. Then use the **IDirectoryObject::SetObjectAttributes** method to modify the **member** attribute.

> [!Note]  
> Because the [**member**](https://msdn.microsoft.com/library/ms677097) attribute has multiple values, ensure that you use the **ADS\_ATTR\_APPEND** control code to add a distinguished name to the **member** attribute. Using the **ADS\_ATTR\_UPDATE** control code will cause the existing **member** values to be overwritten.

 

The [**IDirectoryObject**](https://msdn.microsoft.com/library/aa746355) interface can also be used to add members to a group when the group is created by specifying the members in the *pAttributeEntries* parameter of the [**IDirectoryObject::CreateDSObject**](https://msdn.microsoft.com/library/aa746356) method.

</dd> <dt>

<span id="Adding_Members_to_a_Group_by_Using_System.DirectoryServices"></span><span id="adding_members_to_a_group_by_using_system.directoryservices"></span><span id="ADDING_MEMBERS_TO_A_GROUP_BY_USING_SYSTEM.DIRECTORYSERVICES"></span>Adding Members to a Group by Using System.DirectoryServices
</dt> <dd>

You can use the [System.DirectoryServices](https://msdn.microsoft.com/library/9t2667d1.aspx) namespace to add members to a group by using the **PropertyValueCollection.Add** method on the **member** property of the group object. For more information, see [Setting Properties on Directory Objects](https://go.microsoft.com/fwlink/p/?linkid=83966).

</dd> <dt>

<span id="Adding_Members_to_a_Group_by_Using_the_LDAP_API"></span><span id="adding_members_to_a_group_by_using_the_ldap_api"></span><span id="ADDING_MEMBERS_TO_A_GROUP_BY_USING_THE_LDAP_API"></span>Adding Members to a Group by Using the LDAP API
</dt> <dd>

You can use the [Lightweight Directory Access Protocol](https://msdn.microsoft.com/library/aa367008) API to add members to a group by using one of the [**ldap\_modify\***](https://msdn.microsoft.com/library/aa366943) functions. For more information, see [Modifying a Directory Entry](https://msdn.microsoft.com/library/aa367010).

</dd> </dl>

 

 





