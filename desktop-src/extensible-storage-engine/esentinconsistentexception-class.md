---
description: "Learn more about: EsentInconsistentException class"
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

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentInconsistentException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
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

[EsentInconsistentException members](./esentinconsistentexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)

## Derived types

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentInconsistentException  
            [Microsoft.Isam.Esent.Interop.EsentAttachedDatabaseMismatchException](./esentattacheddatabasemismatchexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadCheckpointSignatureException](./esentbadcheckpointsignatureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadLogSignatureException](./esentbadlogsignatureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadLogVersionException](./esentbadlogversionexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCheckpointFileNotFoundException](./esentcheckpointfilenotfoundexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentConsistentTimeMismatchException](./esentconsistenttimemismatchexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseDirtyShutdownException](./esentdatabasedirtyshutdownexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseIncompleteIncrementalReseedException](./esentdatabaseincompleteincrementalreseedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseLogSetMismatchException](./esentdatabaselogsetmismatchexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDbTimeTooNewException](./esentdbtimetoonewexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDbTimeTooOldException](./esentdbtimetoooldexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentEndingRestoreLogTooLowException](./esentendingrestorelogtoolowexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentExistingLogFileHasBadSignatureException](./esentexistinglogfilehasbadsignatureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentExistingLogFileIsNotContiguousException](./esentexistinglogfileisnotcontiguousexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFileInvalidTypeException](./esentfileinvalidtypeexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentGivenLogFileHasBadSignatureException](./esentgivenlogfilehasbadsignatureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentGivenLogFileIsNotContiguousException](./esentgivenlogfileisnotcontiguousexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidCreateDbVersionException](./esentinvalidcreatedbversionexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidDatabaseVersionException](./esentinvaliddatabaseversionexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogGenerationMismatchException](./esentloggenerationmismatchexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingCurrentLogFilesException](./esentmissingcurrentlogfilesexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingFileToBackupException](./esentmissingfiletobackupexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingRestoreLogFilesException](./esentmissingrestorelogfilesexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentPageSizeMismatchException](./esentpagesizemismatchexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRequiredLogFilesMissingException](./esentrequiredlogfilesmissingexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentStartingRestoreLogTooHighException](./esentstartingrestorelogtoohighexception-class.md)