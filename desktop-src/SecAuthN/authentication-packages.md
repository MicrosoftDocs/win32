---
description: Authentication packages are contained in dynamic-link libraries.
ms.assetid: b0d7bca1-b4bb-4b3f-822e-04a6a500cd9a
title: Authentication Packages
ms.topic: article
ms.date: 05/31/2018
---

# Authentication Packages

[*Authentication packages*](/windows/desktop/SecGloss/a-gly) are contained in dynamic-link libraries. The [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) loads authentication packages by using configuration information stored in the registry. Loading multiple authentication packages permits the LSA to support multiple logon processes and multiple [*security protocols*](/windows/desktop/SecGloss/s-gly).

Logon processes use authentication packages to analyze logon data. New logon processes are added to a system by adding a [*GINA*](/windows/desktop/SecGloss/g-gly) to collect the required logon data and, if needed, by adding a new authentication package to analyze the data.

Security protocols are implemented by authentication packages. An authentication package analyzes logon data by following the rules and procedures set forth in a security protocol.

Authentication packages are responsible for the following tasks:

-   Analyzing logon data to determine whether a [*security principal*](/windows/desktop/SecGloss/s-gly) is allowed to log on to a system.
-   Establishing a new [*logon session*](/windows/desktop/SecGloss/l-gly) and creating a unique [*logon identifier*](/windows/desktop/SecGloss/l-gly) for the successfully authenticated principal.
-   Passing security information to the LSA for the principal's security token.

When a user attempts an interactive logon, the LSA calls an authentication package to determine whether to permit the user to log on. MSV1\_0, for example, is an authentication package installed with the Microsoft Windows operating system. The MSV1\_0 package accepts a user name and a [*hashed*](/windows/desktop/SecGloss/h-gly) password. It looks up the user name and hashed password combination in the Security Accounts Manager (SAM) database. If the logon data matches the stored [*credentials*](/windows/desktop/SecGloss/c-gly), the authentication package permits the logon to succeed.

After successfully authenticating a [*security principal's*](/windows/desktop/SecGloss/s-gly) credentials, an authentication package is responsible for creating a new LSA logon session for the principal and allocating the [*logon identifier*](/windows/desktop/SecGloss/l-gly) that uniquely identifies the logon session. The authentication package may associate credential information with the logon session for subsequent authentication requests. For example, the MSV1\_0 authentication package (provided by Microsoft) associates the user account name and a hash of the user's password with each logon session.

The authentication package also provides a set of [*security identifiers*](/windows/desktop/SecGloss/s-gly) (SIDs) and other information appropriate for inclusion in the security token created by the LSA. This token will represent the principal's security [*context*](/windows/desktop/SecGloss/c-gly) for access to Windows operations.

After a logon session is created and associated with a principal, subsequent authentication requests made on behalf of the principal are handled differently than the initial logon. The authentication package does not create a new logon session nor return information for creating a token. The authentication package can, however, associate [*supplemental credentials*](/windows/desktop/SecGloss/s-gly) obtained during a subsequent authentication with the principal's existing logon session. Supplemental credentials are obtained when access to a requested resource requires information beyond the credentials established by the initial logon. For example, when a logged-on user requests a Novell network logon, a Novell-specific authentication package can be called and Novell-specific credentials can be authenticated and associated with the logon session. These credentials can be referenced by a Novell redirector (by way of the Novell authentication package) when the user accesses the Novell network.

The following topics discuss the various types of [*Authentication packages*](/windows/desktop/SecGloss/a-gly):

-   [Windows Authentication Packages](windows-authentication-packages.md)
-   [Security Support Provider/Authentication Packages](security-support-provider-authentication-packages.md)
-   [Authentication Packages Provided by Microsoft](authentication-packages-provided-by-microsoft.md)
-   [Subauthentication Packages](subauthentication-packages.md)

 

 
