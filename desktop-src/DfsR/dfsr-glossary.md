---
title: DFSR Glossary
description: This topic provides a glossary of technical terms used in the Distributed File System Replication (DFSR) SDK documentation.
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cb90e9ec-036d-495f-a2ec-4067bd729ba1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Distributed File System Replication Files , glossary"]
---

# DFSR Glossary

This topic provides a glossary of technical terms used in the Distributed File System Replication (DFSR) SDK documentation.

<dl> <dt>

<span id="fs.dfsr_glossary_conflict"></span><span id="FS.DFSR_GLOSSARY_CONFLICT"></span>**conflict**
</dt> <dd>

DFSR is a multi-master replicator where changes can originate on any member of the replication group. When changes originate independently without each member knowing of the other's changes, the changes are said to be in conflict. There are typically two types of conflicts: name conflicts and update conflicts. A name conflict occurs when two different versions of a file are created with the same name. An update conflict occurs if conflicting updates are made to the same version of the file.

</dd> <dt>

<span id="fs.dfsr_glossary_conflict_directory"></span><span id="FS.DFSR_GLOSSARY_CONFLICT_DIRECTORY"></span>**Conflict and Deleted folder**
</dt> <dd>

The folder that receives the files and folders that are discarded during conflict resolution. The manifest file, ConflictAndDeletedManifest.xml, specifies the location of the file and the name of the conflicted file.

</dd> <dt>

<span id="fs.dfsr_glossary_connection"></span><span id="FS.DFSR_GLOSSARY_CONNECTION"></span>**connection**
</dt> <dd>

A logical DFSR interconnection between two nodes. Connections are defined by their bandwidth and duration. A closed connection implies a connection of bandwidth 0.

</dd> <dt>

<span id="fs.dfsr_glossary_content_set"></span><span id="FS.DFSR_GLOSSARY_CONTENT_SET"></span>**content set**
</dt> <dd>

See *replicated folder*.

</dd> <dt>

<span id="fs.dfsr_glossary_activity_log"></span><span id="FS.DFSR_GLOSSARY_ACTIVITY_LOG"></span>**debug log**
</dt> <dd>

The log used to record DFSR activity for debugging. By default, this log is located in the %systemdir%\\debug folder.

</dd> <dt>

<span id="fs.dfsr_glossary_dfsn"></span><span id="FS.DFSR_GLOSSARY_DFSN"></span>**DFS Namespaces (DFSN)**
</dt> <dd>

A service that system administrators can use to organize distributed network shares into a logical namespace. This enables users to access files without specifying their physical location. It also provides load sharing across the network.

</dd> <dt>

<span id="fs.dfsr_glossary_dfsr"></span><span id="FS.DFSR_GLOSSARY_DFSR"></span>**DFS Replication (DFSR)**
</dt> <dd>

A service that manages keeping DFS folders in sync automatically. DFSR is a state-based, multimaster replication system that supports replication scheduling and bandwidth throttling.

</dd> <dt>

<span id="fs.dfsr_glossary_dfs"></span><span id="FS.DFSR_GLOSSARY_DFS"></span>**Distributed File System (DFS)**
</dt> <dd>

DFS refers to two technologies, DFS Namespaces (DFSN) and DFS Replication (DFSR), that can be used together to provide simplified, fault-tolerant access to files, load sharing, and WAN-friendly replication.

</dd> <dt>

<span id="fs.dfsr_glossary_fence"></span><span id="FS.DFSR_GLOSSARY_FENCE"></span>**fence**
</dt> <dd>

An operation that protects a file so that the version with the highest fence will win during a conflict resolution.

</dd> <dt>

<span id="fs.dfsr_glossary_frs"></span><span id="FS.DFSR_GLOSSARY_FRS"></span>**File Replication Service (FRS)**
</dt> <dd>

A service that replicates files and folders stored in shared folders. When FRS detects that a change has been made to a file or folder within a replicated shared folder, FRS replicates the updated file or folder to the other servers. By keeping files and folders synchronized across servers, FRS enables organizations to increase data availability; it also enables organizations to make data available across multiple geographic locations such that users can access a server in or close to their current site.

</dd> <dt>

<span id="fs.dfsr_glossary_folder"></span><span id="FS.DFSR_GLOSSARY_FOLDER"></span>**folder**
</dt> <dd>

A folder that contains links or other folders.

</dd> <dt>

<span id="fs.dfsr_glossary_link"></span><span id="FS.DFSR_GLOSSARY_LINK"></span>**link**
</dt> <dd>

The logical name of a folder that is redirected to another network share.

</dd> <dt>

<span id="fs.dfsr_glossary_link_target"></span><span id="FS.DFSR_GLOSSARY_LINK_TARGET"></span>**link target**
</dt> <dd>

The destination of a link; for example, a shared folder or a path that begins with a DFS root.

</dd> <dt>

<span id="fs.dfsr_glossary_member"></span><span id="FS.DFSR_GLOSSARY_MEMBER"></span>**member**
</dt> <dd>

A computer participating in replication.

</dd> <dt>

<span id="fs.dfsr_glossary_namespace"></span><span id="FS.DFSR_GLOSSARY_NAMESPACE"></span>**namespace**
</dt> <dd>

A virtual view of shared folders on different servers that is provided by DFS. A namespace consists of a root, folders, and links.

</dd> <dt>

<span id="fs.dfsr_glossary_partner"></span><span id="FS.DFSR_GLOSSARY_PARTNER"></span>**partner**
</dt> <dd>

A computer that a member communicates with through the replication service.

</dd> <dt>

<span id="fs.dfsr_glossary_rdc"></span><span id="FS.DFSR_GLOSSARY_RDC"></span>**Remote differential compression (RDC)**
</dt> <dd>

A client-server algorithm that synchronizes two files across a network with a minimum amount of data transfer over the network.

</dd> <dt>

<span id="fs.dfsr_glossary_replica"></span><span id="FS.DFSR_GLOSSARY_REPLICA"></span>**replica**
</dt> <dd>

A network share that backs a link.

</dd> <dt>

<span id="fs.dfsr_glossary_replicated_folder"></span><span id="FS.DFSR_GLOSSARY_REPLICATED_FOLDER"></span>**replicated folder**
</dt> <dd>

Defines a set of files and folder to be kept in sync across multiple servers in a replication group. Replicated folders are defined using the computer name, the local path of the data on each server in a replication group, and on-demand replication characteristics for each server. Replicated folders are also called "content sets."

</dd> <dt>

<span id="fs.dfsr_glossary_replication_group"></span><span id="FS.DFSR_GLOSSARY_REPLICATION_GROUP"></span>**replication group**
</dt> <dd>

Defines a set of computers that participate in replication. It also defines the connections between these computers, including scheduling and bandwidth throttling. Each replication group can have multiple replicated folders.

</dd> <dt>

<span id="fs.dfsr_glossary_root"></span><span id="FS.DFSR_GLOSSARY_ROOT"></span>**root**
</dt> <dd>

The starting point of a namespace. A root maps to one or more root targets, each of which corresponds to a shared folder on a separate server. The root must reside on an NTFS volume; it has one of the following formats: \\\\*server*\\*root* or \\\\*domain*\\*root*.

Domain roots have their configuration information stored in the Active Directory. Standalone roots have their information stored locally in the registry of the host server.

</dd> <dt>

<span id="fs.dfsr_glossary_slow_sync"></span><span id="FS.DFSR_GLOSSARY_SLOW_SYNC"></span>**slow sync**
</dt> <dd>

A pairwise database comparison algorithm that resolves any inconsistencies that result from tombstoning.

</dd> <dt>

<span id="fs.dfsr_glossary_staging_directory"></span><span id="FS.DFSR_GLOSSARY_STAGING_DIRECTORY"></span>**staging folder**
</dt> <dd>

A holding area used by the replication service when creating a compressed version of a file for serving.

</dd> <dt>

<span id="fs.dfsr_glossary_tombstone"></span><span id="FS.DFSR_GLOSSARY_TOMBSTONE"></span>**tombstone**
</dt> <dd>

A delete operation cannot cause a resource to be deleted from the internal database until the operation has propagated to all members of a replication group. Until the entry is deleted, it is tombstoned on the member.

</dd> </dl>

 

 




