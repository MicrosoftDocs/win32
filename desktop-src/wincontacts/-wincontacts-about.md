---
title: About Windows Contacts
description: New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.
ms.assetid: 7c8066e3-296a-4acb-aa02-610502c1630f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Windows Contacts

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

The Windows Vista mechanism for storing and retrieving contact information has changed substantially from that used by Windows Address Book (WAB). This document describes important aspects of the new mechanism and the reasons for making the changes. It also directs the user to more-in-depth information.

This document includes the following topics:

-   [Why Windows Contacts?](#why-windows-contacts)
-   [XML Format](#xml-format)
-   [Two Levels of Extensibility](#two-levels-of-extensibility)
    -   [Simple Extensibility](#simple-extensibility)
    -   [XML Extensibility](#xml-extensibility)

## Why Windows Contacts?

There are several advantages to using Windows Contacts:

-   Simplifies the Windows Contacts platform and unifies contacts across Microsoft. Contacts is designed to replace all other storages of personal contacts in the system; WAB is a good example. Contacts also includes custom data storage for non-Microsoft personal contacts, but not for security principals.
-   Simplifies the mechanism for interacting with individual contacts from COM clients.
-   Provides an extensible mechanism for synchronizing cell phones and other hardware devices with Windows Contacts.
-   Supports all legacy uses of WAB.

## XML Format

-   Provides an alternative to vCard as a standard interoperability format. IMPORTANT: Windows Contacts does not replace vCard as a standard.
-   Supplies a minimal set of common contact data types for both single-value and multi-value property types. Provides labels to differentiate instances of multi-value property types; enables the creation of new custom labels in the form of URIs.
-   Provides version numbers and modification dates.
-   Enables other users to freely add property types to the built-in types by prepending a unique namespace to the new property type.
-   Provides a built-in schema to express and organize the properties that form contacts. See [Windows Contact Schema](-wincontacts-schema-entry.md).

## Two Levels of Extensibility

The Windows Contacts  API gives programmers two levels of extensibility:

### Simple Extensibility

-   Declare your own namespace.
-   Adopt the built-in data model.
-   Use the built-in data reader/writer.

### XML Extensibility

-   Declare your own namespace.
-   Define your own data model elements blob.
-   Create your own data reader/writer. (Blob goes with message, but is not seen without your reader.)

 

 




