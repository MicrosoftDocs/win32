---
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
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentStateException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
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

[EsentStateException members](dn334927\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentApiException](dn334231\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentStateException  
            [Microsoft.Isam.Esent.Interop.EsentBackupInProgressException](dn274026\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBackupNotAllowedYetException](dn274032\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadItagSequenceException](dn274018\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBufferTooSmallException](dn274053\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCallbackFailedException](dn274120\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseAlreadyUpgradedException](dn334272\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseFailedIncrementalReseedException](dn334404\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseIncompleteUpgradeException](dn334320\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseLeakInSpaceException](dn334349\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDirtyShutdownException](dn334452\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFileNotFoundException](dn274377\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexInUseException](dn350505\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexNotFoundException](dn350459\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidBufferSizeException](dn319475\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLogDataSequenceException](dn319536\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyDuplicateException](dn319603\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentKeyTruncatedException](dn334565\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogFileSizeMismatchDatabasesConsistentException](dn334552\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogSectorSizeMismatchDatabasesConsistentException](dn334645\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLSNotSetException](dn334676\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingFullBackupException](dn334670\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMultiValuedDuplicateAfterTruncationException](dn334700\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMultiValuedDuplicateException](dn319652\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentNoAttachmentsFailedIncrementalReseedException](dn334719\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentNoBackupException](dn334724\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentNoCurrentRecordException](dn334730\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentObjectNotFoundException](dn319660\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentOSSnapshotNotAllowedException](dn319702\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordDeletedException](dn319818\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordNotFoundException](dn319846\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordTooBigException](dn319857\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordTooBigForBackwardCompatibilityException](dn350529\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRecoveredWithErrorsException](dn319863\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRecoveredWithoutUndoDatabasesConsistentException](dn350538\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRecoveredWithoutUndoException](dn350537\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRestoreInProgressException](dn350560\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSeparatedLongValueException](dn350615\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSurrogateBackupInProgressException](dn334878\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTableDuplicateException](dn334948\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTableInUseException](dn334903\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentTestInjectionNotSupportedException](dn334978\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentWriteConflictException](dn350876\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentWriteConflictPrimaryIndexException](dn350897\(v=exchg.10\).md)