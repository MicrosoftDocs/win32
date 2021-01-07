---
description: This topic discusses alternatives to using Transactional NTFS API (TxF) in common usage scenarios.
ms.assetid: 9ee26e7e-990e-4cd3-8180-f0fcaac2b752
title: Alternatives to using Transactional NTFS
ms.topic: article
ms.date: 05/31/2018
---

# Alternatives to using Transactional NTFS

-   [Abstract](#abstract)
-   [Introduction](#introduction)
-   [Alternatives to TxF by Scenario](#alternatives-to-txf-by-scenario)
-   [Applications updating a single file with "document-like" data](#applications-updating-a-single-file-with-document-like-data)
-   [Applications performing updates to multiple files and/or to the registry hive](#applications-performing-updates-to-multiple-files-andor-to-the-registry-hive)
-   [Applications managing a set of structured data](#applications-managing-a-set-of-structured-data)
-   [Applications with Transactions involving files on a local NTFS volume and Tables in an external SQL database](#applications-with-transactions-involving-files-on-a-local-ntfs-volume-and-tables-in-an-external-sql-database)
-   [Closing & Recommended Action](/windows)

## Abstract

Microsoft strongly recommends developers investigate utilizing the discussed alternatives (or in some cases, investigate other alternatives) rather than adopting an API platform which may not be available in future versions of Windows.

## Introduction

TxF was introduced with Windows Vista as a means to introduce atomic file transactions to Windows. It allows for Windows developers to have transactional atomicity for file operations in transactions with a single file, in transactions involving multiple files, and in transactions spanning multiple sources – such as the Registry (through TxR), and databases (such as SQL). While TxF is a powerful set of APIs, there has been extremely limited developer interest in this API platform since Windows Vista primarily due to its complexity and various nuances which developers need to consider as part of application development. As a result, Microsoft is considering deprecating TxF APIs in a future version of Windows to focus development and maintenance efforts on other features and APIs which have more value to a larger majority of customers. The next section describes sample alternative methods to achieve similar results as TxF would for several types of application scenarios.

## Alternatives to TxF by Scenario

With the limitations described above, developers should investigate alternatives to TxF to cover application scenarios which are not met by TxF. Discussed here are some suggested alternatives to common uses of TxF for developers to consider. Note that this list is neither exhaustive nor complete.

## Applications updating a single file with "document-like" data

Many applications which deal with "document-like" data tend to load the entire document into memory, operate on it, and then write it back out to save the changes. The needed atomicity here is that the changes either are completely applied or not applied at all, as an inconsistent state would render the file corrupt. A common approach is to write the document to a new file, then replace the original file with the new one. One method to do this is with the [**ReplaceFile**](/windows/desktop/api/WinBase/nf-winbase-replacefilea) API.

## Applications performing updates to multiple files and/or to the registry hive

There are many applications which need to atomically perform an update to a set of files and to the registry. This scenario is most commonly achieved through an installer application, such as Windows Installer. For more information on Windows Installer, please refer to [Windows Installer](/windows/desktop/Msi/windows-installer-portal).

## Applications managing a set of structured data

Many applications manage some set of proprietary data structures of varying types as a means to store data. A significant challenge for these applications is the process of maintaining the integrity of internal pointers/references if a failure occurs during an update operation. Creating the mechanism for this is indeed a "hard problem", and therefore most applications will rely on a true database server to manage their dataset.

Two suggestions to help manage structured data are:

-   Microsoft provides the Extensible Storage Engine (ESE) inbox in Windows to enable applications to perform transacted data update and retrieval operations. For more information on the Extensible Storage Engine (ESE), please see <https://msdn.microsoft.com/library/gg269259.aspx>.
-   For applications that require a more powerful, robust, and scalable database provider, it is recommended that customers consider using the Filestream feature available with Microsoft SQL Server. For more information on SQL Filestreams, please see <https://technet.microsoft.com/library/bb933993.aspx>.

## Applications with Transactions involving files on a local NTFS volume and Tables in an external SQL database

There are classes of applications which either have large dataset needs, or need to have transactional atomicity in an operation involving an external database and local storage. For this scenario, it is highly recommended that developers consider using SQL Filestreams to perform transactional file operations. For more information on SQL Filestreams, please see <https://technet.microsoft.com/library/bb933993.aspx>.

## Closing & Recommended Action

TxF is a complex and nuanced set of APIs which are not commonly used by 3rd party applications. With the possibility that these APIs may not be available in future versions of Windows, and the fact that there are simpler alternative means to achieve many of the scenarios which TxF was developed for, Microsoft strongly recommends developers to investigate those alternative means instead of creating a dependency on TxF in their applications.

 

 
