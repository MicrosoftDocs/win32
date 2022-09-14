---
description: "Learn more about: EsentStateException class"
title: EsentStateException class
TOCTitle: EsentStateException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentStateException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentstateexception(v=EXCHG.10)
ms:contentKeyID: 55102986
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentStateException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentStateException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentStateException class

Base class for State exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentStateException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public MustInherit Class EsentStateException _
    Inherits EsentApiException
'Usage
Dim instance As EsentStateException
```

``` csharp
[SerializableAttribute]
public abstract class EsentStateException : EsentApiException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentStateException members](./esentstateexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)

## Derived types

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](./esentapiexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentStateException  
            [Microsoft.Isam.Esent.Interop.EsentBackupInProgressException](./esentbackupinprogressexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBackupNotAllowedYetException](./esentbackupnotallowedyetexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadItagSequenceException](./esentbaditagsequenceexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBufferTooSmallException](./esentbuffertoosmallexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCallbackFailedException](./esentcallbackfailedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseAlreadyUpgradedException](./esentdatabasealreadyupgradedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseFailedIncrementalReseedException](./esentdatabasefailedincrementalreseedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseIncompleteUpgradeException](./esentdatabaseincompleteupgradeexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseLeakInSpaceException](./esentdatabaseleakinspaceexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDirtyShutdownException](./esentdirtyshutdownexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFileNotFoundException](./esentfilenotfoundexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexInUseException](./esentindexinuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexNotFoundException](./esentindexnotfoundexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidBufferSizeException](./esentinvalidbuffersizeexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLogDataSequenceException](./esentinvalidlogdatasequenceexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyDuplicateException](./esentkeyduplicateexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyTruncatedException](./esentkeytruncatedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogFileSizeMismatchDatabasesConsistentException](./esentlogfilesizemismatchdatabasesconsistentexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogSectorSizeMismatchDatabasesConsistentException](./esentlogsectorsizemismatchdatabasesconsistentexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLSNotSetException](./esentlsnotsetexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingFullBackupException](./esentmissingfullbackupexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMultiValuedDuplicateAfterTruncationException](./esentmultivaluedduplicateaftertruncationexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMultiValuedDuplicateException](./esentmultivaluedduplicateexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentNoAttachmentsFailedIncrementalReseedException](./esentnoattachmentsfailedincrementalreseedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentNoBackupException](./esentnobackupexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentNoCurrentRecordException](./esentnocurrentrecordexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentObjectNotFoundException](./esentobjectnotfoundexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentOSSnapshotNotAllowedException](./esentossnapshotnotallowedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordDeletedException](./esentrecorddeletedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordNotFoundException](./esentrecordnotfoundexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordTooBigException](./esentrecordtoobigexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordTooBigForBackwardCompatibilityException](./esentrecordtoobigforbackwardcompatibilityexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRecoveredWithErrorsException](./esentrecoveredwitherrorsexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRecoveredWithoutUndoDatabasesConsistentException](./esentrecoveredwithoutundodatabasesconsistentexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRecoveredWithoutUndoException](./esentrecoveredwithoutundoexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRestoreInProgressException](./esentrestoreinprogressexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSeparatedLongValueException](./esentseparatedlongvalueexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSurrogateBackupInProgressException](./esentsurrogatebackupinprogressexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTableDuplicateException](./esenttableduplicateexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTableInUseException](./esenttableinuseexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentTestInjectionNotSupportedException](./esenttestinjectionnotsupportedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentWriteConflictException](./esentwriteconflictexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentWriteConflictPrimaryIndexException](./esentwriteconflictprimaryindexexception-class.md)