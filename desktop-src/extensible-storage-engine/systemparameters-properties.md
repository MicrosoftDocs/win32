---
description: "Learn more about: SystemParameters properties"
title: SystemParameters properties
TOCTitle: SystemParameters properties
ms:assetid: Properties.T:Microsoft.Isam.Esent.Interop.SystemParameters
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.systemparameters_properties(v=EXCHG.10)
ms:contentKeyID: 55104035
ms.date: 07/30/2014
ms.topic: article
---

# SystemParameters properties

Include protected members  
Include inherited members  

The [SystemParameters](./systemparameters-class.md) type exposes the following members.

## Properties

<table>
<thead>
<tr class="header">
<th> </th>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351215(v=exchg.10).md">BookmarkMost</a></td>
<td>Gets the maximum size of a bookmark. <a href="dn292149(v=exchg.10).md">JetGetBookmark(JET_SESID, JET_TABLEID, [], Int32, Int32)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351214(v=exchg.10).md">CacheSize</a></td>
<td>Gets or sets the size of the database cache in pages. By default the database cache will automatically tune its size, setting this property to a non-zero value will cause the cache to adjust itself to the target size.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351149(v=exchg.10).md">CacheSizeMax</a></td>
<td>Gets or sets the maximum size of the database page cache. The size is in database pages. If this parameter is left to its default value, then the maximum size of the cache will be set to the size of physical memory when JetInit is called.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351216(v=exchg.10).md">CacheSizeMin</a></td>
<td>Gets or sets the minimum size of the database page cache, in database pages.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351151(v=exchg.10).md">ColumnsKeyMost</a></td>
<td>Gets the maximum number of components in a sort or index key.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351218(v=exchg.10).md">Configuration</a></td>
<td>Gets or sets a value specifying the default values for the entire set of system parameters. When this parameter is set to a specific configuration, all system parameter values are reset to their default values for that configuration. If the configuration is set for a specific instance then global system parameters will not be reset to their default values. Small Configuration (0): The database engine is optimized for memory use. Legacy Configuration (1): The database engine has its traditional defaults. Supported on Windows Vista and up. Ignored on Windows XP and Windows Server 2003.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351153(v=exchg.10).md">DatabasePageSize</a></td>
<td>Gets or sets the size of the database pages, in bytes.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351221(v=exchg.10).md">EnableAdvanced</a></td>
<td>Gets or sets a value indicating whether the database engine accepts or rejects changes to a subset of the system parameters. This parameter is used in conjunction with <a href="dn351218(v=exchg.10).md">Configuration</a> to prevent some system parameters from being set away from the selected configuration's defaults. Supported on Windows Vista and up. Ignored on Windows XP and Windows Server 2003.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351152(v=exchg.10).md">EnableFileCache</a></td>
<td>Gets or sets a value indicating whether the database engine should use the OS file cache for all managed files.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351220(v=exchg.10).md">EnableViewCache</a></td>
<td>Gets or sets a value indicating whether the database engine should use memory mapped file I/O for database files.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351223(v=exchg.10).md">EventLoggingLevel</a></td>
<td>Gets or sets the detail level of eventlog messages that are emitted to the eventlog by the database engine. Higher numbers will result in more detailed eventlog messages.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351154(v=exchg.10).md">ExceptionAction</a></td>
<td>Gets or sets the value encoding what to do with exceptions generated within JET.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351227(v=exchg.10).md">HungIOActions</a></td>
<td>Gets or sets the set of actions to be taken on IOs that appear hung.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351155(v=exchg.10).md">HungIOThreshold</a></td>
<td>Gets or sets the threshold for what is considered a hung IO that should be acted upon.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351156(v=exchg.10).md">KeyMost</a></td>
<td>Gets the maximum key size. This depends on the Esent version and database page size.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351229(v=exchg.10).md">LegacyFileNames</a></td>
<td>Gets or sets backwards compatibility with the file naming conventions of earlier releases of the database engine.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351157(v=exchg.10).md">LVChunkSizeMost</a></td>
<td>Gets the lv chunks size. This depends on the database page size.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351230(v=exchg.10).md">MaxInstances</a></td>
<td>Gets or sets the maximum number of instances that can be created.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351160(v=exchg.10).md">MinDataForXpress</a></td>
<td>Gets or sets the smallest amount of data that should be compressed with xpress compression.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351159(v=exchg.10).md">OutstandingIOMax</a></td>
<td>This parameter controls how many database file I/Os can be queued per-disk in the host operating system at one time. A larger value for this parameter can significantly help the performance of a large database application.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351158(v=exchg.10).md">ProcessFriendlyName</a></td>
<td>Gets or sets the friendly name for this instance of the process.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351161(v=exchg.10).md">StartFlushThreshold</a></td>
<td>Gets or sets the threshold at which the database page cache begins evicting pages from the cache to make room for pages that are not cached. When the number of page buffers in the cache drops below this threshold then a background process will be started to replenish that pool of available buffers. This threshold is always relative to the maximum cache size as set by JET_paramCacheSizeMax. This threshold must also always be less than the stop threshold as set by JET_paramStopFlushThreshold. The distance height of the start threshold will determine the response time that the database page cache must have to produce available buffers before the application needs them. A high start threshold will give the background process more time to react. However, a high start threshold implies a higher stop threshold and that will reduce the effective size of the database page cache.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn351231(v=exchg.10).md">StopFlushThreshold</a></td>
<td>Gets or sets the threshold at which the database page cache ends evicting pages from the cache to make room for pages that are not cached. When the number of page buffers in the cache rises above this threshold then the background process that was started to replenish that pool of available buffers is stopped. This threshold is always relative to the maximum cache size as set by JET_paramCacheSizeMax. This threshold must also always be greater than the start threshold as set by JET_paramStartFlushThreshold. The distance between the start threshold and the stop threshold affects the efficiency with which database pages are flushed by the background process. A larger gap will make it more likely that writes to neighboring pages may be combined. However, a high stop threshold will reduce the effective size of the database page cache.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[SystemParameters class](./systemparameters-class.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
