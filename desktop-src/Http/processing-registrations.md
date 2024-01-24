---
title: Processing Registrations
description: The HTTP Server APIs use the routing database to apply access checks during registrations.
ms.assetid: d72aa213-b8e8-4fe9-b98c-41114d2cea56
ms.topic: article
ms.date: 05/31/2018
---

# Processing Registrations

The HTTP Server APIs use the routing database to apply access checks during registrations. A registration for a [UrlPrefix](urlprefix-strings.md) must pass a series of access checks to ensure that the user registering for the namespace has access rights. Use the [**HttpAddUrl**](/windows/desktop/api/Http/nf-http-httpaddurl) function to add a new registration.

**To add a new registration with HttpAddUrl**

1.  If the port number in the UrlPrefix has reservations or registrations for a scheme different from the scheme in the UrlPrefix, the registration fails. HTTP and HTTPS cannot be supported on the same port.
2.  The registration is slotted into the appropriate bucket for the registration. The buckets are based on the host type of the URL as outlined in the [Routing Incoming Requests](routing-incoming-requests.md) section. The following steps are relative to this particular bucket.
3.  If a duplicate registration entry exists, return an error code.
4.  Select reservation entries with scheme, host and port components that are equal to those of the UrlPrefix. From these, locate the entry with the longest **relativeUri** match. If the entry exists, check permissions based on the ACL associated with that entry and return success. If the entry does not exist, return an ERROR\_ALREADY\_EXISTS code.

The following examples illustrate the process to install a registration in the routing database. Reservations 1 and 2 exist in the routing database.

-   Reservation 1: `https://+:80/vroot/subdir/` for User A and User C. This reservation is placed in the "+" bucket.
-   Reservation 2: `https://adatum.com:80/vroot/` for User B. This reservation is placed in the "Explicit Host" bucket.
-   Registration: `https://+:80/vroot/subdir/` by User B fails due to reservation 1.
-   Registration: `https://adatum.com:80/vroot/subdir/` by User B succeeds due to reservation 2.
-   Registration: `https://adatum.com:80/vroot/subdir/` by User C fails due to the more explicit reservation 2. The strong wildcard reservation does not have meaning within the context of the explicit reservation or registration.
-   Registration: `https://+:80/vroot/subdir/` by User A succeeds due to reservation 1.
-   Registration: `https://adatum.com:80/vroot/anotherdir/` by User B succeeds due to reservation 2.

The access check for registration does not include checks for delegation privileges. There are no access checks based on reservations (see [**HttpRemoveUrl**](/windows/desktop/api/Http/nf-http-httpremoveurl)). The only requirement for deleting a registration us that the calling process must have created the registration.

 

 




