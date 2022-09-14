---
description: When an application uses the Credentials Management API to prompt for credentials, the user is expected to enter information that can be validated, either by the operating system or by the application.
ms.assetid: 53ed2eb4-2c29-48fd-b7fa-0c27bf155758
title: User Name Formats
ms.topic: article
ms.date: 05/31/2018
---

# User Name Formats

When an application uses the Credentials Management API to prompt for credentials, the user is expected to enter information that can be validated, either by the operating system or by the application. The user can specify domain credentials information in one of the following formats:

-   [User Principal Name](#user-principal-name)
-   [Down-Level Logon Name](#down-level-logon-name)

## User Principal Name

[*User principal name*](../secgloss/u-gly.md) (UPN) format is used to specify an Internet-style name, such as <b>UserName@Example.Microsoft.com</b>. The following table summarizes the parts of a UPN.



| Part                                                        | Example                                |
|-------------------------------------------------------------|----------------------------------------|
| User account name. Also known as the logon name.<br/> | *UserName*<br/>                  |
| Separator. A character literal, the at sign (@).<br/> | @<br/>                           |
| UPN suffix. Also known as the domain name.<br/>       | *Example.Microsoft.com* <br/> |



 

A UPN can be implicitly or explicitly defined. An implicit UPN is of the form <b>UserName@DNSDomainName.com</b>. An implicit UPN is always associated with the user's account, even if an explicit UPN is not defined. An explicit UPN is of the form <i><b>Name@Suffix</b></i>, where both the name and suffix strings are explicitly defined by the administrator.

## Down-Level Logon Name

The down-level logon name format is used to specify a domain and a user account in that domain, for example, <i><b>DOMAIN\\UserName</b></i>. The following table summarizes the parts of a down-level logon name.



| Part                                                           | Example               |
|----------------------------------------------------------------|-----------------------|
| NetBIOS domain name.<br/>                                | *DOMAIN*<br/>   |
| Separator. A character literal, the backslash (\\).<br/> | **\\**<br/>     |
| User account name. Also known as the logon name.<br/>    | *UserName*<br/> |



 

 

 
