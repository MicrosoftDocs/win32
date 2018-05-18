---
Description: 'The Microsoft Peer Distribution service supports the following structures.'
ms.assetid: '26badfe6-3a5a-4c2e-9ef1-534c2e8573d0'
title: Peer Distribution API Structures
---

# Peer Distribution API Structures

The Microsoft Peer Distribution service supports the following structures.



| Structure                                                              | Description                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PEERDIST\_CLIENT\_BASIC\_INFO**](peerdist-client-basic-info.md)    | Indicates whether or not there are many clients simultaneously downloading the same content.                                                                                                                                                                                             |
| [**PEERDIST\_CONTENT\_TAG**](peerdist-content-tag.md)                 | Contains a client supplied tag which is an input value for [**PeerDistClientOpenContent**](peerdistclientopencontent.md). The tag is associated with the content segment and is used in content management APIs, like [**PeerDistClientFlushContent**](peerdistclientflushcontent.md). |
| [**PEERDIST\_PUBLICATION\_OPTIONS**](peerdist-publication-options.md) | Contains publication options, including the API version information and possible option flags.                                                                                                                                                                                           |
| [**PEER\_RETRIEVAL\_OPTIONS**](peerdist-retrieval-options.md)         | Contains version of the content information to retrieve.                                                                                                                                                                                                                                 |
| [**PEERDIST\_STATUS\_INFO**](peerdist-status-info.md)                 | Contains information about the current status and capabilities of the BranchCache service on the local computer.                                                                                                                                                                         |



 

## Related topics

<dl> <dt>

[Peer Distribution API Reference](peer-distribution-api-reference.md)
</dt> </dl>

 

 



