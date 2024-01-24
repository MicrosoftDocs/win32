---
title: Adding a Reservation
description: The routing database contains the reservation list.
ms.assetid: c36e731c-6a0b-42a8-bc92-106a8e017b0d
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Reservation

The routing database contains the reservation list. The reservation list consists of the users that are allowed access to the namespace, as well as the level of access for each user listed under the reservation. When reservations are added or deleted, the routing database is searched to determine access privileges.

In addition to checking the users ID, the HTTP Server API also checks for conflicts in existing reservations before installing a new reservation.

**To add a new reservation**

1.  If the port number in the UrlPrefix has reservations or registrations for a scheme different from the scheme in the UrlPrefix, the registration fails. HTTP and HTTPS cannot be supported on the same port.
2.  Locate the appropriate bucket for the registration (see the [Routing Incoming Requests](routing-incoming-requests.md) section), based on the host type. The remaining steps are relative to this bucket.
3.  Select reservation entries with scheme, host and port components that match the UrlPrefix being reserved. From these, locate the entry with the longest matching *relativeUri* that is not equal to the relativeUri in the reservation (that is, the *parent node*). If the entry exists, then evaluate access rights based on the ACL assigned to that entry.
4.  If a parent node was not found, this is a reservation with an empty relativeUri, or *root reservation*. Grant access rights only if the caller is registered under the LocalSystem or Administrator accounts.
5.  If access rights are granted, check for duplicate reservations. If a reservation entry exists with the same scheme, port, host and relativeUri, an ERROR\_ALREADY\_EXISTS code is returned.
    > [!Note]  
    > Updating an existing entry should be performed in two steps: delete the entry and add a new one.

     

If the above steps succeed, a new reservation entry is entered into the reservation database.

> [!Note]  
> The new entry is created with the specified ACL and does not inherit ACLs from the *parent* entry.

 

The following examples illustrate the reservation process.

-   Reservation 1: `https://+:80/vroot/subdir/` by Admin for User A and User C succeeds and is entered into the "+" bucket.
-   Reservation 2: `https://adatum.com:80/vroot/` by Admin for User B succeeds and is entered into the "Explicit host" bucket.
-   Reservation 3: `https://adatum.com:80/vroot/subdir/otherdir/` by User B for User C succeeds due to reservation 2.
-   Reservation 4: `https://+:80/vroot/subdir/otherdir/` by User A for User E succeeds due to reservation 1.
-   Reservation 5: `https://adatum.com:80/vroot/subdir/otherdir/` by User A for User E fails. Access denied due to reservation 2.
-   Reservation 6: `https://+:80/vroot/subdir/` by Admin for User A fails. The reservation conflicts with reservation 1.
-   Reservation 7: `https://adatum.com:80/newroot/` by User A for User A fails. Access denied due to implicit root reservation of `https://adatum.com:80/` for LocalSystem or Administrator.

Reservations can affect the set of URLs in requests delivered to a process that has previously registered a UrlPrefix. For example, consider the following scenario.

-   Registration: `https://adatum.com:80/vroot/` by application 1 for User A.
-   A request for `https://adatum.com:80/vroot/subdir/file.htm` is delivered to application 1.
-   Reservation: `https://+:80/vroot/subdir/` for User B.
-   A request for `https://adatum.com:80/vroot/subdir/file.htm` is now rejected.
-   Registration: `https://adatum.com:80/vroot/subdir/` by application 2 for User B.
-   A request for `https://adatum.com:80/vroot/subdir/file.htm` is delivered to application 2.

 

 




