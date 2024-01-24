---
description: For Credential Security Support Provider protocol (CredSSP) to delegate credentials, you must specify which servers can be delegated to.
ms.assetid: 15ed9a62-2eee-4f29-92c5-ccf2754cdf13
title: CredSSP Group Policy Settings
ms.topic: article
ms.date: 05/31/2018
---

# CredSSP Group Policy Settings

For [Credential Security Support Provider protocol (CredSSP)](credential-security-support-provider.md) to delegate credentials, you must specify which servers can be delegated to. To specify those servers, modify settings in the Group Policy Editor (GPE) Microsoft Management Console (MMC) snap-in. The GPE settings that control delegation are under **Computer Configuration \| Administrative Templates \| System \| Credentials Delegation**.

> [!Caution]  
> This is not constrained delegation. CredSSP passes the user's full credentials to the server without any constraint.

 

Group policy settings control delegation of the following types of credentials.



| Credentials Type                                                                                                                                 | Description                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <span id="Default_credentials"></span><span id="default_credentials"></span><span id="DEFAULT_CREDENTIALS"></span>Default credentials<br/> | The credentials obtained when the user first logs on to Windows.<br/>                   |
| <span id="Fresh_credentials"></span><span id="fresh_credentials"></span><span id="FRESH_CREDENTIALS"></span>Fresh credentials<br/>         | The credentials that the user is prompted for when executing an application.<br/>       |
| <span id="Saved_credentials"></span><span id="saved_credentials"></span><span id="SAVED_CREDENTIALS"></span>Saved credentials<br/>         | The credentials that are saved using [Credential Manager](credential-manager.md).<br/> |



 

To include a server in the category associated with a particular group policy setting, add the [*Service Principal Name*](/windows/desktop/SecGloss/s-gly) (SPN) of that server to the list of servers for that group policy setting. The SPN can contain a single wildcard character.

 

