---
title: EsentObsoleteException class (Microsoft.Isam.Esent.Interop)
TOCTitle: EsentObsoleteException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentObsoleteException
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/microsoft.isam.esent.interop.esentobsoleteexception(v=EXCHG.10)
ms:contentKeyID: 55102357
ms.date: 07/30/2014
ms.topic: article
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

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentObsoleteException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
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

[EsentObsoleteException members](dn319669\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

## Inheritance hierarchy

[System.Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  
  [System.Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentObsoleteException  
            [Microsoft.Isam.Esent.Interop.EsentAccessDeniedException](dn273978\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadBackupDatabaseSizeException](dn273987\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadBookmarkException](dn274043\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadDbSignatureException](dn274009\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadPatchPageException](dn274093\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadSLVSignatureException](dn274107\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotAddFixedVarColumnToDerivedTableException](dn274130\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCannotNestDistributedTransactionsException](dn274174\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnIndexedException](dn274164\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnInRelationshipException](dn334259\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentColumnLongException](dn334271\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentContainerNotEmptyException](dn334323\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCurrencyStackOutOfMemoryException](dn334249\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabase200FormatException](dn334342\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabase400FormatException](dn334253\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabase500FormatException](dn334350\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseIdInUseException](dn334396\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabasePatchFileMismatchException](dn334483\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabasesNotFromSameSnapshotException](dn334386\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseStreamingFileMismatchException](dn334493\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseUnavailableException](dn274227\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDataHasChangedException](dn334397\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDistributedTransactionAlreadyPreparedToCommitException](dn334490\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDistributedTransactionNotYetPreparedToCommitException](dn274293\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDTCCallbackUnexpectedErrorException](dn334500\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDTCMissingCallbackException](dn334508\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDTCMissingCallbackOnRecoveryException](dn274310\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFileCloseException](dn274332\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFileIOAbortException](dn274355\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFileIOFailException](dn274360\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFileIORetryException](dn274364\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFileIOSparseException](dn274375\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexCantBuildException](dn350436\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexTuplesTooManyColumnsException](dn319427\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidCountryException](dn319498\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidFilenameException](dn319520\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLogDirectoryException](dn319548\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLoggedOperationException](dn319545\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidObjectException](dn319564\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidOnSortException](dn319570\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidSystemPathException](dn334526\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyBoundaryException](dn319605\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyTooBigException](dn319610\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLanguageNotSupportedException](dn334570\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLinkNotSupportedException](dn334571\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogBufferTooSmallException](dn334573\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingPatchPageException](dn334679\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMustCommitDistributedTransactionToLevel0Exception](dn319638\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMustDisableLoggingForDbUpgradeException](dn319640\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentNotInDistributedTransactionException](dn334734\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentObjectDuplicateException](dn319723\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentPageBoundaryException](dn319768\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentPatchFileMissingException](dn319782\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRfsFailureException](dn350565\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRfsNotArmedException](dn350589\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRollbackRequiredException](dn350571\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVBufferTooSmallException](dn350651\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVColumnCannotDeleteException](dn350654\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVColumnDefaultValueNotAllowedException](dn350661\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVCorruptedException](dn350672\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVDatabaseMissingException](dn350668\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVEAListCorruptException](dn350681\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVEAListTooBigException](dn350686\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVEAListZeroAllocationException](dn350689\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileAccessDeniedException](dn350725\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileInUseException](dn350728\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileInvalidPathException](dn350694\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileIOException](dn350696\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileNotFoundException](dn334780\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileStaleException](dn334783\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVFileUnknownException](dn334785\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVHeaderBadChecksumException](dn350706\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVHeaderCorruptedException](dn334793\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVInvalidPathException](dn334798\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVOwnerMapAlreadyExistsException](dn334804\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVOwnerMapCorruptedException](dn350716\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVOwnerMapPageNotFoundException](dn350722\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVPagesNotCommittedException](dn350720\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVPagesNotDeletedException](dn350724\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVPagesNotFreeException](dn350715\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVPagesNotReservedException](dn350735\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVProviderNotLoadedException](dn334827\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVProviderVersionMismatchException](dn350740\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVReadVerifyFailureException](dn334832\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVRootNotSpecifiedException](dn334835\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVRootPathInvalidException](dn334837\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVRootStillOpenException](dn350749\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVSpaceCorruptedException](dn350755\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVSpaceWriteConflictException](dn350752\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileAlreadyExistsException](dn334850\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileFullException](dn350758\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileInUseException](dn334857\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileMissingException](dn334870\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileNotCreatedException](dn334768\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSLVStreamingFileReadOnlyException](dn334778\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSoftRecoveryOnSnapshotException](dn334794\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSPAvailExtCacheOutOfMemoryException](dn334906\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSPAvailExtCacheOutOfSyncException](dn334808\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSQLLinkNotSupportedException](dn334854\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentStreamingDataNotLoggedException](dn334874\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTaggedNotNULLException](dn334954\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTempFileOpenErrorException](dn334964\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManyOpenDatabasesException](dn350781\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTooManySplitsException](dn350850\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentUnicodeTranslationBufferTooSmallException](dn350843\(v=exchg.10\).md)

