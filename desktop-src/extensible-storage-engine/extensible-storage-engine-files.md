---
description: "Learn more about: Extensible Storage Engine Files"
title: Extensible Storage Engine Files
TOCTitle: Extensible Storage Engine Files
ms:assetid: b89a8f78-f2c4-4cbf-a000-a95c34589033
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294069(v=EXCHG.10)
ms:contentKeyID: 32765684
ms.date: 09/22/2016
ms.topic: article
---

# Extensible Storage Engine Files


_**Applies to:** Windows | Windows Server_

## Extensible Storage Engine Files

The Extensible Storage Engine uses the following types of files:

- [Transaction Log Files](#transaction-log-files)

- [Temporary Transaction Log Files](#temporary-transaction-log-files)

- [Reserved Transaction Log Files](#reserved-transaction-log-files)

- [Checkpoint Files](#checkpoint-files)

- [Database Files](#database-files)

- [Temporary Databases](#temporary-databases)

- [Flush Map Files](#flush-map-files)

This table contains an overview of the data file names that are managed by ESE. For Windows Vista and later, the JET_paramLegacyNames setting impacts the file names that are used.

<table xmlns="https://www.w3.org/1999/xhtml">
  <tr>
    <th>
      <p>Operating System</p>
    </th>
    <th>
      <p>Windows Server 2003 and earlier<br /><br /></p>
    </th>
    <th colspan="2">
      <p></p>
      <p>Windows Vista and later (client) <br />
Windows Server 2008 and later (server)
</p>
    </th>
    <th>
      <p>Windows 10 Anniversary Update and later (client) <br />
Windows Server 2016 and later (server)
</p>
    </th>
  </tr>
  <tr>
    <td>
      <p>
        <strong>JET_paramLegacyNames setting</strong>
      </p>
    </td>
    <td>
      <p>
        <strong>N/A</strong>
      </p>
    </td>
    <td>
      <p>
        <strong>None</strong>
      </p>
    </td>
    <td>
      <p>
        <strong>JET_bitESE98FileNames</strong>
      </p>
    </td>
    <td>
      <p>
        <strong>Same as Windows Vista/Server 2008</strong>
      </p>
    </td>
  </tr>
  <tr>
    <td>
      <p>Current Log</p>
    </td>
    <td>
      <p>&lt;inst&gt;.log</p>
    </td>
    <td>
      <p>&lt;inst&gt;.jtx</p>
    </td>
    <td>
      <p>&lt;inst&gt;.log</p>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Pre-Init Log</p>
    </td>
    <td>
      <p>&lt;inst&gt;tmp.log</p>
    </td>
    <td>
      <p>&lt;inst&gt;tmp.jtx</p>
    </td>
    <td>
      <p>&lt;inst&gt;tmp.log</p>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>Rotated Logs</p>
    </td>
    <td>
      <p>&lt;inst&gt;XXXXX.log</p>
    </td>
    <td>
      <p>&lt;inst&gt;XXXXX.jtx after FFFFF switch to &lt;inst&gt;XXXXXXXX.jtx</p>
    </td>
    <td>
      <p>&lt;inst&gt;XXXXX.log after FFFFF switch to &lt;inst&gt;XXXXXXXX.log.</p>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>
        <a href="gg294069(v=exchg.10).md">Checkpoint Files</a>
      </p>
    </td>
    <td>
      <p>&lt;inst&gt;.chk</p>
    </td>
    <td>
      <p>&lt;inst&gt;.jcp</p>
    </td>
    <td>
      <p>&lt;inst&gt;.chk</p>
    </td>
    <td rowspan="2"></td>
  </tr>
  <tr>
    <td>
      <p>
        <a href="gg294069(v=exchg.10).md">Temporary Databases</a>
      </p>
    </td>
    <td>
      <p>&lt;temp db file name&gt; Default: tmp.edb</p>
    </td>
    <td>
      <p>&lt;temp db file name&gt; Default: tmp.edb</p>
    </td>
    <td>
      <p>&lt;temp db file name&gt; Default: tmp.edb</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>
        <a href="gg294069(v=exchg.10).md">Reserved Transaction Log Files</a>
      </p>
    </td>
    <td>
      <p>res1.log &amp; res2.log</p>
    </td>
    <td>
      <p>&lt;inst&gt;RESXXXXX.jrs</p>
    </td>
    <td colspan="2">
      <p>&lt;inst&gt;RESXXXXX.jrs</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>
        <a href="gg294069(v=exchg.10).md">Database Files</a>
      </p>
    </td>
    <td>
      <p>&lt;db file name&gt;</p>
    </td>
    <td>
      <p>&lt;db file name&gt;</p>
    </td>
    <td>
      <p>&lt;db file name&gt;</p>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>
      <p>
        <a href="gg294069(v=exchg.10).md">Flush Map Files</a>
      </p>
    </td>
    <td>
      <p>N/A</p>
    </td>
    <td>
      <p>N/A</p>
    </td>
    <td>
      <p>N/A</p>
    </td>
    <td>
      <p>&lt;db file name without extension&gt;.jfm</p>
    </td>
  </tr>
</table>


### Transaction Log Files

Transaction log files contain operations on database files. They contain enough information to bring a database to a logically consistent state after an unexpected process termination or system shutdown.

The names of the log files are dependent on a three-letter base name, which can be set with [JET_paramBaseName](./transaction-log-parameters.md). The examples below use a base name of "edb", because that is the default base name. The extension for the transaction log files will be either .log or .jtx depending upon whether the JET_bitESE98FileNames is set in the JET_paramLegacyFileNames parameter. For more information, see [Extensible Storage Engine System Parameters](./extensible-storage-engine-system-parameters.md).

Transaction log files are named \<base\>\<generation-number\>.log, beginning with 1. The log generation number is in hexadecimal format. For example, edb00001.log is the first log, and edb000ff.log is the 255th log. The log files have five hexadecimal digits in the log file name, until the 1048576th log file, at which point the log files start being named in an 11.3 format (for example, edb00100000.log). \<base\>.log is always the log file that is currently being used. If the database engine is not active, the generation of edb.log can be identified using the following command: **esentutl.exe -ml edb.log**.

Although transaction log files have the .LOG extension commonly associated with text files, transaction log files are in a binary format and should never be edited by a user.Database operations are written to the log first. The data can be written to the database file later; possibly immediately, potentially much later. In the event of unexpected process or system termination, the operations are still present in the log files, and incomplete transactions can be rolled back. The act of replaying transaction log files is called *soft recovery*, and it is done automatically when [JetInit](./jetinit-function.md) or [JetInit2](./jetinit2-function.md) is called. Soft recovery can also be performed manually with the "-r" option of the Esentutl.exe program. The act of replaying transaction log files on a database that is restored from a backup is called *hard recovery*.

Log files are of a fixed size, customizable with [JET_paramLogFileSize](./transaction-log-parameters.md). When the current log file (that is, edb.log) gets filled, it gets renamed to \<base\>\<generation-number\>.log, and a new transaction log file is needed in the transaction log stream.

Each database instance has a single log file sequence associated with it. Windows XP introduced [JetCreateInstance](./jetcreateinstance-function.md), allowing multiple transaction log file sequences to be used by a single process. Multiple transaction log file sequences cannot exist in the same directory, however.

Transaction log files should almost never be manually manipulated, renamed, moved, or deleted because data corruption can result.

Transaction log files will be deleted by the database engine during a full backup (see [JetBackup](./jetbackup-function.md), [JetTruncateLog](./jettruncatelog-function.md), [JetTruncateLogInstance](./jettruncateloginstance-function.md)), or during normal operations, if circular logging is enabled.

After a transaction log file is filled up, the database engine needs to create a new log file. Circular logging is a means by which log files can be automatically cleaned up by the database engine when they are no longer required for crash recovery. This process is an alternative to removing log files as a by-product of performing a backup. Circular logging can be controlled with the [JET_paramCircularLog](./transaction-log-parameters.md) system parameter. Transaction log files should not be deleted using any other method.

### Temporary Transaction Log Files

When edb.log fills up, ESE needs to create a new file. The new log transaction file is known as a temporary transaction log file prior to its use by ESE.

While a new log file is created and its size extended, it will be called \<base\>tmp.log. Creating a new file can be a potentially costly operation, so ESE will create the next log file proactively as a background task.

Because the temporary transaction log file is created in anticipation of need for a new transaction log file, it does not contain any useful information.

### Reserved Transaction Log Files

The reserved transaction log files are created when the engine starts to allow important operations to be logged to get a clean shutdown.

**Windows Vista:** In Windows Vista and later, the Reserved Transaction Log Files are named \<base\>RESXXXXX.jrs.

**Windows Server 2003:** In Windows Server 2003 and earlier, The Reserved Transaction Log Files are named res1.log and res2.log.

When the database engine runs out of disk space it cannot create a new log file. The safest thing to do is to shut down cleanly, but some operations (such as rollback operations) must still be logged. Most database operations will fail during this stage.

Because the reserved transaction log files are created in anticipation of need for transaction log files in an out-of-disk scenario, they do not contain any useful information.

### Checkpoint Files

The checkpoint file stores the checkpoint for a particular transaction log file sequence. The checkpoint file is named \<base\>.chk or \<base\>.jcp, depending upon whether the JET_bitESE98FileNames is set in the JET_paramLegacyFileNames parameter, and its location is given by [JET_paramSystemPath](./transaction-log-parameters.md).

Database operations are first written to the log files and then cached in memory. At some later point, the operations get written to the database file, but for performance reasons, the order in which operations are written to the database file might not match the order in which they were originally logged. Operations written to the transaction log file will be in one of two states:

  - Written to the transaction log file and the database file.

  - Written to the transaction log file and not yet written to the database file.

Many database operations can be stored in a single transaction log file. A given log file can consist of the following items:

  - All operations written to the database file.

  - No operations written to the database file

  - A mix of operations written to the database file and operations not yet written to the database file.

The checkpoint refers to the point in time in the transaction log stream where all operations prior to the checkpoint have been written to the database file. There is no guarantee about the operations that occur after the checkpoint; some might be in memory, and some might be written to the database.

Since all the operations in the log files prior to the checkpoint are represented in the database file, only the transaction log files after the checkpoint are needed for soft recovery to bring a particular database into a clean state.

### Database Files

The database file contains the schema for all of the tables in the database, the records for all of the tables in the database, and the indexes over the tables. Its location is given using [JetCreateDatabase](./jetcreatedatabase-function.md), [JetCreateDatabase2](./jetcreatedatabase2-function.md), [JetAttachDatabase](./jetattachdatabase-function.md), or [JetAttachDatabase2](./jetattachdatabase2-function.md).

A database is cleanly shut down only after a successful call to [JetTerm](./jetterm-function.md) or [JetTerm2](./jetterm2-function.md).

The Esentutl.exe program can detect whether a database is shut down cleanly with the "-mh" option. For example, "esentutl.exe -mh sample.edb" will read the database header of a database named sample.edb, and print out the state of sample.edb. It may print out "State: Clean Shutdown" or "State: Dirty Shutdown".

A database that has not been cleanly shut down is in a dirty shutdown state. Prior to Windows XP, this state was called *inconsistent*. A dirty (inconsistent) database can be brought to a clean state with soft recovery. A corrupt database is not the same as a dirty ("inconsistent") database.

A corrupt database refers to a physical or logical corruption, and cannot be fixed with soft recovery. Physical corruptions can be bit flips, which will frequently be caught by the checksums on the database pages. A failed checksum in a database file manifests itself as a JET_errReadVerifyFailure error.

Only cleanly shut down databases can be safely moved around or renamed. If a database was not cleanly shut down, it cannot be automatically safely moved or renamed.

Multiple databases can be associated with a single transaction log file sequence.

### Temporary Databases

The temporary database is used as a backing store for temptables and it is also used when creating indices.

The name and location is configured with [JET_paramTempPath](./temporary-database-parameters.md).

Temptables are created with [JetOpenTempTable](./jetopentemptable-function.md), [JetOpenTempTable2](./jetopentemptable2-function.md), [JetOpenTempTable3](./jetopentemptable3-function.md), [JetOpenTemporaryTable](./jetopentemporarytable-function.md). They are also created by some API calls and used to return schema information (such as [JetGetIndexInfo](./jetgetindexinfo-function.md)).

## Flush Map Files

Starting with the Windows 10 Anniversary Update (client) and Windows Server 2016 (server), ESE added an additional level of protection against lost writes (or lost flushes) 1, allowing it to detect such events cross-process re-initialization2. This feature requires persisting metadata to a separate file called a "flush map" file.

One flush map file is created for each database file, and is located in the same directory. The file is named similarly to the database file, but with a different extension. For example, if the client application creates a database with the full path C:\\MyDirectory\\MyDabatase.edb, its corresponding flush map file is C:\\MyDirectory\\MyDabatase.jfm.

This enhancement introduces two requirements for how database files must be named:

  - Two databases in the same directory must not have the same filename with different extensions. For example: C:\\MyDirectory\\MyDabatase.db1 and C:\\MyDirectory\\MyDabatase.db2.

  - 2\. A database must not have a .jfm extension.

When you manually copy or move a database file, its corresponding flush map file should also be, respectively, copied or moved to the same destination directory. If a flush map file is not present at the time of a new database attachment (via [JetAttachDatabase](./jetattachdatabase-function.md), a new one will be created and re-populated on-demand as pages are read in from the database. Mixing mismatching database and flush map files is handled by ESE, and forces the mismatched flush map to be deleted and re-created from scratch.

The size of a flush map file is directly proportional to its associated database file and approximately equal to (all sizes in bytes, result must be rounded up to the next multiple of 8,192):

`8,192 + ((<database file size> / <database page size>) / 4)`

For example: for a 1.5GB database using a 32KB page size, the approximate size of the flush map is 24,576 bytes (or 24KB).

The flush map file needs to be refreshed as database pages are flushed. If transactional logging is enabled (for example, [JET_paramRecovery](./transaction-log-parameters.md) set to "on", the default), refreshing the flush map is performed as the client application makes modifications to the database. On average, the entire flush map is written to the non-volatile media once for every 20% of [JET_paramCheckpointDepthMax](./database-cache-parameters.md) -worth (in bytes) of transactional logs generated. The number of write operations depends on how distributed throughout the database the modifications are. But it is at most, approximately (all sizes in bytes):

`<flush map file size> / JET_paramMaxCoalesceWriteSize`

If transactional logging is disabled (for example, [JET_paramRecovery](./transaction-log-parameters.md) set to "off"), the flush map gets refreshed only once when the database is explicitly detached cleanly (via [JetDetachDatabase](./jetdetachdatabase-function.md), or implicitly detached cleanly by terminating its associated ESE instance (via any of the [JetTerm](./jetterm-function.md) functions, as long as [JET_bitTermDirty](./jetterm2-function.md) is not passed).

1 A lost write (or lost flush) is defined as a write operation that returns successfully from the operating system to the ESE database engine but the actual data never gets persisted to the database file in the non-volatile media. It is usually caused by a malfunctioning or misconfigured storage stack (software or hardware). Client applications may receive a [JET_errReadLostFlushVerifyFailure](./extensible-storage-engine-error-codes.md) error from ESE functions that require reading data from the database if the data is located in a region that underwent a lost write event.

2 The ability to detect lost writes within a process's lifetime has been present since Windows 8 (client) and Windows Server 2012 (server).
