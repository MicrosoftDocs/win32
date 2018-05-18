---
Description: 'Authentication is interactive when a user is prompted to supply logon information. The Local Security Authority (LSA) performs an interactive authentication when a user logs on through the GINA user interface.'
ms.assetid: '86a318fa-4d7c-4191-a309-d25b492dd915'
title: Interactive Authentication
---

# Interactive Authentication

Authentication is interactive when a user is prompted to supply logon information. The [*Local Security Authority*](security.l_gly#-security-local-security-authority-gly) (LSA) performs an interactive authentication when a user logs on through the [*GINA*](security.g_gly#-security-gina-gly) user interface. The following illustration shows the parts of a typical interactive authentication.

![interactive authentication](images/lsaint3.png)

A user signals the system to begin the logon sequence by typing the CTRL+ALT+DEL [*secure attention sequence*](security.s_gly#-security-secure-attention-sequence-gly) (SAS). [*Winlogon*](security.w_gly#-security-winlogon-gly) receives the SAS and calls the GINA to display a user interface and obtain the user's logon data, such as a user name and password.

After obtaining the logon data, the GINA calls the [**LsaLogonUser**](lsalogonuser.md) function to authenticate the user, specifying which authentication package must be used to evaluate the logon data.

The LSA calls the specified authentication package and passes the logon data to it. The authentication package examines the data and determines whether the authentication is successful. The authentication result is returned to the LSA and from the LSA, to the GINA.

The GINA displays the success or failure of the authentication to the user and returns the result of the authentication to Winlogon. If the authentication succeeds, the user's logon session begins and a set of logon [*credentials*](security.c_gly#-security-credentials-gly) are saved for future reference.

> [!Note]  
> In general, a developer who writes a custom GINA to accept specialized logon data, such as a [*smart card*](security.s_gly#-security-smart-card-gly) or retinal-scan data, must also write an authentication package responsible for processing that data and determining its authenticity.

 

For more information about Winlogon and GINAs, see [Winlogon and GINA](winlogon-and-gina.md). For more information about authentication packages, see [Creating Custom Security Packages](creating-custom-security-packages.md).

 

 



