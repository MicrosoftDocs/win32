---
description: "Learn more about: EsentUsageException class"
title: EsentUsageException class
TOCTitle: EsentUsageException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentUsageException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentusageexception(v=EXCHG.10)
ms:contentKeyID: 55103173
ms.date: 07/30/2014
ms.topic: reference
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

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentUsageException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
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

[EsentUsageException members](./esentusageexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)

## Derived types

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentUsageException  
            [Microsoft.Isam.Esent.Interop.EsentAfterInitializationException](./esentafterinitializationexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentAlreadyInitializedException](./esentalreadyinitializedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentAlreadyPreparedException](./esentalreadypreparedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBackupDirectoryNotEmptyException](./esentbackupdirectorynotemptyexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadColumnIdException](./esentbadcolumnidexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadRestoreTargetInstanceException](./esentbadrestoretargetinstanceexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCallbackNotResolvedException](./esentcallbacknotresolvedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotBeTaggedException](./esentcannotbetaggedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotDeleteSystemTableException](./esentcannotdeletesystemtableexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotDeleteTemplateTableException](./esentcannotdeletetemplatetableexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotDeleteTempTableException](./esentcannotdeletetemptableexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotDisableVersioningException](./esentcannotdisableversioningexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotIndexException](./esentcannotindexexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotMaterializeForwardOnlySortException](./esentcannotmaterializeforwardonlysortexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotNestDDLException](./esentcannotnestddlexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotSeparateIntrinsicLVException](./esentcannotseparateintrinsiclvexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnCannotBeCompressedException](./esentcolumncannotbecompressedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnDoesNotFitException](./esentcolumndoesnotfitexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnDuplicateException](./esentcolumnduplicateexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnInUseException](./esentcolumninuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnNoChunkException](./esentcolumnnochunkexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnNotFoundException](./esentcolumnnotfoundexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnNotUpdatableException](./esentcolumnnotupdatableexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnRedundantException](./esentcolumnredundantexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnTooBigException](./esentcolumntoobigexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseAlreadyRunningMaintenanceException](./esentdatabasealreadyrunningmaintenanceexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseCorruptedNoRepairException](./esentdatabasecorruptednorepairexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseDuplicateException](./esentdatabaseduplicateexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseFileReadOnlyException](./esentdatabasefilereadonlyexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseInUseException](./esentdatabaseinuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseInvalidIncrementalReseedException](./esentdatabaseinvalidincrementalreseedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseInvalidNameException](./esentdatabaseinvalidnameexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseInvalidPagesException](./esentdatabaseinvalidpagesexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseInvalidPathException](./esentdatabaseinvalidpathexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseLockedException](./esentdatabaselockedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseNotFoundException](./esentdatabasenotfoundexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseSharingViolationException](./esentdatabasesharingviolationexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseSignInUseException](./esentdatabasesigninuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDDLNotInheritableException](./esentddlnotinheritableexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDefaultValueTooBigException](./esentdefaultvaluetoobigexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDensityInvalidException](./esentdensityinvalidexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDisabledFunctionalityException](./esentdisabledfunctionalityexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentEntryPointNotFoundException](./esententrypointnotfoundexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentExclusiveTableLockRequiredException](./esentexclusivetablelockrequiredexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFeatureNotAvailableException](./esentfeaturenotavailableexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFileCompressedException](./esentfilecompressedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFilteredMoveNotSupportedException](./esentfilteredmovenotsupportedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFixedDDLException](./esentfixedddlexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFixedInheritedDDLException](./esentfixedinheritedddlexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentForceDetachNotAllowedException](./esentforcedetachnotallowedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIllegalOperationException](./esentillegaloperationexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexDuplicateException](./esentindexduplicateexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexHasPrimaryException](./esentindexhasprimaryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexInvalidDefException](./esentindexinvaliddefexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexMustStayException](./esentindexmuststayexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesCannotRetrieveFromIndexException](./esentindextuplescannotretrievefromindexexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesInvalidLimitsException](./esentindextuplesinvalidlimitsexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesKeyTooSmallException](./esentindextupleskeytoosmallexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesNonUniqueOnlyException](./esentindextuplesnonuniqueonlyexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesSecondaryIndexOnlyException](./esentindextuplessecondaryindexonlyexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesTextBinaryColumnsOnlyException](./esentindextuplestextbinarycolumnsonlyexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesVarSegMacNotAllowedException](./esentindextuplesvarsegmacnotallowedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInstanceNameInUseException](./esentinstancenameinuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInTransactionException](./esentintransactionexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidBackupException](./esentinvalidbackupexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidBackupSequenceException](./esentinvalidbackupsequenceexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidBookmarkException](./esentinvalidbookmarkexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidCodePageException](./esentinvalidcodepageexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidColumnTypeException](./esentinvalidcolumntypeexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidCreateIndexException](./esentinvalidcreateindexexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidDatabaseException](./esentinvaliddatabaseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidDatabaseIdException](./esentinvaliddatabaseidexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidGrbitException](./esentinvalidgrbitexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidIndexIdException](./esentinvalidindexidexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidInstanceException](./esentinvalidinstanceexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLanguageIdException](./esentinvalidlanguageidexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLCMapStringFlagsException](./esentinvalidlcmapstringflagsexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidNameException](./esentinvalidnameexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidOperationException](./esentinvalidoperationexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidParameterException](./esentinvalidparameterexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidPathException](./esentinvalidpathexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidPlaceholderColumnException](./esentinvalidplaceholdercolumnexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidPrereadException](./esentinvalidprereadexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidSesidException](./esentinvalidsesidexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidSettingsException](./esentinvalidsettingsexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidTableIdException](./esentinvalidtableidexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyIsMadeException](./esentkeyismadeexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyNotMadeException](./esentkeynotmadeexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogFileNotCopiedException](./esentlogfilenotcopiedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogFilePathInUseException](./esentlogfilepathinuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogFileSizeMismatchException](./esentlogfilesizemismatchexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLoggingDisabledException](./esentloggingdisabledexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLSAlreadySetException](./esentlsalreadysetexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLSCallbackNotSpecifiedException](./esentlscallbacknotspecifiedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMultiValuedColumnMustBeTaggedException](./esentmultivaluedcolumnmustbetaggedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMultiValuedIndexViolationException](./esentmultivaluedindexviolationexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMustBeSeparateLongValueException](./esentmustbeseparatelongvalueexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMustRollbackException](./esentmustrollbackexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentNoBackupDirectoryException](./esentnobackupdirectoryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentNoCurrentIndexException](./esentnocurrentindexexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentNotInitializedException](./esentnotinitializedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentNotInTransactionException](./esentnotintransactionexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentNullInvalidException](./esentnullinvalidexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentNullKeyDisallowedException](./esentnullkeydisallowedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentOneDatabasePerSessionException](./esentonedatabasepersessionexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentOSSnapshotInvalidSequenceException](./esentossnapshotinvalidsequenceexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentOSSnapshotInvalidSnapIdException](./esentossnapshotinvalidsnapidexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentPartiallyAttachedDBException](./esentpartiallyattacheddbexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentPermissionDeniedException](./esentpermissiondeniedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentQueryNotSupportedException](./esentquerynotsupportedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordNoCopyException](./esentrecordnocopyexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordPrimaryChangedException](./esentrecordprimarychangedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRestoreOfNonBackupDatabaseException](./esentrestoreofnonbackupdatabaseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRunningInMultiInstanceModeException](./esentrunninginmultiinstancemodeexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRunningInOneInstanceModeException](./esentrunninginoneinstancemodeexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSesidTableIdMismatchException](./esentsesidtableidmismatchexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSessionContextAlreadySetException](./esentsessioncontextalreadysetexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSessionContextNotSetByThisThreadException](./esentsessioncontextnotsetbythisthreadexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSessionInUseException](./esentsessioninuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSessionSharingViolationException](./esentsessionsharingviolationexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSessionWriteConflictException](./esentsessionwriteconflictexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSoftRecoveryOnBackupDatabaseException](./esentsoftrecoveryonbackupdatabaseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSpaceHintsInvalidException](./esentspacehintsinvalidexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSystemParamsAlreadySetException](./esentsystemparamsalreadysetexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSystemPathInUseException](./esentsystempathinuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTableLockedException](./esenttablelockedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTableNotEmptyException](./esenttablenotemptyexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTempPathInUseException](./esenttemppathinuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyActiveUsersException](./esenttoomanyactiveusersexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyAttachedDatabasesException](./esenttoomanyattacheddatabasesexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyColumnsException](./esenttoomanycolumnsexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyIndexesException](./esenttoomanyindexesexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyKeysException](./esenttoomanykeysexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyOpenTablesAndCleanupTimedOutException](./esenttoomanyopentablesandcleanuptimedoutexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyTestInjectionsException](./esenttoomanytestinjectionsexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTransReadOnlyException](./esenttransreadonlyexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTransTooDeepException](./esenttranstoodeepexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentUnicodeNormalizationNotSupportedException](./esentunicodenormalizationnotsupportedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentUpdateMustVersionException](./esentupdatemustversionexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentUpdateNotPreparedException](./esentupdatenotpreparedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentVersionStoreOutOfMemoryAndCleanupTimedOutException](./esentversionstoreoutofmemoryandcleanuptimedoutexception-class.md)