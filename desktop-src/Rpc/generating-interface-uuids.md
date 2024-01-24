---
title: Generating Interface UUIDs
description: Generating interface Universal Unique Identifiers (UUIDs) and using Uuidgen.
ms.assetid: a973b7f9-71c5-46a0-aa0c-51f150560dbc
ms.topic: article
ms.date: 05/31/2018
---

# Generating Interface UUIDs

This section presents information on Universal Unique Identifiers (UUIDs) and the Uuidgen utility in the following topics:

-   [What is a UUID?](#what-is-a-uuid)
-   [Using Uuidgen](#using-uuidgen)

## What is a UUID?

All interfaces must be uniquely identified on a network so that clients can find them. On small networks, the interface's name alone may be sufficient to identify it. However, that is usually not feasible on large networks. Therefore, developers typically assign a Universal Unique Identifier (UUID, interchangeable with the term GUID, or Globally Unique Identifier) to each interface. A UUID is a string that contains a set of hexadecimal digits. Each interface has a different UUID. For details, see [String UUID](string-uuid.md).

The textual representation of a UUID is a string consisting of 8 hexadecimal digits followed by a hyphen, followed by three hyphen-separated groups of 4 hexadecimal digits, followed by a hyphen, followed by 12 hexadecimal digits. The following example is a valid UUID string:

ba209999-0c6c-11d2-97cf-00c04f8eea45

Empty UUIDs are referred to as nil UUIDs rather than **NULL** UUIDs. The term nil indicates anything that is zero, blank, empty, or uninitialized. An empty string, an empty database record, or an uninitialized UUID are all examples of nil values.

> [!Note]  
> The value **NULL** is the specific value zero. It is often used in C and C++ programming in conjunction with pointers. Nil is a more general term than **NULL**. Uninitialized object interface UUIDs should always be referred to as nil UUIDs rather than **NULL** UUIDs.

 

## Using Uuidgen

Microsoft provides a utility program called Uuidgen to generate your UUIDs. The Uuidgen utility generates the UUID in IDL file format or C-language format.

When you run the Uuidgen utility from the command line, you can use the following command switches.



| Uuidgen switch           | Description                                                                |
|--------------------------|----------------------------------------------------------------------------|
| **/i**                   | Outputs UUID to an IDL interface template.                                 |
| **/s**                   | Outputs UUID as an initialized C structure.                                |
| **/o**<*filename*> | Redirects output to a file; specified immediately after the **/o** switch. |
| **/n**<*number*>   | Specifies the number of UUIDs to generate.                                 |
| **/v**                   | Displays version information about Uuidgen.                                |
| **/h** or **?**          | Displays command-option summary.                                           |



 

Typically, you will use the Uuidgen utility as shown in the following example.

**uuidgen -i -oMyApp.idl**

This command generates a UUID and stores it in a MIDL file that you can use as a template. When the preceding command is executed, the contents of MyApp.idl are similar to the following:

``` syntax
[
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
  version(1.0)
]
interface INTERFACENAME
{

}
```

The next step would be to replace the placeholder name, INTERFACENAME, with the actual name of your interface.

 

 




