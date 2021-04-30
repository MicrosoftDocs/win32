---
description: "Learn more about: EsentObsoleteException class"
title: EsentObsoleteException class
TOCTitle: EsentObsoleteException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentObsoleteException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentobsoleteexception(v=EXCHG.10)
ms:contentKeyID: 55102357
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentObsoleteException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentObsoleteException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentObsoleteException class

Base class for Obsolete exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentObsoleteException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public MustInherit Class EsentObsoleteException _
    Inherits EsentApiException
'Usage
Dim instance As EsentObsoleteException
```

``` csharp
[SerializableAttribute]
public abstract class EsentObsoleteException : EsentApiException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentObsoleteException members](./esentobsoleteexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)

## Derived types

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentObsoleteException  
            [Microsoft.Isam.Esent.Interop.EsentAccessDeniedException](./esentaccessdeniedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadBackupDatabaseSizeException](./esentbadbackupdatabasesizeexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadBookmarkException](./esentbadbookmarkexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadDbSignatureException](./esentbaddbsignatureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadPatchPageException](./esentbadpatchpageexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadSLVSignatureException](./esentbadslvsignatureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotAddFixedVarColumnToDerivedTableException](./esentcannotaddfixedvarcolumntoderivedtableexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotNestDistributedTransactionsException](./esentcannotnestdistributedtransactionsexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnIndexedException](./esentcolumnindexedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnInRelationshipException](./esentcolumninrelationshipexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnLongException](./esentcolumnlongexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentContainerNotEmptyException](./esentcontainernotemptyexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCurrencyStackOutOfMemoryException](./esentcurrencystackoutofmemoryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabase200FormatException](./esentdatabase200formatexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabase400FormatException](./esentdatabase400formatexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabase500FormatException](./esentdatabase500formatexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseIdInUseException](./esentdatabaseidinuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabasePatchFileMismatchException](./esentdatabasepatchfilemismatchexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabasesNotFromSameSnapshotException](./esentdatabasesnotfromsamesnapshotexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseStreamingFileMismatchException](./esentdatabasestreamingfilemismatchexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseUnavailableException](./esentdatabaseunavailableexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDataHasChangedException](./esentdatahaschangedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDistributedTransactionAlreadyPreparedToCommitException](./esentdistributedtransactionalreadypreparedtocommitexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDistributedTransactionNotYetPreparedToCommitException](./esentdistributedtransactionnotyetpreparedtocommitexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDTCCallbackUnexpectedErrorException](./esentdtccallbackunexpectederrorexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDTCMissingCallbackException](./esentdtcmissingcallbackexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDTCMissingCallbackOnRecoveryException](./esentdtcmissingcallbackonrecoveryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFileCloseException](./esentfilecloseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFileIOAbortException](./esentfileioabortexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFileIOFailException](./esentfileiofailexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFileIORetryException](./esentfileioretryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFileIOSparseException](./esentfileiosparseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexCantBuildException](./esentindexcantbuildexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesTooManyColumnsException](./esentindextuplestoomanycolumnsexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidCountryException](./esentinvalidcountryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidFilenameException](./esentinvalidfilenameexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLogDirectoryException](./esentinvalidlogdirectoryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLoggedOperationException](./esentinvalidloggedoperationexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidObjectException](./esentinvalidobjectexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidOnSortException](./esentinvalidonsortexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidSystemPathException](./esentinvalidsystempathexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyBoundaryException](./esentkeyboundaryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyTooBigException](./esentkeytoobigexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLanguageNotSupportedException](./esentlanguagenotsupportedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLinkNotSupportedException](./esentlinknotsupportedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogBufferTooSmallException](./esentlogbuffertoosmallexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingPatchPageException](./esentmissingpatchpageexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMustCommitDistributedTransactionToLevel0Exception](./esentmustcommitdistributedtransactiontolevel0exception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMustDisableLoggingForDbUpgradeException](./esentmustdisableloggingfordbupgradeexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentNotInDistributedTransactionException](./esentnotindistributedtransactionexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentObjectDuplicateException](./esentobjectduplicateexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentPageBoundaryException](./esentpageboundaryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentPatchFileMissingException](./esentpatchfilemissingexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRfsFailureException](./esentrfsfailureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRfsNotArmedException](./esentrfsnotarmedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRollbackRequiredException](./esentrollbackrequiredexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVBufferTooSmallException](./esentslvbuffertoosmallexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVColumnCannotDeleteException](./esentslvcolumncannotdeleteexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVColumnDefaultValueNotAllowedException](./esentslvcolumndefaultvaluenotallowedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVCorruptedException](./esentslvcorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVDatabaseMissingException](./esentslvdatabasemissingexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVEAListCorruptException](./esentslvealistcorruptexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVEAListTooBigException](./esentslvealisttoobigexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVEAListZeroAllocationException](./esentslvealistzeroallocationexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileAccessDeniedException](./esentslvfileaccessdeniedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileInUseException](./esentslvfileinuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileInvalidPathException](./esentslvfileinvalidpathexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileIOException](./esentslvfileioexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileNotFoundException](./esentslvfilenotfoundexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileStaleException](./esentslvfilestaleexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileUnknownException](./esentslvfileunknownexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVHeaderBadChecksumException](./esentslvheaderbadchecksumexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVHeaderCorruptedException](./esentslvheadercorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVInvalidPathException](./esentslvinvalidpathexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVOwnerMapAlreadyExistsException](./esentslvownermapalreadyexistsexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVOwnerMapCorruptedException](./esentslvownermapcorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVOwnerMapPageNotFoundException](./esentslvownermappagenotfoundexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVPagesNotCommittedException](./esentslvpagesnotcommittedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVPagesNotDeletedException](./esentslvpagesnotdeletedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVPagesNotFreeException](./esentslvpagesnotfreeexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVPagesNotReservedException](./esentslvpagesnotreservedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVProviderNotLoadedException](./esentslvprovidernotloadedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVProviderVersionMismatchException](./esentslvproviderversionmismatchexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVReadVerifyFailureException](./esentslvreadverifyfailureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVRootNotSpecifiedException](./esentslvrootnotspecifiedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVRootPathInvalidException](./esentslvrootpathinvalidexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVRootStillOpenException](./esentslvrootstillopenexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVSpaceCorruptedException](./esentslvspacecorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVSpaceWriteConflictException](./esentslvspacewriteconflictexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileAlreadyExistsException](./esentslvstreamingfilealreadyexistsexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileFullException](./esentslvstreamingfilefullexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileInUseException](./esentslvstreamingfileinuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileMissingException](./esentslvstreamingfilemissingexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileNotCreatedException](./esentslvstreamingfilenotcreatedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileReadOnlyException](./esentslvstreamingfilereadonlyexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSoftRecoveryOnSnapshotException](./esentsoftrecoveryonsnapshotexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSPAvailExtCacheOutOfMemoryException](./esentspavailextcacheoutofmemoryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSPAvailExtCacheOutOfSyncException](./esentspavailextcacheoutofsyncexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSQLLinkNotSupportedException](./esentsqllinknotsupportedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentStreamingDataNotLoggedException](./esentstreamingdatanotloggedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTaggedNotNULLException](./esenttaggednotnullexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTempFileOpenErrorException](./esenttempfileopenerrorexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyOpenDatabasesException](./esenttoomanyopendatabasesexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManySplitsException](./esenttoomanysplitsexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentUnicodeTranslationBufferTooSmallException](./esentunicodetranslationbuffertoosmallexception-class.md)