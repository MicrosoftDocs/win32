---
description: The user begins logging on to the network by typing a logon name and password. The Kerberos client on the user's workstation converts the password to an encryption key and saves the result in a program variable.
ms.assetid: fcb3b601-9953-474c-9a08-1fa25706f3d7
title: Authentication Service Exchange
ms.topic: article
ms.date: 05/31/2018
---

# Authentication Service Exchange

The user begins logging on to the network by typing a logon name and password. The [*Kerberos*](/windows/desktop/SecGloss/k-gly) client on the user's workstation converts the password to an encryption key and saves the result in a program variable.

The client then requests [*credentials*](/windows/desktop/SecGloss/c-gly) for the ticket-granting service (TGS) of the [*Key Distribution Center*](/windows/desktop/SecGloss/k-gly) (KDC) by sending the KDC's authentication service a message of type KRB\_AS\_REQ (Kerberos Authentication Service Request). The first part of this message identifies the user and the TGS service being requested. The second part of this message contains preauthentication data intended to prove that the user knows the password. This is simply an authenticator message that is encrypted with the [*master key*](/windows/desktop/SecGloss/m-gly) derived from the user's logon password.

When the KDC receives KRB\_AS\_REQ, it looks up the user in its database, gets the associated user's master key, decrypts the preauthentication data, and evaluates the time stamp inside. If the time stamp is valid, the KDC can be assured that the preauthentication data was encrypted with the user's master key and thus that the client is genuine.

After the KDC has verified the user's identity, it creates credentials that the client can present to the TGS, as follows:

1.  The KDC invents a logon [*session key*](/windows/desktop/SecGloss/s-gly) and encrypts a copy with the user's master key.
2.  The KDC embeds another copy of the logon session key and the user's authorization data in a ticket-granting ticket (TGT), and encrypts the TGT with the KDC's own master key.
3.  The KDC sends these credentials back to the client by replying with a message of type KRB\_AS\_REP (Kerberos Authentication Service Reply).
4.  When the client receives the reply, it uses the key derived from the user's password to decrypt the new logon session key.
5.  The client stores the new key in its ticket cache.
6.  The client extracts the TGT from the message and stores that in its ticket cache as well.

 

 
