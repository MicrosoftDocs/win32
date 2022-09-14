---
title: Comma-separated Value (CSV) Scripts
description: Windows 2000 includes a command-line utility, CSVDE, to import directory objects using .csv files and export directory objects as .csv files.
ms.assetid: fda242eb-7561-444f-b560-94bd87fe4e39
ms.tgt_platform: multiple
keywords:
- Comma-separated Value Scripts AD
- Scripts, Comma-separated Value AD
ms.topic: article
ms.date: 05/31/2018
---

# Comma-separated Value (CSV) Scripts

Windows 2000 includes a command-line utility, CSVDE, to import directory objects using .csv files and export directory objects as .csv files. CSV scripts are created for ease-of-use. The first line in the script identifies the attributes in the lines that follow. Columns are separated by commas. The file format is compatible with the Microsoft Excel .csv format, so that files are easily created. Use Excel or any other tool that can read and write .csv files. CSVDE supports Unicode.

## Example CSV File

The following code example is a CSV file that adds an auxiliary class.

``` syntax
DN,adminDisplayName,cn,defaultHidingValue,defaultObjectCategory,description,governsID,lDAPDisplayName,mayContain,mustContain,distinguishedName,objectCategory,objectClass,objectClassCategory,possSuperiors,name,rDNAttID,schemaIDGUID,subClassOf,auxiliaryClass,defaultSecurityDescriptor
"CN=My-Test-Auxiliary-Class1,CN=Schema,CN=Configuration,DC=myorg,DC=mytest,DC=Fabrikam,DC=com",My-Test-Auxiliary-Class1,My-Test-Auxiliary-Class1,FALSE,"CN=My-Test-Auxiliary-Class1,CN=Schema,CN=Configuration,DC=myorg,DC=mytest,DC=Fabrikam,DC=com",Test class used to show how to add an auxiliary class.,1.2.840.113556.1.4.7000.159.24.10.611.11,myTestAuxiliaryClass1,myTestAttributeDNString,description;myTestAttributeUnicodeString,"CN=My-Test-Auxiliary-Class1,CN=Schema,CN=Configuration,DC=myorg,DC=mytest,DC=fabrikam,DC=com","CN=Class-Schema,CN=Schema,CN=Configuration,DC=myorg,DC=mytest,DC=fabrikam,DC=com",classSchema,3,domainDNS;container,My-Test-Auxiliary-Class1,cn,X'9a6b3176c5dbd2118bd00000f875b660',top,,
```

 

 




