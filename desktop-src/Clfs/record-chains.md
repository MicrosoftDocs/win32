---
Description: 'CLFS uses the concept of record chains to imply the next record in a sequence. There are several types of record chains that are used by CLFS.'
ms.assetid: '8730b6fb-0f19-4d9c-9605-7fe037b013c6'
title: Record Chains
---

# Record Chains

CLFS uses the concept of *record chains* to imply the next record in a sequence. There are several types of record chains that are used by CLFS.

The implicit physical chain—the next logical record that can be obtained by calling the [**ReadNextLogRecord**](readnextlogrecord.md) function. In this chain, there is always a record after the current record in this log stream.

The undo-next and undo-previous record chains—the records in this chain are not necessarily sequential in the log. These are logical chains, and are set up by the user. User-defined chains always point to an older record.

> [!Note]  
> All records in a chain must be within the same stream.

 

By convention, the term "previous" applies to the record immediately prior to the current record in the stream. The undo-next chain, by convention, is used by transactional resource managers to point to the previous record that is associated with the current record's transaction. This is not necessarily the same record as the record that is immediately adjacent to it in the log. It is up to the user to determine how these chains are used by their applications. For example, the user can point to every other record in the chain—CLFS does not provide any checking or verification for how chains are used by an application.

 

 



