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
| [**member**](/windows/desktop/ADSchema/a-member)<br/>     | The [**member**](/windows/desktop/ADSchema/a-member) attribute contains the distinguished names for the objects that are members of the group.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**memberOf**](/windows/desktop/ADSchema/a-memberof)<br/> | The [**memberOf**](/windows/desktop/ADSchema/a-memberof) attribute contains the distinguished names of groups that contain the group as a direct member. The **memberOf** attribute does not contain any inherited group membership data. For example, if GroupA is a member of GroupB and GroupB is a member of GroupC, the **memberOf** attribute for GroupA will contain GroupB, but not GroupC.<br/> The Active Directory server maintains this property. When a distinguished name is added to the [**member**](/windows/desktop/ADSchema/a-member) property of another group, that other group's distinguished name is added to this group's [**memberOf**](/windows/desktop/ADSchema/a-memberof) property.<br/> |



 

Each of the following methods can be used to add a member to a group. You can add a member by using the distinguished name of the member or binding to the member object and then adding the member object to the group object.

To add a member that belongs to a downlevel domain to a group in an uplevel domain, use the bindable form of the SID string for the distinguished name. For more information and a code example that shows how to convert an **objectSid** into a bindable string, see the **GetLDAPSidBindStringFromVariantSID** example function in [Example Code for Converting an objectSid into a Bindable String](example-code-for-converting-an-objectsid-into-a-bindable-string-.md).

<dl> <dt>

<span id="Adding_Members_to_a_Group_by_Using_IADsGroup"></span><span id="adding_members_to_a_group_by_using_iadsgroup"></span><span id="ADDING_MEMBERS_TO_A_GROUP_BY_USING_IADSGROUP"></span>Adding Members to a Group by Using IADsGroup
</dt> <dd>

The [**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup) interface can be used to add members to a group by using the [**IADsGroup.Add**](/windows/desktop/api/iads/nf-iads-iadsgroup-add) method. Bind to and obtain the **IADsGroup** interface for the group object. Then the **IADsGroup.Add** method can be used to add members to the group.

</dd> <dt>

<span id="Adding_Members_to_a_Group_by_Using_IDirectoryObject"></span><span id="adding_members_to_a_group_by_using_idirectoryobject"></span><span id="ADDING_MEMBERS_TO_A_GROUP_BY_USING_IDIRECTORYOBJECT"></span>Adding Members to a Group by Using IDirectoryObject
</dt> <dd>

The [**IDirectoryObject**](/windows/desktop/api/iads/nn-iads-idirectoryobject) interface can be used to add members to a group by using the [**IDirectoryObject::SetObjectAttributes**](/windows/desktop/api/iads/nf-iads-idirectoryobject-setobjectattributes) method to modify the [**member**](/windows/desktop/ADSchema/a-member) attribute for the group. Bind to and obtain the **IDirectoryObject** interface for the group object. Then use the **IDirectoryObject::SetObjectAttributes** method to modify the **member** attribute.

> [!Note]  
> Because the [**member**](/windows/desktop/ADSchema/a-member) attribute has multiple values, ensure that you use the **ADS\_ATTR\_APPEND** control code to add a distinguished name to the **member** attribute. Using the **ADS\_ATTR\_UPDATE** control code will cause the existing **member** values to be overwritten.

 

The [**IDirectoryObject**](/windows/desktop/api/iads/nn-iads-idirectoryobject) interface can also be used to add members to a group when the group is created by specifying the members in the *pAttributeEntries* parameter of the [**IDirectoryObject::CreateDSObject**](/windows/desktop/api/iads/nf-iads-idirectoryobject-createdsobject) method.

</dd> <dt>

<span id="Adding_Members_to_a_Group_by_Using_System.DirectoryServices"></span><span id="adding_members_to_a_group_by_using_system.directoryservices"></span><span id="ADDING_MEMBERS_TO_A_GROUP_BY_USING_SYSTEM.DIRECTORYSERVICES"></span>Adding Members to a Group by Using System.DirectoryServices
</dt> <dd>

You can use the [System.DirectoryServices](/dotnet/api/system.directoryservices) namespace to add members to a group by using the **PropertyValueCollection.Add** method on the **member** property of the group object. For more information, see [Setting Properties on Directory Objects](/previous-versions/ms180860(v=vs.90)).

</dd> <dt>

<span id="Adding_Members_to_a_Group_by_Using_the_LDAP_API"></span><span id="adding_members_to_a_group_by_using_the_ldap_api"></span><span id="ADDING_MEMBERS_TO_A_GROUP_BY_USING_THE_LDAP_API"></span>Adding Members to a Group by Using the LDAP API
</dt> <dd>

You can use the [Lightweight Directory Access Protocol](/previous-versions/windows/desktop/ldap/lightweight-directory-access-protocol-ldap-api) API to add members to a group by using one of the [**ldap\_modify\***](/previous-versions/windows/desktop/api/winldap/nf-winldap-ldap_modify_s) functions. For more information, see [Modifying a Directory Entry](/previous-versions/windows/desktop/ldap/modifying-a-directory-entry).

</dd> </dl>

 

