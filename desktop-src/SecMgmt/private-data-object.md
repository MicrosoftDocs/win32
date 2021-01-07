---
description: A limited number of private data objects are available on each system for the purpose of storing information in a protected, encrypted, fashion.
ms.assetid: 927473d7-b5bc-4b6f-b303-8a0f8680731d
title: Private Data Object
ms.topic: article
ms.date: 05/31/2018
---

# Private Data Object

A limited number of private data objects are available on each system for the purpose of storing information in a protected, encrypted, fashion.

Private data objects are provided primarily to support storage of server account passwords. This is useful for servers that run in a specific account. The password of the server account is private data that should be secured but is needed to log the server on.

Private data objects may be general purpose, or they may be one of three specialized types: local, global, and machine.

Local private data objects can only be read locally from the computer storing the object. Attempting to read them remotely results in a STATUS\_ACCESS\_DENIED error. Local private data objects have key names that begin with the prefix "L$". In addition to the local private objects you create, the operating system defines the following local private objects: $machine.acc, SAC, SAI, and SANSC.

Global private data objects are global in the sense that if they are created on a domain controller, they will be automatically replicated to all domain controllers in that domain. In other words, each domain controller in that domain will have access to the values the global private data object contains. In contrast, global private data objects created on a system that is not a domain controller, as well as nonglobal private data objects, are not replicated. Global private data objects have key names beginning with "G$".

Machine private data objects can be accessed only by the operating system. These objects have key names that begin with "M$".

**Note**  You can set, but you cannot retrieve, machine private data objects.

In addition to these prefixes, the following values also indicate local or machine objects. These values are supported for backward compatibility and should not be used when you create new local or machine objects. The key name of local private data objects may also start with "RasDialParms" or "RasCredentials". The key name for machine objects may also start with, "NL$" or "\_sc\_".

Private data objects that are not one of the preceding specialized types use key names that do not start with a prefix. These objects are not replicated and can be read either locally or remotely by applications.

 

 



