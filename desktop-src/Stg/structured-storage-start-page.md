---
title: Structured Storage
description: Structured Storage provides file and data persistence in COM by handling a single file as a structured collection of objects known as storages and streams.
ms.assetid: 57a5f34d-c3db-47c5-9836-6e2163732d30
keywords:
- Structured Storage Strctd Stg
- Structured Storage Strctd Stg , start page
ms.topic: article
ms.date: 05/31/2018
---

# Structured Storage

## Purpose

Structured Storage provides file and data persistence in COM by handling a single file as a structured collection of objects known as storages and streams.

The purpose of Structured Storage is to reduce the performance penalties and overhead associated with storing separate objects in a single file. Structured Storage provides a solution by defining how to handle a single file entity as a structured collection of two types of objects storages and streams through a standard implementation called Compound Files. This enables the user to interact with, and manage, a compound file as if it were a single file rather than a nested hierarchy of separate objects.

## Where applicable

Structured Storage can be used on Microsoft COM-based operating systems.

## Developer audience

The Structured Storage documentation is intended for experienced C and C++ programmers and COM-based system developers.

Structured Storage primarily supports C and C++ programming languages, however any COM-based technology will also support any programming language that utilizes interface pointers.

A solid understanding of COM technologies is prerequisite to the developmental use of Structured Storage.

## Run-time requirements

For more information about which operating systems are required to use a particular API element, see the Requirements section of the documentation for the element.

## In this section



| Topic                                                               | Description                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Overview](about-structured-storage.md)<br/>                 | General information about Structured Storage.<br/>                                                                                                                                                                                                                                                 |
| [Using Structured Storage](using-structured-storage.md)<br/> | Using information for Structured Storage.<br/>                                                                                                                                                                                                                                                     |
| [Reference](structured-storage-reference.md)<br/>            | Documentation of Structured Storage specific interfaces, functions, structures, and enumerations.<br/>                                                                                                                                                                                             |
| [Samples](samples.md)<br/>                                   | Code examples written in C++. For more information, see [Names in IStorage](names-in-istorage.md), [Property Set Header](property-set-header.md), [Section](section.md), [Storing Property Sets](storing-property-sets.md), and [Using Structured Storage](using-structured-storage.md).<br/> |



 

## Related topics

<dl> <dt>

[The Component Object Model](../com/the-component-object-model.md)
</dt> </dl>

 

