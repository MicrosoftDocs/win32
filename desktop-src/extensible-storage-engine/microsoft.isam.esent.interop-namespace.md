---
description: "Learn more about: Microsoft.Isam.Esent.Interop namespace"
title: Microsoft.Isam.Esent.Interop namespace ()
TOCTitle: '@NoTitle'
ms:assetid: N:Microsoft.Isam.Esent.Interop
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop(v=EXCHG.10)
ms:contentKeyID: 39515215
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop
dev_langs:
- CSharp
- JScript
- VB
- other
---

# Microsoft.Isam.Esent.Interop namespace

## Classes

<table>
<thead>
<tr class="header">
<th> </th>
<th>Class</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn292211(v=exchg.10).md">Api</a></td>
<td>Managed versions of the ESENT API. This class contains static methods that correspond to the unmanaged ESENT API. These methods throw exceptions when errors are returned. Helper methods for the ESENT API. These wrap JetMakeKey. Internal-only methods of the API. Helper methods for the ESENT API. These do data conversion for JetMakeKey. Helper methods for the ESENT API. These methods deal with database metadata. Helper methods for the ESENT API. These aren't interop versions of the API, but encapsulate very common uses of the functions. API members that are marked as obsolete. Helper methods for the ESENT API. These aren't interop versions of the API, but encapsulate very common uses of the functions. Helper methods for the ESENT API. These do data conversion for setting columns.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334148(v=exchg.10).md">BoolColumnValue</a></td>
<td>A <a href="/dotnet/api/system.boolean">Boolean</a> column value.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334109(v=exchg.10).md">ByteColumnValue</a></td>
<td>A <a href="/dotnet/api/system.byte">Byte</a> column value.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334170(v=exchg.10).md">BytesColumnValue</a></td>
<td>A byte array column value.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334128(v=exchg.10).md">ColumnInfo</a></td>
<td>Information about one Esent column. This is not an interop class, but is used by the meta-data helper methods.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334143(v=exchg.10).md">ColumnStream</a></td>
<td>This class provides a streaming interface to a long-value column (i.e. a column of type <a href="hh577895(v=exchg.10).md">LongBinary</a> or <a href="hh577895(v=exchg.10).md">LongText</a>).</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334206(v=exchg.10).md">ColumnValue</a></td>
<td>Base class for objects that represent a column value to be set.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334171(v=exchg.10).md">ColumnValueOfStruct&lt;T&gt;</a></td>
<td>Set a column of a struct type (e.g. Int32/Guid).</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334230(v=exchg.10).md">Conversions</a></td>
<td>Provide methods to convert data and flags between Win32 and the .NET Framework.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334238(v=exchg.10).md">DateTimeColumnValue</a></td>
<td>A <a href="/dotnet/api/system.guid">Guid</a> column value.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn273972(v=exchg.10).md">DoubleColumnValue</a></td>
<td>A <a href="/dotnet/api/system.double">Double</a> column value.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn273978(v=exchg.10).md">EsentAccessDeniedException</a></td>
<td>Base class for JET_err.AccessDenied exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334220(v=exchg.10).md">EsentAfterInitializationException</a></td>
<td>Base class for JET_err.AfterInitialization exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn273989(v=exchg.10).md">EsentAlreadyInitializedException</a></td>
<td>Base class for JET_err.AlreadyInitialized exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334228(v=exchg.10).md">EsentAlreadyPreparedException</a></td>
<td>Base class for JET_err.AlreadyPrepared exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334231(v=exchg.10).md">EsentApiException</a></td>
<td>Base class for API exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334236(v=exchg.10).md">EsentAttachedDatabaseMismatchException</a></td>
<td>Base class for JET_err.AttachedDatabaseMismatch exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274014(v=exchg.10).md">EsentBackupAbortByServerException</a></td>
<td>Base class for JET_err.BackupAbortByServer exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn273970(v=exchg.10).md">EsentBackupDirectoryNotEmptyException</a></td>
<td>Base class for JET_err.BackupDirectoryNotEmpty exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274026(v=exchg.10).md">EsentBackupInProgressException</a></td>
<td>Base class for JET_err.BackupInProgress exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274032(v=exchg.10).md">EsentBackupNotAllowedYetException</a></td>
<td>Base class for JET_err.BackupNotAllowedYet exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn273987(v=exchg.10).md">EsentBadBackupDatabaseSizeException</a></td>
<td>Base class for JET_err.BadBackupDatabaseSize exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274043(v=exchg.10).md">EsentBadBookmarkException</a></td>
<td>Base class for JET_err.BadBookmark exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn273995(v=exchg.10).md">EsentBadCheckpointSignatureException</a></td>
<td>Base class for JET_err.BadCheckpointSignature exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274004(v=exchg.10).md">EsentBadColumnIdException</a></td>
<td>Base class for JET_err.BadColumnId exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274009(v=exchg.10).md">EsentBadDbSignatureException</a></td>
<td>Base class for JET_err.BadDbSignature exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274059(v=exchg.10).md">EsentBadEmptyPageException</a></td>
<td>Base class for JET_err.BadEmptyPage exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274018(v=exchg.10).md">EsentBadItagSequenceException</a></td>
<td>Base class for JET_err.BadItagSequence exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274072(v=exchg.10).md">EsentBadLogSignatureException</a></td>
<td>Base class for JET_err.BadLogSignature exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274023(v=exchg.10).md">EsentBadLogVersionException</a></td>
<td>Base class for JET_err.BadLogVersion exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274083(v=exchg.10).md">EsentBadPageLinkException</a></td>
<td>Base class for JET_err.BadPageLink exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274033(v=exchg.10).md">EsentBadParentPageLinkException</a></td>
<td>Base class for JET_err.BadParentPageLink exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274093(v=exchg.10).md">EsentBadPatchPageException</a></td>
<td>Base class for JET_err.BadPatchPage exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274044(v=exchg.10).md">EsentBadRestoreTargetInstanceException</a></td>
<td>Base class for JET_err.BadRestoreTargetInstance exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274107(v=exchg.10).md">EsentBadSLVSignatureException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274053(v=exchg.10).md">EsentBufferTooSmallException</a></td>
<td>Base class for JET_err.BufferTooSmall exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274120(v=exchg.10).md">EsentCallbackFailedException</a></td>
<td>Base class for JET_err.CallbackFailed exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274063(v=exchg.10).md">EsentCallbackNotResolvedException</a></td>
<td>Base class for JET_err.CallbackNotResolved exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274130(v=exchg.10).md">EsentCannotAddFixedVarColumnToDerivedTableException</a></td>
<td>Base class for JET_err.CannotAddFixedVarColumnToDerivedTable exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274074(v=exchg.10).md">EsentCannotBeTaggedException</a></td>
<td>Base class for JET_err.CannotBeTagged exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274139(v=exchg.10).md">EsentCannotDeleteSystemTableException</a></td>
<td>Base class for JET_err.CannotDeleteSystemTable exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274084(v=exchg.10).md">EsentCannotDeleteTemplateTableException</a></td>
<td>Base class for JET_err.CannotDeleteTemplateTable exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274088(v=exchg.10).md">EsentCannotDeleteTempTableException</a></td>
<td>Base class for JET_err.CannotDeleteTempTable exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274157(v=exchg.10).md">EsentCannotDisableVersioningException</a></td>
<td>Base class for JET_err.CannotDisableVersioning exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274099(v=exchg.10).md">EsentCannotIndexException</a></td>
<td>Base class for JET_err.CannotIndex exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274165(v=exchg.10).md">EsentCannotLogDuringRecoveryRedoException</a></td>
<td>Base class for JET_err.CannotLogDuringRecoveryRedo exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274102(v=exchg.10).md">EsentCannotMaterializeForwardOnlySortException</a></td>
<td>Base class for JET_err.CannotMaterializeForwardOnlySort exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274172(v=exchg.10).md">EsentCannotNestDDLException</a></td>
<td>Base class for JET_err.CannotNestDDL exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274174(v=exchg.10).md">EsentCannotNestDistributedTransactionsException</a></td>
<td>Base class for JET_err.CannotNestDistributedTransactions exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274117(v=exchg.10).md">EsentCannotSeparateIntrinsicLVException</a></td>
<td>Base class for JET_err.CannotSeparateIntrinsicLV exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274191(v=exchg.10).md">EsentCatalogCorruptedException</a></td>
<td>Base class for JET_err.CatalogCorrupted exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274132(v=exchg.10).md">EsentCheckpointCorruptException</a></td>
<td>Base class for JET_err.CheckpointCorrupt exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274195(v=exchg.10).md">EsentCheckpointDepthTooDeepException</a></td>
<td>Base class for JET_err.CheckpointDepthTooDeep exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274140(v=exchg.10).md">EsentCheckpointFileNotFoundException</a></td>
<td>Base class for JET_err.CheckpointFileNotFound exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274150(v=exchg.10).md">EsentClientRequestToStopJetServiceException</a></td>
<td>Base class for JET_err.ClientRequestToStopJetService exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274217(v=exchg.10).md">EsentColumnCannotBeCompressedException</a></td>
<td>Base class for JET_err.ColumnCannotBeCompressed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334250(v=exchg.10).md">EsentColumnDoesNotFitException</a></td>
<td>Base class for JET_err.ColumnDoesNotFit exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274156(v=exchg.10).md">EsentColumnDuplicateException</a></td>
<td>Base class for JET_err.ColumnDuplicate exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274164(v=exchg.10).md">EsentColumnIndexedException</a></td>
<td>Base class for JET_err.ColumnIndexed exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334259(v=exchg.10).md">EsentColumnInRelationshipException</a></td>
<td>Base class for JET_err.ColumnInRelationship exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274180(v=exchg.10).md">EsentColumnInUseException</a></td>
<td>Base class for JET_err.ColumnInUse exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334271(v=exchg.10).md">EsentColumnLongException</a></td>
<td>Base class for JET_err.ColumnLong exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274190(v=exchg.10).md">EsentColumnNoChunkException</a></td>
<td>Base class for JET_err.ColumnNoChunk exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274196(v=exchg.10).md">EsentColumnNotFoundException</a></td>
<td>Base class for JET_err.ColumnNotFound exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334291(v=exchg.10).md">EsentColumnNotUpdatableException</a></td>
<td>Base class for JET_err.ColumnNotUpdatable exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274198(v=exchg.10).md">EsentColumnRedundantException</a></td>
<td>Base class for JET_err.ColumnRedundant exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334298(v=exchg.10).md">EsentColumnTooBigException</a></td>
<td>Base class for JET_err.ColumnTooBig exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274206(v=exchg.10).md">EsentCommittedLogFileCorruptException</a></td>
<td>Base class for JET_err.CommittedLogFileCorrupt exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334311(v=exchg.10).md">EsentCommittedLogFilesMissingException</a></td>
<td>Base class for JET_err.CommittedLogFilesMissing exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274215(v=exchg.10).md">EsentConsistentTimeMismatchException</a></td>
<td>Base class for JET_err.ConsistentTimeMismatch exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334323(v=exchg.10).md">EsentContainerNotEmptyException</a></td>
<td>Base class for JET_err.ContainerNotEmpty exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274225(v=exchg.10).md">EsentCorruptionException</a></td>
<td>Base class for Corruption exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334249(v=exchg.10).md">EsentCurrencyStackOutOfMemoryException</a></td>
<td>Base class for JET_err.CurrencyStackOutOfMemory exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334342(v=exchg.10).md">EsentDatabase200FormatException</a></td>
<td>Base class for JET_err.Database200Format exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334253(v=exchg.10).md">EsentDatabase400FormatException</a></td>
<td>Base class for JET_err.Database400Format exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334350(v=exchg.10).md">EsentDatabase500FormatException</a></td>
<td>Base class for JET_err.Database500Format exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334266(v=exchg.10).md">EsentDatabaseAlreadyRunningMaintenanceException</a></td>
<td>Base class for JET_err.DatabaseAlreadyRunningMaintenance exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334272(v=exchg.10).md">EsentDatabaseAlreadyUpgradedException</a></td>
<td>Base class for JET_err.DatabaseAlreadyUpgraded exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334366(v=exchg.10).md">EsentDatabaseBufferDependenciesCorruptedException</a></td>
<td>Base class for JET_err.DatabaseBufferDependenciesCorrupted exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334279(v=exchg.10).md">EsentDatabaseCorruptedException</a></td>
<td>Base class for JET_err.DatabaseCorrupted exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334384(v=exchg.10).md">EsentDatabaseCorruptedNoRepairException</a></td>
<td>Base class for JET_err.DatabaseCorruptedNoRepair exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334290(v=exchg.10).md">EsentDatabaseDirtyShutdownException</a></td>
<td>Base class for JET_err.DatabaseDirtyShutdown exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334296(v=exchg.10).md">EsentDatabaseDuplicateException</a></td>
<td>Base class for JET_err.DatabaseDuplicate exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334404(v=exchg.10).md">EsentDatabaseFailedIncrementalReseedException</a></td>
<td>Base class for JET_err.DatabaseFailedIncrementalReseed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334306(v=exchg.10).md">EsentDatabaseFileReadOnlyException</a></td>
<td>Base class for JET_err.DatabaseFileReadOnly exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334396(v=exchg.10).md">EsentDatabaseIdInUseException</a></td>
<td>Base class for JET_err.DatabaseIdInUse exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334412(v=exchg.10).md">EsentDatabaseIncompleteIncrementalReseedException</a></td>
<td>Base class for JET_err.DatabaseIncompleteIncrementalReseed exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334320(v=exchg.10).md">EsentDatabaseIncompleteUpgradeException</a></td>
<td>Base class for JET_err.DatabaseIncompleteUpgrade exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334322(v=exchg.10).md">EsentDatabaseInUseException</a></td>
<td>Base class for JET_err.DatabaseInUse exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334430(v=exchg.10).md">EsentDatabaseInvalidIncrementalReseedException</a></td>
<td>Base class for JET_err.DatabaseInvalidIncrementalReseed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334450(v=exchg.10).md">EsentDatabaseInvalidNameException</a></td>
<td>Base class for JET_err.DatabaseInvalidName exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334339(v=exchg.10).md">EsentDatabaseInvalidPagesException</a></td>
<td>Base class for JET_err.DatabaseInvalidPages exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334460(v=exchg.10).md">EsentDatabaseInvalidPathException</a></td>
<td>Base class for JET_err.DatabaseInvalidPath exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334349(v=exchg.10).md">EsentDatabaseLeakInSpaceException</a></td>
<td>Base class for JET_err.DatabaseLeakInSpace exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334474(v=exchg.10).md">EsentDatabaseLockedException</a></td>
<td>Base class for JET_err.DatabaseLocked exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334359(v=exchg.10).md">EsentDatabaseLogSetMismatchException</a></td>
<td>Base class for JET_err.DatabaseLogSetMismatch exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334481(v=exchg.10).md">EsentDatabaseNotFoundException</a></td>
<td>Base class for JET_err.DatabaseNotFound exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334483(v=exchg.10).md">EsentDatabasePatchFileMismatchException</a></td>
<td>Base class for JET_err.DatabasePatchFileMismatch exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334374(v=exchg.10).md">EsentDatabaseSharingViolationException</a></td>
<td>Base class for JET_err.DatabaseSharingViolation exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334488(v=exchg.10).md">EsentDatabaseSignInUseException</a></td>
<td>Base class for JET_err.DatabaseSignInUse exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334386(v=exchg.10).md">EsentDatabasesNotFromSameSnapshotException</a></td>
<td>Base class for JET_err.DatabasesNotFromSameSnapshot exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334493(v=exchg.10).md">EsentDatabaseStreamingFileMismatchException</a></td>
<td>Base class for JET_err.DatabaseStreamingFileMismatch exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274227(v=exchg.10).md">EsentDatabaseUnavailableException</a></td>
<td>Base class for JET_err.DatabaseUnavailable exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334392(v=exchg.10).md">EsentDataException</a></td>
<td>Base class for Data exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334397(v=exchg.10).md">EsentDataHasChangedException</a></td>
<td>Base class for JET_err.DataHasChanged exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274236(v=exchg.10).md">EsentDbTimeCorruptedException</a></td>
<td>Base class for JET_err.DbTimeCorrupted exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334407(v=exchg.10).md">EsentDbTimeTooNewException</a></td>
<td>Base class for JET_err.DbTimeTooNew exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274245(v=exchg.10).md">EsentDbTimeTooOldException</a></td>
<td>Base class for JET_err.DbTimeTooOld exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334413(v=exchg.10).md">EsentDDLNotInheritableException</a></td>
<td>Base class for JET_err.DDLNotInheritable exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274251(v=exchg.10).md">EsentDecompressionFailedException</a></td>
<td>Base class for JET_err.DecompressionFailed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334424(v=exchg.10).md">EsentDefaultValueTooBigException</a></td>
<td>Base class for JET_err.DefaultValueTooBig exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274267(v=exchg.10).md">EsentDeleteBackupFileFailException</a></td>
<td>Base class for JET_err.DeleteBackupFileFail exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334433(v=exchg.10).md">EsentDensityInvalidException</a></td>
<td>Base class for JET_err.DensityInvalid exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274270(v=exchg.10).md">EsentDerivedColumnCorruptionException</a></td>
<td>Base class for JET_err.DerivedColumnCorruption exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334452(v=exchg.10).md">EsentDirtyShutdownException</a></td>
<td>Base class for JET_err.DirtyShutdown exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274277(v=exchg.10).md">EsentDisabledFunctionalityException</a></td>
<td>Base class for JET_err.DisabledFunctionality exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334464(v=exchg.10).md">EsentDiskException</a></td>
<td>Base class for Disk exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334461(v=exchg.10).md">EsentDiskFullException</a></td>
<td>Base class for JET_err.DiskFull exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274289(v=exchg.10).md">EsentDiskIOException</a></td>
<td>Base class for JET_err.DiskIO exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274287(v=exchg.10).md">EsentDiskReadVerificationFailureException</a></td>
<td>Base class for JET_err.DiskReadVerificationFailure exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334490(v=exchg.10).md">EsentDistributedTransactionAlreadyPreparedToCommitException</a></td>
<td>Base class for JET_err.DistributedTransactionAlreadyPreparedToCommit exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274293(v=exchg.10).md">EsentDistributedTransactionNotYetPreparedToCommitException</a></td>
<td>Base class for JET_err.DistributedTransactionNotYetPreparedToCommit exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334500(v=exchg.10).md">EsentDTCCallbackUnexpectedErrorException</a></td>
<td>Base class for JET_err.DTCCallbackUnexpectedError exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334508(v=exchg.10).md">EsentDTCMissingCallbackException</a></td>
<td>Base class for JET_err.DTCMissingCallback exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274310(v=exchg.10).md">EsentDTCMissingCallbackOnRecoveryException</a></td>
<td>Base class for JET_err.DTCMissingCallbackOnRecovery exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274239(v=exchg.10).md">EsentEndingRestoreLogTooLowException</a></td>
<td>Base class for JET_err.EndingRestoreLogTooLow exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274309(v=exchg.10).md">EsentEntryPointNotFoundException</a></td>
<td>Base class for JET_err.EntryPointNotFound exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274314(v=exchg.10).md">EsentErrorException</a></td>
<td>Base class for ESENT error exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274257(v=exchg.10).md">EsentExclusiveTableLockRequiredException</a></td>
<td>Base class for JET_err.ExclusiveTableLockRequired exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274318(v=exchg.10).md">EsentExistingLogFileHasBadSignatureException</a></td>
<td>Base class for JET_err.ExistingLogFileHasBadSignature exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274260(v=exchg.10).md">EsentExistingLogFileIsNotContiguousException</a></td>
<td>Base class for JET_err.ExistingLogFileIsNotContiguous exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274321(v=exchg.10).md">EsentFatalException</a></td>
<td>Base class for Fatal exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274291(v=exchg.10).md">EsentFeatureNotAvailableException</a></td>
<td>Base class for JET_err.FeatureNotAvailable exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274324(v=exchg.10).md">EsentFileAccessDeniedException</a></td>
<td>Base class for JET_err.FileAccessDenied exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274332(v=exchg.10).md">EsentFileCloseException</a></td>
<td>Base class for JET_err.FileClose exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274343(v=exchg.10).md">EsentFileCompressedException</a></td>
<td>Base class for JET_err.FileCompressed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274337(v=exchg.10).md">EsentFileInvalidTypeException</a></td>
<td>Base class for JET_err.FileInvalidType exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274355(v=exchg.10).md">EsentFileIOAbortException</a></td>
<td>Base class for JET_err.FileIOAbort exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274354(v=exchg.10).md">EsentFileIOBeyondEOFException</a></td>
<td>Base class for JET_err.FileIOBeyondEOF exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274360(v=exchg.10).md">EsentFileIOFailException</a></td>
<td>Base class for JET_err.FileIOFail exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274364(v=exchg.10).md">EsentFileIORetryException</a></td>
<td>Base class for JET_err.FileIORetry exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274375(v=exchg.10).md">EsentFileIOSparseException</a></td>
<td>Base class for JET_err.FileIOSparse exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274377(v=exchg.10).md">EsentFileNotFoundException</a></td>
<td>Base class for JET_err.FileNotFound exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274381(v=exchg.10).md">EsentFileSystemCorruptionException</a></td>
<td>Base class for JET_err.FileSystemCorruption exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn274384(v=exchg.10).md">EsentFilteredMoveNotSupportedException</a></td>
<td>Base class for JET_err.FilteredMoveNotSupported exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350411(v=exchg.10).md">EsentFixedDDLException</a></td>
<td>Base class for JET_err.FixedDDL exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350413(v=exchg.10).md">EsentFixedInheritedDDLException</a></td>
<td>Base class for JET_err.FixedInheritedDDL exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350463(v=exchg.10).md">EsentForceDetachNotAllowedException</a></td>
<td>Base class for JET_err.ForceDetachNotAllowed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350462(v=exchg.10).md">EsentFragmentationException</a></td>
<td>Base class for Fragmentation exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350421(v=exchg.10).md">EsentGivenLogFileHasBadSignatureException</a></td>
<td>Base class for JET_err.GivenLogFileHasBadSignature exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350479(v=exchg.10).md">EsentGivenLogFileIsNotContiguousException</a></td>
<td>Base class for JET_err.GivenLogFileIsNotContiguous exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350477(v=exchg.10).md">EsentIllegalOperationException</a></td>
<td>Base class for JET_err.IllegalOperation exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350488(v=exchg.10).md">EsentInconsistentException</a></td>
<td>Base class for Inconsistent exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350493(v=exchg.10).md">EsentIndexBuildCorruptedException</a></td>
<td>Base class for JET_err.IndexBuildCorrupted exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350436(v=exchg.10).md">EsentIndexCantBuildException</a></td>
<td>Base class for JET_err.IndexCantBuild exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350438(v=exchg.10).md">EsentIndexDuplicateException</a></td>
<td>Base class for JET_err.IndexDuplicate exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350439(v=exchg.10).md">EsentIndexHasPrimaryException</a></td>
<td>Base class for JET_err.IndexHasPrimary exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350505(v=exchg.10).md">EsentIndexInUseException</a></td>
<td>Base class for JET_err.IndexInUse exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319396(v=exchg.10).md">EsentIndexInvalidDefException</a></td>
<td>Base class for JET_err.IndexInvalidDef exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319399(v=exchg.10).md">EsentIndexMustStayException</a></td>
<td>Base class for JET_err.IndexMustStay exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350459(v=exchg.10).md">EsentIndexNotFoundException</a></td>
<td>Base class for JET_err.IndexNotFound exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319401(v=exchg.10).md">EsentIndexTuplesCannotRetrieveFromIndexException</a></td>
<td>Base class for JET_err.IndexTuplesCannotRetrieveFromIndex exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319411(v=exchg.10).md">EsentIndexTuplesInvalidLimitsException</a></td>
<td>Base class for JET_err.IndexTuplesInvalidLimits exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350474(v=exchg.10).md">EsentIndexTuplesKeyTooSmallException</a></td>
<td>Base class for JET_err.IndexTuplesKeyTooSmall exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319420(v=exchg.10).md">EsentIndexTuplesNonUniqueOnlyException</a></td>
<td>Base class for JET_err.IndexTuplesNonUniqueOnly exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350485(v=exchg.10).md">EsentIndexTuplesSecondaryIndexOnlyException</a></td>
<td>Base class for JET_err.IndexTuplesSecondaryIndexOnly exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350490(v=exchg.10).md">EsentIndexTuplesTextBinaryColumnsOnlyException</a></td>
<td>Base class for JET_err.IndexTuplesTextBinaryColumnsOnly exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319427(v=exchg.10).md">EsentIndexTuplesTooManyColumnsException</a></td>
<td>Base class for JET_err.IndexTuplesTooManyColumns exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319430(v=exchg.10).md">EsentIndexTuplesVarSegMacNotAllowedException</a></td>
<td>Base class for JET_err.IndexTuplesVarSegMacNotAllowed exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350503(v=exchg.10).md">EsentInitInProgressException</a></td>
<td>Base class for JET_err.InitInProgress exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319385(v=exchg.10).md">EsentInstanceNameInUseException</a></td>
<td>Base class for JET_err.InstanceNameInUse exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319387(v=exchg.10).md">EsentInstanceUnavailableDueToFatalLogDiskFullException</a></td>
<td>Base class for JET_err.InstanceUnavailableDueToFatalLogDiskFull exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319441(v=exchg.10).md">EsentInstanceUnavailableException</a></td>
<td>Base class for JET_err.InstanceUnavailable exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319452(v=exchg.10).md">EsentInternalErrorException</a></td>
<td>Base class for JET_err.InternalError exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319457(v=exchg.10).md">EsentInTransactionException</a></td>
<td>Base class for JET_err.InTransaction exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319406(v=exchg.10).md">EsentInvalidBackupException</a></td>
<td>Base class for JET_err.InvalidBackup exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319414(v=exchg.10).md">EsentInvalidBackupSequenceException</a></td>
<td>Base class for JET_err.InvalidBackupSequence exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319464(v=exchg.10).md">EsentInvalidBookmarkException</a></td>
<td>Base class for JET_err.InvalidBookmark exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319475(v=exchg.10).md">EsentInvalidBufferSizeException</a></td>
<td>Base class for JET_err.InvalidBufferSize exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319443(v=exchg.10).md">EsentInvalidCodePageException</a></td>
<td>Base class for JET_err.InvalidCodePage exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319487(v=exchg.10).md">EsentInvalidColumnException</a></td>
<td>Exception thrown when a column conversion fails.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319454(v=exchg.10).md">EsentInvalidColumnTypeException</a></td>
<td>Base class for JET_err.InvalidColumnType exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319498(v=exchg.10).md">EsentInvalidCountryException</a></td>
<td>Base class for JET_err.InvalidCountry exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319468(v=exchg.10).md">EsentInvalidCreateDbVersionException</a></td>
<td>Base class for JET_err.InvalidCreateDbVersion exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319507(v=exchg.10).md">EsentInvalidCreateIndexException</a></td>
<td>Base class for JET_err.InvalidCreateIndex exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319474(v=exchg.10).md">EsentInvalidDatabaseException</a></td>
<td>Base class for JET_err.InvalidDatabase exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319512(v=exchg.10).md">EsentInvalidDatabaseIdException</a></td>
<td>Base class for JET_err.InvalidDatabaseId exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319486(v=exchg.10).md">EsentInvalidDatabaseVersionException</a></td>
<td>Base class for JET_err.InvalidDatabaseVersion exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319520(v=exchg.10).md">EsentInvalidFilenameException</a></td>
<td>Base class for JET_err.InvalidFilename exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319518(v=exchg.10).md">EsentInvalidGrbitException</a></td>
<td>Base class for JET_err.InvalidGrbit exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319523(v=exchg.10).md">EsentInvalidIndexIdException</a></td>
<td>Base class for JET_err.InvalidIndexId exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319502(v=exchg.10).md">EsentInvalidInstanceException</a></td>
<td>Base class for JET_err.InvalidInstance exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319529(v=exchg.10).md">EsentInvalidLanguageIdException</a></td>
<td>Base class for JET_err.InvalidLanguageId exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319538(v=exchg.10).md">EsentInvalidLCMapStringFlagsException</a></td>
<td>Base class for JET_err.InvalidLCMapStringFlags exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319536(v=exchg.10).md">EsentInvalidLogDataSequenceException</a></td>
<td>Base class for JET_err.InvalidLogDataSequence exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319548(v=exchg.10).md">EsentInvalidLogDirectoryException</a></td>
<td>Base class for JET_err.InvalidLogDirectory exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319545(v=exchg.10).md">EsentInvalidLoggedOperationException</a></td>
<td>Base class for JET_err.InvalidLoggedOperation exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319554(v=exchg.10).md">EsentInvalidLogSequenceException</a></td>
<td>Base class for JET_err.InvalidLogSequence exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319541(v=exchg.10).md">EsentInvalidNameException</a></td>
<td>Base class for JET_err.InvalidName exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319564(v=exchg.10).md">EsentInvalidObjectException</a></td>
<td>Base class for JET_err.InvalidObject exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319570(v=exchg.10).md">EsentInvalidOnSortException</a></td>
<td>Base class for JET_err.InvalidOnSort exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319571(v=exchg.10).md">EsentInvalidOperationException</a></td>
<td>Base class for JET_err.InvalidOperation exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319601(v=exchg.10).md">EsentInvalidParameterException</a></td>
<td>Base class for JET_err.InvalidParameter exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319577(v=exchg.10).md">EsentInvalidPathException</a></td>
<td>Base class for JET_err.InvalidPath exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319579(v=exchg.10).md">EsentInvalidPlaceholderColumnException</a></td>
<td>Base class for JET_err.InvalidPlaceholderColumn exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334516(v=exchg.10).md">EsentInvalidPrereadException</a></td>
<td>Base class for JET_err.InvalidPreread exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319584(v=exchg.10).md">EsentInvalidSesidException</a></td>
<td>Base class for JET_err.InvalidSesid exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334521(v=exchg.10).md">EsentInvalidSettingsException</a></td>
<td>Base class for JET_err.InvalidSettings exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334526(v=exchg.10).md">EsentInvalidSystemPathException</a></td>
<td>Base class for JET_err.InvalidSystemPath exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334527(v=exchg.10).md">EsentInvalidTableIdException</a></td>
<td>Base class for JET_err.InvalidTableId exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319595(v=exchg.10).md">EsentIOException</a></td>
<td>Base class for IO exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319605(v=exchg.10).md">EsentKeyBoundaryException</a></td>
<td>Base class for JET_err.KeyBoundary exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319603(v=exchg.10).md">EsentKeyDuplicateException</a></td>
<td>Base class for JET_err.KeyDuplicate exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334548(v=exchg.10).md">EsentKeyIsMadeException</a></td>
<td>Base class for JET_err.KeyIsMade exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334554(v=exchg.10).md">EsentKeyNotMadeException</a></td>
<td>Base class for JET_err.KeyNotMade exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319610(v=exchg.10).md">EsentKeyTooBigException</a></td>
<td>Base class for JET_err.KeyTooBig exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334565(v=exchg.10).md">EsentKeyTruncatedException</a></td>
<td>Base class for JET_err.KeyTruncated exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334570(v=exchg.10).md">EsentLanguageNotSupportedException</a></td>
<td>Base class for JET_err.LanguageNotSupported exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334571(v=exchg.10).md">EsentLinkNotSupportedException</a></td>
<td>Base class for JET_err.LinkNotSupported exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334573(v=exchg.10).md">EsentLogBufferTooSmallException</a></td>
<td>Base class for JET_err.LogBufferTooSmall exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319628(v=exchg.10).md">EsentLogCorruptDuringHardRecoveryException</a></td>
<td>Base class for JET_err.LogCorruptDuringHardRecovery exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334512(v=exchg.10).md">EsentLogCorruptDuringHardRestoreException</a></td>
<td>Base class for JET_err.LogCorruptDuringHardRestore exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334510(v=exchg.10).md">EsentLogCorruptedException</a></td>
<td>Base class for JET_err.LogCorrupted exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334591(v=exchg.10).md">EsentLogDisabledDueToRecoveryFailureException</a></td>
<td>Base class for JET_err.LogDisabledDueToRecoveryFailure exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334539(v=exchg.10).md">EsentLogDiskFullException</a></td>
<td>Base class for JET_err.LogDiskFull exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334601(v=exchg.10).md">EsentLogFileCorruptException</a></td>
<td>Base class for JET_err.LogFileCorrupt exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334541(v=exchg.10).md">EsentLogFileNotCopiedException</a></td>
<td>Base class for JET_err.LogFileNotCopied exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334545(v=exchg.10).md">EsentLogFilePathInUseException</a></td>
<td>Base class for JET_err.LogFilePathInUse exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334552(v=exchg.10).md">EsentLogFileSizeMismatchDatabasesConsistentException</a></td>
<td>Base class for JET_err.LogFileSizeMismatchDatabasesConsistent exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334627(v=exchg.10).md">EsentLogFileSizeMismatchException</a></td>
<td>Base class for JET_err.LogFileSizeMismatch exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334564(v=exchg.10).md">EsentLogGenerationMismatchException</a></td>
<td>Base class for JET_err.LogGenerationMismatch exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334582(v=exchg.10).md">EsentLoggingDisabledException</a></td>
<td>Base class for JET_err.LoggingDisabled exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334583(v=exchg.10).md">EsentLogReadVerifyFailureException</a></td>
<td>Base class for JET_err.LogReadVerifyFailure exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334645(v=exchg.10).md">EsentLogSectorSizeMismatchDatabasesConsistentException</a></td>
<td>Base class for JET_err.LogSectorSizeMismatchDatabasesConsistent exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334646(v=exchg.10).md">EsentLogSectorSizeMismatchException</a></td>
<td>Base class for JET_err.LogSectorSizeMismatch exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334651(v=exchg.10).md">EsentLogSequenceEndDatabasesConsistentException</a></td>
<td>Base class for JET_err.LogSequenceEndDatabasesConsistent exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334652(v=exchg.10).md">EsentLogSequenceEndException</a></td>
<td>Base class for JET_err.LogSequenceEnd exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334657(v=exchg.10).md">EsentLogTornWriteDuringHardRecoveryException</a></td>
<td>Base class for JET_err.LogTornWriteDuringHardRecovery exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334605(v=exchg.10).md">EsentLogTornWriteDuringHardRestoreException</a></td>
<td>Base class for JET_err.LogTornWriteDuringHardRestore exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334607(v=exchg.10).md">EsentLogWriteFailException</a></td>
<td>Base class for JET_err.LogWriteFail exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334614(v=exchg.10).md">EsentLSAlreadySetException</a></td>
<td>Base class for JET_err.LSAlreadySet exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334617(v=exchg.10).md">EsentLSCallbackNotSpecifiedException</a></td>
<td>Base class for JET_err.LSCallbackNotSpecified exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334676(v=exchg.10).md">EsentLSNotSetException</a></td>
<td>Base class for JET_err.LSNotSet exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334680(v=exchg.10).md">EsentLVCorruptedException</a></td>
<td>Base class for JET_err.LVCorrupted exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334692(v=exchg.10).md">EsentMakeBackupDirectoryFailException</a></td>
<td>Base class for JET_err.MakeBackupDirectoryFail exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334636(v=exchg.10).md">EsentMemoryException</a></td>
<td>Base class for Memory exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334701(v=exchg.10).md">EsentMissingCurrentLogFilesException</a></td>
<td>Base class for JET_err.MissingCurrentLogFiles exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334656(v=exchg.10).md">EsentMissingFileToBackupException</a></td>
<td>Base class for JET_err.MissingFileToBackup exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334670(v=exchg.10).md">EsentMissingFullBackupException</a></td>
<td>Base class for JET_err.MissingFullBackup exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334746(v=exchg.10).md">EsentMissingLogFileException</a></td>
<td>Base class for JET_err.MissingLogFile exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334679(v=exchg.10).md">EsentMissingPatchPageException</a></td>
<td>Base class for JET_err.MissingPatchPage exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334685(v=exchg.10).md">EsentMissingPreviousLogFileException</a></td>
<td>Base class for JET_err.MissingPreviousLogFile exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334755(v=exchg.10).md">EsentMissingRestoreLogFilesException</a></td>
<td>Base class for JET_err.MissingRestoreLogFiles exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334758(v=exchg.10).md">EsentMultiValuedColumnMustBeTaggedException</a></td>
<td>Base class for JET_err.MultiValuedColumnMustBeTagged exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334700(v=exchg.10).md">EsentMultiValuedDuplicateAfterTruncationException</a></td>
<td>Base class for JET_err.MultiValuedDuplicateAfterTruncation exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319652(v=exchg.10).md">EsentMultiValuedDuplicateException</a></td>
<td>Base class for JET_err.MultiValuedDuplicate exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334706(v=exchg.10).md">EsentMultiValuedIndexViolationException</a></td>
<td>Base class for JET_err.MultiValuedIndexViolation exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334710(v=exchg.10).md">EsentMustBeSeparateLongValueException</a></td>
<td>Base class for JET_err.MustBeSeparateLongValue exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319638(v=exchg.10).md">EsentMustCommitDistributedTransactionToLevel0Exception</a></td>
<td>Base class for JET_err.MustCommitDistributedTransactionToLevel0 exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319640(v=exchg.10).md">EsentMustDisableLoggingForDbUpgradeException</a></td>
<td>Base class for JET_err.MustDisableLoggingForDbUpgrade exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319646(v=exchg.10).md">EsentMustRollbackException</a></td>
<td>Base class for JET_err.MustRollback exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334719(v=exchg.10).md">EsentNoAttachmentsFailedIncrementalReseedException</a></td>
<td>Base class for JET_err.NoAttachmentsFailedIncrementalReseed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319659(v=exchg.10).md">EsentNoBackupDirectoryException</a></td>
<td>Base class for JET_err.NoBackupDirectory exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334724(v=exchg.10).md">EsentNoBackupException</a></td>
<td>Base class for JET_err.NoBackup exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334726(v=exchg.10).md">EsentNoCurrentIndexException</a></td>
<td>Base class for JET_err.NoCurrentIndex exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334730(v=exchg.10).md">EsentNoCurrentRecordException</a></td>
<td>Base class for JET_err.NoCurrentRecord exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334734(v=exchg.10).md">EsentNotInDistributedTransactionException</a></td>
<td>Base class for JET_err.NotInDistributedTransaction exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334741(v=exchg.10).md">EsentNotInitializedException</a></td>
<td>Base class for JET_err.NotInitialized exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334745(v=exchg.10).md">EsentNotInTransactionException</a></td>
<td>Base class for JET_err.NotInTransaction exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334749(v=exchg.10).md">EsentNTSystemCallFailedException</a></td>
<td>Base class for JET_err.NTSystemCallFailed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319698(v=exchg.10).md">EsentNullInvalidException</a></td>
<td>Base class for JET_err.NullInvalid exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319701(v=exchg.10).md">EsentNullKeyDisallowedException</a></td>
<td>Base class for JET_err.NullKeyDisallowed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319723(v=exchg.10).md">EsentObjectDuplicateException</a></td>
<td>Base class for JET_err.ObjectDuplicate exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319660(v=exchg.10).md">EsentObjectNotFoundException</a></td>
<td>Base class for JET_err.ObjectNotFound exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319668(v=exchg.10).md">EsentObsoleteException</a></td>
<td>Base class for Obsolete exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319719(v=exchg.10).md">EsentOneDatabasePerSessionException</a></td>
<td>Base class for JET_err.OneDatabasePerSession exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319727(v=exchg.10).md">EsentOperationException</a></td>
<td>Base class for Operation exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319729(v=exchg.10).md">EsentOSSnapshotInvalidSequenceException</a></td>
<td>Base class for JET_err.OSSnapshotInvalidSequence exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319741(v=exchg.10).md">EsentOSSnapshotInvalidSnapIdException</a></td>
<td>Base class for JET_err.OSSnapshotInvalidSnapId exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319702(v=exchg.10).md">EsentOSSnapshotNotAllowedException</a></td>
<td>Base class for JET_err.OSSnapshotNotAllowed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319704(v=exchg.10).md">EsentOSSnapshotTimeOutException</a></td>
<td>Base class for JET_err.OSSnapshotTimeOut exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319752(v=exchg.10).md">EsentOutOfAutoincrementValuesException</a></td>
<td>Base class for JET_err.OutOfAutoincrementValues exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319715(v=exchg.10).md">EsentOutOfBuffersException</a></td>
<td>Base class for JET_err.OutOfBuffers exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319764(v=exchg.10).md">EsentOutOfCursorsException</a></td>
<td>Base class for JET_err.OutOfCursors exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319717(v=exchg.10).md">EsentOutOfDatabaseSpaceException</a></td>
<td>Base class for JET_err.OutOfDatabaseSpace exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319775(v=exchg.10).md">EsentOutOfDbtimeValuesException</a></td>
<td>Base class for JET_err.OutOfDbtimeValues exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319728(v=exchg.10).md">EsentOutOfFileHandlesException</a></td>
<td>Base class for JET_err.OutOfFileHandles exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319790(v=exchg.10).md">EsentOutOfLongValueIDsException</a></td>
<td>Base class for JET_err.OutOfLongValueIDs exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319786(v=exchg.10).md">EsentOutOfMemoryException</a></td>
<td>Base class for JET_err.OutOfMemory exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319746(v=exchg.10).md">EsentOutOfObjectIDsException</a></td>
<td>Base class for JET_err.OutOfObjectIDs exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319807(v=exchg.10).md">EsentOutOfSequentialIndexValuesException</a></td>
<td>Base class for JET_err.OutOfSequentialIndexValues exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319800(v=exchg.10).md">EsentOutOfSessionsException</a></td>
<td>Base class for JET_err.OutOfSessions exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319762(v=exchg.10).md">EsentOutOfThreadsException</a></td>
<td>Base class for JET_err.OutOfThreads exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319768(v=exchg.10).md">EsentPageBoundaryException</a></td>
<td>Base class for JET_err.PageBoundary exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319771(v=exchg.10).md">EsentPageNotInitializedException</a></td>
<td>Base class for JET_err.PageNotInitialized exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319780(v=exchg.10).md">EsentPageSizeMismatchException</a></td>
<td>Base class for JET_err.PageSizeMismatch exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319835(v=exchg.10).md">EsentPartiallyAttachedDBException</a></td>
<td>Base class for JET_err.PartiallyAttachedDB exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319782(v=exchg.10).md">EsentPatchFileMissingException</a></td>
<td>Base class for JET_err.PatchFileMissing exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319785(v=exchg.10).md">EsentPermissionDeniedException</a></td>
<td>Base class for JET_err.PermissionDenied exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319852(v=exchg.10).md">EsentPreviousVersionException</a></td>
<td>Base class for JET_err.PreviousVersion exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319793(v=exchg.10).md">EsentPrimaryIndexCorruptedException</a></td>
<td>Base class for JET_err.PrimaryIndexCorrupted exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319805(v=exchg.10).md">EsentQueryNotSupportedException</a></td>
<td>Base class for JET_err.QueryNotSupported exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319806(v=exchg.10).md">EsentQuotaException</a></td>
<td>Base class for Quota exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319812(v=exchg.10).md">EsentReadLostFlushVerifyFailureException</a></td>
<td>Base class for JET_err.ReadLostFlushVerifyFailure exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319871(v=exchg.10).md">EsentReadPgnoVerifyFailureException</a></td>
<td>Base class for JET_err.ReadPgnoVerifyFailure exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319876(v=exchg.10).md">EsentReadVerifyFailureException</a></td>
<td>Base class for JET_err.ReadVerifyFailure exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319818(v=exchg.10).md">EsentRecordDeletedException</a></td>
<td>Base class for JET_err.RecordDeleted exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319884(v=exchg.10).md">EsentRecordFormatConversionFailedException</a></td>
<td>Base class for JET_err.RecordFormatConversionFailed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350517(v=exchg.10).md">EsentRecordNoCopyException</a></td>
<td>Base class for JET_err.RecordNoCopy exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350508(v=exchg.10).md">EsentRecordNotDeletedException</a></td>
<td>Base class for JET_err.RecordNotDeleted exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319846(v=exchg.10).md">EsentRecordNotFoundException</a></td>
<td>Base class for JET_err.RecordNotFound exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319853(v=exchg.10).md">EsentRecordPrimaryChangedException</a></td>
<td>Base class for JET_err.RecordPrimaryChanged exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319857(v=exchg.10).md">EsentRecordTooBigException</a></td>
<td>Base class for JET_err.RecordTooBig exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350529(v=exchg.10).md">EsentRecordTooBigForBackwardCompatibilityException</a></td>
<td>Base class for JET_err.RecordTooBigForBackwardCompatibility exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319863(v=exchg.10).md">EsentRecoveredWithErrorsException</a></td>
<td>Base class for JET_err.RecoveredWithErrors exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350538(v=exchg.10).md">EsentRecoveredWithoutUndoDatabasesConsistentException</a></td>
<td>Base class for JET_err.RecoveredWithoutUndoDatabasesConsistent exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350537(v=exchg.10).md">EsentRecoveredWithoutUndoException</a></td>
<td>Base class for JET_err.RecoveredWithoutUndo exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319891(v=exchg.10).md">EsentRecoveryVerifyFailureException</a></td>
<td>Base class for JET_err.RecoveryVerifyFailure exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319858(v=exchg.10).md">EsentRedoAbruptEndedException</a></td>
<td>Base class for JET_err.RedoAbruptEnded exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350548(v=exchg.10).md">EsentRequiredLogFilesMissingException</a></td>
<td>Base class for JET_err.RequiredLogFilesMissing exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn319890(v=exchg.10).md">EsentResource</a></td>
<td>This is the base class for all esent resource objects. Subclasses of this class can allocate and release unmanaged resources.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350557(v=exchg.10).md">EsentResourceException</a></td>
<td>Base class for Resource exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350560(v=exchg.10).md">EsentRestoreInProgressException</a></td>
<td>Base class for JET_err.RestoreInProgress exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350584(v=exchg.10).md">EsentRestoreOfNonBackupDatabaseException</a></td>
<td>Base class for JET_err.RestoreOfNonBackupDatabase exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350565(v=exchg.10).md">EsentRfsFailureException</a></td>
<td>Base class for JET_err.RfsFailure exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350589(v=exchg.10).md">EsentRfsNotArmedException</a></td>
<td>Base class for JET_err.RfsNotArmed exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350592(v=exchg.10).md">EsentRollbackErrorException</a></td>
<td>Base class for JET_err.RollbackError exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350571(v=exchg.10).md">EsentRollbackRequiredException</a></td>
<td>Base class for JET_err.RollbackRequired exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350596(v=exchg.10).md">EsentRunningInMultiInstanceModeException</a></td>
<td>Base class for JET_err.RunningInMultiInstanceMode exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350604(v=exchg.10).md">EsentRunningInOneInstanceModeException</a></td>
<td>Base class for JET_err.RunningInOneInstanceMode exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350606(v=exchg.10).md">EsentSecondaryIndexCorruptedException</a></td>
<td>Base class for JET_err.SecondaryIndexCorrupted exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350610(v=exchg.10).md">EsentSectorSizeNotSupportedException</a></td>
<td>Base class for JET_err.SectorSizeNotSupported exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350615(v=exchg.10).md">EsentSeparatedLongValueException</a></td>
<td>Base class for JET_err.SeparatedLongValue exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350621(v=exchg.10).md">EsentSesidTableIdMismatchException</a></td>
<td>Base class for JET_err.SesidTableIdMismatch exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350632(v=exchg.10).md">EsentSessionContextAlreadySetException</a></td>
<td>Base class for JET_err.SessionContextAlreadySet exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350627(v=exchg.10).md">EsentSessionContextNotSetByThisThreadException</a></td>
<td>Base class for JET_err.SessionContextNotSetByThisThread exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350638(v=exchg.10).md">EsentSessionInUseException</a></td>
<td>Base class for JET_err.SessionInUse exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350642(v=exchg.10).md">EsentSessionSharingViolationException</a></td>
<td>Base class for JET_err.SessionSharingViolation exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350646(v=exchg.10).md">EsentSessionWriteConflictException</a></td>
<td>Base class for JET_err.SessionWriteConflict exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350651(v=exchg.10).md">EsentSLVBufferTooSmallException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350654(v=exchg.10).md">EsentSLVColumnCannotDeleteException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350661(v=exchg.10).md">EsentSLVColumnDefaultValueNotAllowedException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350672(v=exchg.10).md">EsentSLVCorruptedException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350668(v=exchg.10).md">EsentSLVDatabaseMissingException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350681(v=exchg.10).md">EsentSLVEAListCorruptException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350686(v=exchg.10).md">EsentSLVEAListTooBigException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350689(v=exchg.10).md">EsentSLVEAListZeroAllocationException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350725(v=exchg.10).md">EsentSLVFileAccessDeniedException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350728(v=exchg.10).md">EsentSLVFileInUseException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350694(v=exchg.10).md">EsentSLVFileInvalidPathException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350696(v=exchg.10).md">EsentSLVFileIOException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334780(v=exchg.10).md">EsentSLVFileNotFoundException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334783(v=exchg.10).md">EsentSLVFileStaleException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334785(v=exchg.10).md">EsentSLVFileUnknownException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350706(v=exchg.10).md">EsentSLVHeaderBadChecksumException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334793(v=exchg.10).md">EsentSLVHeaderCorruptedException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334798(v=exchg.10).md">EsentSLVInvalidPathException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334804(v=exchg.10).md">EsentSLVOwnerMapAlreadyExistsException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350716(v=exchg.10).md">EsentSLVOwnerMapCorruptedException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350722(v=exchg.10).md">EsentSLVOwnerMapPageNotFoundException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350720(v=exchg.10).md">EsentSLVPagesNotCommittedException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350724(v=exchg.10).md">EsentSLVPagesNotDeletedException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350715(v=exchg.10).md">EsentSLVPagesNotFreeException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350735(v=exchg.10).md">EsentSLVPagesNotReservedException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334827(v=exchg.10).md">EsentSLVProviderNotLoadedException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350740(v=exchg.10).md">EsentSLVProviderVersionMismatchException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334832(v=exchg.10).md">EsentSLVReadVerifyFailureException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334835(v=exchg.10).md">EsentSLVRootNotSpecifiedException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334837(v=exchg.10).md">EsentSLVRootPathInvalidException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350749(v=exchg.10).md">EsentSLVRootStillOpenException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350755(v=exchg.10).md">EsentSLVSpaceCorruptedException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350752(v=exchg.10).md">EsentSLVSpaceWriteConflictException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334850(v=exchg.10).md">EsentSLVStreamingFileAlreadyExistsException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350758(v=exchg.10).md">EsentSLVStreamingFileFullException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334857(v=exchg.10).md">EsentSLVStreamingFileInUseException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334870(v=exchg.10).md">EsentSLVStreamingFileMissingException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334768(v=exchg.10).md">EsentSLVStreamingFileNotCreatedException</a></td>
<td></td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334778(v=exchg.10).md">EsentSLVStreamingFileReadOnlyException</a></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334788(v=exchg.10).md">EsentSoftRecoveryOnBackupDatabaseException</a></td>
<td>Base class for JET_err.SoftRecoveryOnBackupDatabase exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334794(v=exchg.10).md">EsentSoftRecoveryOnSnapshotException</a></td>
<td>Base class for JET_err.SoftRecoveryOnSnapshot exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334800(v=exchg.10).md">EsentSpaceHintsInvalidException</a></td>
<td>Base class for JET_err.SpaceHintsInvalid exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334906(v=exchg.10).md">EsentSPAvailExtCacheOutOfMemoryException</a></td>
<td>Base class for JET_err.SPAvailExtCacheOutOfMemory exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334808(v=exchg.10).md">EsentSPAvailExtCacheOutOfSyncException</a></td>
<td>Base class for JET_err.SPAvailExtCacheOutOfSync exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334914(v=exchg.10).md">EsentSPAvailExtCorruptedException</a></td>
<td>Base class for JET_err.SPAvailExtCorrupted exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334917(v=exchg.10).md">EsentSPOwnExtCorruptedException</a></td>
<td>Base class for JET_err.SPOwnExtCorrupted exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334854(v=exchg.10).md">EsentSQLLinkNotSupportedException</a></td>
<td>Base class for JET_err.SQLLinkNotSupported exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334858(v=exchg.10).md">EsentStartingRestoreLogTooHighException</a></td>
<td>Base class for JET_err.StartingRestoreLogTooHigh exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334920(v=exchg.10).md">EsentStateException</a></td>
<td>Base class for State exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334867(v=exchg.10).md">EsentStopwatch</a></td>
<td>Provides a set of methods and properties that you can use to measure ESENT work statistics for a thread. If the current version of ESENT doesn't support <a href="dn351264(v=exchg.10).md">JetGetThreadStats(JET_THREADSTATS)</a> then all ESENT statistics will be 0.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334874(v=exchg.10).md">EsentStreamingDataNotLoggedException</a></td>
<td>Base class for JET_err.StreamingDataNotLogged exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334878(v=exchg.10).md">EsentSurrogateBackupInProgressException</a></td>
<td>Base class for JET_err.SurrogateBackupInProgress exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334938(v=exchg.10).md">EsentSystemParamsAlreadySetException</a></td>
<td>Base class for JET_err.SystemParamsAlreadySet exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334943(v=exchg.10).md">EsentSystemPathInUseException</a></td>
<td>Base class for JET_err.SystemPathInUse exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334948(v=exchg.10).md">EsentTableDuplicateException</a></td>
<td>Base class for JET_err.TableDuplicate exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334903(v=exchg.10).md">EsentTableInUseException</a></td>
<td>Base class for JET_err.TableInUse exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334909(v=exchg.10).md">EsentTableLockedException</a></td>
<td>Base class for JET_err.TableLocked exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334941(v=exchg.10).md">EsentTableNotEmptyException</a></td>
<td>Base class for JET_err.TableNotEmpty exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334954(v=exchg.10).md">EsentTaggedNotNULLException</a></td>
<td>Base class for JET_err.TaggedNotNULL exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334958(v=exchg.10).md">EsentTaskDroppedException</a></td>
<td>Base class for JET_err.TaskDropped exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334964(v=exchg.10).md">EsentTempFileOpenErrorException</a></td>
<td>Base class for JET_err.TempFileOpenError exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334969(v=exchg.10).md">EsentTempPathInUseException</a></td>
<td>Base class for JET_err.TempPathInUse exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334979(v=exchg.10).md">EsentTermInProgressException</a></td>
<td>Base class for JET_err.TermInProgress exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334978(v=exchg.10).md">EsentTestInjectionNotSupportedException</a></td>
<td>Base class for JET_err.TestInjectionNotSupported exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334984(v=exchg.10).md">EsentTooManyActiveUsersException</a></td>
<td>Base class for JET_err.TooManyActiveUsers exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335011(v=exchg.10).md">EsentTooManyAttachedDatabasesException</a></td>
<td>Base class for JET_err.TooManyAttachedDatabases exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334989(v=exchg.10).md">EsentTooManyColumnsException</a></td>
<td>Base class for JET_err.TooManyColumns exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334994(v=exchg.10).md">EsentTooManyIndexesException</a></td>
<td>Base class for JET_err.TooManyIndexes exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335021(v=exchg.10).md">EsentTooManyInstancesException</a></td>
<td>Base class for JET_err.TooManyInstances exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335003(v=exchg.10).md">EsentTooManyIOException</a></td>
<td>Base class for JET_err.TooManyIO exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn334998(v=exchg.10).md">EsentTooManyKeysException</a></td>
<td>Base class for JET_err.TooManyKeys exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350776(v=exchg.10).md">EsentTooManyMempoolEntriesException</a></td>
<td>Base class for JET_err.TooManyMempoolEntries exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350781(v=exchg.10).md">EsentTooManyOpenDatabasesException</a></td>
<td>Base class for JET_err.TooManyOpenDatabases exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350784(v=exchg.10).md">EsentTooManyOpenIndexesException</a></td>
<td>Base class for JET_err.TooManyOpenIndexes exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350787(v=exchg.10).md">EsentTooManyOpenTablesAndCleanupTimedOutException</a></td>
<td>Base class for JET_err.TooManyOpenTablesAndCleanupTimedOut exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350769(v=exchg.10).md">EsentTooManyOpenTablesException</a></td>
<td>Base class for JET_err.TooManyOpenTables exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350779(v=exchg.10).md">EsentTooManySortsException</a></td>
<td>Base class for JET_err.TooManySorts exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350850(v=exchg.10).md">EsentTooManySplitsException</a></td>
<td>Base class for JET_err.TooManySplits exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350799(v=exchg.10).md">EsentTooManyTestInjectionsException</a></td>
<td>Base class for JET_err.TooManyTestInjections exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350809(v=exchg.10).md">EsentTransReadOnlyException</a></td>
<td>Base class for JET_err.TransReadOnly exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350808(v=exchg.10).md">EsentTransTooDeepException</a></td>
<td>Base class for JET_err.TransTooDeep exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350816(v=exchg.10).md">EsentUnicodeLanguageValidationFailureException</a></td>
<td>Base class for JET_err.UnicodeLanguageValidationFailure exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350818(v=exchg.10).md">EsentUnicodeNormalizationNotSupportedException</a></td>
<td>Base class for JET_err.UnicodeNormalizationNotSupported exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350843(v=exchg.10).md">EsentUnicodeTranslationBufferTooSmallException</a></td>
<td>Base class for JET_err.UnicodeTranslationBufferTooSmall exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350826(v=exchg.10).md">EsentUnicodeTranslationFailException</a></td>
<td>Base class for JET_err.UnicodeTranslationFail exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350835(v=exchg.10).md">EsentUnloadableOSFunctionalityException</a></td>
<td>Base class for JET_err.UnloadableOSFunctionality exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350839(v=exchg.10).md">EsentUpdateMustVersionException</a></td>
<td>Base class for JET_err.UpdateMustVersion exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350844(v=exchg.10).md">EsentUpdateNotPreparedException</a></td>
<td>Base class for JET_err.UpdateNotPrepared exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350849(v=exchg.10).md">EsentUsageException</a></td>
<td>Base class for Usage exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335007(v=exchg.10).md">EsentVersion</a></td>
<td>Gives information about the version of ESENT being used.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350862(v=exchg.10).md">EsentVersionStoreEntryTooBigException</a></td>
<td>Base class for JET_err.VersionStoreEntryTooBig exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350869(v=exchg.10).md">EsentVersionStoreOutOfMemoryAndCleanupTimedOutException</a></td>
<td>Base class for JET_err.VersionStoreOutOfMemoryAndCleanupTimedOut exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350874(v=exchg.10).md">EsentVersionStoreOutOfMemoryException</a></td>
<td>Base class for JET_err.VersionStoreOutOfMemory exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350876(v=exchg.10).md">EsentWriteConflictException</a></td>
<td>Base class for JET_err.WriteConflict exceptions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350897(v=exchg.10).md">EsentWriteConflictPrimaryIndexException</a></td>
<td>Base class for JET_err.WriteConflictPrimaryIndex exceptions.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350880(v=exchg.10).md">FloatColumnValue</a></td>
<td>A <a href="/dotnet/api/system.single">Single</a> column value.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350902(v=exchg.10).md">GuidColumnValue</a></td>
<td>A <a href="/dotnet/api/system.guid">Guid</a> column value.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350919(v=exchg.10).md">IndexInfo</a></td>
<td>Information about one esent index. This is not an interop class, but is used by the meta-data helper methods.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350912(v=exchg.10).md">IndexSegment</a></td>
<td>Describes one segment of an index.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350923(v=exchg.10).md">Instance</a></td>
<td>A class that encapsulates a <a href="hh564593(v=exchg.10).md">JET_INSTANCE</a> in a disposable object. The instance must be closed last and closing the instance releases all other resources for the instance.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350942(v=exchg.10).md">InstanceParameters</a></td>
<td>This class provides properties to set and get system parameters on an ESENT instance. This class provides static properties to set and get per-instance ESENT system parameters.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351017(v=exchg.10).md">Int16ColumnValue</a></td>
<td>An <a href="/dotnet/api/system.int16">Int16</a> column value.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn350992(v=exchg.10).md">Int32ColumnValue</a></td>
<td>An <a href="/dotnet/api/system.int32">Int32</a> column value.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351016(v=exchg.10).md">Int64ColumnValue</a></td>
<td>An <a href="/dotnet/api/system.int64">Int64</a> column value.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335045(v=exchg.10).md">JET_COLUMNBASE</a></td>
<td>Describes a column in a table of an ESENT database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335028(v=exchg.10).md">JET_COLUMNCREATE</a></td>
<td>Describes a column in a table of an ESENT database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335038(v=exchg.10).md">JET_COLUMNDEF</a></td>
<td>Describes a column in a table of an ESENT database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335047(v=exchg.10).md">JET_COLUMNLIST</a></td>
<td>Information about a temporary table containing information about all columns for a given table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335053(v=exchg.10).md">JET_CONDITIONALCOLUMN</a></td>
<td>Defines how conditional indexing is performed for a given index. A conditional index contains an index entry for only those rows that match the specified condition. However, the conditional column is not part of the index's key, it only controls the presence of the index entry.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335061(v=exchg.10).md">JET_CONVERT</a></td>
<td><strong>Obsolete.</strong> Conversion options for <a href="dn292112(v=exchg.10).md">JetCompact(JET_SESID, String, String, JET_PFNSTATUS, JET_CONVERT, CompactGrbit)</a>. This feature was discontinued in Windows Server 2003.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="hh538867(v=exchg.10).md">JET_DBINFOMISC</a></td>
<td>Holds miscellaneous information about a database. This is the information that is contained in the database header.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335081(v=exchg.10).md">JET_ENUMCOLUMN</a></td>
<td>Enumerates the column values of a record using the JetEnumerateColumns function. JetEnumerateColumns returns an array of JET_ENUMCOLUMNVALUE structures. The array is returned in memory that was allocated using the callback that was supplied to that function.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335139(v=exchg.10).md">JET_ENUMCOLUMNID</a></td>
<td>Enumerates a specific set of columns and, optionally, a specific set of multiple values for those columns when the JetEnumerateColumns function is used. JetEnumerateColumns optionally takes an array of JET_ENUMCOLUMNID structures.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335142(v=exchg.10).md">JET_ENUMCOLUMNVALUE</a></td>
<td>Enumerates the column values of a record using the JetEnumerateColumns function. <a href="dn292148(v=exchg.10).md">JetEnumerateColumns(JET_SESID, JET_TABLEID, Int32, [], Int32, [], JET_PFNREALLOC, IntPtr, Int32, EnumerateColumnsGrbit)</a> returns an array of JET_ENUMCOLUMNVALUE structures. The array is returned in memory that was allocated using the callback that was supplied to that function.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335112(v=exchg.10).md">JET_INDEXCREATE</a></td>
<td>Contains the information needed to create an index over data in an ESE database. Contains the information needed to create an index over data in an ESE database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335123(v=exchg.10).md">JET_INDEXLIST</a></td>
<td>Information about a temporary table containing information about all indexes for a given table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335175(v=exchg.10).md">JET_INDEXRANGE</a></td>
<td>Identifies an index range when it is used with the JetIntersectIndexes function.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335182(v=exchg.10).md">JET_INSTANCE_INFO</a></td>
<td>Receives information about running database instances when used with the JetGetInstanceInfo and JetOSSnapshotFreeze functions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335219(v=exchg.10).md">JET_OBJECTINFO</a></td>
<td>The JET_OBJECTINFO structure holds information about an object. Tables are the only object types that are currently supported.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335206(v=exchg.10).md">JET_OBJECTLIST</a></td>
<td>Information about a temporary table containing information about all tables for a given database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335223(v=exchg.10).md">JET_RECORDLIST</a></td>
<td>Information about a temporary table containing information about all indexes for a given table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335256(v=exchg.10).md">JET_RECPOS</a></td>
<td>Represents a fractional position within an index. This is used by JetGotoPosition and JetGetRecordPosition.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335277(v=exchg.10).md">JET_RETINFO</a></td>
<td>Contains optional input and output parameters for JetRetrieveColumn.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351033(v=exchg.10).md">JET_RETRIEVECOLUMN</a></td>
<td>Contains input and output parameters for <a href="dn334004(v=exchg.10).md">JetRetrieveColumns(JET_SESID, JET_TABLEID, [], Int32)</a>. Fields in the structure describe what column value to retrieve, how to retrieve it, and where to save results.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335235(v=exchg.10).md">JET_RSTINFO</a></td>
<td>Contains optional input and output parameters for JetRetrieveColumn.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351048(v=exchg.10).md">JET_RSTMAP</a></td>
<td>Enables the remapping of database file paths that are stored in the transaction logs during recovery.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn335260(v=exchg.10).md">JET_SETCOLUMN</a></td>
<td>Contains input and output parameters for <a href="dn334006(v=exchg.10).md">JetSetColumns(JET_SESID, JET_TABLEID, [], Int32)</a>. Fields in the structure describe what column value to set, how to set it, and where to get the column set data.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351059(v=exchg.10).md">JET_SETINFO</a></td>
<td>Settings for JetSetColumn.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351044(v=exchg.10).md">JET_SNPROG</a></td>
<td>Contains information about the progress of a long-running operation.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351095(v=exchg.10).md">JET_SPACEHINTS</a></td>
<td>Describes a column in a table of an ESENT database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351072(v=exchg.10).md">JET_TABLECREATE</a></td>
<td>Contains the information needed to create a table in an ESE database. Contains the information needed to create a table in an ESE database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351106(v=exchg.10).md">JET_UNICODEINDEX</a></td>
<td>Customizes how Unicode data gets normalized when an index is created over a Unicode column. Customizes how Unicode data gets normalized when an index is created over a Unicode column.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351164(v=exchg.10).md">Session</a></td>
<td>A class that encapsulates a JET_SESID in a disposable object.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351135(v=exchg.10).md">StringColumnValue</a></td>
<td>A Unicode string column value.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351139(v=exchg.10).md">SystemParameters</a></td>
<td>Constants for the ESENT API. These don't have to be looked up via system parameters. This class provides static properties to set and get global ESENT system parameters. This class provides static properties to set and get global ESENT system parameters.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351163(v=exchg.10).md">Table</a></td>
<td>A class that encapsulates a JET_TABLEID in a disposable object. This opens an existing table. To create a table use the JetCreateTable method.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351174(v=exchg.10).md">Transaction</a></td>
<td>A class that encapsulates a transaction on a JET_SESID.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351247(v=exchg.10).md">UInt16ColumnValue</a></td>
<td>A <a href="/dotnet/api/system.uint16">UInt16</a> column value.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351251(v=exchg.10).md">UInt32ColumnValue</a></td>
<td>A <a href="/dotnet/api/system.uint32">UInt32</a> column value.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351190(v=exchg.10).md">UInt64ColumnValue</a></td>
<td>A <a href="/dotnet/api/system.uint64">UInt64</a> column value.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292085.pubclass(EXCHG.10).gif" title="Public class" alt="Public class" /></td>
<td><a href="dn351191(v=exchg.10).md">Update</a></td>
<td>A class that encapsulates an update on a JET_TABLEID.</td>
</tr>
</tbody>
</table>


## Structures

<table>
<thead>
<tr class="header">
<th> </th>
<th>Structure</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh577892(v=exchg.10).md">JET_BKINFO</a></td>
<td>Holds a collection of data about a specific backup event.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh557662(v=exchg.10).md">JET_BKLOGTIME</a></td>
<td>Describes a date/time when a backup occured.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh564510(v=exchg.10).md">JET_COLUMNID</a></td>
<td>A JET_COLUMNID identifies a column within a table.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh596176(v=exchg.10).md">JET_DBID</a></td>
<td>A JET_DBID contains the handle to the database. A database handle is used to manage the schema of a database. It can also be used to manage the tables inside of that database.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh558081(v=exchg.10).md">JET_HANDLE</a></td>
<td>A JET_HANDLE contains a generic handle.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh557060(v=exchg.10).md">JET_INDEXID</a></td>
<td>Holds an index ID. An index ID is a hint that is used to accelerate the selection of the current index using JetSetCurrentIndex. It is most useful when there is a very large number of indexes over a table. The index ID can be retrieved using JetGetIndexInfo or JetGetTableIndexInfo.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh564593(v=exchg.10).md">JET_INSTANCE</a></td>
<td>A JET_INSTANCE contains a handle to the instance of the database to use for calls to the JET API.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh578063(v=exchg.10).md">JET_LGPOS</a></td>
<td>Describes an offset in the log sequence.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh557188(v=exchg.10).md">JET_LOGTIME</a></td>
<td>Describes a date/time.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh557499(v=exchg.10).md">JET_LS</a></td>
<td>Local storage for an ESENT handle. Used by <a href="dn292177(v=exchg.10).md">JetGetLS(JET_SESID, JET_TABLEID, JET_LS, LsGrbit)</a> and <a href="dn334015(v=exchg.10).md">JetSetLS(JET_SESID, JET_TABLEID, JET_LS, LsGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh558483(v=exchg.10).md">JET_OSSNAPID</a></td>
<td>A JET_OSSNAPID contains a handle to a snapshot of a database.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh596745(v=exchg.10).md">JET_SESID</a></td>
<td>A JET_SESID contains a handle to the session to use for calls to the JET APIr-.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh564644(v=exchg.10).md">JET_SIGNATURE</a></td>
<td>The JET_SIGNATURE structure contains information that uniquely identifies a database or logfile sequence.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubstructure(exchg.10).gif" title="Public structure" alt="Public structure" /></td>
<td><a href="hh566310(v=exchg.10).md">JET_TABLEID</a></td>
<td>A JET_TABLEID contains a handle to the database cursor to use for a call to the JET API. A cursor can only be used with the session that was used to open that cursor.</td>
</tr>
</tbody>
</table>


## Interfaces

<table>
<thead>
<tr class="header">
<th> </th>
<th>Interface</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/hh596136.pubinterface(exchg.10).gif" title="Public interface" alt="Public interface" /></td>
<td><a href="hh578046(v=exchg.10).md">IContentEquatable&lt;T&gt;</a></td>
<td>Interface for objects that can have their contents compared against each other. This should be used for equality comparisons on mutable reference objects where overriding Equals() and GetHashCode() isn't a good idea.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubinterface(exchg.10).gif" title="Public interface" alt="Public interface" /></td>
<td><a href="hh565368(v=exchg.10).md">IDeepCloneable&lt;T&gt;</a></td>
<td>Interface for objects that can be cloned. This creates a deep copy of the object. It is used for cloning meta-data objects.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubinterface(exchg.10).gif" title="Public interface" alt="Public interface" /></td>
<td><a href="hh596687(v=exchg.10).md">IJET_LOGTIME</a></td>
<td>Interface for common methods between JET_LOGTIME and JET_BKLOGTIME.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubinterface(exchg.10).gif" title="Public interface" alt="Public interface" /></td>
<td><a href="hh578599(v=exchg.10).md">INullableJetStruct</a></td>
<td>Interface for Jet structures that are nullable (can have null values).</td>
</tr>
</tbody>
</table>


## Delegates

<table>
<thead>
<tr class="header">
<th> </th>
<th>Delegate</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/hh596136.pubdelegate(exchg.10).gif" title="Public delegate" alt="Public delegate" /></td>
<td><a href="hh566065(v=exchg.10).md">JET_CALLBACK</a></td>
<td>A multi-purpose callback function used by the database engine to inform the application of an event involving online defragmentation and cursor state notifications.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubdelegate(exchg.10).gif" title="Public delegate" alt="Public delegate" /></td>
<td><a href="hh566077(v=exchg.10).md">JET_PFNREALLOC</a></td>
<td>Callback used by JetEnumerateColumns to allocate memory for its output buffers.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubdelegate(exchg.10).gif" title="Public delegate" alt="Public delegate" /></td>
<td><a href="hh565966(v=exchg.10).md">JET_PFNSTATUS</a></td>
<td>Receives information about the progress of long-running operations, such as defragmentation, backup, or restore operations. During such operations, the database engine calls this callback function to give an update on the progress of the operation.</td>
</tr>
</tbody>
</table>


## Enumerations

<table>
<thead>
<tr class="header">
<th> </th>
<th>Enumeration</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh579378(v=exchg.10).md">AttachDatabaseGrbit</a></td>
<td>Options for JetAttachDatabase.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh557664(v=exchg.10).md">BackupGrbit</a></td>
<td>Options for <a href="dn292102(v=exchg.10).md">JetBackupInstance(JET_INSTANCE, String, BackupGrbit, JET_PFNSTATUS)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh557018(v=exchg.10).md">BeginExternalBackupGrbit</a></td>
<td>Options for <a href="dn292104(v=exchg.10).md">JetBeginExternalBackupInstance(JET_INSTANCE, BeginExternalBackupGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh558568(v=exchg.10).md">BeginTransactionGrbit</a></td>
<td>Options for <a href="dn292106(v=exchg.10).md">JetBeginTransaction2(JET_SESID, BeginTransactionGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh578203(v=exchg.10).md">CloseDatabaseGrbit</a></td>
<td>Options for <a href="dn292107(v=exchg.10).md">JetCloseDatabase(JET_SESID, JET_DBID, CloseDatabaseGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh578986(v=exchg.10).md">ColumndefGrbit</a></td>
<td>Options for the JET_COLUMNDEF structure.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh564415(v=exchg.10).md">CommitTransactionGrbit</a></td>
<td>Options for JetCommitTransaction.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh556919(v=exchg.10).md">CompactGrbit</a></td>
<td>Options for <a href="dn292112(v=exchg.10).md">JetCompact(JET_SESID, String, String, JET_PFNSTATUS, JET_CONVERT, CompactGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh578990(v=exchg.10).md">ConditionalColumnGrbit</a></td>
<td>Options for the JET_CONDITIONALCOLUMN structure.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh596559(v=exchg.10).md">CreateDatabaseGrbit</a></td>
<td>Options for <a href="dn292118(v=exchg.10).md">JetCreateDatabase(JET_SESID, String, String, JET_DBID, CreateDatabaseGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh578433(v=exchg.10).md">CreateIndexGrbit</a></td>
<td>Options for JetCreateIndex.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh566808(v=exchg.10).md">CreateInstanceGrbit</a></td>
<td>Options for JetCreateInstance2.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh566466(v=exchg.10).md">CreateTableColumnIndexGrbit</a></td>
<td>Options for JetCreateTableColumnIndex.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh596803(v=exchg.10).md">DefragGrbit</a></td>
<td>Options for <a href="dn292130(v=exchg.10).md">JetDefragment(JET_SESID, JET_DBID, String, Int32, Int32, DefragGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh565122(v=exchg.10).md">DeleteColumnGrbit</a></td>
<td>Options for <a href="dn292132(v=exchg.10).md">JetDeleteColumn2(JET_SESID, JET_TABLEID, String, DeleteColumnGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn334195(v=exchg.10).md">DetachDatabaseGrbit</a></td>
<td>Options for <a href="dn292136(v=exchg.10).md">JetDetachDatabase2(JET_SESID, String, DetachDatabaseGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh558129(v=exchg.10).md">DupCursorGrbit</a></td>
<td>Options for <a href="dn292137(v=exchg.10).md">JetDupCursor(JET_SESID, JET_TABLEID, JET_TABLEID, DupCursorGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh566745(v=exchg.10).md">EndExternalBackupGrbit</a></td>
<td>Options for <a href="dn292142(v=exchg.10).md">JetEndExternalBackupInstance(JET_INSTANCE)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh578244(v=exchg.10).md">EndSessionGrbit</a></td>
<td>Options for JetEndSession.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh566564(v=exchg.10).md">EnumerateColumnsGrbit</a></td>
<td>Options for JetEnumerateColumns.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh565476(v=exchg.10).md">EscrowUpdateGrbit</a></td>
<td>Options for JetEscrowUpdate.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn350898(v=exchg.10).md">EventLoggingLevels</a></td>
<td>Options for EventLoggingLevel.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh578647(v=exchg.10).md">GetLockGrbit</a></td>
<td>Options for JetGetLock.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh565815(v=exchg.10).md">GetRecordSizeGrbit</a></td>
<td>Options for <a href="dn335320(v=exchg.10).md">JetGetRecordSize(JET_SESID, JET_TABLEID, JET_RECSIZE, GetRecordSizeGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh564940(v=exchg.10).md">GetSecondaryIndexBookmarkGrbit</a></td>
<td>Options for <a href="dn292180(v=exchg.10).md">JetGetSecondaryIndexBookmark(JET_SESID, JET_TABLEID, [], Int32, Int32, [], Int32, Int32, GetSecondaryIndexBookmarkGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh596145(v=exchg.10).md">GotoSecondaryIndexBookmarkGrbit</a></td>
<td>Options for <a href="dn292205(v=exchg.10).md">JetGotoSecondaryIndexBookmark(JET_SESID, JET_TABLEID, [], Int32, [], Int32, GotoSecondaryIndexBookmarkGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh565607(v=exchg.10).md">IdleGrbit</a></td>
<td>Options for <a href="dn292208(v=exchg.10).md">JetIdle(JET_SESID, IdleGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh579266(v=exchg.10).md">IndexKeyGrbit</a></td>
<td>Key definition grbits. Used when retrieving information about an index.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh558064(v=exchg.10).md">IndexRangeGrbit</a></td>
<td>Options for the JET_INDEXRANGE object.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh596658(v=exchg.10).md">InitGrbit</a></td>
<td>Options for <a href="dn292214(v=exchg.10).md">JetInit2(JET_INSTANCE, InitGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh577525(v=exchg.10).md">IntersectIndexesGrbit</a></td>
<td>Options for JetIntersectIndexes.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh564847(v=exchg.10).md">JET_cbtyp</a></td>
<td>Type of progress being reported.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh577895(v=exchg.10).md">JET_coltyp</a></td>
<td>ESENT column types.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh558581(v=exchg.10).md">JET_CP</a></td>
<td>Codepage for an ESENT column.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh163267(v=exchg.10).md">JET_DbInfo</a></td>
<td>Info levels for retrieving database info.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh578316(v=exchg.10).md">JET_dbstate</a></td>
<td>Database states (used in <a href="hh538867(v=exchg.10).md">JET_DBINFOMISC</a>).</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh564840(v=exchg.10).md">JET_err</a></td>
<td>ESENT error codes.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="dn335150(v=exchg.10).md">JET_ExceptionAction</a></td>
<td>Constants to be used with JET_paramExceptionAction.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh566739(v=exchg.10).md">JET_filetype</a></td>
<td>Esent file types.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh565119(v=exchg.10).md">JET_IdxInfo</a></td>
<td>Info levels for retrieve index information with JetGetIndexInfo. and JetGetTableIndexInfo.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh558184(v=exchg.10).md">JET_Move</a></td>
<td>Offsets for JetMove.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh565069(v=exchg.10).md">JET_objtyp</a></td>
<td>Type of an ESENT object.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh596135(v=exchg.10).md">JET_param</a></td>
<td>ESENT system parameters.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh557183(v=exchg.10).md">JET_prep</a></td>
<td>Update types for JetPrepareUpdate.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh577944(v=exchg.10).md">JET_SNP</a></td>
<td>The type of operation that progress is being reported for.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh577987(v=exchg.10).md">JET_SNT</a></td>
<td>Type of progress being reported.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh557667(v=exchg.10).md">JET_TblInfo</a></td>
<td>Info levels for retrieving table info with JetGetTableInfo.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh557250(v=exchg.10).md">JET_wrn</a></td>
<td>ESENT warning codes.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh579487(v=exchg.10).md">LsGrbit</a></td>
<td>Options for <a href="dn334015(v=exchg.10).md">JetSetLS(JET_SESID, JET_TABLEID, JET_LS, LsGrbit)</a> and <a href="dn292177(v=exchg.10).md">JetGetLS(JET_SESID, JET_TABLEID, JET_LS, LsGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh578182(v=exchg.10).md">MakeKeyGrbit</a></td>
<td>Options for JetMakeKey.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh558238(v=exchg.10).md">MoveGrbit</a></td>
<td>Options for JetMove.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh566138(v=exchg.10).md">ObjectInfoFlags</a></td>
<td>Flags for ESENT objects (tables). Used in <a href="dn335219(v=exchg.10).md">JET_OBJECTINFO</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh163294(v=exchg.10).md">ObjectInfoGrbit</a></td>
<td>Table options, used in <a href="dn335219(v=exchg.10).md">JET_OBJECTINFO</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh579532(v=exchg.10).md">OpenDatabaseGrbit</a></td>
<td>Options for <a href="dn292219(v=exchg.10).md">JetOpenDatabase(JET_SESID, String, String, JET_DBID, OpenDatabaseGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh557460(v=exchg.10).md">OpenTableGrbit</a></td>
<td>Options for JetOpenTable.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh577800(v=exchg.10).md">RenameColumnGrbit</a></td>
<td>Options for <a href="dn332990(v=exchg.10).md">JetRenameColumn(JET_SESID, JET_TABLEID, String, String, RenameColumnGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh596202(v=exchg.10).md">ResetTableSequentialGrbit</a></td>
<td>Options for JetResetTableSequential.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh578120(v=exchg.10).md">RetrieveColumnGrbit</a></td>
<td>Options for JetRetrieveColumn.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh564639(v=exchg.10).md">RetrieveKeyGrbit</a></td>
<td>Options for JetRetrieveKey.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh565408(v=exchg.10).md">RollbackTransactionGrbit</a></td>
<td>Options for JetRollbackTransaction.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh566176(v=exchg.10).md">SeekGrbit</a></td>
<td>Options for JetSeek.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh596297(v=exchg.10).md">SetColumnDefaultValueGrbit</a></td>
<td>Options for <a href="dn334010(v=exchg.10).md">JetSetColumnDefaultValue(JET_SESID, JET_DBID, String, String, [], Int32, SetColumnDefaultValueGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh538951(v=exchg.10).md">SetColumnGrbit</a></td>
<td>Options for JetSetColumn.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh558524(v=exchg.10).md">SetCurrentIndexGrbit</a></td>
<td>Options for <a href="dn334005(v=exchg.10).md">JetSetCurrentIndex2(JET_SESID, JET_TABLEID, String, SetCurrentIndexGrbit)</a> and <a href="dn334012(v=exchg.10).md">JetSetCurrentIndex3(JET_SESID, JET_TABLEID, String, SetCurrentIndexGrbit, Int32)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh558634(v=exchg.10).md">SetIndexRangeGrbit</a></td>
<td>Options for JetSetIndexRange.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh565734(v=exchg.10).md">SetTableSequentialGrbit</a></td>
<td>Options for JetSetTableSequential.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh558163(v=exchg.10).md">SnapshotFreezeGrbit</a></td>
<td>Options for <a href="dn332998(v=exchg.10).md">JetOSSnapshotFreeze(JET_OSSNAPID, Int32, [], SnapshotFreezeGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh566001(v=exchg.10).md">SnapshotPrepareGrbit</a></td>
<td>Options for <a href="dn292235(v=exchg.10).md">JetOSSnapshotPrepare(JET_OSSNAPID, SnapshotPrepareGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh579066(v=exchg.10).md">SnapshotThawGrbit</a></td>
<td>Options for <a href="dn332986(v=exchg.10).md">JetOSSnapshotThaw(JET_OSSNAPID, SnapshotThawGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh163400(v=exchg.10).md">SpaceHintsGrbit</a></td>
<td>Options for <a href="dn351095(v=exchg.10).md">JET_SPACEHINTS</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh558517(v=exchg.10).md">TempTableGrbit</a></td>
<td>Options for temporary table creation.</td>
</tr>
<tr class="even">
<td><img src="../images/hh596136.pubenumeration(exchg.10).gif" title="Public enumeration" alt="Public enumeration" /></td>
<td><a href="hh577872(v=exchg.10).md">TermGrbit</a></td>
<td>Options for <a href="dn334037(v=exchg.10).md">JetTerm2(JET_INSTANCE, TermGrbit)</a>.</td>
</tr>
</tbody>
</table>
