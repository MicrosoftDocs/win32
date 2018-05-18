---
title: About DSML Services for Windows
description: Directory Services Markup Language (DSML) Services for Windows enables applications to use XML documents to read from and write to Active Directory and Active Directory Application Mode (ADAM).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '3b8982d6-eed5-48be-adab-cfe95f1809c4'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["DSML Services for Windows, About", "About DSML Services for Windows", "DSML Services for Windows DSML", "DSML Services for Windows, described"]
---

# About DSML Services for Windows

Directory Services Markup Language (DSML) Services for Windows enables applications to use [*XML*](glossary.md#xml) documents to read from and write to Active Directory and Active Directory Application Mode (ADAM). Both Active Directory and ADAM are directories based on [*Lightweight Directory Access Protocol (LDAP)*](glossary.md#lightweight-directory-access-protocol).

[*DSML Services for Windows*](glossary.md#dsml-services-for-windows) converts [*XML*](glossary.md#xml) elements and attributes into LDAP commands that can both make changes to and retrieve data from a directory. *DSML Services for Windows* converts the results of the LDAP commands back into XML elements and attributes. These XML-to-LDAP and LDAP-to-XML conversions are based on and are in compliance with the [DSML V2 specification](http://go.microsoft.com/fwlink/p/?linkid=84151), a standard approved by the [*Organization for the Advancement of Structural Information Standards (OASIS)*](glossary.md#organization-for-the-advancement-of-structured-information-standards) and supported by many directory services vendors.

For architecture information, see [DSML Services for Windows Architecture](dsml-services-for-windows-architecture.md).

## Greater Interoperability Through Open Standards

DSML Services for Windows extends the features of Active Directory. Because DSML Services for Windows uses open standards such as HTTP, XML, and [*SOAP*](glossary.md#simple-object-access-protocol), a greater level of interoperability with Active Directory is possible than is available with directory service APIs. The use of open standards provides a number of key benefits for IT administrators and independent software vendors (ISVs), who now have even more open-standard choices for accessing Active Directory.

By supporting the DSML V2 specification, DSML Services for Windows enables you to achieve greater interoperability with other directory services vendors that support this standard.

Another advantage of using DSML Services for Windows is that XML documents can interact with existing LDAP directories without making changes to the directories: for example, without converting the LDAP directories to XML documents or schemas. In addition, you can use the tools that develop XML-based applications to enable those applications to access LDAP directories.

## Features of DSML Services for Windows

DSML Services for Windows includes the following features:

-   SOAP listener

    The SOAP listener component intercepts DSML V2 requests and returns corresponding DSML V2 responses.

-   Support for equivalent LDAP operations

    DSML Services for Windows performs equivalent LDAP operations such as addRequest, modifyRequest, and searchRequest. It also supports advanced operations such as LDAP controls and extended requests.

-   Session support

    Although DSML was designed around and based on the request/response protocol, DSML Services for Windows enables users to keep the state between requests by specifying the session ID in the SOAP header. This is useful for some LDAP control operations that span multiple requests, such as a page-size control operation.

-   IIS security support

    DSML Services for Windows supports all IIS security configurations, including integrated Windows authentication, basic authentication, basic authentication over secure sockets layer (SSL), and digest authentication.

-   Connection pooling

    The connection pooling component manages incoming requests and promotes scalability.

-   Multiple configuration options

    There is support for many different configuration options that optimize the performance of DSML Services for Windows.

-   Directory Services Data Exchange

    DSML Services for Windows includes Directory Services Data Exchange (DSDE), a command line import/export utility that supports both DSML and LDAP protocols.

## Application of DSML Services for Windows

DSML Services for Windows can be used for a variety of purposes. The following list describes common scenarios for using DSML Services for Windows:

-   Web services

    The use of directories in web services is growing rapidly. Additionally, XML is becoming the default language for use with web services. DSML Services for Windows provides the critical link between XML documents and LDAP directories. Therefore, DSML Services for Windows will become a critical service for many applications that must provide or use web services.

-   Handheld and portable devices

    Data-enabled cell phones or PDAs that must access directory data may not contain an LDAP client but might be able to use DSML Services for Windows to access the directory over the Internet.

-   Firewall access

    Certain firewalls cannot pass LDAP traffic because they cannot audit it, but these same firewalls can pass XML. In such cases, applications can use DSML Services for Windows to communicate across a firewall.

 

 




