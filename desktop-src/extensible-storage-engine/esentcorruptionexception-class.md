---
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

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentCorruptionException  
            

**Namespace:**  [Microsoft.Isam.Esent.Interop](hh596136\(v=exchg.10\).md)  
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

[EsentCorruptionException members](dn334328\(v=exchg.10\).md)

[Microsoft.Isam.Esent.Interop namespace](hh596136\(v=exchg.10\).md)

## Inheritance hierarchy

[System.Object](https://docs.microsoft.com/dotnet/api/system.object?redirectedfrom=MSDN)  
  [System.Exception](https://docs.microsoft.com/dotnet/api/system.exception?redirectedfrom=MSDN)  
    [Microsoft.Isam.Esent.EsentException](dn292088\(v=exchg.10\).md)  
      [Microsoft.Isam.Esent.Interop.EsentErrorException](dn274314\(v=exchg.10\).md)  
        [Microsoft.Isam.Esent.Interop.EsentDataException](dn334392\(v=exchg.10\).md)  
          Microsoft.Isam.Esent.Interop.EsentCorruptionException  
            [Microsoft.Isam.Esent.Interop.EsentBadEmptyPageException](dn274059\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadPageLinkException](dn274083\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentBadParentPageLinkException](dn274033\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCatalogCorruptedException](dn274191\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCheckpointCorruptException](dn274132\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCommittedLogFileCorruptException](dn274206\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentCommittedLogFilesMissingException](dn334311\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseBufferDependenciesCorruptedException](dn334366\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDatabaseCorruptedException](dn334279\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDbTimeCorruptedException](dn274236\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDecompressionFailedException](dn274251\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDerivedColumnCorruptionException](dn274270\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentDiskReadVerificationFailureException](dn274287\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFileIOBeyondEOFException](dn274354\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentFileSystemCorruptionException](dn274381\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentIndexBuildCorruptedException](dn350493\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentInvalidLogSequenceException](dn319554\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogCorruptDuringHardRecoveryException](dn319628\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogCorruptDuringHardRestoreException](dn334512\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogCorruptedException](dn334510\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogFileCorruptException](dn334601\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogReadVerifyFailureException](dn334583\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRecoveryException](dn334657\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLogTornWriteDuringHardRestoreException](dn334605\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentLVCorruptedException](dn334680\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingLogFileException](dn334746\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentMissingPreviousLogFileException](dn334685\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentPageNotInitializedException](dn319771\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentPrimaryIndexCorruptedException](dn319793\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentReadLostFlushVerifyFailureException](dn319812\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentReadPgnoVerifyFailureException](dn319871\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentReadVerifyFailureException](dn319876\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRecordFormatConversionFailedException](dn319884\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRecoveryVerifyFailureException](dn319891\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentRedoAbruptEndedException](dn319858\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSecondaryIndexCorruptedException](dn350606\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSPAvailExtCorruptedException](dn334914\(v=exchg.10\).md)  
            [Microsoft.Isam.Esent.Interop.EsentSPOwnExtCorruptedException](dn334917\(v=exchg.10\).md)

