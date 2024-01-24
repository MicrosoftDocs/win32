---
title: ADSI Schema Model
description: A schema is similar to a dictionary in that it holds the definition of every type of object known to a directory service.
ms.assetid: 70561a11-1560-4b1c-a999-e2a7b2002ab0
ms.tgt_platform: multiple
keywords:
- ADSI Schema Model ADSI
- ADSI ADSI , about, schema
ms.topic: article
ms.date: 05/31/2018
---

# ADSI Schema Model

A schema is similar to a dictionary in that it holds the definition of every type of object known to a directory service. ADSI client applications can browse through a schema to discover the features of any given ADSI implementation. In addition, ADSI supplies schema management interfaces that can be used to communicate with a directory service's underlying schema.

Some schemas are extensible and ADSI providers or third-party suppliers may choose to publish new interfaces or additional properties for existing interfaces there. ADSI clients use this data to determine what features are supported for each directory service.

There are three kinds of schema objects: classes, properties, and syntaxes, each respectively supporting the schema management interfaces [**IADsClass**](/windows/desktop/api/Iads/nn-iads-iadsclass), [**IADsProperty**](/windows/desktop/api/Iads/nn-iads-iadsproperty), and [**IADsSyntax**](/windows/desktop/api/Iads/nn-iads-iadssyntax).

> [!Note]  
> Class is an overloaded term. There are C++ classes, Java classes, COM classes, and ADSI classes. In this document, the word class, unless otherwise qualified, refers to a category or type of schema object.

 

ADSI abstracts the schema of every directory service and places it in every top-level root node in the **Namespace** object. To identify what classes a directory service supports on a given root-node, you enumerate the schema object and get a list of class objects, property objects, and syntax objects. For more information, see [Using the ADSI Schema](using-the-adsi-schema.md).

## ADSI LDAP Provider Schema Cache

The LDAP provider for ADSI attempts to cache schema data to the local computer. A subschema is identified by a distinguished name stored in the [**subSchemaSubEntry**](/windows/desktop/ADSchema/a-subschemasubentry) attribute located in the root of the directory service enterprise (rootDSE). In addition to providing the subschema data, LDAP v3 servers should expose a [**modifyTimeStamp**](/windows/desktop/ADSchema/a-modifytimestamp) attribute that is used to determine the last time the schema was modified.

When ADSI first binds to the LDAP server, it retrieves the subschema data using the [**subSchemaSubEntry**](/windows/desktop/ADSchema/a-subschemasubentry) attribute. If ADSI succeeds in finding the subschema object, it stores a pointer to the data in the registry on the computer that is connecting to the LDAP server. For information on exactly where these values are stored in the registry, see [ADSI and User Account Control](adsi-and-uac.md).

ADSI then attempts to process the schema data and reads the [**modifyTimeStamp**](/windows/desktop/ADSchema/a-modifytimestamp) attribute. If the **modifyTimeStamp** attribute exists and ADSI successfully processes the schema, ADSI writes the subschema to disk and creates the two following registry values under the key. If the subschema data exists, but cannot be processed, neither of these registry values is created:

-   A **Time** value, which contains the [**modifyTimeStamp**](/windows/desktop/ADSchema/a-modifytimestamp) attribute. This value is used to ensure that the schema data is current and prevents the constant reloading of the schema data.
-   A **File** value, which contains the path to where ADSI stores the schema data in the file system. By default, ADSI caches the subschema in the &lt;systemroot&gt;\\SchCache directory with a file name corresponding to the name of the LDAP server.

If the subschema data can be processed, but no [**modifyTimeStamp**](/windows/desktop/ADSchema/a-modifytimestamp) attribute is exposed, the schema data is cached in memory, but not written to disk. If an LDAP v3 server has been contacted through ADSI on the local computer and a cached subschema is not present, it is most likely for one of the following reasons:

-   The server did not expose the correct properties.
-   ADSI was unable to process the schema.
-   ADSI was unable to write the file to the file system.

 

 
