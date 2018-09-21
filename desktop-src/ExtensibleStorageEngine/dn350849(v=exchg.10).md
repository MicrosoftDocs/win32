---
title: EsentUsageException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentUsageException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentUsageException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentusageexception(v=EXCHG.10)
ms:contentKeyID: 55103173
ms.date: 07/30/2014
mtps_version: v=EXCHG.10
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentUsageException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentUsageException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentUsageException class

Base class for Usage exceptions.

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentUsageException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public MustInherit Class EsentUsageException _
    Inherits EsentApiException
'Usage
Dim instance As EsentUsageException
```

``` csharp
[SerializableAttribute]
public abstract class EsentUsageException : EsentApiException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentUsageException members](dn350859\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentUsageException  
            [Microsoft.Isam.Esent.Interop.EsentAfterInitializationException](dn334220\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentAlreadyInitializedException](dn273989\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentAlreadyPreparedException](dn334228\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBackupDirectoryNotEmptyException](dn273970\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadColumnIdException](dn274004\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadRestoreTargetInstanceException](dn274044\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCallbackNotResolvedException](dn274063\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotBeTaggedException](dn274074\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotDeleteSystemTableException](dn274139\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotDeleteTemplateTableException](dn274084\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotDeleteTempTableException](dn274088\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotDisableVersioningException](dn274157\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotIndexException](dn274099\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotMaterializeForwardOnlySortException](dn274102\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotNestDDLException](dn274172\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotSeparateIntrinsicLVException](dn274117\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnCannotBeCompressedException](dn274217\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnDoesNotFitException](dn334250\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnDuplicateException](dn274156\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnInUseException](dn274180\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnNoChunkException](dn274190\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnNotFoundException](dn274196\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnNotUpdatableException](dn334291\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnRedundantException](dn274198\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnTooBigException](dn334298\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseAlreadyRunningMaintenanceException](dn334266\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseCorruptedNoRepairException](dn334384\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseDuplicateException](dn334296\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseFileReadOnlyException](dn334306\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseInUseException](dn334322\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseInvalidIncrementalReseedException](dn334430\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseInvalidNameException](dn334450\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseInvalidPagesException](dn334339\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseInvalidPathException](dn334460\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseLockedException](dn334474\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseNotFoundException](dn334481\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseSharingViolationException](dn334374\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseSignInUseException](dn334488\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDDLNotInheritableException](dn334413\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDefaultValueTooBigException](dn334424\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDensityInvalidException](dn334433\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDisabledFunctionalityException](dn274277\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentEntryPointNotFoundException](dn274309\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentExclusiveTableLockRequiredException](dn274257\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFeatureNotAvailableException](dn274291\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFileCompressedException](dn274343\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFilteredMoveNotSupportedException](dn274384\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFixedDDLException](dn350411\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFixedInheritedDDLException](dn350413\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentForceDetachNotAllowedException](dn350463\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIllegalOperationException](dn350477\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexDuplicateException](dn350438\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexHasPrimaryException](dn350439\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexInvalidDefException](dn319396\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexMustStayException](dn319399\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesCannotRetrieveFromIndexException](dn319401\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesInvalidLimitsException](dn319411\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesKeyTooSmallException](dn350474\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesNonUniqueOnlyException](dn319420\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesSecondaryIndexOnlyException](dn350485\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesTextBinaryColumnsOnlyException](dn350490\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesVarSegMacNotAllowedException](dn319430\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInstanceNameInUseException](dn319385\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInTransactionException](dn319457\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidBackupException](dn319406\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidBackupSequenceException](dn319414\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidBookmarkException](dn319464\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidCodePageException](dn319443\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidColumnTypeException](dn319454\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidCreateIndexException](dn319507\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidDatabaseException](dn319474\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidDatabaseIdException](dn319512\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidGrbitException](dn319518\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidIndexIdException](dn319523\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidInstanceException](dn319502\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLanguageIdException](dn319529\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLCMapStringFlagsException](dn319538\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidNameException](dn319541\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidOperationException](dn319571\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidParameterException](dn319601\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidPathException](dn319577\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidPlaceholderColumnException](dn319579\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidPrereadException](dn334516\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidSesidException](dn319584\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidSettingsException](dn334521\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidTableIdException](dn334527\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyIsMadeException](dn334548\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyNotMadeException](dn334554\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogFileNotCopiedException](dn334541\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogFilePathInUseException](dn334545\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogFileSizeMismatchException](dn334627\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLoggingDisabledException](dn334582\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLSAlreadySetException](dn334614\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLSCallbackNotSpecifiedException](dn334617\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMultiValuedColumnMustBeTaggedException](dn334758\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMultiValuedIndexViolationException](dn334706\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMustBeSeparateLongValueException](dn334710\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMustRollbackException](dn319646\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentNoBackupDirectoryException](dn319659\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentNoCurrentIndexException](dn334726\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentNotInitializedException](dn334741\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentNotInTransactionException](dn334745\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentNullInvalidException](dn319698\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentNullKeyDisallowedException](dn319701\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentOneDatabasePerSessionException](dn319719\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentOSSnapshotInvalidSequenceException](dn319729\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentOSSnapshotInvalidSnapIdException](dn319741\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentPartiallyAttachedDBException](dn319835\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentPermissionDeniedException](dn319785\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentQueryNotSupportedException](dn319805\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordNoCopyException](dn350517\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordPrimaryChangedException](dn319853\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRestoreOfNonBackupDatabaseException](dn350584\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRunningInMultiInstanceModeException](dn350596\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRunningInOneInstanceModeException](dn350604\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSesidTableIdMismatchException](dn350621\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSessionContextAlreadySetException](dn350632\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSessionContextNotSetByThisThreadException](dn350627\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSessionInUseException](dn350638\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSessionSharingViolationException](dn350642\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSessionWriteConflictException](dn350646\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSoftRecoveryOnBackupDatabaseException](dn334788\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSpaceHintsInvalidException](dn334800\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSystemParamsAlreadySetException](dn334938\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSystemPathInUseException](dn334943\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTableLockedException](dn334909\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTableNotEmptyException](dn334941\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTempPathInUseException](dn334969\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyActiveUsersException](dn334984\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyAttachedDatabasesException](dn335011\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyColumnsException](dn334989\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyIndexesException](dn334994\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyKeysException](dn334998\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyOpenTablesAndCleanupTimedOutException](dn350787\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyTestInjectionsException](dn350799\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTransReadOnlyException](dn350809\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTransTooDeepException](dn350808\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentUnicodeNormalizationNotSupportedException](dn350818\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentUpdateMustVersionException](dn350839\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentUpdateNotPreparedException](dn350844\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentVersionStoreOutOfMemoryAndCleanupTimedOutException](dn350869\(v=exchg.10\).md)

