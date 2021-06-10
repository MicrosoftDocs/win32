---
title: IAgent Load
description: IAgent Load
ms.assetid: 8f25e6b6-a117-4b37-969a-d8f80c7be224
ms.topic: article
ms.date: 05/31/2018
---

# IAgent::Load

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Load(
   VARIANT vLoadKey,  // data provider
   long * pdwCharID,  // address of a variable for character ID
   long * pdwReqID    // address of a variable for request ID
);
```

Loads a character into the [**Characters**](./iagent.md) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="vLoadKey"></span><span id="vloadkey"></span><span id="VLOADKEY"></span>*vLoadKey*
</dt> <dd>

A variant datatype that must be one of the following:



| Value           | Description                                                                      |
|------------|-----------------------------------------------------------------------|
| *filespec* | The local file location of the specified character's definition file. |
| *URL*      | The HTTP address for the character's definition file.                 |



 

</dd> <dt>

<span id="pdwCharID"></span><span id="pdwcharid"></span><span id="PDWCHARID"></span>*pdwCharID*
</dt> <dd>

Address of a variable that receives the character's ID.

</dd> <dt>

<span id="pdwReqID"></span><span id="pdwreqid"></span><span id="PDWREQID"></span>*pdwReqID*
</dt> <dd>

Address of a variable that receives the [**Load**](load-method.md) request ID.

</dd> </dl>

You can load characters from the Microsoft Agent subdirectory by specifying a relative path (one that does not include a colon or leading slash character). This prefixes the path with Agent's characters directory (located in the localized %windows%\\msagent directory). You can also use a relative address to specify your own directory in Agent's Chars directory.

You cannot load the same character (a character having the same GUID) more than once from a single connection. Similarly, you cannot load the default character and other characters at the same time from a single connection, because the default character could be the same as the other character. However, you can create another connection (using CoCreateInstance) and load the same character.

Microsoft Agent's data provider supports loading character data stored as a single structured file (.ACS) with character data and animation data together, or as separate character data (.ACF) and animation (.ACA) files. Generally, use the single structured .ACS file to load a character that is stored on a local disk drive or network and accessed using conventional file protocol (such as UNC pathnames). Use the separate .ACF and .ACA files when you want to load the animation files individually from a remote site where they are accessed using HTTP protocol.

For .ACS files, using the [**Load**](load-method.md) method provides access a character's animations; once loaded, you can use the [**Play**](play-method.md) method to animate the character. For .ACF files, you also use the [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) method to load animation data. The **Load** method does not support downloading .ACS files from an HTTP site.

Loading a character does not automatically display the character. Use the [**Show**](show-method.md) method first to make the character visible.

 

 