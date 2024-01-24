---
description: Access to WMI namespaces and their data is controlled by security descriptors.
ms.assetid: 3c2dc148-df6a-4bcb-a657-59b56c358d14
ms.tgt_platform: multiple
title: Securing WMI Namespaces
ms.topic: article
ms.date: 05/31/2018
---

# Securing WMI Namespaces

Access to WMI namespaces and their data is controlled by [*security descriptors*](gloss-s.md). You can protect data in your [*namespaces*](gloss-n.md) by adjusting the namespace security descriptor to control who has access to the data and methods. For more information, see [Access to WMI Securable Objects](access-to-wmi-securable-objects.md).


The following topics describe WMI namespace security and how to control access to namespaces.

<dl> <dt>

<span id="Access_to_WMI_Namespaces"></span><span id="access_to_wmi_namespaces"></span><span id="ACCESS_TO_WMI_NAMESPACES"></span>[Access to WMI Namespaces](access-to-wmi-namespaces.md)
</dt> <dd>

WMI namespace security relies on standard Windows user [*security identifiers*](/windows/desktop/SecGloss/s-gly) (SIDs) and access control lists. Administrators and users have different default permissions.

</dd> <dt>

<span id="Setting_Namespace_Security_Descriptors"></span><span id="setting_namespace_security_descriptors"></span><span id="SETTING_NAMESPACE_SECURITY_DESCRIPTORS"></span>[Setting Namespace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dd>

After a namespace exists in the WMI repository, you can change the security on the namespace by using the WMI Control or by calling the methods of [**\_\_SystemSecurity**](--systemsecurity.md).

</dd> <dt>

<span id="Requiring_an_Encrypted_Connection_to_a_Namespace"></span><span id="requiring_an_encrypted_connection_to_a_namespace"></span><span id="REQUIRING_AN_ENCRYPTED_CONNECTION_TO_A_NAMESPACE"></span>[Requiring an Encrypted Connection to a Namespace](requiring-an-encrypted-connection-to-a-namespace.md)
</dt> <dd>

The **RequiresEncryption** qualifier on a namespace requires the WMI client application or script to use the authentication level which encrypts remote procedure calls. Both incoming data requests and asynchronous callbacks must be encrypted.

</dd> <dt>

<span id="Establishing_Inheritance_of_Namespace_Security"></span><span id="establishing_inheritance_of_namespace_security"></span><span id="ESTABLISHING_INHERITANCE_OF_NAMESPACE_SECURITY"></span>[Establishing Inheritance of Namespace Security](establishing-inheritance-of-namespace-security.md)
</dt> <dd>

You can control whether a child namespace inherits the security descriptor of the parent namespace.

</dd> </dl>

## Related topics

<dl> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> <dt>

[Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md)
</dt> <dt>

[Creating a Namespace with the WMI API](creating-a-namespace-with-the-wmi-api.md)
</dt> <dt>

[WMI Security Descriptor Objects](wmi-security-descriptor-objects.md)
</dt> </dl>

 

 
