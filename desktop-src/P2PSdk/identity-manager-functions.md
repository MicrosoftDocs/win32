---
Description: 'The Peer Identity Manager API uses the following functions.'
ms.assetid: '7621d26b-92e3-40c9-b0ce-94647d67f2c4'
title: Identity Manager Functions
---

# Identity Manager Functions

The Peer Identity Manager API uses the following functions.



| Function                                                           | Description                                                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerCreatePeerName**](peercreatepeername.md)                   | Creates a new name based on the existing name of the specified peer identity and classifier. However, a new identity is not created by a call to [**PeerCreatePeerName**](peercreatepeername.md).                                                                                                     |
| [**PeerEnumGroups**](peerenumgroups.md)                           | Creates and returns a peer enumeration handle used to enumerate all the peer groups associated with a specific peer identity.                                                                                                                                                                          |
| [**PeerEnumIdentities**](peerenumidentities.md)                   | Creates and returns a peer enumeration handle used to enumerate all the peer identities that belong to a specific user.                                                                                                                                                                                |
| [**PeerEndEnumeration**](peerendenumeration.md)                   | Releases an enumeration, for example, a record or member enumeration, and deallocates all resources associated with the enumeration.                                                                                                                                                                   |
| [**PeerFreeData**](peerfreedata.md)                               | Deallocates a block of data and returns it to the memory pool.                                                                                                                                                                                                                                         |
| [**PeerGetItemCount**](peergetitemcount.md)                       | Returns a count of the items in a peer enumeration.                                                                                                                                                                                                                                                    |
| [**PeerGetNextItem**](peergetnextitem.md)                         | Returns a specific number of items from a peer enumeration.                                                                                                                                                                                                                                            |
| [**PeerIdentityCreate**](peeridentitycreate.md)                   | Creates a new peer identity and returns its name. The name of the peer identity must be passed in all subsequent calls to the Peer Identity Manager, Peer Grouping, or PNRP functions that operate on behalf of the peer identity. The peer identity name specifies which peer identity is being used. |
| [**PeerIdentityDelete**](peeridentitydelete.md)                   | Deletes a peer identity. This includes removing all certificates, private keys, and all group information associated with a specified peer identity.                                                                                                                                                   |
| [**PeerIdentityExport**](peeridentityexport.md)                   | Allows a user to export one peer identity. The user can then transfer the peer identity to a different computer.                                                                                                                                                                                       |
| [**PeerIdentityGetCryptKey**](peeridentitygetcryptkey.md)         | Retrieves a handle to a cryptographic service provider (CSP).                                                                                                                                                                                                                                          |
| [**PeerIdentityGetDefault**](peeridentitygetdefault.md)           | Retrieves the default peer name set for the current user.                                                                                                                                                                                                                                              |
| [**PeerIdentityGetFriendlyName**](peeridentitygetfriendlyname.md) | Returns the friendly name of the peer identity.                                                                                                                                                                                                                                                        |
| [**PeerIdentityGetXML**](peeridentitygetxml.md)                   | Returns a description of the peer identity, which can then be passed to third parties and used to invite a peer identity into a peer group. This information is returned as an XML fragment.                                                                                                           |
| [**PeerIdentityImport**](peeridentityimport.md)                   | Imports one peer identity. If the peer identity exists on a computer, **PEER\_E\_ALREADY\_EXISTS** is returned.                                                                                                                                                                                        |
| [**PeerIdentitySetFriendlyName**](peeridentitysetfriendlyname.md) | Modifies the friendly name for a specified peer identity. The friendly name is the human-readable name.                                                                                                                                                                                                |



 

 

 



