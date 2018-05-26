---
Description: An application can use the MsiOpenDatabase function to open a new or existing installation database (.msi file) or patch package (.msp file.) The application checks the return value of MsiOpenDatabase before using the database handle.
ms.assetid: 54a8d571-ebc3-42d5-bc34-8f29b245b4d8
title: A Database and Patch Example
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# A Database and Patch Example

An application can use the [**MsiOpenDatabase**](/windows/win32/Msiquery/nf-msiquery-msiopendatabasea?branch=master) function to open a new or existing installation database (.msi file) or patch package (.msp file.) The application checks the return value of **MsiOpenDatabase** before using the database handle.

The following examples use the **PMSIHANDLE** type variables defined in msi.h. It is recommended to use the **PMSIHANDLE** type because the installer closes **PMSIHANDLE** objects as they go out of scope, whereas your application must close **MSIHANDLE** objects by calling [**MsiCloseHandle**](/windows/win32/Msi/nf-msi-msiclosehandle?branch=master). For more information see [Use PMSIHANDLE instead of HANDLE](windows-installer-best-practices.md#use-pmsihandle-instead-of-handle) section in the [Windows Installer Best Practices](windows-installer-best-practices.md).

The following example opens a database, sample.msi, for reading only. [**MsiOpenDatabase**](/windows/win32/Msiquery/nf-msiquery-msiopendatabasea?branch=master) succeeds only if sample.msi exists in the c:\\test directory. Upon success, the returned database handle can be used to query the data in the installation package using [**MsiDatabaseOpenView**](/windows/win32/Msiquery/nf-msiquery-msidatabaseopenviewa?branch=master) and [**MsiGetSummaryInformation**](/windows/win32/Msiquery/nf-msiquery-msigetsummaryinformationa?branch=master).


```C++
PMSIHANDLE hDbReadOnly = 0;
UINT uiStatus1 = MsiOpenDatabase(TEXT("c:\\test\\sample.msi"), MSIDBOPEN_READONLY, &amp;hDbReadOnly);
if (ERROR_SUCCESS != uiStatus1)
{
    // process error
    return uiStatus1;
}
```



The following example opens the database for reading and writing. If the application calls [**MsiDatabaseCommit**](/windows/win32/Msiquery/nf-msiquery-msidatabasecommit?branch=master), all changes made to the database are saved. If the application does not call **MsiDatabaseCommit**, no changes are made to the database.


```C++
PMSIHANDLE hDbTransact = 0;
UINT uiStatus2 = MsiOpenDatabase(TEXT("c:\\test\\example.msi"), MSIDBOPEN_TRANSACT, &amp;hDbTransact);
if (ERROR_SUCCESS != uiStatus2)
{
    // process error
    return uiStatus2;
}
```



The following example takes an existing database, text.msi, and creates a new database, newtest.msi. Any changes that are made can be saved in the new database by calling [**MsiDatabaseCommit**](/windows/win32/Msiquery/nf-msiquery-msidatabasecommit?branch=master). The existing database specified in the *szDatabasePath* parameter is unchanged.


```C++
PMSIHANDLE hDbOutput = 0;
UINT uiStatus3 = MsiOpenDatabase(TEXT("c:\\test\\test.msi"), TEXT("c:\\test\\newtest.msi"), &amp;hDbOutput);
if (ERROR_SUCCESS != uiStatus3)
{
    // process error
    return uiStatus3;
}
```



The following example opens a Windows Installer patch package (.msp file) for reading only. The returned patch handle can be used to determine the cabinets and transform substorages included in the patch package by queries on the [\_Streams](-streams-table.md) and [\_Storages](-storages-table.md) tables.

**Windows Installer 2.0:** Not supported. Beginning with Windows Installer 3.0, the application can query the [MsiPatchSequence table](msipatchsequence-table.md) present in a patch package that uses the new patch sequencing information.


```C++
PMSIHANDLE hDbPatch = 0;
LPCTSTR szPersistMode = MSIDBOPEN_READONLY + MSIDBOPEN_PATCHFILE;
UINT uiStatus4 = MsiOpenDatabase(TEXT("c:\\test\\sample.msp"), szPersistMode, &amp;hDbPatch);
if (ERROR_SUCCESS != uiStatus4)
{
    // process error
    return uiStatus4;
}
```



 

 



