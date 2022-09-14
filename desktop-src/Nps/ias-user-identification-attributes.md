---
title: User Identification Attributes
description: The identity of the user requesting authentication is supplied to the NPS Extension DLLs in a number of different attributes.
ms.assetid: 2f741a81-e432-47fe-a14a-8b77ecd41e28
ms.tgt_platform: multiple
keywords:
- Attributes, User Identification
ms.topic: article
ms.date: 05/31/2018
---

# User Identification Attributes

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

The identity of the user requesting authentication is supplied to the NPS Extension DLLs in a number of different attributes.

-   **ratUserName**
-   **ratStrippedUserName**
-   **ratFQUserName**

Each attribute provides the user identity in a different format. In general, developers should use **ratStrippedUserName**. The uses of the **ratUserName** and **ratFQUserName** attributes are more specialized.

> [!Note]  
> The User-Password attribute, **ratUserPassword**, has already been decrypted when it is sent to the extension DLL and is usable in that form.

 

## ratUserName

The **ratUserName** attribute contains the name that was actually sent "over the wire." NPS has not, in any way, processed or validated the contents of this attribute. This attribute may not be available at all because the user may have been identified through a means such as caller ID.

When using [**RadiusExtensionProcess/Ex**](/windows/desktop/api/authif/nc-authif-pradius_extension_process_ex), if this attribute is available, it is available only at the Authentication Extension DLL plug-in point. The **ratUserName** attribute is not available at the Authorization Extension DLL plug-in point because in Authorization Extension DLLs the **RadiusExtensionProcess/Ex** functions see only the "outbound" attributes.

When using [**RadiusExtensionProcess2**](/windows/desktop/api/authif/nc-authif-pradius_extension_process_2), if this attribute is available, it is available at both the Authentication Extension DLL plug-in point and the Authorization Extension DLL plug-in point.

## ratStrippedUserName

The **ratStrippedUserName** is the user's identity after "realm stripping." For more information on realm stripping, see the [Realm names](/previous-versions/windows/it-pro/windows-server-2003/cc779938(v=ws.10)) topic on http:\\\\technet2.microsoft.com.

This attribute may be present at the Authentication Extension DLL plug-in point, the Authorization Extension DLL plug-in point, or both. This attribute is guaranteed to have the format:

*Domain***\\***UserName*

Where *Domain* is the NetBIOS domain name.

## ratFQUserName

The **ratFQUserName** attribute is the "fully qualified" user name.

This attribute may be present in the Authentication Extension DLL plug-in point, the Authorization Extension DLL plug-in point, or both. However, the format of the attribute may differ between the two plug-in points. At the Authentication Extension DLL plug-in point, this attribute will always be of the form:

*Domain***\\***UserName*

The format of the **ratFQUserName** attribute at the Authorization Extension DLL plug-in point depends on whether the user is an Active Directory user.

-   If the user is a local user **ratFQUserName** has the same format as for the Authentication Extension DLL plug-in point:

    *Domain***\\***UserName*

    .

-   If the user is an Active Directory user, **ratFQUserName** may contain the user's name in "canonical" format. Canonical format is the format used by the Active Directory to identify the user. It is the path from the root of the Active Directory tree, and includes the user's Organizational Unit (OU).

## Related topics

<dl> <dt>

[Setting Up the Extension DLLs](/windows/desktop/Nps/ias-setting-up-the-extension-and-authorization-dlls)
</dt> <dt>

[Invoking the Extension DLLs](/windows/desktop/Nps/ias-authentication-and-authorization-process)
</dt> </dl>

 

 