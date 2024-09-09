---
description: Transactional NTFS (TxF) allows file operations on an NTFS file system volume to be performed in a transaction.
ms.assetid: e8c3ceed-d391-4934-b3f7-12c2123c8c23
title: Transactional NTFS (TxF)
ms.topic: article
ms.date: 05/31/2018
---

# Transactional NTFS (TxF)

\[Microsoft strongly recommends developers utilize alternative means to achieve your application's needs. Many scenarios that TxF was developed for can be achieved through simpler and more readily available techniques. Furthermore, TxF may not be available in future versions of Microsoft Windows. For more information, and alternatives to TxF, please see [Alternatives to using Transactional NTFS](deprecation-of-txf.md).\]

## Purpose

Transactional NTFS (TxF) allows file operations on an NTFS file system volume to be performed in a transaction. TxF transactions increase application reliability by protecting data integrity across failures and simplify application development by greatly reducing the amount of error handling code.

TxF uses the transaction framework provided by the [Kernel Transaction Manager](/windows/desktop/Ktm/kernel-transaction-manager-portal) (KTM). This allows TxF file operations to be part of a transaction involving other data sources such as SQL Server and Transacted Registry (TxR).

## Where applicable

An application can use TxF to preserve the integrity of data on disk caused by unexpected error conditions and help resolve concurrent file-system user scenarios by isolating your changes from others while the changes are being made.

## Developer audience

Before using TxF, you should have a working knowledge of transactions using either KTM or [Distributed Transaction Coordinator (DTC)](/previous-versions/windows/desktop/ms684146(v=vs.85)).

## Run-time requirements

TxF is available starting with Windows Vista.

## In this section



| Topic                                                    | Description                                                                                                |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [About](about-transactional-ntfs.md)<br/>         | General information about Transactional NTFS.<br/>                                                   |
| [Reference](transactional-ntfs-reference.md)<br/> | Documentation for the functions, data structures, enumerations, and other programming elements.<br/> |



 

 

