---
Description: You cannot access an installer session from a custom action that is not the current installation session.
ms.assetid: 8aa0ac17-1341-4399-987e-d26175150874
title: Accessing a Database or Session from Inside a Custom Action
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Accessing a Database or Session from Inside a Custom Action

You cannot access an installer session from a custom action that is not the current installation session. Custom actions are limited to working with only the active database of the session and no other databases. The following Windows Installer [Database Functions](database-functions.md) must not be called from a custom action, because they require a handle to a database that is not the database of the current installation session:

[**MsiDatabaseMerge**](/windows/win32/Msiquery/nf-msiquery-msidatabasemergea?branch=master)

 

[**MsiCreateTransformSummaryInfo**](/windows/win32/Msiquery/nf-msiquery-msicreatetransformsummaryinfoa?branch=master)

 

[**MsiDatabaseApplyTransform**](/windows/win32/Msiquery/nf-msiquery-msidatabaseapplytransforma?branch=master)

 

[**MsiDatabaseCommit**](/windows/win32/Msiquery/nf-msiquery-msidatabasecommit?branch=master)

 

[**MsiDatabaseExport**](/windows/win32/Msiquery/nf-msiquery-msidatabaseexporta?branch=master)

 

[**MsiDatabaseGenerateTransform**](/windows/win32/Msiquery/nf-msiquery-msidatabasegeneratetransforma?branch=master)

 

[**MsiDatabaseImport**](/windows/win32/Msiquery/nf-msiquery-msidatabaseimporta?branch=master)

 

[**MsiEnableUIPreview**](/windows/win32/Msiquery/nf-msiquery-msienableuipreview?branch=master)

 

[**MsiGetDatabaseState**](/windows/win32/Msiquery/nf-msiquery-msigetdatabasestate?branch=master)

## Related topics

<dl> <dt>

[Accessing the Current Installer Session from Inside a Custom Action](accessing-the-current-installer-session-from-inside-a-custom-action.md)
</dt> </dl>

 

 



