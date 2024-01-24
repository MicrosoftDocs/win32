---
description: The following functions are used with network DDE.
ms.assetid: 5fd61759-1792-4db0-9ad4-adf112294b9c
title: Network DDE Functions
ms.topic: article
ms.date: 05/31/2018
---

# Network DDE Functions

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

The following functions are used with network DDE.



| Function                                                   | Description                                                                                                           |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**NDdeGetErrorString**](nddegeterrorstring.md)           | Converts an error code returned by a network DDE function into an error string that explains the returned error code. |
| [**NDdeGetShareSecurity**](nddegetsharesecurity.md)       | Retrieves the security descriptor associated with the DDE share.                                                      |
| [**NDdeGetTrustedShare**](nddegettrustedshare.md)         | Retrieves the options associated with a DDE share that is in the server user's list of trusted shares.                |
| [**NDdeIsValidAppTopicList**](nddeisvalidapptopiclist.md) | Determines whether an application and topic string ("*AppName*\|*TopicName*") uses the proper syntax.                 |
| [**NDdeIsValidShareName**](nddeisvalidsharename.md)       | Determines whether a share name uses the proper syntax.                                                               |
| [**NDdeSetShareSecurity**](nddesetsharesecurity.md)       | Sets the security descriptor associated with the DDE share.                                                           |
| [**NDdeSetTrustedShare**](nddesettrustedshare.md)         | Grants the specified DDE share trusted status within the current user's context.                                      |
| [**NDdeShareAdd**](nddeshareadd.md)                       | Creates and adds a new DDE share to the DDE share database manager (DSDM).                                            |
| [**NDdeShareDel**](nddesharedel.md)                       | Deletes a DDE share from the DSDM.                                                                                    |
| [**NDdeShareEnum**](nddeshareenum.md)                     | Retrieves the list of available DDE shares.                                                                           |
| [**NDdeShareGetInfo**](nddesharegetinfo.md)               | Retrieves DDE share information.                                                                                      |
| [**NDdeShareSetInfo**](nddesharesetinfo.md)               | Sets DDE share information.                                                                                           |
| [**NDdeTrustedShareEnum**](nddetrustedshareenum.md)       | Retrieves the names of all network DDE shares that are trusted in the context of the calling process.                 |



 

 

 



