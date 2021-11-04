---
description: "Learn more about: EsentCorruptionException class"
title: EsentCorruptionException class
TOCTitle: EsentCorruptionException class
ms:assetid: T:Microsoft.Isam.Esent.Interop.EsentCorruptionException
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.esentcorruptionexception(v=EXCHG.10)
ms:contentKeyID: 55101411
ms.date: 07/30/2014
ms.topic: reference
f1_keywords:
- Microsoft.Isam.Esent.Interop.EsentCorruptionException
dev_langs:
- CSharp
- JScript
- VB
- other
api_name: 
- Microsoft.Isam.Esent.Interop.EsentCorruptionException
topic_type: 
- kbSyntax
- apiref
api_type: 
- Managed
api_location: 
- Microsoft.Isam.Esent.Interop.dll
ROBOTS: INDEX,FOLLOW

---

# EsentCorruptionException class

Base class for Corruption exceptions.

## Inheritance hierarchy

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentCorruptionException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)  
**Assembly:**  Microsoft.Isam.Esent.Interop (in Microsoft.Isam.Esent.Interop.dll)

## Syntax

``` vb
'Declaration
<SerializableAttribute> _
Public MustInherit Class EsentCorruptionException _
    Inherits EsentDataException
'Usage
Dim instance As EsentCorruptionException
```

``` csharp
[SerializableAttribute]
public abstract class EsentCorruptionException : EsentDataException
```

## Thread safety

Any public static (Shared in Visual Basic) members of this type are thread safe. Any instance members are not guaranteed to be thread safe.

## See also

#### Reference

[EsentCorruptionException members](./esentcorruptionexception-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)

## Derived types

[System.Object](/dotnet/api/system.object)  
  [System.Exception](/dotnet/api/system.exception)  
    [Microsoft.Isam.Esent.EsentException](./esentexception-class.md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](./esenterrorexception-class.md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](./esentdataexception-class.md)  
          Microsoft.Isam.Esent.Interop.EsentCorruptionException  
            [Microsoft.Isam.Esent.Interop.EsentBadEmptyPageException](./esentbademptypageexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadPageLinkException](./esentbadpagelinkexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentBadParentPageLinkException](./esentbadparentpagelinkexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCatalogCorruptedException](./esentcatalogcorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCheckpointCorruptException](./esentcheckpointcorruptexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCommittedLogFileCorruptException](./esentcommittedlogfilecorruptexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentCommittedLogFilesMissingException](./esentcommittedlogfilesmissingexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseBufferDependenciesCorruptedException](./esentdatabasebufferdependenciescorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseCorruptedException](./esentdatabasecorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDbTimeCorruptedException](./esentdbtimecorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDecompressionFailedException](./esentdecompressionfailedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDerivedColumnCorruptionException](./esentderivedcolumncorruptionexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentDiskReadVerificationFailureException](./esentdiskreadverificationfailureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFileIOBeyondEOFException](./esentfileiobeyondeofexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentFileSystemCorruptionException](./esentfilesystemcorruptionexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexBuildCorruptedException](./esentindexbuildcorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLogSequenceException](./esentinvalidlogsequenceexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogCorruptDuringHardRecoveryException](./esentlogcorruptduringhardrecoveryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogCorruptDuringHardRestoreException](./esentlogcorruptduringhardrestoreexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogCorruptedException](./esentlogcorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogFileCorruptException](./esentlogfilecorruptexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogReadVerifyFailureException](./esentlogreadverifyfailureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRecoveryException](./esentlogtornwriteduringhardrecoveryexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRestoreException](./esentlogtornwriteduringhardrestoreexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentLVCorruptedException](./esentlvcorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingLogFileException](./esentmissinglogfileexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingPreviousLogFileException](./esentmissingpreviouslogfileexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentPageNotInitializedException](./esentpagenotinitializedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentPrimaryIndexCorruptedException](./esentprimaryindexcorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentReadLostFlushVerifyFailureException](./esentreadlostflushverifyfailureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentReadPgnoVerifyFailureException](./esentreadpgnoverifyfailureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentReadVerifyFailureException](./esentreadverifyfailureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordFormatConversionFailedException](./esentrecordformatconversionfailedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRecoveryVerifyFailureException](./esentrecoveryverifyfailureexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentRedoAbruptEndedException](./esentredoabruptendedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSecondaryIndexCorruptedException](./esentsecondaryindexcorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSPAvailExtCorruptedException](./esentspavailextcorruptedexception-class.md)  
            [Microsoft.Isam.Esent.Interop.EsentSPOwnExtCorruptedException](./esentspownextcorruptedexception-class.md)