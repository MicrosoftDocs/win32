---
title: Windows Projected File System glossary
description: Special terms used in ProjFS.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: <GUID-GOES-HERE>
ms.date: 01/17/2020
ms.topic: article
---

# Windows Projected File System glossary

Special terms used in ProjFS.

<dl>
<dt>

<span id="projfs.glossary_backing_store"></span><span id="PROJFS.GLOSSARY_BACKING_STORE"></span>**backing store**
</dt>
<dd>

Provider-maintained hierarchical data that is projected into the file system as files and directories.
</dd>

<dt>

<span id="projfs.glossary_dirty_placeholder"></span><span id="PROJFS.GLOSSARY_DIRTY_PLACEHOLDER"></span>**dirty placeholder**
</dt>
<dd>

A file or directory that has been locally modified and is no longer a cache of its state in the provider's store.  See [Cache State in the Virtualization Root](cache-state.md).
</dd>

<dt>

<span id="projfs.glossary_full_file_directory"></span><span id="PROJFS.GLOSSARY_FULL_FILE_DIRECTORY"></span>**full file/directory**
</dt>
<dd>

A file or directory that was created in the local file system, or a file that has been modified, making it no longer a cache of its state in the backing store.  See [Cache State in the Virtualization Root](cache-state.md).
</dd>

<dt>

<span id="projfs.glossary_hydrated_placeholder"></span><span id="PROJFS.GLOSSARY_HYDRATED_PLACEHOLDER"></span>**hydrated placeholder**
</dt>
<dd>

A file whose content and metadata have been cached to disk.  See [Cache State in the Virtualization Root](cache-state.md).
</dd>

<dt>

<span id="projfs.glossary_placeholder"></span><span id="PROJFS.GLOSSARY_PLACEHOLDER"></span>**placeholder**
</dt>
<dd>

A file or directory that is not fully present on disk.  See [Cache State in the Virtualization Root](cache-state.md).
</dd>

<dt>

<span id="projfs.glossary_tombstone"></span><span id="PROJFS.GLOSSARY_TOMBSTONE"></span>**tombstone**
</dt>
<dd>

A special hidden placeholder that represents an item that has been deleted from the local file system.  See [Cache State in the Virtualization Root](cache-state.md).
</dd>

<dt>

<span id="projfs.glossary_virtual_file_directory"></span><span id="PROJFS.GLOSSARY_virtual_file_directory"></span>**virtual file/directory**
</dt>
<dd>

A file or directory that does not physically exist on disk, but is projected into enumeration results.  See [Cache State in the Virtualization Root](cache-state.md).
</dd>

<dt>

<span id="projfs.glossary_virtualization_instance"></span><span id="PROJFS.GLOSSARY_VIRTUALIZATION_INSTANCE"></span>**virtualization instance**
</dt>
<dd>

An in-memory object that manages communication between the provider and ProjFS for the set of files and directories located under a particular virtualization root.
</dd>

<dt>

<span id="projfs.glossary_virtualization_root"></span><span id="PROJFS.GLOSSARY_VIRTUALIZATION_ROOT"></span>**virtualization root**
</dt>
<dd>

A directory in the file system under which the provider's data is projected.
</dd>

</dl>

<!--
<dt>

<span id="projfs.glossary_"></span><span id="PROJFS.GLOSSARY_"></span>**TERM**
</dt>
<dd>

DEFINITION
</dd>
-->