---
description: You can assign privileges to accounts either by using the Local Security Policy Microsoft Management Console (MMC) snap-in (Secpol.msc) or by calling the LsaAddAccountRights function.
ms.assetid: F2DAB2E3-8B24-49A3-A2DD-E83B5181E9A2
title: Assigning Privileges to an Account
ms.topic: article
ms.date: 05/31/2018
---

# Assigning Privileges to an Account

You can assign privileges to accounts either by using the Local Security Policy Microsoft Management Console (MMC) snap-in (Secpol.msc) or by calling the [**LsaAddAccountRights**](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsaaddaccountrights) function.

Assigning a privilege to an account does not affect existing user tokens. A user must log off and then log back on to get an access token with the newly assigned privilege.

To assign privileges by using the Local Security Policy MMC snap-in, edit the list of users for each privilege listed under **Security Settings/Local Policies/User Rights Assignment**.

 

 
