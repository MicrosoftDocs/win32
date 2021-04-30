---
title: Provider Overview
description: Conceptual overview of a provider application.
ms.assetid: <GUID-GOES-HERE>
ms.date: 01/17/2020
ms.topic: article
---

# Provider Overview

The provider is a user-mode application that maintains and understands a backing data store.  The provider implements ProjFS callbacks and uses the ProjFS API to project this data store into the file system where it appears to the user as files and directories.  The provider’s backing store may be local to the user’s system, or it may be located remotely.

## Data Projection

The part of the file system that the provider owns, where its data is projected, is rooted in a directory called the “virtualization root”.  When the provider wants to start projecting its data it starts a "virtualization instance", which is an object that manages communication between the provider and ProjFS for the set of files and directories located under a particular virtualization root.  Any files and directories that are descendants of the virtualization root that have not been created locally by the user are materialized by the provider via the ProjFS API.  These items start off as virtual files and directories, meaning that they do not exist on the user’s local storage device, but are injected into enumeration results by ProjFS.  As the items are opened and read, ProjFS invokes callbacks implemented by the provider to request data, and the provider uses ProjFS APIs to send that data to the local storage where it is cached for subsequent access.  If the user's view of the backing data store needs to change, for instance if the contents of the data store have changed, the provider can use ProjFS APIs to update or delete local items to reflect the new view of the data store.

## Callback return codes

Each callback lists a number of possible return values specific to that callback.  In addition to the return values listed for a given callback, a callback may also return certain other error codes.  This is the complete list of error codes that a callback may return:

| Error Code                                    | Meaning
|-----------------------------------------------|--------
| S_OK                                          | Operation Successful
| E_OUTOFMEMORY                                 | Failed to allocate necessary memory.
| HRESULT_FROM_WIN32(ERROR_IO_PENDING)          | The provider wishes to complete the operation at a later time.
| HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER) | A buffer passed to a callback was too small.
| HRESULT_FROM_WIN32(ERROR_FILE_NOT_FOUND)      | The file does not exist in the provider’s backing store.
| HRESULT_FROM_WIN32(ERROR_INVALID_PARAMETER)   | A callback argument is invalid.  For example, an enumeration ID doesn't correspond to an active enumeration session.
| HRESULT_FROM_WIN32(ERROR_ACCESS_DENIED)       | The provider wishes to prevent an operation, such as a rename or delete, from taking place.

Callbacks may also return any errors they may receive from calls to ProjFS APIs.
If a callback returns an error code that is not on the preceding list or that did not come from a ProjFS API, ProjFS will return it to the file system as STATUS_INTERNAL_ERROR.
