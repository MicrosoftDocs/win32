---
description: As the Kerberos protocol was originally designed, a master key for a user was derived from a password provided by the user.
ms.assetid: b8fcb68d-751e-4495-ab92-8b70c96aaa7a
title: Ticket-Granting Tickets
ms.topic: article
ms.date: 05/31/2018
---

# Ticket-Granting Tickets

As the [*Kerberos protocol*](../secgloss/k-gly.md) was originally designed, a master key for a user was derived from a password provided by the user. When a user logged on, the Kerberos client on the user's workstation accepted the password from the user and converted it into an encryption key by passing the text through a one-way [*hash*](../secgloss/h-gly.md) function. The resulting hash was the user's [*master key*](../secgloss/m-gly.md). The client used this *master key* to decrypt [*session keys*](../secgloss/s-gly.md) received from KDC.

The problem with the original Kerberos design is the client needs the user's master key each time it decrypts a session key from the KDC. That means either the client must ask the user for the password at the beginning of every client/server exchange, or the client must store the user's key on the workstation. Frequent interruptions of the user are too intrusive. Storing the key on the workstation risks compromising a key derived from the user password which is a long term key.

The Kerberos protocol's solution to this problem is for the client to get a temporary key from the KDC. This temporary key is good only for this [*logon session*](../secgloss/l-gly.md). When a user logs on, the client requests a ticket for the KDC just as it would request a ticket for any other service. The KDC responds by creating a logon session key and a ticket for a special server, the KDC's full ticket-granting service. One copy of the logon session key is embedded in the ticket, and the ticket is encrypted with the KDC's master key. Another copy of the logon session key is encrypted with the user's master key derived from the user's logon password. Both the ticket and the encrypted session key are sent to the client.

When the client gets the KDC's reply, it decrypts the logon session key with the user's master key derived from the user's password. The client no longer needs the key derived from the user's password because the client will now use the logon session key to decrypt its copy of any server session key it gets from the KDC. The client stores the logon session key in its ticket cache along with its ticket for the KDC's full ticket-granting service.

The ticket for the full ticket-granting service is called a ticket-granting ticket (TGT). When the client asks the KDC for a ticket to a server, it presents [*credentials*](../secgloss/c-gly.md) in the form of an authenticator message and a ticket — in this case a TGT — just as it would present credentials to any other service. The ticket-granting service opens the TGT with its master key, extracts the logon session key for this client, and uses the logon session key to encrypt the client's copy of a session key for the server.

 

 
