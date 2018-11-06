---
title: GUID Creation and Optimizations
description: GUID Creation and Optimizations
ms.assetid: 698322f2-db89-4553-90c6-4278e96716dc
ms.topic: article
ms.date: 05/31/2018
---

# GUID Creation and Optimizations

Because a CLSID, like an interface identifier (IID), is a GUID, no other class, no matter who writes it, has a duplicate CLSID. Server implementers generally obtain CLSIDs through the [**CoCreateGuid**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateguid) function. This function is guaranteed to produce unique CLSIDs, so server implementers across the world can independently develop and deploy their software without fear of accidental collision with software written by others.

Using unique CLSIDs avoids the possibility of name collisions among classes because CLSIDs are in no way connected to the names used in the underlying implementation. For example, two different vendors can write classes called "StackClass," but each would have a unique CLSID and therefore could not be confused.

COM frequently must map GUIDs (IIDs and CLSIDs) to some arbitrarily large set of other values. As an application developer, you can help speed up such searches, and thereby enhance system performance, by generating the GUIDs for your application as a block of consecutive values.

The most efficient way to generate a block of consecutive GUIDs is to run the uuidgen utility using the -n and -x switches, which generates a block of UUIDs, each of whose first DWORD value is incremented by one.

For example, if you were to type

**uuidgen -n5 -x**

the uuidgen utility would generate a block of UUIDs similar to the following:

``` syntax
12340001-4980-1920-6788-123456789012
12340002-4980-1920-6788-123456789012
12340003-4980-1920-6788-123456789012
12340004-4980-1920-6788-123456789012
12340005-4980-1920-6788-123456789012
 
```

One method for generating and tracking GUIDs for an entire project begins with generating a block of some arbitrarily large number of UUIDs, say 500. For example, if you were to type

**uuidgen -n500 -x > guids.txt**

the utility would generate 500 consecutive UUIDs and write them to the specified text file. You could then check this file into your source tree, providing a single repository for all GUIDs to be used in a project. As people require GUIDs for their portions of the project, they can check out the file, take however many GUIDs they need, marking them as taken and leaving a note about where in the code or "spec" they are using them.

In addition to improving system performance, generating blocks of consecutive GUIDs in this way has the following benefits:

-   A central file containing all GUIDs for an application makes it easy to keep track of which GUIDs are for what and which people are using them.
-   A block of consecutive GUIDs associated with a particular application helps developers and testers recognize internal GUIDs during debugging and makes it easier to find them in the system registry because they are stored sequentially.

## Related topics

<dl> <dt>

[COM Server Responsibilities](com-server-responsibilities.md)
</dt> </dl>

 

 




