---
title: Binding String
description: Due to the number of objects accessible from a directory service, naming collisions can occur.
ms.assetid: b4c44b19-d7b6-4dde-b44c-4a49cecbacf2
ms.tgt_platform: multiple
keywords:
- Binding String ADSI
- ADsPath ADSI , Description
ms.topic: article
ms.date: 05/31/2018
---

# Binding String

Due to the number of objects accessible from a directory service, naming collisions can occur. The binding string, which is commonly referred to as the ADsPath, enables you to specify a particular object without causing a naming collision. This can be applied for a single directory service provider or across multiple directory service providers.

An ADsPath is a string that uniquely identifies an ADSI object on a directory service. Because ADSI objects exist within the context of the namespace of the underlying directory service, part of the syntax of an ADsPath name is provider-specific.

The following table lists the ADSI providers provided by default.



| Provider         | Description                                                                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WinNT<br/> | Used to communicate with Windows domain controllers. For more information about the WinNT ADsPath, see [WinNT ADsPath](winnt-adspath.md).<br/>           |
| LDAP<br/>  | Used to communicate with LDAP servers, such as Active Directory. For more information about the LDAP ADsPath, see [LDAP ADsPath](ldap-adspath.md).<br/>  |
| ADs<br/>   | Provides an [**IADsNamespaces**](/windows/desktop/api/Iads/nn-iads-iadsnamespaces) implementation that can be used to enumerate all of the ADSI providers installed on the client.<br/> |



 

Use these provider names to access the default provider namespace. For example, if you bind to LDAP, ADSI binds to a container that contains the domain object currently logged on. If you bind to WinNT, ADSI binds to a container that holds objects that correlate to all domains on the network.

The initial elements of the ADsPath string are the programmatic identifier (progID) of the ADSI provider, followed by "://", followed by syntax dictated by the provider namespace. The progID string may or may not be case-sensitive, depending on the provider. The progID strings for the providers listed above are case-sensitive.

The path string may or may not be case-sensitive, depending on the provider. The path strings for the providers listed above are not case-sensitive.

The following are examples of ADsPaths.

``` syntax
LDAP://CN=Jeff Smith,CN=users,DC=fabrikam,DC=com
LDAP://server01/CN=Jeff Smith,CN=users,DC=fabrikam,DC=com
 
WinNT://MyDomain/ComputerName,Computer
WinNT://MyDomain/UserAccount
```

To find all providers installed on your computer, bind to the ADs provider as shown in the following code example.


```VB
Set x = GetObject("ADs:")
For Each provider In x
    provider.Name
Next
```



Using the LDAP provider, you can specify the ADsPath either in an X.500 distinguished name (DN) form, starting with the CN tag, or you can specify its hierarchical inverse, starting with the O tag. The form you use in the initial ADsPath determines the order of the tags.

The following table lists ADsPath special characters.



| Name                      | Character           | Description                                                                                                                                                                                           |
|---------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Double quote<br/>   | "<br/>        | Used to quote any part of the ADsPath that may contain a special character so that the string is interpreted literally. For example, "CN=Name/Prefix".<br/>                                     |
| Backslash<br/>      | \\<br/>       | Used to precede special characters to signify they should be used as literals. For more information and a list of special characters, see [Distinguished Names](/previous-versions/windows/desktop/ldap/distinguished-names).<br/> |
| Slash<br/>          | /<br/>        | Component separator.<br/>                                                                                                                                                                       |
| Angle brackets<br/> | <><br/> | Delimit an ADsPath within another naming convention.<br/>                                                                                                                                       |



 

To delimit an ADsPath in a search specification or as part of a URL, use the left and right angle bracket (< >). For example, "&lt;WinNT://MyDomain/UserAccount&gt;".

Some ADSI providers may have added syntax restrictions due to namespace requirements.

## Active Directory Binding Options

Active Directory provides the ability to bind to an object using several other types of binding strings, such as a COM globally unique identifier (GUID) or a security identifier (SID). For more information, see [Binding to Active Directory](/windows/desktop/AD/binding-to-active-directory-domain-services).

 

