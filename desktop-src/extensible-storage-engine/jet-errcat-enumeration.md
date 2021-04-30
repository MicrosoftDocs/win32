---
description: "Learn more about: JET_ERRCAT enumeration"
title: JET_ERRCAT enumeration (Microsoft.Isam.Esent.Interop.Windows8)
TOCTitle: JET_ERRCAT enumeration
ms:assetid: T:Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.windows8.jet_errcat(v=EXCHG.10)
ms:contentKeyID: 55104419
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Api
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Corruption
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Data
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Disk
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Error
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Fatal
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Fragmentation
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Inconsistent
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Memory
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Resource
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.State
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Usage
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Operation
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Obsolete
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Quota
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Max
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.IO
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Unknown
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Max
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Obsolete
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Unknown
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Operation
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Usage
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Disk
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.IO
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Error
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Resource
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Api
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Data
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Inconsistent
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Quota
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Corruption
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Fragmentation
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Memory
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.Fatal
- Microsoft.Isam.Esent.Interop.Windows8.JET_ERRCAT.State
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# JET_ERRCAT enumeration

The error category. The hierarchy is as follows: JET_errcatError | |-- JET_errcatOperation | |-- JET_errcatFatal | |-- JET_errcatIO // bad IO issues, may or may not be transient. | |-- JET_errcatResource | |-- JET_errcatMemory // out of memory (all variants) | |-- JET_errcatQuota | |-- JET_errcatDisk // out of disk space (all variants) |-- JET_errcatData | |-- JET_errcatCorruption | |-- JET_errcatInconsistent // typically caused by user Mishandling | |-- JET_errcatFragmentation |-- JET_errcatApi |-- JET_errcatUsage |-- JET_errcatState |-- JET_errcatObsolete

**Namespace:**  [Microsoft.Isam.Esent.Interop.Windows8](./microsoft.isam.esent.interop.windows8-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
Public Enumeration JET_ERRCAT
'Usage
Dim instance As JET_ERRCAT
```

``` csharp
public enum JET_ERRCAT
```

## Members

<table>
<thead>
<tr class="header">
<th></th>
<th>Member name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>Unknown</td>
<td>Unknown category.</td>
</tr>
<tr class="even">
<td></td>
<td>Error</td>
<td>A generic category.</td>
</tr>
<tr class="odd">
<td></td>
<td>Operation</td>
<td>Errors that can usually happen any time due to uncontrollable conditions. Frequently temporary, but not always. Recovery: Probably retry, or eventually inform the operator.</td>
</tr>
<tr class="even">
<td></td>
<td>Fatal</td>
<td>This sort error happens only when ESE encounters an error condition so grave, that we can not continue on in a safe (often transactional) way, and rather than corrupt data we throw errors of this category. Recovery: Restart the instance or process. If the problem persists inform the operator.</td>
</tr>
<tr class="odd">
<td></td>
<td>IO</td>
<td>O errors come from the OS, and are out of ESE's control, this sort of error is possibly temporary, possibly not. Recovery: Retry. If not resolved, ask operator about disk issue.</td>
</tr>
<tr class="even">
<td></td>
<td>Resource</td>
<td>This is a category that indicates one of many potential out-of-resource conditions.</td>
</tr>
<tr class="odd">
<td></td>
<td>Memory</td>
<td>Classic out of memory condition. Recovery: Wait a while and retry, free up memory, or quit.</td>
</tr>
<tr class="even">
<td></td>
<td>Quota</td>
<td>Certain &quot;specialty&quot; resources are in pools of a certain size, making it easier to detect leaks of these resources. Recovery: Might require some minor code changes. Your application should have a debug only action, such as an Assert, on these conditions in order to detect them during development. For retail code, we recommend that you treat this error like the Memory category error and either retry, free up memory, or quit the operation.</td>
</tr>
<tr class="odd">
<td></td>
<td>Disk</td>
<td>Out of disk conditions. Recovery: Can retry later in the hope more space is available, or ask the operator to free some disk space.</td>
</tr>
<tr class="even">
<td></td>
<td>Data</td>
<td>A data-related error.</td>
</tr>
<tr class="odd">
<td></td>
<td>Corruption</td>
<td>My hard drive ate my homework. Classic corruption issues, frequently permanent without corrective action. Recovery: Restore from backup, perhaps the ese utilities repair operation (which only salvages what data is left / lossy) .Also in the case of recovery(JetInit) perhaps recovery can be performed by allowing data loss.</td>
</tr>
<tr class="even">
<td></td>
<td>Inconsistent</td>
<td>This is similar to Corruption in that the database and/or log files are in a state that is inconsistent and unreconcilable with each other. Often this is caused by application/administrator mishandling. Recovery: Restore from backup, perhaps the ese utilities repair operation (which only salvages what data is left / lossy). Also in the case of recovery(JetInit) perhaps recovery can be performed by allowing data loss.</td>
</tr>
<tr class="odd">
<td></td>
<td>Fragmentation</td>
<td>This is a class of errors where some persisted internal resource ran out. Recovery: For database errors, offline defragmentation will rectify the problem, for the log files _first_ recover all attached databases to a clean shutdown, and then delete all the log files and checkpoint.</td>
</tr>
<tr class="even">
<td></td>
<td>Api</td>
<td>A container for Usage and State.</td>
</tr>
<tr class="odd">
<td></td>
<td>Usage</td>
<td>Classic usage error, this means the client code did not pass correct arguments to the JET API. This error will likely not go away with retry. Recovery: Generally speaking client code should Assert() this class of errors is not returned, so issues can be caught during development. In retail, the app will probably have little option but to return the issue up to the operator.</td>
</tr>
<tr class="even">
<td></td>
<td>State</td>
<td>This is the classification for different signals the API could return describe the state of the database, a classic case is JET_errRecordNotFound which can be returned by JetSeek() when the record you asked for was not found. Recovery: Not really relevant, depends greatly on the API.</td>
</tr>
<tr class="odd">
<td></td>
<td>Obsolete</td>
<td>The error is recognized as a valid error, but is not expected to be returned by this version of the API.</td>
</tr>
<tr class="even">
<td></td>
<td>Max</td>
<td>The maximum value for the enum. This should not be used.</td>
</tr>
</tbody>
</table>


## See also

#### Reference

[Microsoft.Isam.Esent.Interop.Windows8 namespace](./microsoft.isam.esent.interop.windows8-namespace.md)
