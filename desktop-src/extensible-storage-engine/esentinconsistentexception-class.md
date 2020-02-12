---
title: EsentInconsistentException class
TOCTitle: EsentInconsistentException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentInconsistentException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentinconsistentexception(v=EXCHG.10)
ms:contentKeyID: 55101798
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentInconsistentException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentInconsistentException
topic_type: 
- apiref
- kbSyntax
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentInconsistentException class

Base class for Inconsistent exceptions.

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentInconsistentException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public MustInherit Class EsentInconsistentException _
    Inherits EsentDataException
'Usage
Dim instance As EsentInconsistentException
```

``` csharp
[SerializableAttribute]
public abstract class EsentInconsistentException : EsentDataException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentInconsistentException members](dn350428\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentInconsistentException  
            [Microsoft.Isam.Esent.Interop.EsentAttachedDatabaseMismatchException](dn334236\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadCheckpointSignatureException](dn273995\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadLogSignatureException](dn274072\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadLogVersionException](dn274023\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCheckpointFileNotFoundException](dn274140\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentConsistentTimeMismatchException](dn274215\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseDirtyShutdownException](dn334290\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseIncompleteIncrementalReseedException](dn334412\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseLogSetMismatchException](dn334359\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDbTimeTooNewException](dn334407\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDbTimeTooOldException](dn274245\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentEndingRestoreLogTooLowException](dn274239\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentExistingLogFileHasBadSignatureException](dn274318\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentExistingLogFileIsNotContiguousException](dn274260\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFileInvalidTypeException](dn274337\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentGivenLogFileHasBadSignatureException](dn350421\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentGivenLogFileIsNotContiguousException](dn350479\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidCreateDbVersionException](dn319468\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidDatabaseVersionException](dn319486\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogGenerationMismatchException](dn334564\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingCurrentLogFilesException](dn334701\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingFileToBackupException](dn334656\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingRestoreLogFilesException](dn334755\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentPageSizeMismatchException](dn319780\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRequiredLogFilesMissingException](dn350548\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentStartingRestoreLogTooHighException](dn334858\(v=exchg.10\).md)

